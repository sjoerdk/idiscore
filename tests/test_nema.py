from idiscore.identifiers import PrivateTags, SingleTag
from idiscore.nema import ActionCodes, RawNemaRuleList
from idiscore.operations import Clean, Remove


def test_raw_nema_rule_list():
    raw_list = RawNemaRuleList(
        rules=(
            (SingleTag("patientID"), ActionCodes.REMOVE),
            (PrivateTags(), ActionCodes.CLEAN),
        )
    )

    rule_list = raw_list.compile(
        action_mapping={ActionCodes.REMOVE: Remove(), ActionCodes.CLEAN: Clean()}
    )

    assert rule_list.rules[0].operation.name == "Remove"
    assert rule_list.rules[1].operation.name == "Clean"
