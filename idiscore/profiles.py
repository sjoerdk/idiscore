"""Profiles and rule sets to deidentify many dicom tags at once

Contains default implementations of the DICOM standard deidentification profiles and
options. Also some useful additions to this.
"""
from typing import Dict

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
from idiscore.nema import ActionCode, ActionCodes
from idiscore.operations import (
    Clean,
    Empty,
    GenerateUID,
    Keep,
    Operator,
    Remove,
    Replace,
)

# Maps action code in DICOM table E1-1 with actual python function
DEFAULT_MAPPING = {
    ActionCodes.DUMMY: Replace(),
    ActionCodes.EMPTY: Empty(),
    ActionCodes.REMOVE: Remove(),
    ActionCodes.KEEP: Keep(),
    ActionCodes.CLEAN: Clean(),
    ActionCodes.UID: GenerateUID(),
    ActionCodes.REPLACE_OR_DUMMY: Replace(),
    ActionCodes.REMOVE_OR_EMPTY: Remove(),
    ActionCodes.REMOVE_OR_DUMMY: Remove(),
    ActionCodes.REMOVE_OR_EMPTY_OR_DUMMY: Remove(),
    ActionCodes.REMOVE_OR_EMPTY_OR_UID: Remove(),
}


class DICOMProfiles:
    """Holds the DICOM deidentification profiles and options"""

    def __init__(self, action_mapping: Dict[ActionCode, Operator] = None):
        if action_mapping:
            mapping = DEFAULT_MAPPING.update(action_mapping)
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
