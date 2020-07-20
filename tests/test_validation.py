import pytest
from dicomgenerator.factory import CTDatasetFactory
from pydicom.tag import Tag

from idiscore.annotation import AnnotatedDataset, ContainsPII, MustNotChange
from idiscore.insertions import PATIENT_IDENTITY_REMOVED
from idiscore.validation import (
    Validation,
    extract_signature,
)
from idiscore.delta import Delta, DeltaStatusCodes


@pytest.fixture
def a_core(a_core_with_some_rules):
    """A dummy core with some rules and a tag insertion"""
    a_core_with_some_rules.insertions.append(PATIENT_IDENTITY_REMOVED)
    return a_core_with_some_rules


def test_validate(a_core, a_dataset):

    core_instance = a_core
    # create an example dataset with annotation that PatientName is bad
    example = AnnotatedDataset(
        description="example1",
        dataset=a_dataset,
        annotations=[
            ContainsPII(
                tag=Tag("PatientName"), explanation="This contains an actual name"
            ),
            MustNotChange(tag=Tag("PatientID"), explanation="Patient ID is needed"),
        ],
    )

    example2 = AnnotatedDataset(
        description="example2",
        dataset=a_dataset,
        annotations=[
            ContainsPII(
                tag=Tag("Modality"),
                explanation="Modality must not be known here for some reason",
            ),
            MustNotChange(tag=Tag("PatientID"), explanation="Patient ID is needed"),
        ],
    )

    example3 = AnnotatedDataset(
        description="example3",
        dataset=a_dataset,
        annotations=[
            ContainsPII(tag=Tag("PatientID"), explanation="This is a name! bad.")
        ],
    )

    validation = Validation(
        deidentifier=core_instance, examples=[example, example2, example3]
    )
    result = validation.run()
    summary = result.summarize()

    assert "2/3 failed" in summary


def test_signature(a_core, a_dataset):

    deltas = extract_signature(a_core, a_dataset)
    assert [x.status for x in deltas] == [
        DeltaStatusCodes.UNCHANGED,
        DeltaStatusCodes.CHANGED,
        DeltaStatusCodes.UNCHANGED,
        DeltaStatusCodes.REMOVED,
        DeltaStatusCodes.REMOVED,
        DeltaStatusCodes.REMOVED,
        DeltaStatusCodes.REMOVED,
        DeltaStatusCodes.CREATED,
    ]


def test_signature_leave_input_dataset_unaltered(a_core, a_dataset):
    """Make sure extracting a signature does not alter input dataset"""

    len_before = len(a_dataset)
    extract_signature(a_core, a_dataset)
    assert len(a_dataset) == len_before


def test_signature_include_each_element(a_core, a_dataset):
    """Make sure all DICOM elements in dataset get a delta"""

    deltas = extract_signature(a_core, a_dataset)
    assert len(deltas) == len(a_dataset) + 1  # +1 because a_core inserts 1 element


def test_signature_realistic_dataset(a_core):
    """Check with a realistic dataset. Nothing should crash"""
    deltas = extract_signature(a_core, CTDatasetFactory())
    assert len([x for x in deltas if x.has_changed()]) == 19


@pytest.mark.parametrize(
    "before, after, expected_status",
    [
        ("123", "123", DeltaStatusCodes.UNCHANGED),
        ("123", "dummy", DeltaStatusCodes.CHANGED),
        ("123", "", DeltaStatusCodes.EMPTIED),
        ("123", None, DeltaStatusCodes.REMOVED),
        (None, "123", DeltaStatusCodes.CREATED),
    ],
)
def test_delta(before, after, expected_status):

    assert (
        Delta(tag=Tag("PatientID"), before=before, after=after).status
        == expected_status
    )
