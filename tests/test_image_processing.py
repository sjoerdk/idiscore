import pytest
from copy import copy

from dicomgenerator.factory import CTDatasetFactory
from idiscore.image_processing import (
    PIILocation,
    PIILocationList,
    PixelDataProcessorException,
    PixelProcessor,
    SquareArea,
)
from numpy.core.multiarray import ndarray
from pydicom.dataset import Dataset
from pydicom.uid import ExplicitVRLittleEndian
from tests.factories import quick_dataset


@pytest.fixture
def a_dataset_with_transfer_syntax():
    """Transfer Syntax is needed for interpreting PixelData. This is not
    recorded with CTDatasetFactory()
    """
    dataset = CTDatasetFactory()
    dataset.file_meta = Dataset()
    dataset.file_meta.TransferSyntaxUID = ExplicitVRLittleEndian
    return dataset


def test_basic_image_processing(a_dataset_with_transfer_syntax):
    """Basic painting of some blocks into some image data"""
    dataset = a_dataset_with_transfer_syntax
    dataset.Modality = "US"  # will be suspicious, and cleaned

    location = PIILocation(
        areas=[SquareArea(5, 10, 4, 12), SquareArea(0, 0, 20, 3)],
        criterion=lambda x: x.Modality == "US",
    )

    processor = PixelProcessor(location_list=PIILocationList([location]))

    before = copy(dataset.pixel_array)
    after = processor.clean_pixel_data(dataset=dataset).pixel_array

    def is_different(before_in: ndarray, after_in: ndarray, x: int, y: int) -> bool():
        """True if the value for pixel x,y in 'before' differs from 'after'

        numpy switches the x and y in indexing. Probably for a good reason I do
        not understand. Just switching for now.
        My assumption is x is horizontal, y is vertical:
        coordinate (10, 4) means
        10 from the left (x=10)
        4 from the top (y=4)
        """
        return before_in[y, x] != after_in[y, x]

    # inside the blocks
    assert is_different(before, after, 6, 12)
    assert is_different(before, after, 8, 20)
    assert is_different(before, after, 1, 1)

    # outside the blocks
    assert not is_different(before, after, 21, 1)
    assert not is_different(before, after, 20, 10)


def test_needs_cleaning():
    """Verify that DICOM files that do not need cleaning are not cleaned"""
    processor = PixelProcessor(location_list=PIILocationList([]))
    assert processor.needs_cleaning(quick_dataset(Modality="US")) is True
    assert (
        processor.needs_cleaning(quick_dataset(Modality="CT", SOPClassUID="123"))
        is False
    )
    assert (
        processor.needs_cleaning(quick_dataset(Modality="SC", BurnedInAnnotation="No"))
        is False
    )
    assert (
        processor.needs_cleaning(quick_dataset(Modality="SC", BurnedInAnnotation="Yes"))
        is True
    )


@pytest.mark.parametrize(
    "dataset",
    [Dataset(), quick_dataset(Modality="CT")],  # No Modality  # no SOPClassUID
)
def test_needs_cleaning_exceptions(dataset):
    """Verify cannot determine whether this needs cleaning"""
    with pytest.raises(PixelDataProcessorException):
        PixelProcessor(PIILocationList([])).needs_cleaning(dataset)


def test_process_pixel_data_exception():
    """A suspicious dataset that cannot be cleaned should raise exception"""

    processor = PixelProcessor(location_list=PIILocationList([]))
    with pytest.raises(PixelDataProcessorException) as e:
        processor.clean_pixel_data(CTDatasetFactory(Modality="US"))

    assert "could not find any location to clean" in str(e.value)

    # but this should not raise exceptions because its not suspicious
    processor.clean_pixel_data(CTDatasetFactory())
