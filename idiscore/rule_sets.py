"""Common sets of rules to deidentify multiple dicom elements

Contains default implementations of the DICOM standard deidentification profiles and
options and other useful sets
"""
from typing import Dict, Optional

from idiscore._public_dicom import (
    basic_profile,
    clean_descriptors,
    clean_graphics,
    clean_structured_content,
    retain_device_id,
    retain_full_dates,
    retain_institution_id,
    retain_modified_dates,
    retain_patient_characteristics,
    retain_safe_private,
    retain_uid,
)
from idiscore.dicom import ActionCode, ActionCodes
from idiscore.operators import (
    Clean,
    Empty,
    HashUID,
    Keep,
    Operator,
    Remove,
    Replace,
)

# Dict[ActionCode, Operator]
# Determines what function apply for each of the action codes in DICOM table E1-1
DEFAULT_MAPPING = {
    ActionCodes.DUMMY: Replace(),
    ActionCodes.EMPTY: Empty(),
    ActionCodes.REMOVE: Remove(),
    ActionCodes.KEEP: Keep(),
    ActionCodes.CLEAN: Clean(),
    ActionCodes.UID: HashUID(),
    ActionCodes.EMPTY_OR_DUMMY: Empty(),
    ActionCodes.REPLACE_OR_DUMMY: Replace(),
    ActionCodes.REMOVE_OR_EMPTY: Remove(),
    ActionCodes.REMOVE_OR_DUMMY: Remove(),
    ActionCodes.REMOVE_OR_EMPTY_OR_DUMMY: Remove(),
    ActionCodes.REMOVE_OR_EMPTY_OR_UID: Remove(),
}


class DICOMRuleSets:
    """Holds the rule sets for DICOM deidentification basic profile and options

    These are lists of rules that implement the actions designated in table E3

    Notes
    -----
    More information on profile and options found here:
    http://dicom.nema.org/medical/dicom/current/output/chtml/part15/sect_E.3.html
    """

    def __init__(self, action_mapping: Optional[Dict[ActionCode, Operator]] = None):
        """

        Parameters
        ----------
        action_mapping: Optional[Dict[ActionCode, Operator]]
            Overrule the default Operator for each given action code. For example:

            >>> p = DICOMRuleSets(action_mapping={ActionCodes.CLEAN, MyCleaner()})
            >>> p.clean_descriptors.rules
            ...
            00 = {Rule} (0018, 4000) - MyCleaner
            01 = {Rule} (0018, 1400) - MyCleaner
            ...

        """
        if action_mapping:
            mapping = DEFAULT_MAPPING.copy()  # don't alter the original dict
            mapping.update(action_mapping)
        else:
            mapping = DEFAULT_MAPPING

        self.basic_profile = basic_profile.compile(mapping)
        self.retain_safe_private = retain_safe_private.compile(mapping)
        self.retain_uid = retain_uid.compile(mapping)
        self.retain_device_id = retain_device_id.compile(mapping)
        self.retain_institution_id = retain_institution_id.compile(mapping)
        self.retain_patient_characteristics = retain_patient_characteristics.compile(
            mapping
        )
        self.retain_full_dates = retain_full_dates.compile(mapping)
        self.retain_modified_dates = retain_modified_dates.compile(mapping)
        self.clean_descriptors = clean_descriptors.compile(mapping)
        self.clean_structured_content = clean_structured_content.compile(mapping)
        self.clean_graphics = clean_graphics.compile(mapping)
