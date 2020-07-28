"""Classes and methods for working with image part of a DICOM dataset"""
from typing import Callable, List
from dataclasses import dataclass

from idiscore.dataset import RequiredDataset, RequiredTagNotFound
from idiscore.exceptions import IDISCoreException
from pydicom._storage_sopclass_uids import SecondaryCaptureImageStorage
from pydicom.dataset import Dataset


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
        self, areas: List[SquareArea], criterion: Callable[[Dataset], bool] = None
    ):
        """

        Parameters
        ----------
        areas: List[SquareArea]
            The
        criterion: Callable[[Dataset], bool], optional
            Function that return True if this PIILocation exists in the given dataset
            May return CriterionException if a True or False answer cannot be given.
            Defaults to always returning True.
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
        else:
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
        reasonably skip image processing altogether.

        Raises
        ------
        PixelDataProcessorException
            When it cannot be determined whether this dataset needs cleaning
            or not. Usually due to missing DICOM elements

        """

        def says_no_burned_in_info(dataset_in: RequiredDataset) -> bool:
            """Dataset_in explicitly states that it has no burned in information"""
            try:
                return dataset_in.BurnedInAnnotation in ["NO", "No", "no"]
            except RequiredTagNotFound:
                return False  # not found so no specific burned in info disclaimer

        def is_suspicious(dataset_in: RequiredDataset) -> bool:
            return (
                dataset.Modality in ["US", "SC"]
                or dataset.SOPClassUID == SecondaryCaptureImageStorage
            )

        dataset = RequiredDataset(dataset)  # catch missing keys

        # Cleaning might be needed in the the following cases:
        try:
            if not is_suspicious(dataset):
                return False
            else:
                if says_no_burned_in_info(dataset):
                    return False  # if dataset says it's clean we believe it
                else:
                    return True

        except RequiredTagNotFound as e:
            raise PixelDataProcessorException(
                f"Missing DICOM element. I can not determine whether to clean "
                f"the pixels or not. Original error: {e}"
            )

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
        pixel_array = dataset.pixel_array
        for location in self.get_locations(dataset):
            for area in location.areas:

                # extract the square location an set its value to 0
                pixel_array[
                    area.origin_y : area.origin_y + area.height,
                    area.origin_x : area.origin_x + area.width,
                ] = 0

                # write back data
                dataset.PixelData = pixel_array.tobytes()
        return dataset


class CriterionException(IDISCoreException):
    pass


class PixelDataProcessorException(IDISCoreException):
    pass
