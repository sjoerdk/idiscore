from idiscore.exceptions import IDISCoreException
from pydicom.dataset import Dataset
from pydicom.uid import UID


def get_value(dataset, dicom_key):
    """Get the given value from dataset, raise distinctive error if not possible

    Made this to avoid duplicate code in bouncers which often have to fail if
    required values cannot be found.

    Returns
    -------
    The value of dicom_key in dataset

    Raises
    ------
    RequiredTagNotFound
        When dicom key is not in dataset
    """
    if dicom_key not in dataset:
        raise RequiredTagNotFound(f'tag "{dicom_key}" is not in dataset')
    return dataset.get(dicom_key)


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

    def inspect(self, dataset: Dataset):
        """Reject all DICOM that is not one of the standard SOPClass types.

        All standard types are listed in DICOM PS3.4 section 5B:
        http://dicom.nema.org/dicom/2013/output/chtml/part04/sect_B.5.html
        """
        try:
            sop_class_uid = dataset.SOPClassUID
        except IndexError:
            raise BouncerException(
                f"Could not determine SOPClassUID of this dataset."
                f"I cannot determine whether this dataset is safe"
            )
        if not str(sop_class_uid).startswith("1.2.840.10008"):
            raise BouncerException(
                f'This dataset has SOPClassUID "{sop_class_uid}", which is '
                f"non-standard. Deidentification would be too risky"
            )


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
        reject_outright = UID("1.2.840.10008.5.1.4.1.1.88.59")

        reject_if_not_annotation = [
            UID("1.2.840.10008.5.1.4.1.1.11.1"),
            UID("1.2.840.10008.5.1.4.1.1.11.2"),
        ]

        try:
            sop_class_uid = get_value(dataset, "SOPClassUID")
            if sop_class_uid == reject_outright:
                raise BouncerException(
                    f'SOPClass "{sop_class_uid}" often contains'
                    f" physician information"
                )
            elif (sop_class_uid in reject_if_not_annotation) and get_value(
                dataset, "SeriesDescription"
            ) != "Annotation":
                raise BouncerException(
                    f'SOPClass "{sop_class_uid}" is only safe for annotations, '
                    f"but this series is described as "
                    f'"{get_value(dataset, "SeriesDescription")}"'
                )
            else:
                return  # fine. Let through
        except RequiredTagNotFound as e:  # catches exceptions from get_value above
            raise BouncerException(
                f"Required tag not found in dataset. I cannot determine whether"
                f' this is safe. Error: "{e}"'
            )


class BouncerException(IDISCoreException):
    pass


class RequiredTagNotFound(IDISCoreException):
    pass
