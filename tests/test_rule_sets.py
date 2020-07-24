from copy import deepcopy

import pytest
from dicomgenerator.factory import (
    CTDatasetFactory,
    DataElementFactory,
    DataElementFactory as DatEF,
)

from idiscore.core import Core, Profile
from idiscore.bouncers import RejectKOGSPS
from idiscore.identifiers import PrivateTags, RepeatingGroup, SingleTag
from idiscore.nema import ActionCodes
from idiscore.operators import Clean, Hash, Remove
from idiscore.rule_sets import DICOMRuleSets
from idiscore.rules import Rule, RuleSet


def test_compile_rule_list():
    """Just some basic initialization"""
    profiles = DICOMRuleSets()

    basic = profiles.basic_profile
    assert (
        basic.get_rule(DataElementFactory(tag="PatientName")).operation.name == "Empty"
    )
    assert basic.get_rule(DataElementFactory(tag="PatientID")).operation.name == "Empty"


def test_compile_rule_list_overrule_action_code():
    """You can overrule the function to call for an action code"""

    class CustomClean(Clean):
        name = "Custom"

    rule_sets = DICOMRuleSets(action_mapping={ActionCodes.CLEAN: CustomClean()})
    rules = rule_sets.clean_descriptors
    assert (
        rules.get_rule(DataElementFactory(tag=(0x0018, 0x4000))).operation.name
        == "Custom"
    )


def test_realistic_profile():
    """Run a file through a profile that has several options"""

    sets = DICOMRuleSets()
    profile = Profile(
        rule_sets=[
            sets.basic_profile,
            sets.clean_descriptors,
            sets.clean_graphics,
            sets.retain_modified_dates,
            sets.retain_safe_private,
        ]
    )

    final_set = profile.flatten()
    assert len(final_set.rules) == 442

    core = Core(profile=profile)
    dataset = CTDatasetFactory()
    original = deepcopy(dataset)
    deidentified = core.deidentify(dataset)

    assert original.PatientID != deidentified.PatientID


def test_rule_set():
    """Rule set should be able to find the proper rules for tags"""

    # some rules
    rule1 = Rule(SingleTag("PatientName"), Hash())
    rule2 = Rule(RepeatingGroup("50xx,xxxx"), Remove())
    rule3 = Rule(PrivateTags(), Remove())
    rules = RuleSet(rules=[rule1, rule2, rule3])

    assert rules.get_rule(DatEF(tag="PatientName")) == rule1
    assert rules.get_rule(DatEF(tag="Modality")) is None  # This rule is not defined
    assert rules.get_rule(DatEF(tag=(0x5000, 0x0001))) == rule2  # try a repeating rule
    assert (
        rules.get_rule(DatEF(tag=(0x1301, 0x0001))) == rule3
    )  # try a private tag rule


def test_rule_set_remove():

    # some rules
    rule1 = Rule(SingleTag("PatientName"), Hash())
    rule2 = Rule(RepeatingGroup("50xx,xxxx"), Remove())
    rule3 = Rule(PrivateTags(), Remove())
    rules = RuleSet(rules=[rule1, rule2, rule3])

    assert len(rules.as_dict()) == 3
    rules.remove(rule3)
    assert len(rules.as_dict()) == 2
    rules.remove(rule1)
    assert len(rules.as_dict()) == 1

    with pytest.raises(KeyError):
        rules.remove(rule3)

    with pytest.raises(KeyError):
        rules.remove(rule1)


def test_core_description():
    """Human readable answer to the question 'what does this deidentifier do?'"""

    sets = DICOMRuleSets()
    profile = Profile(
        rule_sets=[
            sets.basic_profile,
            sets.clean_descriptors,
            sets.clean_graphics,
            sets.retain_modified_dates,
            sets.retain_safe_private,
        ]
    )

    final_set = profile.flatten()
    assert len(final_set.rules) == 442

    core = Core(profile=profile, bouncers=[RejectKOGSPS])
    test = core.description()
    print(test)
