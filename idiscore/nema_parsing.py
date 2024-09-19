"""Encodes official NEMA information like Basic Application Level Confidentiality
Profile and Options as defined in table E1-1 here:
http://dicom.nema.org/medical/dicom/current/output/chtml/part15/sect_E.3.html
"""

from collections import namedtuple
from typing import Dict, List, Tuple

from idiscore.dicom import ActionCode
from idiscore.exceptions import IDISCoreError
from idiscore.identifiers import TagIdentifier
from idiscore.operators import Operator
from idiscore.rules import Rule, RuleSet

# The header name in table E1-1 for basic profile and options
# with codes from Table CID 7050 in PS3.16
# format: <header name>, <profile or option name>, <short_name>, <code>
NemaDeidMethodInfo = namedtuple(
    "NemaDeidMethodInfo", ["table_header", "full_name", "short_name", "code"]
)

E1_1_METHOD_INFO = [
    NemaDeidMethodInfo(
        "Basic Prof.",
        "Basic Application Level Confidentiality Profile",
        "basic_profile",
        "113100",
    ),
    NemaDeidMethodInfo(
        "Rtn. Safe Priv. Opt.",
        "Retain Safe Private Option",
        "retain_safe_private",
        "113111",
    ),
    NemaDeidMethodInfo("Rtn. UIDs Opt.", "Retain UIDs", "retain_uid", "113110"),
    NemaDeidMethodInfo(
        "Rtn. Dev. Id. Opt.",
        "Retain Device Identity Option",
        "retain_device_id",
        "113109",
    ),
    NemaDeidMethodInfo(
        "Rtn. Inst. Id. Opt.",
        "Retain Institution Identity Option",
        "retain_institution_id",
        "113112",
    ),
    NemaDeidMethodInfo(
        "Rtn. Pat. Chars. Opt.",
        "Retain Patient Characteristics Option",
        "retain_patient_characteristics",
        "113108",
    ),
    NemaDeidMethodInfo(
        "Rtn. Long. Full Dates Opt.",
        "Retain Longitudinal Temporal Information with Full Dates Option",
        "retain_full_dates",
        "113106",
    ),
    NemaDeidMethodInfo(
        "Rtn. Long. Modif. Dates Opt.",
        "Retain Longitudinal Temporal Information with Modified Dates Option",
        "retain_modified_dates",
        "113107",
    ),
    NemaDeidMethodInfo(
        "Clean Desc. Opt.", "Clean Descriptors Option", "clean_descriptors", "113105"
    ),
    NemaDeidMethodInfo(
        "Clean Struct. Cont. Opt.",
        "Clean Structured Content Option",
        "clean_structured_content",
        "113104",
    ),
    NemaDeidMethodInfo(
        "Clean Graph. Opt.", "Clean Graphics Option", "clean_graphics", "113103"
    ),
    NemaDeidMethodInfo(  # This method is not in table E1-1, so no header name
        None, "Clean Pixel Data Option", "clean_pixeldata", "113101"
    ),
    NemaDeidMethodInfo(  # This method is not in table E1-1, so no header name
        None,
        "Clean Recognizable Visual Features Option",
        "clean_visual_features",
        "113102",
    ),
]


class RawNemaRuleSet:
    """Defines the action code from table E1-1 for each DICOM identifier

    'raw' because an action code is just a string and cannot be applied to a tag.
    This class defines an intermediate stage in parsing the DICOM confidentiality
    options. Each identifier has been parsed, but operations have not
    been assigned
    """

    def __init__(
        self, rules: List[Tuple[TagIdentifier, ActionCode]], name: str, code: str
    ):
        self.rules = rules
        self.name = name
        self.code = code

    def compile(self, action_mapping: Dict[ActionCode, Operator]) -> RuleSet:
        """Replace each action code (string) with actual operator (function)"""

        compiled = []
        for identifier, actioncode in self.rules:
            try:
                operation = action_mapping[actioncode]
            except KeyError as e:
                raise IDISCoreError(
                    f'Unknown actioncode "{actioncode}" I do not know which operation'
                    f" to add here"
                ) from e
            compiled.append(Rule(identifier=identifier, operation=operation))

        return RuleSet(rules=compiled, name=self.name)
