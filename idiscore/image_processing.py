"""Classes and methods for working with image part of a DICOM dataset"""
from dataclasses import dataclass
from typing import Callable, List, Optional

from pydicom._storage_sopclass_uids import SecondaryCaptureImageStorage
from pydicom.dataset import Dataset

from idiscore.dataset import RequiredDataset, RequiredTagNotFound
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


class PIILocationList:
    """Defines where in images there might by Personally Identifiable information"""

    def __init__(self, locations: Optional[List[PIILocation]] = None):
        """

        Parameters
        ----------
        locations: List[PIILocation], optional
            Information on all potentials locations containing personally
            identifiable information. Defaults to empty list
        """
        if locations is None:
            locations = []
        self.locations = locations


class PixelProcessor:
    """Finds and removes burned-in sensitive information in images

    Notes
    -----
    Responsibilities:

    * Checking whether a dataset needs cleaning of its pixel data
    * Checking whether redaction can be performed
    * Actually performing the blackout
    """

    def __init__(self, location_list: PIILocationList):
        """

        Parameters
        ----------
        location_list: PIILocationList
            Information on all potentials locations containing personally
            identifiable information

        """
        self.locations = location_list.locations

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

        dataset = RequiredDataset(dataset)  # catch missing keys later

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
            ) from e

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
        """Remove pixel data that needs cleaning and mark the dataset as safe

        If this dataset does not look suspicious it will not be returned unchanged

        Raises
        ------
        PixelDataProcessorException
            If pixel data needs cleaning but no information can be found

        """
        if not self.needs_cleaning(dataset):
            return dataset  # nothing needs to be done

        # find all locations that contain PII
        areas = [
            area for location in self.get_locations(dataset) for area in location.areas
        ]

        if not areas:
            summary = {
                x: dataset.get(x)
                for x in [
                    "Modality",
                    "Manufacturer",
                    "ManufacturerModelName",
                    "Rows",
                    "Columns",
                    "ImageType",
                ]
            }
            raise PixelDataProcessorException(
                f"Image data is suspicious, but I could not find any location to "
                f"clean. You should probably add an image location for {summary}"
            )
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
