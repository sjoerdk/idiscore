from idiscore.profiles import DICOMProfiles


def test_compile_rule_list():
    profiles = DICOMProfiles()

    assert profiles.basic_profile
