import pytest
from dicomgenerator.factory import CTDatasetFactory

from idiscore.core import DeidentificationException
from idiscore.defaults import create_default_core
from idiscore.validation import extract_signature


def test_default_core(a_safe_private_definition):
    core = create_default_core(safe_private_definition=a_safe_private_definition)

    core.deidentify(CTDatasetFactory())
    signature = extract_signature(deidentifier=core, dataset=CTDatasetFactory())
    assert len(signature) == 108

    with pytest.raises(DeidentificationException):
        # suspicious, but this type of dataset is not in a_safe_private_definition
        core.deidentify(CTDatasetFactory(Modality="US"))
