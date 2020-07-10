"""Loaded for each pytest. Contains fixtures shared by multiple tests"""
from typing import List

import pytest
from dicomgenerator.factory import DataElementFactory
from pydicom.dataset import Dataset

from idiscore.core import Core, Profile, Rule, RuleSet
from idiscore.identifiers import PrivateTags, RepeatingGroup, SingleTag
from idiscore.operations import Hash, Remove


@pytest.fixture
def some_rules() -> List[Rule]:
    """Different types of Rules"""
    return [
        Rule(SingleTag("PatientName"), Hash()),
        Rule(RepeatingGroup("50xx,xxxx"), Remove()),
        Rule(PrivateTags(), Remove()),
    ]


@pytest.fixture
def a_core_with_some_rules(some_rules) -> Core:
    """Core instance with a three-rule profile"""
    return Core(profile=Profile([RuleSet(some_rules)]))


@pytest.fixture
def a_dataset() -> Dataset:
    """Tiny Dataset that can be used with some_rules and a_core_with_some_rules"""

    dataset = Dataset()
    dataset.add(DataElementFactory(tag="PatientID", value="12345"))
    dataset.add(DataElementFactory(tag="Modality", value="CT"))
    dataset.add(DataElementFactory(tag="PatientName", value="Martha"))
    dataset.add(DataElementFactory(tag=(0x5010, 0x3000), value=b"Sensitive data"))
    dataset.add(DataElementFactory(tag=(0x1013, 0x0001), value=b"private tag"))
    return dataset
