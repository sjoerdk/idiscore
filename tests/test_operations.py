#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `idiscore` package."""

import pytest
from dicomgenerator.dicom import VRs
from dicomgenerator.factory import DataElementFactory
from factory import random

from idiscore.operators import Clean, Hash


@pytest.fixture
def fix_random_seed():
    """Make sure tests using Faker will have reproducible results"""
    random.reseed_random("fixed seed")


def test_operations():
    """Basic functions of element operations"""
    operation = Hash()

    # Hashing a string-like thing should work.
    element = DataElementFactory(tag="PatientName")
    operation.apply(element)

    # You can also ride roughshod over DICOM VRs, putting a hex value into a
    # numeric VR element. We're not here to police currently
    element = DataElementFactory(tag="Columns")
    operation.apply(element)


def test_clean():
    """Tricky operation, this clean. Test some cases"""
    clean = Clean()
    element = DataElementFactory(tag="AcquisitionDate")
    before = element.value
    result = clean.apply(DataElementFactory(tag="AcquisitionDate"))
    assert result.value != before

    # Other VRs cannot be cleaned currently
    with pytest.raises(ValueError):
        clean.apply(DataElementFactory(tag="(00ee,e324)", VR=VRs.Unknown))
