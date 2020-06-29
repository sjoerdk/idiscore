"""Profiles and rule sets to deidentify many dicom tags at once

Contains default implementations of the DICOM standard deidentification profiles and
options. Also some useful additions to this.
"""
from typing import Dict

from idiscore._public_dicom import basic_profile
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
