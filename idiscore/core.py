from typing import List, Optional

from dicomgenerator.dicom import VRs
from pydicom.dataelem import DataElement
from pydicom.dataset import Dataset
from pydicom.sequence import Sequence

from idiscore import __version__
from idiscore.bouncers import Bouncer, BouncerException
from idiscore.dataset import RequiredTagNotFound
from idiscore.exceptions import IDISCoreError
from idiscore.image_processing import (
    PixelDataProcessorException,
    PixelProcessor,
)
from idiscore.operators import ElementShouldBeRemoved
from idiscore.rules import RuleSet
from idiscore.templates import (
    idiscore_description_rst,
    idiscore_description_txt,
    jinja_env,
    profile_description_rst,
    profile_description_txt,
)


class Profile:
    """Defines what to do with each DICOM tag in a dataset

    Models the complete deidentification of all DICOM elements except for pixel data

    Rules:
    * DICOM tags that are not mentioned explicitly in the profile are kept

    * A Profile holds a list of RuleSets. Later Rules overrule earlier

    * A profile's RuleSets can be 'flattened' to have exactly one operation for
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

    def description(self, text_format: str = "txt") -> str:
        """A multi-line, human-readable description of this profile

        Parameters
        ----------
        text_format: str,optional
            Format of output. Either 'txt' for flat string description, or 'rst'
            for Sphinx rst. Defaults to txt

        Raises
        ------
        ValueError
            For unknown format
        """
        if text_format == "txt" or not text_format:
            template = profile_description_txt
        elif text_format == "rst":
            template = profile_description_rst
        else:
            raise ValueError(
                f"{text_format} is not a valid format. Allowed:" f' ["txt","rst"]'
            )
        rules = self.flatten().rules
        return jinja_env.from_string(template).render(
            profile_name=self.name,
            rule_set_names=[f"* {x.name}" for x in self.rule_sets],
            rule_strings_by_name=sorted(x.as_human_readable() for x in rules),
            rule_strings_by_tag=sorted(
                f"{x.identifier} ({x.identifier.name()}) - {x.operation}" for x in rules
            ),
        )


class Deidentifier:
    """Something that has a deidentify() method that processes pydicom datasets"""

    def deidentify(self, dataset: Dataset) -> Dataset:
        raise NotImplementedError()


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
        DeidentificationError
            If deidentification fails for any reason

        Warnings
        --------
        Input dataset is passed by reference so will be modified. The output
        of this function is the same object as the input
        >>> original_dataset
        >>> deidentified = core.deidentify(original_dataset)
        >>> original_dataset == deidentified  # True

        """
        self.apply_bouncers(dataset)  # should this dataset be rejected outright?
        dataset = self.apply_pixel_processor(dataset)  # clean image data if needed

        deidentified = self.apply_rules(rules=self.profile.flatten(), dataset=dataset)

        # add tags if needed
        for element in self.insertions:
            deidentified.add(element)

        return deidentified

    def apply_rules(self, rules: RuleSet, dataset: Dataset) -> Dataset:
        """Apply rules to each element in dataset, recursing into sequence elements

        Notes
        -----
        This will modify the input Dataset instance. Modification in-place to minimize
        memory footprint
        """

        for element in dataset:
            if element.VR == VRs.Sequence.short_name:  # recurse into sequences
                dataset.add(  # add will overwrite existing
                    DataElement(
                        tag=element.tag,
                        VR=element.VR,
                        value=Sequence(
                            [
                                self.apply_rules(rules, sub_dataset)
                                for sub_dataset in element
                            ]
                        ),
                    )
                )
            elif rule := rules.get_rule(element):  # non-sequence
                try:
                    new = rule.operation.apply(element, dataset)
                    dataset.add(new)
                except ElementShouldBeRemoved:  # Operator signals removal
                    del dataset[element.tag]
            else:  # no rule found. Leave this element unchanged
                pass

        return dataset

    def apply_pixel_processor(self, dataset):
        """Paint parts of image data black if required

        Raises
        ------
        DeidentificationError
            When dataset can not be processed
        """

        if self.pixel_processor and self.pixel_processor.needs_cleaning(dataset):
            try:
                dataset = self.pixel_processor.clean_pixel_data(dataset)
            except PixelDataProcessorException as e:
                raise DeidentificationError(e) from e
        return dataset

    def description(self, text_format: str = "txt") -> str:
        """A multi-line, human-readable description of this instance

        what happens to each tag, which data will be rejected, etc.

        Parameters
        ----------
        text_format: str,optional
            Format of output. Either 'txt' for flat string description, or 'rst'
            for Sphinx rst. Defaults to txt

        Raises
        ------
        ValueError
            For unknown format
        """
        if text_format == "txt" or not text_format:
            template = idiscore_description_txt
        elif text_format == "rst":
            template = idiscore_description_rst
        else:
            raise ValueError(
                f"{text_format} is not a valid format. Allowed:" f' ["txt","rst"]'
            )

        return jinja_env.from_string(template).render(
            idiscore_lib_version=__version__,
            bouncer_descriptions=[x.description for x in self.bouncers],
            profile_description=self.profile.description(text_format=text_format)
            # if applicable, safe private
        )

    def apply_bouncers(self, dataset):
        """Check all bouncers to see whether dataset should be rejected"""

        for bouncer in self.bouncers:
            try:
                bouncer.inspect(dataset)
            except BouncerException as e:
                raise DeidentificationError(e) from e


def handle_key_error(func):
    def decorated(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except KeyError as e:
            raise RequiredTagNotFound(f"Required tag not found: {e}") from e

    return decorated


class DeidentificationError(IDISCoreError):
    pass
