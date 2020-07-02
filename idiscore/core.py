# -*- coding: utf-8 -*-
from typing import Callable, List, Optional, Union

from pydicom.dataelem import DataElement
from pydicom.dataset import Dataset
from pydicom.tag import BaseTag, Tag

from idiscore.exceptions import IDISCoreException
from idiscore.identifiers import SingleTag, TagIdentifier
from idiscore.operations import Operator, Remove
from idiscore.imageprocessing import (
    CriterionException,
    PixelDataProcessorException,
    PixelProcessor,
)


class Rule:
    """Defines what to do with a single DICOM element or single group of elements"""

    def __init__(self, identifier: Union[TagIdentifier, BaseTag], operation: Operator):
        # allow pydicom Tag object for less clutter in Rule init
        if isinstance(identifier, BaseTag):
            identifier = SingleTag(identifier)
        self.identifier = identifier
        self.operation = operation

    def __str__(self):
        return f"{self.identifier} - {self.operation}"

    def number_of_matchable_tags(self) -> int:
        """The number of distinct DICOM tags that this rule could match"""
        return self.identifier.number_of_matchable_tags()

    def matches(self, tag: BaseTag) -> bool:
        """True if this rule matches the given DICOM tag"""
        return self.identifier.matches(tag)


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

        # keep wildcard rule separately for more efficient matching
        self._single_tag_rules_dict = {
            str(x.identifier): x for x in rules if self.is_single_tag_rule(x)
        }

        self._group_rules = [x for x in rules if not self.is_single_tag_rule(x)]
        # Try to match most specific group rules first
        self._group_rules.sort(key=lambda x: x.number_of_matchable_tags())

        self.name = name

    @property
    def rules(self) -> List[Rule]:
        """All rules in this list"""
        return list(self._single_tag_rules_dict.values()) + self._group_rules

    @staticmethod
    def is_single_tag_rule(rule: Rule) -> bool:
        """Targets only a single DICOM tag"""
        return isinstance(rule.identifier, SingleTag)

    def get_rule(self, tag: BaseTag) -> Optional[Rule]:
        """Return the most specific rule for the given DICOM tag, or None if not found

        Returns
        -------
        Rule
            Most specific rule for the given DICOM tag
        None
            If no rule matches the given DICOM tag

        Notes
        -----
        It is possible for multiple rules to match. Lookup is always done from
        specific to general.
        For example, when getting a rule for tag (0010,0010):
        * A rule for (0010,0010) is preferred over (0010,00xx)
        * A rule for (0010,00xx) is preferred over (0010,xx10)
        * A rule for (0010,xx10) is preferred over (xxxx,0010)

        """
        # On single tags we can do efficient dictionary lookup

        if rule := self._single_tag_rules_dict.get(str(tag)):
            return rule

        #  found no specific rule for this tag. Try wildcard tags
        for group_rule in self._group_rules:
            if group_rule.matches(tag):
                return group_rule

        # nothing matches. There is no rule
        return None

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
        profile: Profile,
        bouncers: List[Bouncer] = None,
        safe_private: Optional[PrivateProcessor] = None,
        pixel_processor: Optional[PixelProcessor] = None,
    ):
        """

        Parameters
        ----------
        profile: Profile
            Defines what to do with each DICOM element (except PixelData)
        bouncers: List[Bouncer], optional
            Inspect all incoming data and can reject if it is deemed not fit for
            deidentification. For example rejecting encapsulated PDFs as they are
            too difficult to deidentify. Defaults to empty list (all data allowed)
        safe_private: Optional[PrivateProcessor],
            Defines what to do with private DICOM elements. Some might be safe under
            certain circumstances. Defaults to None
        pixel_processor: Optional[PrivateProcessor],
            Defines what to do with DICOM image data (the PixelData tag). Can remove
            or black out certain parts of an image. Defaults to None

        """
        self.profile = profile
        if not bouncers:
            bouncers = []
        self.bouncers = bouncers
        self.safe_private = safe_private
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
        # apply processors
        self.apply_bouncers(dataset)
        dataset = self.apply_pixel_processor(dataset)

        # add safe private rules and then flatten to get one rule per tag/group
        rules = self.profile.flatten(
            additional_rule_sets=self.get_safe_private_rules(dataset)
        )

        # define a function for walk() below
        def process_element(dataset_in: Dataset, data_element_in: DataElement):
            """Process element according to the rules in the outer scope"""

            # Find the rule to apply for this DICOM element
            rule = rules.get_rule(data_element_in.tag)

            if not rule:
                #  Keep tags for which there is no rule. Important decision
                return
            elif type(rule.operation) == Remove:
                del dataset_in[data_element_in.tag]
            else:
                rule.operation.apply(data_element_in)

        dataset.walk(process_element)

        return dataset

    def get_safe_private_rules(self, dataset) -> Optional[RuleList]:
        """Find any specific exceptions to the default 'remove all private tags'"""

        if self.safe_private:
            try:
                return self.safe_private.get_rule_set(dataset)
            except PrivateProcessorException as e:
                raise DeidentificationException(e)
        else:
            return None

    def apply_pixel_processor(self, dataset):
        """Put blackouts in image data if required"""

        if self.pixel_processor and self.pixel_processor.needs_cleaning(dataset):
            try:
                dataset = self.pixel_processor.clean_pixel_data(dataset)
            except PixelDataProcessorException as e:
                raise DeidentificationException(e)
        return dataset

    def apply_bouncers(self, dataset):
        """Check all bouncers to see whether dataset should be rejected"""

        for bouncer in self.bouncers:
            try:
                bouncer.inspect(dataset)
            except BouncerException as e:
                raise DeidentificationException(e)


class BouncerException(IDISCoreException):
    pass


class PrivateProcessorException(IDISCoreException):
    pass


class DeidentificationException(IDISCoreException):
    pass
