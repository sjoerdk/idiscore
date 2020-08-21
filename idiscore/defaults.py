"""Default implementations of idiscore objects and convenience functions"""
from idiscore.bouncers import RejectEncapsulatedImageStorage, RejectNonStandardDicom
from idiscore.core import Core, Profile
from idiscore.image_processing import PIILocationList, PixelProcessor
from idiscore.insertions import (
    PATIENT_IDENTITY_REMOVED,
    get_deidentification_method,
    get_idis_code_sequence,
)
from idiscore.nema import ActionCodes
from idiscore.operators import Clean
from idiscore.private_processing import SafePrivateDefinition
from idiscore.rule_sets import DICOMRuleSets


def create_default_core(
    safe_private_definition: SafePrivateDefinition = None,
    location_list: PIILocationList = None,
) -> Core:
    """A deidentification core with the following profile:

    * basic_profile
    * clean_descriptors
    * retain_patient_characteristics
    * retain_device_id
    * retain_safe_private

    Which rejects non-standard dicom and encapsulated pdfs
    and inserts some tags that indicate deidentification has been performed

    Parameters
    ----------
    safe_private_definition: SafePrivateDefinition, optional
        Which private tags are safe to keep. Defaults to keeping none
    location_list: PIILocationList, optional
        Definition of where to remove burnt in information from images.
        Defaults to simply rejecting all datasets that might have burnt in
        information

    """
    clean = Clean(safe_private=safe_private_definition)
    sets = DICOMRuleSets(action_mapping={ActionCodes.CLEAN: clean})
    profile = Profile(  # Choose which rule sets to use
        rule_sets=[
            sets.basic_profile,
            sets.clean_descriptors,
            sets.retain_patient_characteristics,
            sets.retain_device_id,
            sets.retain_safe_private,
        ]
    )
    # insert some info on what type of deidentification was performed
    insertions = [
        get_idis_code_sequence([x.name for x in profile.rule_sets]),
        PATIENT_IDENTITY_REMOVED,
        get_deidentification_method(),
    ]

    bouncers = [RejectEncapsulatedImageStorage(), RejectNonStandardDicom()]

    core = Core(
        profile=profile,
        insertions=insertions,
        bouncers=bouncers,
        pixel_processor=PixelProcessor(PIILocationList(location_list)),
    )

    return core
