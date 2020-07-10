# test saving an example as json
import json

from tests import RESOURCE_PATH

from dicomgenerator.factory import CTDatasetFactory, DataElementFactory
from pydicom.tag import Tag

from idiscore.annotation import (
    Annotation,
    AnnotatedDataset,
    ContainsPII,
    MustNotChange,
)


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
    element = DataElementFactory(tag="PatientName", value="WIMS^kees")
    annotation = ContainsPII(
        tag=element.tag, tag_info=str(element), explanation="This is an actual name",
    )

    json_str = json.dumps(annotation.to_dict(), indent=2)

    loaded = Annotation.from_dict(json.loads(json_str))
    assert annotation.tag == loaded.tag
    assert annotation.tag_info == loaded.tag_info
    assert annotation.explanation == loaded.explanation
    assert type(annotation) == type(loaded)


def test_annotated_dataset_serialization():
    """Annotated dataset should contain the dataset, annotations and a description"""
    dataset = CTDatasetFactory()

    annotated = AnnotatedDataset(
        dataset=dataset,
        annotations=[
            MustNotChange(
                tag=Tag("PatientID"), explanation="PatientID contains essential info"
            )
        ],
        description="a CT dataset with test annotations",
    )

    as_dict = annotated.to_dict()

    loaded = AnnotatedDataset.from_dict(as_dict)
    assert annotated.annotations[0].explanation == loaded.annotations[0].explanation
    assert annotated.description == loaded.description
    assert annotated.dataset == loaded.dataset


def test_annotated_dataset_load_save():
    """Test loading from file"""

    loaded = AnnotatedDataset.from_path(RESOURCE_PATH / "annotated_example.json")

    assert len(loaded.dataset) == 108
    assert loaded.annotations[0].key == "contains_pii"
