#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `idiscore` package."""
from typing import List

import pytest
from dicomgenerator.dicom import VRs
from dicomgenerator.factory import DataElementFactory
from factory import random
from pydicom.dataset import Dataset

from idiscore.operators import Clean, Hash, HashUID, SetFixedValue, TimeDeltaProvider


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


@pytest.fixture
def datetime_dataset():
    """A dataset for testing date and time management"""
    dataset = Dataset()
    elements = [
        DataElementFactory(tag="PatientBirthDate", value="19800501"),  # (0010, 0030)
        DataElementFactory(tag="AcquisitionDate", value="19800501"),  # (0008, 0022)
        DataElementFactory(
            tag="AcquisitionDateTime", value="19800501163601"
        ),  # (0008, 002a)
        DataElementFactory(tag="AcquisitionTime", value="163601"),
    ]  # (0008, 0032)]
    for element in elements:
        dataset.add(element)
    return dataset


def test_clean_date_basic(datetime_dataset):
    """By default, a random increment is taken from each date or time"""

    before = datetime_dataset["00100030"]
    assert (
        Clean().clean_date_time(element=before, dataset=datetime_dataset).value
        != before.value
    )


def test_clean_date_input(datetime_dataset):
    """Test date, datetime, time inputs"""
    clean = Clean()
    for element in datetime_dataset:
        before = element.value
        after = clean.clean_date_time(element=element, dataset=datetime_dataset).value
        assert clean.parse_date_time(before)[1] != clean.parse_date_time(after)[1]


def create_date_dataset(siuid: str, date: str) -> Dataset:
    """A dataset with a single PatientBirthDate and a StudyInstanceUID"""
    dataset = Dataset()
    dataset.add(DataElementFactory(tag="PatientBirthDate", value=date))  # (0010, 0030))
    dataset.StudyInstanceUID = siuid
    return dataset


@pytest.fixture
def two_series():
    date1 = "19800501"
    series1 = [
        create_date_dataset(siuid="001", date=date1),
        create_date_dataset(siuid="001", date=date1),
        create_date_dataset(siuid="001", date=date1),
    ]

    series2 = [
        create_date_dataset(siuid="002", date=date1),
        create_date_dataset(siuid="002", date=date1),
        create_date_dataset(siuid="002", date=date1),
    ]
    return series1, series2


def test_clean_date_input_per_study_instance(two_series):
    """Completely random date shuffling destroys a lot of information, and often
    makes a dataset unreadable, by for example destroying the acquisition time order
    within a series. To combat this but maintain deidentification, re-use the random
    date shift for datasets with the same StudyInstanceUID
    """

    series1, series2 = two_series
    clean = Clean()

    def assert_all_the_same_after_cleaning(datasets: List[Dataset]):
        """After cleaning all date values have been shifted the same amount"""
        cleaned = [clean.apply(x["00100030"], x) for x in datasets]
        first_value = cleaned[0].value
        for x in cleaned:
            if x.value != first_value:
                raise AssertionError(
                    f"value {x.value} is not the same as first" f" value {first_value}"
                )

    assert_all_the_same_after_cleaning(series1)
    assert_all_the_same_after_cleaning(series2)
    with pytest.raises(AssertionError):
        assert_all_the_same_after_cleaning(series1 + series2)


def test_time_delta_provider():
    dataset = Dataset()
    dataset.StudyInstanceUID = "123"

    delta_provider = TimeDeltaProvider()
    # should give the same result twice
    delta = delta_provider.get_delta(dataset)
    assert delta == delta_provider.get_delta(dataset)

    # but change for a new study
    dataset.StudyInstanceUID = "1234"
    delta2 = delta_provider.get_delta(dataset)
    assert delta2 != delta
    assert delta2 == delta_provider.get_delta(dataset)


def test_time_delta_provider_exception():
    """Without study information it is not possible to check which study this is"""
    dataset = Dataset()

    delta_provider = TimeDeltaProvider()

    # now the time shift is just random each time
    assert delta_provider.get_delta(dataset) != delta_provider.get_delta(dataset)


def test_hash_uid():
    """UID hashing x should always result in the same hash"""

    hash_uid = HashUID()
    element = DataElementFactory(tag="StudyInstanceUID")

    # hash should always be the same for the same input
    assert hash_uid.apply(element).value == hash_uid.apply(element).value
    # but different for different input
    assert (
        hash_uid.apply(element).value
        != hash_uid.apply(DataElementFactory(tag="StudyInstanceUID")).value
    )


def test_set_fixed_value():
    fixed_value = SetFixedValue(value="FIXED")
    assert (
        fixed_value.apply(DataElementFactory(tag="StudyDescription")).value == "FIXED"
    )

    # should be able to change the value after initialization
    fixed_value.value = 1
    assert fixed_value.apply(DataElementFactory(tag="StudyDescription")).value == 1
