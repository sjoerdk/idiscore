"""Defines 'reasonable deidentification'. An opinionated module.

Contains opinions on:
* Which DICOM files to reject outright as being too risky to try to deidentify
* Which DICOM elements to remove, which to keep, which to encode or hash
* Which parts of DICOM image data to put black boxes over.

These opinions should reflect DICOM deidentification in general. This module should
NOT encode information that is specific hospital or site. Site-specific information
should be put in a separate python library which then imports idiscore.
"""
from pydicom.dataset import Dataset
from pydicom.uid import UID

from idiscore.core import Bouncer, BouncerException


class RejectKOGSPS(Bouncer):

    description = "Reject PresentationStorage and KeyObjectSelectionDocument"

    def inspect(self, dataset: Dataset):
        """Rejects three types of DICOM objects:
        1.2.840.10008.5.1.4.1.1.11.1 - GrayscaleSoftcopyPresentationStateStorage
        1.2.840.10008.5.1.4.1.1.88.59 - KeyObjectSelectionDocument
        1.2.840.10008.5.1.4.1.1.11.2 - ColorSoftcopyPresentationStateStorage
        These often contain ids and physician names in their SeriesDescription.
        See ticket #8465

        Raises
        ------
        BouncerException
            When the dataset is one of these types

        """
        black_list = [
            UID("1.2.840.10008.5.1.4.1.1.11.1"),
            UID("1.2.840.10008.5.1.4.1.1.88.59"),
            UID("1.2.840.10008.5.1.4.1.1.11.2"),
        ]

        def is_annotation(ds) -> bool:
            return ds["SeriesDescription"] == "Annotation"

        for uid in black_list:
            if dataset["SopClassUID"] == uid and not is_annotation(dataset):
                raise BouncerException(
                    f"Data sets of type {uid.name} ({uid}) are not allowed as "
                    f"they often contain physician information"
                )
