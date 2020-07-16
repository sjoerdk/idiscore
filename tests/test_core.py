#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `idiscore` package."""

import pytest
from dicomgenerator.factory import DataElementFactory as DatEF

from pydicom.tag import Tag

from idiscore.core import Core, Profile
from idiscore.rules import Rule, RuleSet
from idiscore.identifiers import PrivateTags, RepeatingGroup, SingleTag
from idiscore.operations import Hash, Keep, Remove
from idiscore.validation import extract_signature


def test_idiscore_deidentify_basic(a_dataset, a_core_with_some_rules):
    """Send a dataset trough a full Core instance"""

    # check before processing
    assert Tag(0x5010, 0x3000) in a_dataset
    assert Tag(0x1013, 0x0001) in a_dataset
    assert a_dataset.PatientID == "12345"
    assert a_dataset.PatientName == "Martha"
    assert len(a_dataset.items()) == 7

    # now apply the rules to the dataset
    core = a_core_with_some_rules
    deidentified = core.deidentify(a_dataset)

    # check whether that worked as expected
    assert Tag(0x5010, 0x3000) not in deidentified  # removed by 50xx,xxxx rule
    assert Tag(0x1013, 0x0001) not in deidentified  # removed by PrivateTags() rule
    assert deidentified.PatientID == "12345"  # not touched. No rule for this
    assert deidentified.PatientName != "Martha"  # should have been hashed
    assert len(deidentified.items()) == 3


@pytest.fixture
def some_pid_rules():
    return [
        Rule(SingleTag("PatientID"), Hash()),
        Rule(SingleTag("PatientID"), Remove()),
        Rule(SingleTag("PatientID"), Keep()),
    ]


def test_profile_flatten(some_pid_rules):
    """A profile can have multiple rule sets, but with flatten you should end up
    with one rule per DICOM tag
    """
    hash_name = Rule(SingleTag("PatientName"), Hash())

    # initial set
    set1 = RuleSet(rules=[some_pid_rules[0], hash_name])
    # set with a different rule for PatientID
    set2 = RuleSet(rules=[some_pid_rules[1], Rule(SingleTag("Modality"), Remove())])

    profile = Profile(rule_sets=[set1, set2])

    # The PatientID rule of set2 should be chosen when flattening
    assert some_pid_rules[1] in profile.flatten().rules
    assert some_pid_rules[0] not in profile.flatten().rules

    # if another set is added, the rules from this should overrule earlier
    set3 = RuleSet(name="another set", rules=[some_pid_rules[2]])
    assert some_pid_rules[2] in profile.flatten(additional_rule_sets=[set3]).rules
    # but any original rule that was not overwritten should still be present
    assert hash_name in profile.flatten(additional_rule_sets=[set3]).rules


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


def test_rule_precedence():
    """Rules are applied in order of generality - most specific first. Verify"""

    # Some rules with a potentially ambivalent order
    rule_a = Rule(PrivateTags(), Remove())  # Remove all private tags
    rule_b = Rule(Tag(0x1301, 0x0000), Keep())  # but keep this private tag
    rule_c = Rule(RepeatingGroup("50xx,xxxx"), Hash())  # match all these
    rule_d = Rule(Tag(0x5002, 0x0002), Keep())  # but specifically remove this
    rule_e = Rule(SingleTag("PatientName"), Hash())  # and one regular rule
    rules = RuleSet(rules=[rule_a, rule_b, rule_c, rule_d, rule_e])

    # now in all these cases, the most specific rule should be returned:
    assert rules.get_rule(DatEF(tag=(0x1301, 0x0000))) == rule_b  # also matches a
    assert rules.get_rule(DatEF(tag=(0x5002, 0x0002))) == rule_d  # also matches c
    assert rules.get_rule(DatEF(tag=(0x5002, 0x0001))) == rule_c
    assert rules.get_rule(DatEF(tag=(0x5001, 0x0001))) == rule_c  # also matches a
    assert rules.get_rule(DatEF(tag=(0x0010, 0x0010))) == rule_e
    assert rules.get_rule(DatEF(tag="Modality")) is None

    # For rules with identical generality, just keep the order of input
    rule_1 = Rule(RepeatingGroup("50xx,xxxx"), Hash())
    rule_2 = Rule(RepeatingGroup("xx10,xxxx"), Hash())
    rules = RuleSet(rules=[rule_1, rule_2])

    assert rules.get_rule(DatEF(tag=(0x5010, 0x0000))) == rule_1  # also matches a
    assert rules.get_rule(DatEF(tag=(0x5110, 0x0000))) == rule_2  # also matches a


def test_rule_set_human_readable(some_rules):

    as_string = RuleSet(some_rules).as_human_readable_list()
    assert "PatientName - (0010, 0010)" in as_string
    assert "Unknown Repeater tag" in as_string


def test_core_deidentify_safe_private(a_dataset, a_private_processor):
    """In core, rules for each safe private tag are added before processing all
    rules in the profile.
    This should only be done if the profile contains a rule PrivateTags() -> Clean()
    """

    rules = [
        Rule(SingleTag("PatientID"), Hash()),
        Rule(PrivateTags(), Remove()),
    ]  # Remove all private tags

    core = Core(profile=Profile([RuleSet(rules)]), safe_private=a_private_processor)

    # now apply the rules to the dataset an check changes
    deltas = extract_signature(deidentifier=core, dataset=a_dataset)

    assert {x.tag: x for x in deltas}[Tag("000b0010")].status == "REMOVED"
