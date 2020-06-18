#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `idiscore` package."""
import pytest

from dicomgenerator.factory import CTDatasetFactory
from idiscore.core import Core, Profile, Rule, RuleSet, PrivateProcessor
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
    a_ruleset = RuleSet(rules={Rule(Tag("PatientID"), Hash())})
    core.profile.rule_sets.append(a_ruleset)

    before = a_dataset.PatientID
    assert len(a_dataset.items()) != 1  # dataset has many elements

    core.deidentify(a_dataset)
    # now the patientID should have been changed
    assert a_dataset.PatientID != before
    # and all other elements should have been removed
    assert len(a_dataset.items()) == 1


def test_profile_flatten():
    """A profile can have multiple rule sets, but with flatten you should end up
    with one rule per DICOM tag
    """
    hash_ptid = Rule(Tag("PatientID"), Hash())
    remove_ptid = Rule(Tag("PatientID"), Remove())
    keep_ptid = Rule(Tag("PatientID"), Keep())

    hash_ptname = Rule(Tag("PatientName"), Hash())

    set1 = RuleSet(name="initial set", rules={hash_ptid, hash_ptname})

    set2 = RuleSet(
        name="second set", rules={remove_ptid, Rule(Tag("Modality"), Remove())}
    )

    set3 = RuleSet(name="another set", rules={keep_ptid})

    profile = Profile(rule_sets=[set1, set2])

    # The PatientID rule of set2 should be chosen when flattening
    assert remove_ptid in profile.flatten().rules
    assert hash_ptid not in profile.flatten().rules

    # if another set is added, the rules from this should overrule earlier
    assert keep_ptid in profile.flatten(additional_rule_sets=[set3]).rules
    # but any original rule that was not overwritten should still be present
    assert hash_ptname in profile.flatten(additional_rule_sets=[set3]).rules
