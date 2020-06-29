# -*- coding: utf-8 -*-
from collections import OrderedDict
from typing import Callable, List, Optional

from pydicom.dataelem import DataElement
from pydicom.dataset import Dataset
from pydicom.tag import Tag

from idiscore.exceptions import IDISCoreException
from idiscore.identifiers import TagIdentifier
from idiscore.operations import Operator, Remove
from idiscore.imageprocessing import CriterionException, PixelProcessor


class Rule:
    """Defines what to do with a single DICOM element or single group of elements"""

    def __init__(self, identifier: TagIdentifier, operation: Operator):
        self.identifier = identifier
        self.operation = operation

    def __str__(self):
        return f"{self.identifier} - {self.operation}"


class RuleList:
    """Defines what to do to one or more DICOM tags

    Models part of a deidentification procedure, such as the Basic Application
    Level Confidentiality Options in DICOM (e.g. Retain Safe Private Option)
    """

    def __init__(self, rules: List[Rule], name: str = "RuleSet"):
        """

        Parameters
        ----------
        rules: List[Rule]
            The rules comprising this set
        name: str, optional
            Human readable name. Defaults to 'RuleSet'
        """

        self.rules_dict = OrderedDict((x.identifier, x) for x in rules)
        self.name = name

    @property
    def rules(self) -> List[Rule]:
        return list(self.rules_dict.values())

    def get_rule(self, tag: Tag) -> Optional[Rule]:
        """Return the most specific rule for the given DICOM tag, or None if not found

        Notes
        -----
        It is possible for multiple rules to match. Lookup is always done from
        specific to general.
        For example, when getting a rule for tag (0010,0010):
        * A rule for (0010,0010) is preferred over (0010,00xx)
        * A rule for (0010,00xx) is preferred over (0010,xx10)
        * A rule for (0010,xx10) is preferred over (xxxx,0010)

        """
        raise NotImplementedError("TODO: incorporate repeater tags")
        # return self.rules_dict.get(tag)

    def __str__(self):
        return f'Ruleset "{self.name}"'


class Profile:
    """Defines what to do with each DICOM tag in a dataset

    Models the complete deidentification of all DICOM elements except for pixel data

    Rules:
    * DICOM tags that are not mentioned explicitly in the profile are removed
    * A Profile holds a list of RuleSets. Later Rules overrule earlier
    * A profile's RuleSets can be 'collapsed' to have one operation for each
      tag

    """

    def __init__(self, rule_sets: List[RuleList], name: str = "Profile"):
        """

        Parameters
        ----------
        rule_sets: List[RuleList]
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

    def flatten(self, additional_rule_sets: List[RuleList] = None) -> RuleList:
        """Collapse all rule sets into one, ensuring only one rule per DICOM tag
        If a sets disagree, later sets (higher index in the list) take precedence.

        Parameters
        ----------
        additional_rule_sets: List[RuleList]
            Append these to the existing rule sets, so they overrule them. Useful
            for one-time additions without changing the profile itself. For example
            when adding dataset-specific safe private rules.

        """
        if not additional_rule_sets:
            additional_rule_sets = []

        output = {}
        for rule_set in self.rule_sets + additional_rule_sets:
            output.update({x.identifier: x for x in rule_set.rules})

        return RuleList(name="flattened", rules=set(output.values()))


class Bouncer:
    """Inspects a dataset and either rejects it or lets it through"""

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


class SafePrivateDefinition:
    """Defines when one or more private DICOM elements can be considered 'safe'
    Safe as in 'not containing personally identifiable information'
    """

    def __init__(self, tags: List[Tag], criterion: Callable[[Dataset], bool]):
        """

        Parameters
        ----------
        tags: List[Tag]
            One ore more Tags of private DICOM elements
        criterion: Callable[[Dataset], bool]
            Function that returns True if these private Elements are safe to keep
            in the given dataset. May return CriterionException if a True or
            False answer cannot be given
        """
        self.tags = tags
        self.criterion = criterion

    def is_safe(self, dataset: Dataset) -> bool:
        """These private tags are safe to keep in the given dataset

        Raises
        ------
        CriterionException
            If no True or False response can be given for this dataset
        """
        return self.criterion(dataset)


class PrivateProcessor:
    """Uses SafePrivateDefinitions to determine all private DICOM elements that
    can be kept for any given dataset

    """

    def __init__(self, definitions: List[SafePrivateDefinition]):
        self.definitions = definitions

    def get_rule_set(self, dataset: Dataset) -> RuleList:
        """Given this dataset, which private elements can be kept?

        Parameters
        ----------
        dataset: Dataset
            The DICOM dataset to inspect

        Returns
        -------
        RuleList
            Rules for all private DICOM elements that are safe for the
            given dataset

        Raises
        ------
        PrivateProcessorException
            When rule set cannot be found properly
        """
        try:
            return RuleList(
                name="safe private",
                rules={x for x in self.definitions if x.is_safe(dataset)},
            )
        except CriterionException as e:
            raise PrivateProcessorException(e)


class Core:
    """Can deidentify a DICOM dataset. Holds all configuration, filters and
    connections needed to do this
    """

    def __init__(
        self,
        bouncers: List[Bouncer],
        profile: Profile,
        safe_private: PrivateProcessor,
        pixel_processor: PixelProcessor,
    ):
        """

        Parameters
        ----------
        bouncers: List[Bouncer]
            Inspect all incoming data and can reject if it is deemed not fit for
            deidentification. For example rejecting encapsulated PDFs as they are
            too difficult to deidentify.
        profile: Profile
            Defines what to do with each DICOM element (except PixelData)
        safe_private: PrivateProcessor
            Defines what to do with private DICOM elements. Some might be safe under
            certain circumstances
        pixel_processor: PixelProcessor
            Defines what to do with DICOM image data (the PixelData tag). Can remove
            or black out certain parts of an image.

        """
        self.profile = profile
        self.bouncers = bouncers
        self.safe_private = safe_private
        self.pixel_processor = pixel_processor

    def deidentify(self, dataset: Dataset):

        # check all bouncers to see whether dataset should be rejected
        for bouncer in self.bouncers:
            bouncer.inspect(dataset)

        # check whether blackout is needed, then check whether a blackout is possible
        # run blackout if required
        if self.pixel_processor.needs_cleaning(dataset):
            dataset = self.pixel_processor.clean_pixel_data(dataset)

        # All private tags are deleted by default. Are there any exceptions for this
        # dataset?
        safe_private = self.safe_private.get_rule_set(dataset)

        # add safe private rules and then flatten all sets into one
        rule_set = self.profile.flatten(additional_rule_sets=[safe_private])

        # run flattened profile (deidentify all tags).
        def process_element(dataset_in: Dataset, data_element_in: DataElement):
            # Find the rule to apply for this DICOM element
            rule = rule_set.get_rule(data_element_in.tag)

            if not rule:
                #  Keep tags for which there is no rule. Important decision
                pass
            elif type(rule) == Remove:
                del dataset_in[data_element_in.tag]
            else:
                rule.operation.apply(data_element_in)

        dataset.walk(process_element)

        return dataset


class BouncerException(IDISCoreException):
    pass


class PrivateProcessorException(IDISCoreException):
    pass
