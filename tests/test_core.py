#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `idiscore` package."""

import pytest
from dicomgenerator.factory import CTDatasetFactory
from pydicom.tag import Tag
from pydicom.uid import UID

from idiscore.core import PixelProcessor, Core, Profile, Rule, RuleSet, \
    PrivateProcessor
from idiscore.operations import Hash


def test_idiscore():
    """Some basic operations"""

    core = Core(bouncers=[],
                profile=Profile(name='empty',
                                rule_sets=[
                                    RuleSet(name='test',
                                            rules={Rule(Tag('PatientID'),
                                                        Hash())})]),
                safe_private=PrivateProcessor(definitions=[]),
                pixel_processor=PixelProcessor(locations=[]))
    a_dataset = CTDatasetFactory()
    deid = core.deidentify(a_dataset)
    test = 1
