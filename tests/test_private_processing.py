import pytest
from dicomgenerator.factory import CTDatasetFactory
from pydicom.dataset import Dataset

from idiscore.identifiers import TagIdentifier
from idiscore.image_processing import CriterionException
from idiscore.private_processing import SafePrivateBlock


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


def test_private_definition_string(some_private_identifier_strings):
    """For convenience you can also init a SafePrivateBlock using strings"""
    block = SafePrivateBlock(tags=some_private_identifier_strings)
    assert all(
        [
            isinstance(x, TagIdentifier)
            for x in block.get_safe_private_tags(CTDatasetFactory())
        ]
    )


def test_private_definition_string_exception():
    """If initialise with rubbish a ValueError will be raised"""
    with pytest.raises(ValueError):
        SafePrivateBlock(tags=["not_a_private_block_tag"])
