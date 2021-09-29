from functools import wraps

from pydicom._storage_sopclass_uids import (
    ColorSoftcopyPresentationStateStorage,
    EncapsulatedCDAStorage,
    EncapsulatedPDFStorage,
    GrayscaleSoftcopyPresentationStateStorage,
    KeyObjectSelectionDocumentStorage,
)
from pydicom.dataset import Dataset

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
            raise BouncerException(
                f"Required tag not found in dataset. I cannot determine whether"
                f' this is safe. Error: "{e}"'
            ) from e

    return decorated


class Bouncer:
    """Inspects a dataset and either rejects it or lets it through"""

    description = "Bouncer"  # single line description used in human-readable output

    def inspect(self, dataset: Dataset):
        """Check given dataset, raise exception if it should be rejected

        Parameters
        ----------
        dataset: Dataset
            The DICOM dataset to inspect

        Returns
        -------
        None

        Raises
        ------
        BouncerException
            When this dataset cannot be deidentified for any reason

        """
        pass


class RejectNonStandardDicom(Bouncer):

    description = "Reject non-standard DICOM types by SOPClassUID"

    @handle_required_tag_not_found
    def inspect(self, dataset: Dataset):
        """Reject all DICOM that is not one of the standard SOPClass types.

        All standard types are listed in DICOM PS3.4 section 5B:
        http://dicom.nema.org/dicom/2013/output/chtml/part04/sect_B.5.html
        """

        if not dataset.SOPClassUID.startswith("1.2.840.10008"):
            raise BouncerException(
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
        BouncerException
            When the dataset is one of these types

        """
        dataset = RequiredDataset(dataset)  # allows catching missing keys

        if dataset.SOPClassUID == KeyObjectSelectionDocumentStorage:
            raise BouncerException(
                f"SOPClass {dataset.SOPClassUID} often contains physician"
                f" information"
            )
        elif dataset.SOPClassUID in [
            ColorSoftcopyPresentationStateStorage,
            GrayscaleSoftcopyPresentationStateStorage,
        ]:
            if dataset.SeriesDescription != "Annotation":
                raise BouncerException(
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
            raise BouncerException(
                f"This dataset has is for encapsulated image data (SOPClassUID "
                f'"{dataset.SOPClassUID}"), which often contains patient'
                f"information. Too risky"
            )


class BouncerException(IDISCoreError):
    pass
