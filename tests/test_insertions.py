import pytest

from idiscore.insertions import get_idis_code_sequence
from idiscore.rule_sets import DICOMRuleSets


@pytest.fixture
def official_rule_sets():
    """A standard implementation of all DICOM rule sets"""

    return DICOMRuleSets()


def test_get_code_sequence(official_rule_sets):
    """Generate the element to add that describes how data has been deidentified"""
    sequence = get_idis_code_sequence(
        [
            official_rule_sets.basic_profile.name,
            official_rule_sets.retain_safe_private.name,
        ]
    )

    assert sequence.value[0] == "113100"  # should be values from Table CID 7050
    assert sequence.value[1] == "113111"


def test_get_code_sequence_exceptions(official_rule_sets):
    """Rule set names that cannot be recognized should raise exception"""

    with pytest.raises(ValueError) as e:
        get_idis_code_sequence(
            [official_rule_sets.basic_profile.name, "unknown option"]
        )
    assert "Could not find" in str(e)
