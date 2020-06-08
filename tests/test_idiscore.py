#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `idiscore` package."""

import pytest
from dicomgenerator.factory import CTDatasetFactory


def test_idiscore():
    dataset = CTDatasetFactory()
    test = 1
