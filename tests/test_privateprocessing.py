from typing import List

import pytest
from dicomgenerator.factory import CTDatasetFactory
from pydicom.dataset import Dataset

from idiscore.identifiers import PrivateBlockTagIdentifier
from idiscore.imageprocessing import CriterionException
from idiscore.privateprocessing import SafePrivateDefinition


@pytest.fixture
def some_private_identifiers() -> List[PrivateBlockTagIdentifier]:
    return [
        PrivateBlockTagIdentifier("0023[SIEMENS MED SP DXMG WH AWS 1]10"),
        PrivateBlockTagIdentifier("0023[SIEMENS MED SP DXMG WH AWS 1]11"),
    ]


def test_private_definition(some_private_identifiers):
    """Define some private elements that are safe for CT"""

    safe_private = SafePrivateDefinition(
        tags=some_private_identifiers, criterion=lambda x: x.Modality == "CT",
    )

    assert len(safe_private.get_safe_private_tags(CTDatasetFactory())) == 2
    assert len(safe_private.get_safe_private_tags(CTDatasetFactory(Modality="US"))) == 0


def test_private_definition_no_criterion(some_private_identifiers):
    """Without a criterion tags are always considered safe"""

    safe_private = SafePrivateDefinition(tags=some_private_identifiers)

    assert len(safe_private.get_safe_private_tags(CTDatasetFactory())) == 2
    assert len(safe_private.get_safe_private_tags(CTDatasetFactory(Modality="US"))) == 2


def test_private_definition_exception(some_private_identifiers):
    """A criterion that cannot be computed"""

    # a criterion that checks Modality
    safe_private = SafePrivateDefinition(
        tags=some_private_identifiers, criterion=lambda x: x.Modality == "CT",
    )
    with pytest.raises(CriterionException):
        safe_private.get_safe_private_tags(Dataset())  # oh no! no modality!
