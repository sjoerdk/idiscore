import pytest

from idiscore.dataset import RequiredDataset, RequiredTagNotFound
from tests.factories import quick_dataset


def test_required_dataset():
    """A Dataset that raises specific exception for missing keys"""
    ds = quick_dataset(PatientID="1", Modality="CT")

    # this should work
    ds.PatientID
    ds["PatientID"]

    # this should not work
    with pytest.raises(AttributeError):
        ds.PatientName
    with pytest.raises(KeyError):
        ds["PatientName"]

    # with required dataset this should be the same exception
    with pytest.raises(RequiredTagNotFound):
        RequiredDataset(ds).PatientName
    with pytest.raises(RequiredTagNotFound):
        RequiredDataset(ds)["PatientName"]
