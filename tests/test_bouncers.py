import pytest

from idiscore.bouncers import RejectKOGSPS, RejectNonStandardDicom
from idiscore.core import Core, DeidentificationException, Profile
from tests.factories import quick_dataset


def test_reject_non_standard():

    a_core = Core(profile=Profile(rule_sets=[]), bouncers=[RejectNonStandardDicom()])

    # this should not raise anything
    a_core.deidentify(quick_dataset(SOPClassUID="1.2.840.10008"))

    with pytest.raises(DeidentificationException):
        a_core.deidentify(quick_dataset(SOPClassUID="123"))


@pytest.mark.parametrize(
    "dataset",
    [
        quick_dataset(SOPClassUID="1.2.840.10008.1234"),  # Not a bad SOPClass
        quick_dataset(
            SOPClassUID="1.2.840.10008.5.1.4.1.1.11.1", SeriesDescription="Annotation"
        ),  # bad, but annotation
    ],
)
def test_reject_kogsps_pass(dataset):
    """Datasets that should be passed"""
    # should not raise exceptions
    assert Core(profile=Profile(rule_sets=[]), bouncers=[RejectKOGSPS()]).deidentify(
        dataset
    )


@pytest.mark.parametrize(
    "dataset",
    [
        quick_dataset(
            SOPClassUID="1.2.840.10008.5.1.4.1.1.11.1"
        ),  # Missing description
        quick_dataset(SeriesDescription="Annotation"),  # Missing SOPClassUID
        quick_dataset(
            SOPClassUID="1.2.840.10008.5.1.4.1.1.11.1",
            SeriesDescription="not_annotation",
        ),  # Wrong description
        quick_dataset(
            SOPClassUID="1.2.840.10008.5.1.4.1.1.88.59", SeriesDescription="Annotation"
        ),  # Description does not matter
    ],
)
def test_reject_kogsps_fail(dataset):
    """Datasets that should be rejected"""

    with pytest.raises(DeidentificationException):
        Core(profile=Profile(rule_sets=[]), bouncers=[RejectKOGSPS()]).deidentify(
            dataset
        )
