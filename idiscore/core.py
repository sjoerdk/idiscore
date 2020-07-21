# -*- coding: utf-8 -*-
from typing import List, Optional

from jinja2 import Template
from pydicom.dataelem import DataElement
from pydicom.dataset import Dataset

from idiscore import __version__
from idiscore.exceptions import IDISCoreException
from idiscore.operators import ElementShouldBeRemoved, Remove
from idiscore.imageprocessing import (
    PixelDataProcessorException,
    PixelProcessor,
)
from idiscore.rules import RuleSet
from idiscore.templates import idiscore_description, profile_description
from idiscore.validation import Deidentifier


class Profile:
    """Defines what to do with each DICOM tag in a dataset

    Models the complete deidentification of all DICOM elements except for pixel data

    Rules:
    * DICOM tags that are not mentioned explicitly in the profile are kept
    * A Profile holds a list of RuleSets. Later Rules overrule earlier
    * A profile's RuleSets can be 'collapsed' to have exactly one operation for
      each tag

    """

    def __init__(self, rule_sets: List[RuleSet], name: str = "Profile"):
        """

        Parameters
        ----------
        rule_sets: List[RuleSet]
            All RuleSets that should be applied. Ordering is important; if two
            RuleSets contain a rule for the same DICOM tag, the RuleSet with the
            higher index takes precedence.
        name: str
            Human-readable name for this profile. Defaults to 'Profile'
        """
        self.rule_sets = rule_sets
        self.name = name

    def __str__(self):
        return f'Profile "{self.name}"'

    def flatten(self, additional_rule_sets: List[RuleSet] = None) -> RuleSet:
        """Collapse all rule sets into one, ensuring only one rule per DICOM tag
        If a sets disagree, later sets (higher index in the list) take precedence.

        Parameters
        ----------
        additional_rule_sets: List[RuleSet]
            Append these to the existing rule sets, so they overrule them. Useful
            for one-time additions without changing the profile itself. For example
            when adding dataset-specific safe private rules.

        """
        if not additional_rule_sets:
            additional_rule_sets = []

        output = {}
        for rule_set in self.rule_sets + additional_rule_sets:
            output.update({x.identifier: x for x in rule_set.rules})

        return RuleSet(name="flattened", rules=set(output.values()))

    def description(self) -> str:
        """A multi-line, human readable description of this profile"""
        rules = self.flatten().rules
        return Template(profile_description).render(
            profile_name=self.name,
            rule_set_names=[f"* {x.name}" for x in self.rule_sets],
            rule_strings_by_name=sorted([x.as_human_readable() for x in rules]),
            rule_strings_by_tag=sorted(
                f"{x.identifier} ({x.identifier.name()}) - {x.operation}" for x in rules
            ),
        )


class Bouncer:
    """Inspects a dataset and either rejects it or lets it through"""

    description = "Bouncer"  # single line description used in human-readable output

    def inspect(self, dataset: Dataset):
        """Check given dataset, raise exception if it should be rejected

        Parameters
        ----------
        dataset: Dataset
            The DICOM dataset to inspect

        Returns
        -------
        None

        Raises
        ------
        BouncerException
            When this dataset cannot be deidentified for any reason

        """
        pass


class Core(Deidentifier):
    """Can deidentify a DICOM dataset. Holds all configuration, filters and
    connections needed to do this
    """

    def __init__(
        self,
        profile: Profile,
        insertions: List[DataElement] = None,
        bouncers: List[Bouncer] = None,
        pixel_processor: Optional[PixelProcessor] = None,
    ):
        """

        Parameters
        ----------
        profile: Profile
            Defines what to do with each DICOM element (except PixelData)
        insertions: List[DataElement]
            DICOM elements to insert into each deidentified dataset
        bouncers: List[Bouncer], optional
            Inspect all incoming data and can reject if it is deemed not fit for
            deidentification. For example rejecting encapsulated PDFs as they are
            too difficult to deidentify. Defaults to empty list (all data allowed)
        pixel_processor: Optional[PrivateProcessor],
            Defines what to do with DICOM image data (the PixelData tag). Can remove
            or black out certain parts of an image. Defaults to None

        """
        self.profile = profile
        self.insertions = insertions if insertions else []  # convert default None
        self.bouncers = bouncers if bouncers else []
        self.pixel_processor = pixel_processor

    def deidentify(self, dataset: Dataset) -> Dataset:
        """Try to remove identifiable information from dataset

        Raises
        ------
        DeidentificationException
            If deidentification fails for any reason

        Notes
        -----
        Input dataset is passed by reference so will be modified. The output
        of this function is the same object as the input
        >>> original_dataset
        >>> deidentified = core.deidentify(original_dataset)
        >>> original_dataset == deidentified  # True

        """
        self.apply_bouncers(dataset)  # should this dataset be rejected outright?
        dataset = self.apply_pixel_processor(dataset)  # clean image data if needed

        # Obtain exactly one rule per tag/group
        rules = self.profile.flatten()

        # define a function for walk() below
        def process_element(dataset_in: Dataset, data_element_in: DataElement):
            """Process element according to the rules in the outer scope"""

            # Find the rule to apply for this DICOM element
            rule = rules.get_rule(data_element_in)

            if not rule:
                #  Keep elements for which there is no rule
                return
            elif type(rule.operation) == Remove:
                del dataset_in[data_element_in.tag]
            else:
                try:
                    if replacement := rule.operation.apply(data_element_in, dataset):
                        dataset_in[data_element_in.tag] = replacement
                    # if no replacement, the element has been modified in place
                except ElementShouldBeRemoved:
                    # clean() operation can signal removal like this.
                    del dataset_in[data_element_in.tag]

        dataset.walk(process_element)

        for element in self.insertions:
            dataset.add(element)

        return dataset

    def apply_pixel_processor(self, dataset):
        """Put blackouts in image data if required"""

        if self.pixel_processor and self.pixel_processor.needs_cleaning(dataset):
            try:
                dataset = self.pixel_processor.clean_pixel_data(dataset)
            except PixelDataProcessorException as e:
                raise DeidentificationException(e)
        return dataset

    def description(self) -> str:
        """A multi-line, human readable description of this instance

        what happens to each tag, which data will be rejected, etc.
        """

        return Template(idiscore_description).render(
            idiscore_lib_version=__version__,
            bouncer_descriptions=[x.description for x in self.bouncers],
            profile_description=self.profile.description()
            # if applicable, safe private
        )

    def apply_bouncers(self, dataset):
        """Check all bouncers to see whether dataset should be rejected"""

        for bouncer in self.bouncers:
            try:
                bouncer.inspect(dataset)
            except BouncerException as e:
                raise DeidentificationException(e)


class BouncerException(IDISCoreException):
    pass


class DeidentificationException(IDISCoreException):
    pass
