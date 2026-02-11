from functools import wraps
from typing import Union, List, Any, Dict

from dicomcriterion import Criterion
from pydicom.dataset import Dataset
from pydicom.uid import (
    ColorSoftcopyPresentationStateStorage,
    EncapsulatedCDAStorage,
    EncapsulatedPDFStorage,
    GrayscaleSoftcopyPresentationStateStorage,
    KeyObjectSelectionDocumentStorage,
)

from idiscore.dataset import RequiredDataset, RequiredTagNotFound
from idiscore.exceptions import IDISCoreError


def handle_required_tag_not_found(func):
    """Decorator for handling missing dataset keys, together with RequiredDataset()

    Reduces duplicated code in most Bouncer.inspect() definitions
    """

    @wraps(func)
    def decorated(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except RequiredTagNotFound as e:  # catches failed dataset key access
            raise BouncerError(
                f"Required tag not found in dataset. I cannot determine whether"
                f' this is safe. Error: "{e}"'
            ) from e

    return decorated


class Bouncer:
    """Inspects a dataset and either rejects it or lets it through"""

    description = "Bouncer"  # single line description used in human-readable output

    def inspect(self, dataset: Dataset) -> bool:
        """Raise DatasetRejected if given dataset is not allowed through

        Notes
        -----
        Bouncer uses the exception DatasetRejected to signal the rejection of a dataset.
        The reason for choosing exception over a simple bool return value is that the
        end user might often be interested in the exact reason for rejection. A reason
        that can be specific to the dataset. An exception allows a fully tailored
        rejection message to be included with the decision to reject.
        Opted to use python's exception handling here as it seems cleaner than
        implementing a custom reject + message return type


        Parameters
        ----------
        dataset: Dataset
            The DICOM dataset to inspect

        Returns
        -------
        None

        Raises
        ------
        DatasetRejected
            When the input dataset is not allowed through

        BouncerError
            When the answer cannot be determined for any reason

        """
        raise NotImplementedError("Implemented in child classes")


class RejectNonStandardDicom(Bouncer):

    description = "Reject non-standard DICOM types by SOPClassUID"

    @handle_required_tag_not_found
    def inspect(self, dataset: Dataset):
        """Reject all DICOM that is not one of the standard SOPClass types.

        All standard types are listed in DICOM PS3.4 section 5B:
        http://dicom.nema.org/dicom/2013/output/chtml/part04/sect_B.5.html
        """

        if not dataset.SOPClassUID.startswith("1.2.840.10008"):
            raise DatasetRejected(
                f'This dataset has SOPClassUID "{dataset.SOPClassUID}", which is '
                f"non-standard. Deidentification would be too risky"
            )


class RejectKOGSPS(Bouncer):

    description = "Reject PresentationStorage and KeyObjectSelectionDocument"

    @handle_required_tag_not_found
    def inspect(self, dataset: Dataset):
        """Rejects three types of DICOM objects:
        1.2.840.10008.5.1.4.1.1.11.1 - GrayscaleSoftcopyPresentationStateStorage
        1.2.840.10008.5.1.4.1.1.88.59 - KeyObjectSelectionDocumentStorage
        1.2.840.10008.5.1.4.1.1.11.2 - ColorSoftcopyPresentationStateStorage
        These often contain ids and physician names in their SeriesDescription.
        See ticket #8465

        Raises
        ------
        DatasetRejected
            When the dataset is one of these types

        """
        dataset = RequiredDataset(dataset)  # allows catching missing keys

        if dataset.SOPClassUID == KeyObjectSelectionDocumentStorage:
            raise DatasetRejected(
                f"SOPClass {dataset.SOPClassUID} often contains physician"
                f" information"
            )
        elif dataset.SOPClassUID in [
            ColorSoftcopyPresentationStateStorage,
            GrayscaleSoftcopyPresentationStateStorage,
        ]:
            if dataset.SeriesDescription != "Annotation":
                raise DatasetRejected(
                    f'SOPClass "{dataset.SOPClassUID}" is only safe for '
                    f"annotations, but this series is described as"
                    f' "{dataset.SeriesDescription}"'
                )


class RejectEncapsulatedImageStorage(Bouncer):

    description = "Reject encapsulated PDF and CDA"

    @handle_required_tag_not_found
    def inspect(self, dataset: Dataset):
        dataset = RequiredDataset(dataset)

        if dataset.SOPClassUID in [EncapsulatedPDFStorage, EncapsulatedCDAStorage]:
            raise DatasetRejected(
                f"This dataset has is for encapsulated image data (SOPClassUID "
                f'"{dataset.SOPClassUID}"), which often contains patient'
                f"information. Too risky"
            )


class CriterionBouncer(Bouncer):
    """Bouncer based on a Criterion, which can be initialized with a string

    Example
    -------
    CriterionBouncer("Modality.equals('US') and BurnedInAnnotation.equals("True"))

    """

    def __init__(self, criterion: Union[Criterion, str], justification: str = ""):
        """

        Parameters
        ----------
        criterion: Criterion or str
            Criterion instance, or string. If string, a Criterion instance is created
        justification: str, optional
            Human-readable reason for this bouncer. Why should matching data be
            rejected? Defaults to empty string

        Raises
        ------
        CriterionError
            If criterion string input could not be parsed

        """
        if isinstance(criterion, str):  # cast from str for convenience
            criterion = Criterion(criterion)
        self.criterion = criterion
        self.justification = justification

    def inspect(self, dataset):
        matched = self.criterion.evaluate(dataset)
        if matched:
            raise DatasetRejected(
                f"Rejected by bouncer. Dataset matched {self.criterion}."
                f" Justification: {self.justification}"
            )


def determine_bouncer_results(bouncers: List[Bouncer], dataset: Dataset):
    """Run dataset through all bouncers. Extract bouncers that require pixel cleaning.

    This function determines two things:
        1) Whether to reject the dataset outright (raise DatsetRejected)
        2) whether to try and run the expensive clean_pixel process on the dataset.
           only needed if the result of clean_pixel potentially changes the bouncer
           results. The function returns those 'maybe allow' bouncers

    Raises
    ------
    DatasetRejected
        If any bouncer rejects this dataset without qualification (whether burned
        in pixel data can be removed or not)
    BouncerError
        If any bouncer cannot determine its answer

    """
    # start with the most positive situation: clean_pixels has succeeded in cleaning
    with PatchedDataset(dataset=dataset, patch={"BurnedInAnnotation": "NO"}) as patched:
        for bouncer in bouncers:
            # if any bouncer raises exceptions here then there is nothing to do. Reject.
            bouncer.inspect(patched)

    # No exceptions raised so far. All bouncers are either OK or Maybe OK.
    maybe_allow = []
    for bouncer in bouncers:
        try:
            bouncer.inspect(dataset)
        except DatasetRejected:
            # This was OK with BurnedInAnnotation=No, and is not OK now.
            # So running clean_pixels and checking these bouncers again might work
            maybe_allow.append(bouncer)

    return maybe_allow


class PatchedDataset:

    # signal 'tag not in dataset'. Using 'None' could hide actual None values
    not_present = object()

    def __init__(self, dataset: Dataset, patch: Dict[str, Any]):
        """Temporarily changes data element values in a dataset and restore them after.
        Useful only as context manager call using the 'with' keyword.

        Parameters
        ----------
        dataset: Dataset
            Apply patch to this
        patch: Dict[str, Any]
            Dict of valid DICOM Keyword: valid value

        Example
        -------
        dataset = quick_dataset(Modality='US', PatientName='name')
        with PatchedDataset(dataset=dataset, patch={"Modality":"CT"}) as patched:
            # now patched.Modality will be CT, but PatientName will remain the same

        # now dataset.Modality will be US again

        """
        self.dataset = dataset
        self.patch = patch
        self.original_values = {
            x: dataset.get(x, default=self.not_present) for x in self.patch.keys()
        }

    def __enter__(self):
        for key, value in self.patch.items():
            # setattr to be able to use pydicom DataElement auto-creation
            setattr(self.dataset, key, value)
        return self.dataset

    def __exit__(self, exc_type, exc_val, exc_tb):
        for key, value in self.original_values.items():
            if value is self.not_present:  # element was not present in original
                del self.dataset[key]
            else:
                self.dataset[key].value = value


class BouncerError(IDISCoreError):
    """Indicates that a Bouncer could not  perform its function for some reason"""

    pass


class DatasetRejected(IDISCoreError):
    """Raised by Bouncer.inspect() to signal not allowing a dataset"""

    pass
