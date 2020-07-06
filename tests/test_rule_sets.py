from copy import deepcopy

from dicomgenerator.factory import CTDatasetFactory
from pydicom.tag import Tag

from idiscore.core import Core, Profile
from idiscore.nema import ActionCodes
from idiscore.operations import Clean
from idiscore.rule_sets import DICOMRuleSets


def test_compile_rule_list():
    """Just some basic initialization"""
    profiles = DICOMRuleSets()

    basic = profiles.basic_profile
    assert basic.get_rule(Tag("PatientName")).operation.name == "Empty"
    assert basic.get_rule(Tag("PatientID")).operation.name == "Empty"


def test_compile_rule_list_overrule_action_code():
    """You can overrule the function to call for an action code"""

    class CustomClean(Clean):
        name = "Custom"

    profiles = DICOMRuleSets(action_mapping={ActionCodes.CLEAN: CustomClean()})
    rules = profiles.clean_descriptors
    assert rules.get_rule(Tag(0x0018, 0x4000)).operation.name == "Custom"


def test_realistic_profile():
    """Run a file through a profile that has several options"""

    sets = DICOMRuleSets()
    profile = Profile(
        rule_sets=[
            sets.basic_profile,
            sets.clean_descriptors,
            sets.clean_graphics,
            sets.retain_modified_dates,
            sets.retain_safe_private,
        ]
    )

    final_set = profile.flatten()
    assert len(final_set.rules) == 432

    core = Core(profile=profile)
    dataset = CTDatasetFactory()
    original = deepcopy(dataset)
    deidentified = core.deidentify(dataset)

    assert original.PatientID != deidentified.PatientID
