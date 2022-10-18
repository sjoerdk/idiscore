from dicomgenerator.templates import CTDatasetFactory

from idiscore.defaults import create_default_core
from idiscore.validation import extract_signature


def test_default_core(a_safe_private_definition):
    core = create_default_core(safe_private_definition=a_safe_private_definition)

    core.deidentify(CTDatasetFactory())
    signature = extract_signature(deidentifier=core, dataset=CTDatasetFactory())
    assert len(signature) == 108
