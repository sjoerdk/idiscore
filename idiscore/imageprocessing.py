"""Classes and methods for working with image part of a DICOM dataset"""
from dataclasses import dataclass

from idiscore.exceptions import IDISCoreException
from pydicom.dataset import Dataset
from typing import Callable, List


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

    def __init__(
        self, name: str, criterion: Callable[[Dataset], bool], areas: List[SquareArea]
    ):
        """

        Parameters
        ----------
        name: str
            Human-readable name for this location
        criterion: Callable[[Dataset], bool]
            Function that return True if this PIILocation exists in the given dataset
            May return CriterionException if a True or False answer cannot be given
        areas: List[SquareArea]
            The
        """
        self.name = name
        self.criterion = criterion
        self.areas = areas

    def exists_in(self, dataset: Dataset) -> bool:
        """True if the given PII location exists in the given dataset

        Raises
        ------
        CriterionException
            If for some reason no True or False response can be given for this
            dataset
        """
        return self.criterion(dataset)


class PixelProcessor:
    """Finds and removes burned-in sensitive information in images

    Notes
    -----
    Responsibilities:
    * Checking whether a dataset needs cleaning of its pixel data
    * Checking whether redaction can be performed
    * Actually performing the blackout
    """

    def __init__(self, locations: List[PIILocation]):
        """

        Parameters
        ----------
        locations: List[PIILocation]
            Information on all potentials locations containing personally
            identifiable information

        """
        self.locations = locations

    @staticmethod
    def needs_cleaning(dataset: Dataset) -> bool:
        """Whether this dataset should be rejected as unsafe without cleaning

        Made this into a separate method as for many DICOM datasets you can
        reasonably skip the slow redaction process all together
        """
        # TODO: check separate criteria for suspicion! not get PPILocations
        return True

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
            raise PixelDataProcessorException(e)

    def clean_pixel_data(self, dataset: Dataset) -> Dataset:
        """Remove pixel data in all PII locations and mark the dataset as safe

        Raises
        ------
        PixelDataProcessorException
            If cleaning pixeldata fails for any reason

        """
        for location in self.get_locations(dataset):
            # TODO: implement
            for area in location:
                print(f"Removing {area} in {dataset}")
        return dataset


class CriterionException(IDISCoreException):
    pass


class PixelDataProcessorException(IDISCoreException):
    pass
