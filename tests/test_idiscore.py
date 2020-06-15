#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `idiscore` package."""

import pytest
from dicomgenerator.factory import CTDatasetFactory
from pydicom.tag import Tag
from pydicom.uid import UID

from idiscore.idiscore import BlackOutDefinition, Core, Profile, Rule, RuleSet, \
    SafePrivateDefinition
from idiscore.operations import Hash


def test_idiscore():
    """Some basic operations"""

    core = Core(bouncers=[],
                profile=Profile(name='empty',
                                rule_sets=[
                                    RuleSet(name='test',
                                            rules={Rule(Tag('PatientID'),
                                                        Hash())})]),
                safe_private=SafePrivateDefinition(),
                black_out=BlackOutDefinition())
    a_dataset = CTDatasetFactory()
    deid = core.deidentify(a_dataset)
    test = 1
