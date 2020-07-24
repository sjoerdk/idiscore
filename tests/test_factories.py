import pytest

from tests.factories import quick_dataset


def test_quick_dataset():

    test = quick_dataset(PatientID=123, PatientName="Jack", StudyDescription="Test")
    assert test.PatientID == 123
    assert test.PatientName == "Jack"
    assert test.StudyDescription == "Test"

    with pytest.raises(ValueError):
        quick_dataset(unknown_tag="shouldfail")
