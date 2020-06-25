# -*- coding: utf-8 -*-
from functools import total_ordering
from typing import Callable, Iterable, List, Optional, Union

from pydicom.dataelem import DataElement
from pydicom.dataset import Dataset
from pydicom.tag import Tag

from idiscore.exceptions import IDISCoreException
from idiscore.operations import Operator, Remove
from idiscore.imageprocessing import CriterionException, PixelProcessor


@total_ordering
class TagIdentifier:
    """Identifies a single DICOM tag or repeating group like (50xx,xxx)


    Using just DICOM tags is too limited for defining deidentification. We want
    to be able to represent for example:
    * all curves (50xx,xxxx)
    * a private tag with a variable group ([PrivateCreatorName]01,0010)
    """

    def matches(self, element: DataElement) -> bool:
        """The given element matches this identifier"""
        return False

    def key(self) -> str:
        """String used for comparison operators"""
        return str(id(self))

    #   Override comparisons to be able to compare and order different
    #   child classes
    def __le__(self, other):
        """Return ``True`` if `self`  is less than or equal to `other`"""
        return self.key() >= other.key()

    def __eq__(self, other):
        if isinstance(other, TagIdentifier):
            return self.key() == other.key()
        else:
            return False

    def __hash__(self):
        # TagIdentifiers are used as dictionary keys
        return hash(self.key())


class SingleTag(TagIdentifier):
    """Matches a single DICOM tag like (0010,0010) or 'PatientName'"""

    def __init__(self, tag: Tag):
        self.tag = tag

    def __str__(self):
        return str(self.tag)

    def matches(self, element: DataElement) -> bool:
        """The given element matches this identifier"""
        return element.tag == self.tag

    def key(self) -> str:
        return str(self.tag)


class RepeatingTag:
    """Dicom tag with x's in it to denote wildcards, like (50xx,xxxx) for curve data

    See http://dicom.nema.org/medical/dicom/current/output/chtml/part05/sect_7.6.html

    Notes
    -----
    I would prefer to take any pydicom way of working with repeater tags, but
    the current version of pydicom (2.0) only offers limited lookup support
    as far as I can see
    """

    def __init__(self, tag: str):
        # check input
        try:
            self.tag = RepeatingTag.parse_tag_string(tag)
        except ValueError as e:
            raise ValueError(
                f'Invalid format "{tag}":{e}. Examples of valid tag '
                f'strings: "(0010,xx10)", "0010,xx10", "0010xx10"'
            )

    def __str__(self):
        """Output format matches pydicom.tag.Tag.__str__()"""
        return f"({self.tag[:4]}, {self.tag[4:]})"

    @staticmethod
    def parse_tag_string(tag: str) -> str:
        """Cleans tag string and outputs it in standard format.
        Raises ValueError if tag is not of the correct format like
        (0010,10xx).

        Returns
        -------
        str
            standard format, 8 character hex string with 'x' for wildcard bytes.
            like 0010xx10 or 75f300xx
        """
        # remove potential brackets and comma. Make lower case to reduce clutter
        tag = tag.replace("(", "").replace(")", "").replace(",", "").lower()
        if len(tag) != 8:
            raise ValueError(f"Tag should be 8 characters long")
        # check whether this is a valid hex string if you discount the x's
        try:
            int(f'0x{tag.replace("x","0")}', 0)
        except ValueError:
            raise ValueError(f'Non "x" parts of this tag are not hexadecimal')

        return tag

    def as_mask(self) -> int:
        """Byte mask that can remove the byte positions that have value 'x'

        RepeatingTag('0010,xx10').as_mask() -> 0xffff00ff
        RepeatingTag('50xx,xxxx').as_mask() -> 0xff000000
        """
        hex_string = f"0x{''.join(map(lambda x: '0' if x=='x' else 'f', self.tag))}"
        return int(hex_string, 0)

    def static_component(self) -> int:
        """The int value of all bytes of this tag that are not 'x'
        RepeatingTag('0010,xx10').static_component() -> 0x00100010
        RepeatingTag('50xx,xxxx').static_component() -> 0x50000000
        """
        return int(f'0x{self.tag.replace("x", "0")}', 0)


class RepeatingGroup(TagIdentifier):
    """A DICOM tag where not all elements are filled. Like (50xx,xxxx)"""

    def __init__(self, tag: Union[str, RepeatingTag]):
        if isinstance(tag, str):
            tag = RepeatingTag(tag)
        self.tag = tag

    def __str__(self):
        return str(self.tag)

    def matches(self, element: DataElement) -> bool:
        """True if the element's tag matches the tag string, ignoring any part
        of the tag_string where there are x marks
        """
        # Following pydicom in using byte operations for this
        return element.tag & self.tag.as_mask() == self.tag.static_component()

    def key(self) -> str:
        """For sane sorting, make sure this matches the key format of other
        identifiers
        """
        return str(self.tag)


class Rule:
    """Defines what to do with a single DICOM element or single group of elements"""

    def __init__(self, identifier: TagIdentifier, operation: Operator):
        self.identifier = identifier
        self.operation = operation

    def __str__(self):
        return f"{self.identifier} - {self.operation}"


class RuleSet:
    """Defines what to do to one or more DICOM tags

    Models part of a deidentification procedure, such as the Basic Application
    Level Confidentiality Options in DICOM (e.g. Retain Safe Private Option)
    """

    def __init__(self, rules: Iterable[Rule], name: str = "RuleSet"):
        """

        Parameters
        ----------
        rules: Set[Rule]
            The rules comprising this set. Internally represented as Dict[Tag, Rule]
            for easier lookup
        name: str, optional
            Human readable name. Defaults to 'RuleSet'

        """

        self.rules_dict = {x.identifier: x for x in rules}
        self.name = name

    @property
    def rules(self) -> List[Rule]:
        return list(self.rules_dict.values())

    def get_rule(self, tag: Tag) -> Optional[Rule]:
        """Return the rule for the given DICOM tag, or None if not found"""
        return self.rules_dict.get(tag)

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

    def get_rule_set(self, dataset: Dataset) -> RuleSet:
        """Given this dataset, which private elements can be kept?

        Parameters
        ----------
        dataset: Dataset
            The DICOM dataset to inspect

        Returns
        -------
        RuleSet
            Rules for all private DICOM elements that are safe for the
            given dataset

        Raises
        ------
        PrivateProcessorException
            When rule set cannot be found properly
        """
        try:
            return RuleSet(
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

        # generate safe private ruleset for this dataset
        safe_private = self.safe_private.get_rule_set(dataset)

        # add safe private rules and then generate one ruleset for all
        rule_set = self.profile.flatten(additional_rule_sets=[safe_private])

        # run flattened profile (deidentify all tags). Maybe use walk with callback?
        def process_element(dataset_in: Dataset, data_element_in: DataElement):
            # Find the rule for this DICOM element
            rule = rule_set.get_rule(data_element_in.tag)

            # Handle special cases:
            if not rule or type(rule) == Remove:
                # Remove all tags that have no rule. The safe option.
                del dataset_in[data_element_in.tag]
            else:
                rule.operation.apply(data_element_in)

        dataset.walk(process_element)

        return dataset


class BouncerException(IDISCoreException):
    pass


class PrivateProcessorException(IDISCoreException):
    pass
