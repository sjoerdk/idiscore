#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `idiscore` package."""
import pytest

from dicomgenerator.factory import CTDatasetFactory, DataElementFactory
from idiscore.core import (
    Core,
    Profile,
    Rule,
    RuleList,
    PrivateProcessor,
)
from idiscore.identifiers import RepeatingGroup, RepeatingTag, SingleTag
from idiscore.imageprocessing import PixelProcessor
from idiscore.operations import Hash, Keep, Remove
from pydicom.dataset import Dataset
from pydicom.tag import Tag


@pytest.fixture
def an_empty_core() -> Core:
    """A deidentification core instance that is empty in all respects. Contains
    a profile with no rule sets, PrivateProcessor with no defintions etc

    Fully functional, but will result in only empty
    """
    return Core(
        bouncers=[],
        profile=Profile(rule_sets=[]),
        safe_private=PrivateProcessor(definitions=[]),
        pixel_processor=PixelProcessor(locations=[]),
    )


@pytest.fixture
def a_dataset() -> Dataset:
    """A realistic mock CT dataset"""
    return CTDatasetFactory()


def test_idiscore_deidentify_basic(an_empty_core, a_dataset):
    """Some basic integration test-like operations"""
    core = an_empty_core

    # Have a single rule to hash the patientID
    a_ruleset = RuleList(rules={Rule(Tag("PatientID"), Hash())})
    core.profile.rule_sets.append(a_ruleset)

    before = a_dataset.PatientID
    assert len(a_dataset.items()) != 1  # dataset has many elements

    core.deidentify(a_dataset)
    # now the patientID should have been changed
    assert a_dataset.PatientID != before
    # and all other elements should have been removed
    assert len(a_dataset.items()) == 1


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
    set1 = RuleList(rules={some_pid_rules[0], hash_name})
    # set with a different rule for PatientID
    set2 = RuleList(rules={some_pid_rules[1], Rule(SingleTag("Modality"), Remove())})

    profile = Profile(rule_sets=[set1, set2])

    # The PatientID rule of set2 should be chosen when flattening
    assert some_pid_rules[1] in profile.flatten().rules
    assert some_pid_rules[0] not in profile.flatten().rules

    # if another set is added, the rules from this should overrule earlier
    set3 = RuleList(name="another set", rules={some_pid_rules[2]})
    assert some_pid_rules[2] in profile.flatten(additional_rule_sets=[set3]).rules
    # but any original rule that was not overwritten should still be present
    assert hash_name in profile.flatten(additional_rule_sets=[set3]).rules


def test_identifier_comparison():
    """Tag Identifiers are hashable and should be sortable as well"""
    # these should equal each other
    assert SingleTag(tag=Tag("PatientID")) == SingleTag(tag=Tag("PatientID"))
    # You can use any initialization that pydicom.tag.Tag allows, still equal
    assert SingleTag(tag=Tag(0x0010, 0x0020)) == SingleTag(tag=Tag("PatientID"))

    assert RepeatingGroup(tag="0010,10xx") == RepeatingGroup(tag="0010,10xx")

    # it should be possible to sort them as well
    taglist = [
        SingleTag(tag=Tag("0020000e")),
        SingleTag(tag=Tag("00100020")),
        RepeatingGroup(tag="001010xx"),
    ]

    taglist.sort(reverse=True)
    assert str(taglist[1]) == "(0010, 10xx)"


def test_identifier_matching():

    repeater = RepeatingGroup("50xx,xxxx")
    assert repeater.matches(DataElementFactory(tag="50100040"))
    assert repeater.matches(DataElementFactory(tag="50ef3340", VR="LO"))
    assert not repeater.matches(DataElementFactory(tag="51ef3340", VR="LO"))

    repeater2 = RepeatingGroup("0010,10xx")
    assert repeater2.matches(DataElementFactory(tag="00101000"))
    assert repeater2.matches(DataElementFactory(tag="001010ef", VR="LO"))
    assert not repeater2.matches(DataElementFactory(tag="001011ef", VR="LO"))


@pytest.mark.parametrize(
    "tag_string",
    [
        "50xx,xxxx",
        "50xxxxxx",  # comma is optional
        "(50xx,xxxx)",  # so are parenthesis
        "100e,10xx",  # characters hex or 'x'
        "FF10,XXXX",  # case does not matter
    ],
)
def test_repeating_tag_format(tag_string):
    """Valid string for initializing a RepeatingTag"""
    RepeatingTag(tag_string)


@pytest.mark.parametrize(
    "tag_string",
    [
        "50xx,xxxxx",  # too long
        "50xx,xxx",  # too short
        "50xRxxxx",  # strange characters
    ],
)
def test_repeating_tag_format_exceptions(tag_string):
    """Invalid string for initializing a RepeatingTag. These should not work"""
    with pytest.raises(ValueError):
        RepeatingTag(tag_string)


def test_repeating_tag_masks():
    """Just checking the byte fiddling that RepeatingTag does"""
    assert hex(RepeatingTag("00xx,23e3").as_mask()) == hex(0xFF00FFFF)
    assert hex(RepeatingTag("(00xx,23e3)").as_mask()) == hex(0xFF00FFFF)
    assert hex(RepeatingTag("(0034,23e3)").as_mask()) == hex(0xFFFFFFFF)
    assert hex(RepeatingTag("(50xx,xxxx)").as_mask()) == hex(0xFF000000)

    assert hex(RepeatingTag("00xx,23e3").static_component()) == hex(0x000023E3)
    assert hex(RepeatingTag("50xx,xxxx").static_component()) == hex(0x50000000)
