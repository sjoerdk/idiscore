from typing import Dict, Iterable, Optional, Set, Union

from pydicom.dataelem import DataElement
from pydicom.tag import BaseTag

from idiscore.identifiers import SingleTag, TagIdentifier
from idiscore.operators import Operator


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

    def as_human_readable(self) -> str:
        return f"{self.identifier.name()} - {self.identifier} - {self.operation}"

    def number_of_matchable_tags(self) -> int:
        """The number of distinct DICOM tags that this rule could match"""
        return self.identifier.number_of_matchable_tags()

    def matches(self, element: DataElement) -> bool:
        """True if this rule matches the given DICOM element"""
        return self.identifier.matches(element)


class RuleSet:
    """Defines what to do to one or more DICOM tags

    Models part of a deidentification procedure, such as the Basic Application
    Level Confidentiality Options in DICOM (e.g. Retain Safe Private Option)
    """

    def __init__(self, rules: Iterable[Rule], name: str = "RuleSet"):
        """

        Parameters
        ----------
        rules: Iterable[Rule]
            The rules comprising this set
        name: str, optional
            Human readable name. Defaults to 'RuleSet'
        """

        # keep single tag rules separately for more efficient matching
        self._single_tag_rules_dict = {
            x.identifier.key(): x for x in rules if self.is_single_tag_rule(x)
        }

        # wildcard rules
        self._group_rules = [x for x in rules if not self.is_single_tag_rule(x)]
        # match most specific group rules first
        self._group_rules.sort(key=lambda x: x.number_of_matchable_tags())

        self.name = name

    @property
    def rules(self) -> Set[Rule]:
        """All rules in this list"""
        return set(self._single_tag_rules_dict.values()) | set(self._group_rules)

    def as_dict(self) -> Dict[TagIdentifier, Rule]:
        return {x.identifier: x for x in self.rules}

    def remove(self, rule: Rule):
        """Remove the given rule from this set

        Raises
        ------
        KeyError
            If rule is not in this set
        """
        if rule in self._group_rules:
            self._group_rules.remove(rule)
        elif (key := rule.identifier.key()) in self._single_tag_rules_dict:
            self._single_tag_rules_dict.pop(key)
        else:
            raise KeyError(f"{rule} is not in this RuleSet")

    @staticmethod
    def is_single_tag_rule(rule: Rule) -> bool:
        """Targets only a single DICOM tag"""
        return isinstance(rule.identifier, SingleTag)

    def get_rule(self, element: DataElement) -> Optional[Rule]:
        """The most specific rule for the given DICOM element, or None if not found

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
        For example, when getting a rule for element with tag (0010,0010):

        * A rule for (0010,0010) is preferred over (0010,00xx)
        * A rule for (0010,00xx) is preferred over (0010,xx10)
        * A rule for (0010,xx10) is preferred over (xxxx,0010)

        Generality is determined by the `number_of_matchable_tags()` function
        of each rule. The more tags that could be matched, the more general
        the rule is
        """
        # On single tags we can do efficient dictionary lookup
        if rule := self._single_tag_rules_dict.get(self.tag_to_key(element.tag)):
            return rule

        #  found no specific rule for this tag. Try wildcard tags
        for group_rule in self._group_rules:
            if group_rule.matches(element):
                return group_rule

        # nothing matches. There is no rule
        return None

    @staticmethod
    def tag_to_key(tag: BaseTag) -> str:
        """Represent tag as single 8 char hex string like '00100010'

        This is the format used as dict key internally
        """
        return f"{tag.group:04x}{tag.element:04x}"

    def as_human_readable_list(self) -> str:
        """All rules in this set sorted by tag name"""
        return "\n".join(sorted(x.as_human_readable() for x in self.rules))

    def __str__(self):
        return f'RuleSet "{self.name}"'
