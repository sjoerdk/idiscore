from dicomgenerator.factory import CTDatasetFactory

from idiscore.identifiers import PrivateBlockTagIdentifier, TagIdentifier
from idiscore.privateprocessing import SafePrivateDefinition


def test_private_definition():
    """Define some private functions"""

    safe_private = SafePrivateDefinition(
        tags=[
            PrivateBlockTagIdentifier("01[SIEMENS MED SP DXMG WH AWS 1]0019"),
            PrivateBlockTagIdentifier("02[SIEMENS MED SP DXMG WH AWS 1]0019"),
        ],
        criterion=lambda x: x.Modality == "CT",
    )

    tags = safe_private.get_safe_private_tags(CTDatasetFactory())
    test = 1
