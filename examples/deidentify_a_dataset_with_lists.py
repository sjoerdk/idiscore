"""How mark safe private tags and known PII locations"""

from idiscore.defaults import create_default_core
from idiscore.image_processing import PIILocation, PIILocationList, SquareArea
from idiscore.private_processing import SafePrivateBlock, SafePrivateDefinition

safe_private = SafePrivateDefinition(
    blocks=[
        SafePrivateBlock(
            tags=[
                "0023[SIEMENS MED SP DXMG WH AWS 1]10",
                "0023[SIEMENS MED SP DXMG WH AWS 1]11",
                "00b1[TestCreator]01",
                "00b1[TestCreator]02",
            ],
            criterion=lambda x: x.Modality == "CT",
            comment="Some test tags, only valid for CT datasets",
        ),
        SafePrivateBlock(
            tags=["00b1[othercreator]11", "00b1[othercreator]12"],
            comment="Some more test tags, without a criterion",
        ),
    ]
)

location_list = PIILocationList(
    [
        PIILocation(
            areas=[SquareArea(5, 10, 4, 12), SquareArea(0, 0, 20, 3)],
            criterion=lambda x: x.Rows == 265 and x.Columns == 512,
        ),
        PIILocation(
            areas=[SquareArea(0, 200, 4, 12)],
            criterion=lambda x: x.Rows == 265 and x.Columns == 712,
        ),
    ]
)

core = create_default_core(
    safe_private_definition=safe_private, location_list=location_list
)
