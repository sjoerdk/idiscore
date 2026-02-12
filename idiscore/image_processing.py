"""Classes and methods for working with image part of a DICOM dataset"""
from dataclasses import dataclass
from typing import List, Optional

from dicomcriterion import Criterion
from dicomcriterion.exceptions import EvaluationError
from pydicom.dataset import Dataset

from idiscore.exceptions import IDISCoreError


@dataclass(frozen=True)
class SquareArea:
    """A 2D square in pixel coordinates"""

    origin_x: int
    origin_y: int
    width: int
    height: int


class PIILocation:
    """One or more areas in a DICOM image slice that might contain Personally
    Identifiable Information (PPI)

    Notes
    -----
    A PIILocation is 2D. Cleaning will be done on each slice individually.

    Responsibilities:

    * Holds location information. Does not alter PixelData itself
    * Determine whether it applies to a given Dataset
    """

    def __init__(self, areas: List[SquareArea], criterion: Optional[Criterion]):
        """

        Parameters
        ----------
        areas: List[SquareArea]
            The
        criterion: Optional[Criterion]
            If this criterion matches, the PIILocations exist in the given dataset.
            For example Manufacturer.equals('a_company') and
            ManufacturerModelName.equals('Model_A2')
        """
        self.areas = areas
        self.criterion = criterion

    def exists_in(self, dataset: Dataset) -> bool:
        """True if the given PII location exists in the given dataset

        Raises
        ------
        CriterionException
            If for some reason no True or False response can be given for this
            dataset
        """
        if not self.criterion:
            return True
        try:
            return self.criterion.evaluate(dataset)
        except EvaluationError as e:
            raise CriterionException() from e


class PixelProcessor:
    """Finds and removes burned-in sensitive information in images

    Notes
    -----
    Responsibilities:

    * Checking whether a dataset needs cleaning of its pixel data
    * Checking whether redaction can be performed
    * Actually performing the blackout
    """

    def __init__(self, location_list: List[PIILocation]):
        """

        Parameters
        ----------
        location_list: List[PIILocation]
            all potential locations containing personally identifiable information
        """
        self.locations = location_list

    def get_locations(self, dataset: Dataset) -> List[PIILocation]:
        """Get all locations with person information in the current dataset

        Raises
        ------
        PixelDataProcessorException
            When locations cannot be found properly
        """
        try:
            return [x for x in self.locations if x.exists_in(dataset)]
        except CriterionException as e:
            raise PixelDataProcessorException(e) from e

    def clean_pixel_data(self, dataset: Dataset) -> Dataset:
        """Try to remove pixel data and mark the dataset as safe.

        If no pre-determined PI locations can be found, returns the dataset
        unaltered. This function does not raise exceptions
        """

        # find all locations that contain PII
        areas = [
            area for location in self.get_locations(dataset) for area in location.areas
        ]

        if not areas:
            pass
        else:
            pixel_array = dataset.pixel_array
            for area in areas:

                # extract the square location an set its value to 0
                pixel_array[
                    area.origin_y : area.origin_y + area.height,
                    area.origin_x : area.origin_x + area.width,
                ] = 0

            # write back data
            dataset.PixelData = pixel_array.tobytes()

            # mark as having no burned in annotation as per PS3.15 E3.1
            dataset.BurnedInAnnotation = "NO"

        return dataset


class CriterionException(IDISCoreError):
    pass


class PixelDataProcessorException(IDISCoreError):
    pass
