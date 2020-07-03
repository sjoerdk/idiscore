from idiscore.identifiers import PrivateTags, SingleTag
from idiscore.nema import ActionCodes, RawNemaRuleSet
from idiscore.operations import Clean, Remove


def test_raw_nema_rule_list():
    raw_list = RawNemaRuleSet(
        rules=(
            (SingleTag("PatientID"), ActionCodes.REMOVE),
            (PrivateTags(), ActionCodes.CLEAN),
        )
    )

    rule_set = raw_list.compile(
        action_mapping={ActionCodes.REMOVE: Remove(), ActionCodes.CLEAN: Clean()}
    )

    assert rule_set.as_dict()[SingleTag("PatientID")].operation.name == "Remove"
    assert rule_set.as_dict()[PrivateTags()].operation.name == "Clean"
