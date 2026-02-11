import pytest
from pydicom.dataset import Dataset

from idiscore.bouncers import (
    DatasetRejected,
    RejectEncapsulatedImageStorage,
    RejectKOGSPS,
    RejectNonStandardDicom,
    BouncerError,
    CriterionBouncer,
    determine_bouncer_results,
    PatchedDataset,
)
from idiscore.core import Core, DeidentificationError, Profile
from tests.factories import quick_dataset


def test_reject_non_standard():

    a_core = Core(profile=Profile(rule_sets=[]), bouncers=[RejectNonStandardDicom()])

    # this should not raise anything
    a_core.deidentify(quick_dataset(SOPClassUID="1.2.840.10008"))

    with pytest.raises(DeidentificationError):
        a_core.deidentify(quick_dataset(SOPClassUID="123"))


@pytest.mark.parametrize(
    "dataset",
    [
        quick_dataset(SOPClassUID="1.2.840.10008.1234"),  # Not a bad SOPClass
        quick_dataset(
            SOPClassUID="1.2.840.10008.5.1.4.1.1.11.1", SeriesDescription="Annotation"
        ),  # bad, but annotation
    ],
)
def test_reject_kogsps_pass(dataset):
    """Datasets that should be passed"""
    # should not raise exceptions
    assert Core(profile=Profile(rule_sets=[]), bouncers=[RejectKOGSPS()]).deidentify(
        dataset
    )


@pytest.mark.parametrize(
    "dataset",
    [
        quick_dataset(
            SOPClassUID="1.2.840.10008.5.1.4.1.1.11.1"
        ),  # Missing description
        quick_dataset(SeriesDescription="Annotation"),  # Missing SOPClassUID
        quick_dataset(
            SOPClassUID="1.2.840.10008.5.1.4.1.1.11.1",
            SeriesDescription="not_annotation",
        ),  # Wrong description
        quick_dataset(
            SOPClassUID="1.2.840.10008.5.1.4.1.1.88.59", SeriesDescription="Annotation"
        ),  # Description does not matter
    ],
)
def test_reject_kogsps_fail(dataset):
    """Datasets that should be rejected"""

    with pytest.raises(DeidentificationError):
        Core(profile=Profile(rule_sets=[]), bouncers=[RejectKOGSPS()]).deidentify(
            dataset
        )


@pytest.mark.parametrize(
    "dataset",
    [
        quick_dataset(SOPClassUID="1.2.840.10008.5.1.4.1.1.104.1"),  # pdf
        quick_dataset(SOPClassUID="1.2.840.10008.5.1.4.1.1.104.2"),  # csa
    ],
)
def test_reject_encapsulated_should_reject(dataset):
    """None of these should get through"""
    with pytest.raises(DatasetRejected):
        RejectEncapsulatedImageStorage().inspect(dataset)


def test_reject_encapsulated_should_reject_bouncer_error():
    """Not having enough info should also cause bouncing"""
    with pytest.raises(BouncerError):
        RejectEncapsulatedImageStorage().inspect(Dataset())  # too little information)


@pytest.mark.parametrize("dataset", [quick_dataset(SOPClassUID="123")])
def test_reject_encapsulated_should_pass(dataset):
    """These should not be a problem"""
    assert RejectEncapsulatedImageStorage().inspect(dataset) is None


def test_split_bouncer_results():
    """Just run this method through its paces. See method for description"""

    bouncers = [
        CriterionBouncer(
            "Modality.equals('US') and " "not BurnedInAnnotation.equals('NO')"
        ),
        CriterionBouncer("Modality.equals('CT')", "We just don't like CT"),
    ]

    # criterion 2 will just reject any CT
    with pytest.raises(DatasetRejected):
        determine_bouncer_results(bouncers, quick_dataset(Modality="CT"))

    # an ultrasound is not trusted but might be OK after cleaning. Return
    maybe_ok = determine_bouncer_results(bouncers, quick_dataset(Modality="US"))
    assert maybe_ok[0] == bouncers[0]

    # a different scan, not in bouncers, will just be accepted, no maybe
    maybe_ok = determine_bouncer_results(bouncers, quick_dataset(Modality="PT"))
    assert not maybe_ok


def test_patched_dataset():
    dataset = quick_dataset(Modality="US", PatientName="name")
    assert dataset.Modality == "US"
    assert dataset.PatientName == "name"

    with PatchedDataset(
        dataset=dataset, patch={"Modality": "CT", "PatientID": "123"}
    ) as patched:
        assert patched.Modality == "CT"  # should have been changed
        assert patched.PatientName == "name"  # should have been untouched
        assert patched.PatientID == "123"  # should have been added

    assert dataset.Modality == "US"  # should have changed back
    assert dataset.PatientName == "name"  # should still be there
    assert patched.get("PatientID") is None  # should not exist any more
