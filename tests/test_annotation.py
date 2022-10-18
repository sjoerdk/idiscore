# test saving an example as json
import json

from dicomgenerator.templates import CTDatasetFactory

from idiscore.annotation import (
    Annotation,
    ContainsPII,
    ExampleDataset,
    MustNotChange,
    annotate,
)
from idiscore.defaults import get_dicom_rule_sets
from tests import RESOURCE_PATH


def test_annotation_serialization():
    """Text representation should be something like this:

    (0008, 0023) Content Date - DA: '20121019'
        annotation: None
        reason: None

    (0010, 0010) Patient's Name - PN: 'Estey^Leah'
        annotation: contains_pii
        reason: A name is personally quite identifiable

    (7005, [TOSHIBA_MEC_CT3]0b) [Filter] UN: b'ORG '
        annotation: must_not_change
        reason: this toshiba private tag is needed for computing filter functions

    """
    annotation = ContainsPII(explanation="This is an actual name")

    json_str = json.dumps(annotation.to_json_dict(), indent=2)

    loaded = Annotation.from_json_dict(json.loads(json_str))
    assert annotation.explanation == loaded.explanation
    assert type(annotation) == type(loaded)


def test_annotated_dataset_serialization():
    """Annotated dataset should contain the dataset, annotations and a description"""
    dataset = CTDatasetFactory()

    annotated = ExampleDataset(
        dataset=dataset,
        annotations={
            "PatientID": MustNotChange(explanation="PatientID contains essential info")
        },
        description="a CT dataset with test annotations",
    )

    as_dict = annotated.to_json_dict()

    loaded = ExampleDataset.from_json_dict(as_dict)
    assert (
        annotated.get_annotation("PatientID").description
        == loaded.get_annotation("PatientID").description
    )
    assert annotated.description == loaded.description
    assert annotated.dataset == loaded.dataset


def test_annotated_dataset_load_save():
    """Test loading from file"""
    with open(RESOURCE_PATH / "annotated_example.json") as f:
        loaded = ExampleDataset.load(f)

    assert len(loaded.dataset) == 108
    assert loaded.get_annotation((0x0010, 0x0010)).explanation == "This is PII"


def test_annotate(a_dataset):
    example = ExampleDataset(dataset=a_dataset)
    profile = get_dicom_rule_sets().basic_profile
    assert len(example.annotations) == 0
    annotated = annotate(example, profile)
    assert len(annotated.annotations) == 6
