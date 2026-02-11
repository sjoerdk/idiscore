from copy import copy

import pytest
from dicomgenerator.templates import CTDatasetFactory
from numpy.core.multiarray import ndarray
from pydicom.dataset import Dataset
from pydicom.uid import ExplicitVRLittleEndian

from idiscore.image_processing import (
    PIILocation,
    PIILocationList,
    PixelProcessor,
    SquareArea,
)


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
