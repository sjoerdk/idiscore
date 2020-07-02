"""Encodes official NEMA information like Basic Application Level Confidentiality
Profile and Options as defined in table E1-1 here:
http://dicom.nema.org/medical/dicom/current/output/chtml/part15/sect_E.3.html

This module should model public DICOM information. Any additional information
such as default implementations for the action codes should be put in 'profiles.py'
"""
from collections import namedtuple
from typing import Dict, List, Tuple

from idiscore.core import Rule, RuleList
from idiscore.exceptions import IDISCoreException
from idiscore.identifiers import TagIdentifier
from idiscore.operations import Operator

ActionCode = namedtuple("ActionCode", ["key", "var_name"])


class ActionCodes:
    """NEMA specifications from table E1-1 of what to do with each tag

    Modelling these to lessen room for error and to make it easier to
    write this to disk
    """

    DUMMY = ActionCode("D", "DUMMY")  # replace with dummy
    EMPTY = ActionCode("Z", "EMPTY")  # replace with zero length
    REMOVE = ActionCode("X", "REMOVE")  # remove
    KEEP = ActionCode("K", "KEEP")  # keep
    CLEAN = ActionCode("C", "CLEAN")  # clean
    UID = ActionCode("U", "UID")  # replace with consistent UID
    REPLACE_OR_DUMMY = ActionCode("Z/D", "REPLACE_OR_DUMMY")  # Z unless D is
    # required for consistency
    REMOVE_OR_EMPTY = ActionCode("X/Z", "REMOVE_OR_EMPTY")  # X unless Z is
    # required for consistency
    REMOVE_OR_DUMMY = ActionCode("X/D", "REMOVE_OR_DUMMY")  # X unless D is
    # required for consistency
    REMOVE_OR_EMPTY_OR_DUMMY = ActionCode(
        "X/Z/D", "REMOVE_OR_EMPTY_OR_DUMMY"
    )  # X unless Z
    # or D is required
    REMOVE_OR_EMPTY_OR_UID = ActionCode(
        "X/Z/U*", "REMOVE_OR_EMPTY_OR_UID"
    )  # X unless Z or
    # U is required

    ALL = {
        DUMMY,
        EMPTY,
        REMOVE,
        KEEP,
        CLEAN,
        UID,
        REPLACE_OR_DUMMY,
        REMOVE_OR_EMPTY,
        REMOVE_OR_DUMMY,
        REMOVE_OR_EMPTY_OR_DUMMY,
        REMOVE_OR_EMPTY_OR_UID,
    }

    PER_STRING = {x.key: x for x in ALL}

    @classmethod
    def get_code(cls, key: str):
        """I've got a string. Which action code is this?"""
        try:
            return cls.PER_STRING[key]
        except KeyError:
            raise ValueError(
                f"Unknown action code '{key}'. I "
                f"know {','.join([str(x) for x in cls.ALL])}"
            )


# The header name in table E1-1 for basic profile and options
# format: <header name>, <profile or option name>, <short_name>
NemaProfile = namedtuple("NemaProfile", ["table_header", "full_name", "short_name"])

E1_1_HEADER_NAMES = [
    NemaProfile(
        "Basic Prof.",
        "Basic Application Level Confidentiality Profile",
        "basic_profile",
    ),
    NemaProfile(
        "Rtn. Safe Priv. Opt.", "Retain Safe Private Option", "retain_safe_private"
    ),
    NemaProfile("Rtn. UIDs Opt.", "Retain UIDs", "retain_uid"),
    NemaProfile(
        "Rtn. Dev. Id. Opt.", "Retain Device Identity Option", "retain_device_id"
    ),
    NemaProfile(
        "Rtn. Inst. Id. Opt.",
        "Retain Institution Identity Option",
        "retain_institution_id",
    ),
    NemaProfile(
        "Rtn. Pat. Chars. Opt.",
        "Retain Patient Characteristics Option",
        "retain_patient_characteristics",
    ),
    NemaProfile(
        "Rtn. Long. Full Dates Opt.",
        "Retain Longitudinal Temporal Information with Full Dates Option",
        "retain_full_dates",
    ),
    NemaProfile(
        "Rtn. Long. Modif. Dates Opt.",
        "Retain Longitudinal Temporal Information with Modified Dates Option",
        "retain_modified_dates",
    ),
    NemaProfile("Clean Desc. Opt.", "Clean Descriptors Option", "clean_descriptors"),
    NemaProfile(
        "Clean Struct. Cont. Opt.",
        "Clean Structured Content Option",
        "clean_structured_content",
    ),
    NemaProfile("Clean Graph. Opt.", "Clean Graphics Option", "clean_graphics"),
]


class RawNemaRuleList:
    """Defines the action code from table E1-1 for each DICOM identifier

    'raw' because an action code is just a string and cannot be applied to a tag.
    This class defines an intermediate stage in parsing the DICOM confidentiality
    options. Each identifier has been parsed, but operations have not
    been assigned
    """

    def __init__(self, rules=List[Tuple[TagIdentifier, ActionCode]], name: str = ""):
        self.rules = rules
        self.name = name

    def compile(self, action_mapping: Dict[ActionCode, Operator]) -> RuleList:
        """Replace each action code (string) with actual operator (function)"""

        compiled = []
        for identifier, actioncode in self.rules:
            try:
                operation = action_mapping[actioncode]
            except KeyError:
                raise IDISCoreException(
                    f'Unknown actioncode "{actioncode}" I do'
                    f" not know which operation add here"
                )
            compiled.append(Rule(identifier=identifier, operation=operation))

        return RuleList(rules=compiled, name=self.name)
