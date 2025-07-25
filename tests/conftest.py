"""Loaded for each pytest. Contains fixtures shared by multiple tests"""
from typing import List

import pytest
from dicomgenerator.generators import DataElementFactory
from pydicom.dataset import Dataset
from pydicom.uid import CTImageStorage, ExplicitVRLittleEndian

from idiscore.core import Core, Profile
from idiscore.identifiers import (
    PrivateBlockTagIdentifier,
    PrivateTags,
    RepeatingGroup,
    SingleTag,
)
from idiscore.operators import Hash, Remove
from idiscore.private_processing import SafePrivateBlock, SafePrivateDefinition
from idiscore.rules import Rule, RuleSet


@pytest.fixture
def some_rules() -> List[Rule]:
    """Different types of Rules"""
    return [
        Rule(SingleTag("PatientName"), Hash()),
        Rule(RepeatingGroup("50xx,xxxx"), Remove()),
        Rule(PrivateTags(), Remove()),
    ]


@pytest.fixture
def a_core_with_some_rules(some_rules) -> Core:
    """Core instance with a three-rule profile"""
    return Core(profile=Profile([RuleSet(some_rules)]))


@pytest.fixture
def a_dataset() -> Dataset:
    """Tiny Dataset that can be used with some_rules and a_core_with_some_rules"""

    dataset = Dataset()
    dataset.add(DataElementFactory(tag="PatientID", value="12345"))
    dataset.add(DataElementFactory(tag="Modality", value="CT"))
    dataset.add(DataElementFactory(tag="PatientName", value="Martha"))
    dataset.add(
        DataElementFactory(tag=(0x5010, 0x3000), value=b"Sensitive data", VR="OB")
    )
    dataset.add(DataElementFactory(tag=(0x1013, 0x0001), value="private tag"))
    dataset.SOPInstanceUID = "1.2.3.4"
    dataset.ensure_file_meta()  # add if needed
    dataset.file_meta.MediaStorageSOPClassUID = CTImageStorage
    dataset.file_meta.MediaStorageSOPInstanceUID = dataset.SOPInstanceUID
    dataset.file_meta.TransferSyntaxUID = ExplicitVRLittleEndian

    block = dataset.private_block(0x00B1, "TestCreator", create=True)
    block.add_new(0x01, "SH", "my testvalue")
    return dataset


@pytest.fixture
def a_path_to_dataset(a_dataset, tmp_path):
    """Path to throw-away valid DICOM dataset"""
    # set most common options to allow saving to disk
    a_dataset.is_little_endian = True
    a_dataset.is_implicit_VR = False

    dataset_path = tmp_path / "datasets" / "a_dataset.dcm"
    dataset_path.parent.mkdir()

    a_dataset.save_as(dataset_path, write_like_original=False)

    return dataset_path


@pytest.fixture
def some_private_identifiers() -> List[PrivateBlockTagIdentifier]:
    return [
        PrivateBlockTagIdentifier("0023[SIEMENS MED SP DXMG WH AWS 1]10"),
        PrivateBlockTagIdentifier("0023[SIEMENS MED SP DXMG WH AWS 1]11"),
        PrivateBlockTagIdentifier("00b1[TestCreator]01"),
        PrivateBlockTagIdentifier("00b1[TestCreator]02"),
    ]


@pytest.fixture
def some_private_identifier_strings() -> List[str]:
    return [
        "0023[SIEMENS MED SP DXMG WH AWS 1]10",
        "0023[SIEMENS MED SP DXMG WH AWS 1]11",
        "00b1[TestCreator]01",
        "00b1[TestCreator]02",
    ]


@pytest.fixture
def a_ct_safe_private_definition(some_private_identifiers):
    """Some safe private rules that only apply to Modality=CT datasets"""
    return SafePrivateBlock(
        tags=some_private_identifiers,
        criterion=lambda x: x.Modality == "CT",
    )


@pytest.fixture
def a_safe_private_definition(a_ct_safe_private_definition):
    return SafePrivateDefinition(blocks=[a_ct_safe_private_definition])
