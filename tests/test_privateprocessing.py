import pytest
from dicomgenerator.factory import CTDatasetFactory
from pydicom.dataset import Dataset

from idiscore.imageprocessing import CriterionException
from idiscore.privateprocessing import SafePrivateBlock


def test_private_definition(a_ct_safe_private_definition):
    """Define some private elements that are safe for CT"""

    assert (
        len(a_ct_safe_private_definition.get_safe_private_tags(CTDatasetFactory())) == 4
    )
    assert (
        len(
            a_ct_safe_private_definition.get_safe_private_tags(
                CTDatasetFactory(Modality="US")
            )
        )
        == 0
    )


def test_private_definition_no_criterion(some_private_identifiers):
    """Without a criterion tags are always considered safe"""

    safe_private = SafePrivateBlock(tags=some_private_identifiers)

    assert len(safe_private.get_safe_private_tags(CTDatasetFactory())) == 4
    assert len(safe_private.get_safe_private_tags(CTDatasetFactory(Modality="US"))) == 4


def test_private_definition_exception(a_ct_safe_private_definition):
    """A criterion that cannot be computed"""

    with pytest.raises(CriterionException):
        a_ct_safe_private_definition.get_safe_private_tags(Dataset())  # no modality!
