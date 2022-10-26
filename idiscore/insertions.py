"""Common DICOM elements you might like to insert into deidentified datasets

This includes the insertions from DICOM PS3.15 E1-1.6:

The attribute Patient Identity Removed (0012,0062) shall be replaced or added to the
dataset with a value of YES, and one or more codes from CID 7050
“De-identification Method” corresponding to the profile and options used shall
be added to De-identification Method Code Sequence (0012,0064). A text string
describing the method used may also be inserted in or added to
De-identification Method (0012,0063), but is not required.
"""
from typing import List

from dicomgenerator.dicom import VRs
from pydicom.dataelem import DataElement
from pydicom.dataset import Dataset
from pydicom.sequence import Sequence
from pydicom.tag import Tag

from idiscore import __version__
from idiscore.nema_parsing import E1_1_METHOD_INFO


def get_idis_code_sequence(ruleset_names: List[str]) -> DataElement:
    """Create the element (0012,0064) - DeIdentificationMethodCodeSequence

    This sequence specifies what kind of anonymization has been performed. It is
    quite free form. This implementation uses the following format:

    DeIdentificationMethodCodeSequence will contain the code of each official
    DICOM deidentification profile that was used. Codes are taken from
    Table CID 7050

    Parameters
    ----------
    ruleset_names: List[str]
        list of names as defined in nema.E1_1_METHOD_INFO

    Returns
    -------
    DataElement
        Sequence element (0012,0064) - DeIdentificationMethodCodeSequence. Will
         contain the code of each official DICOM deidentification profile passed

    Raises
    ------
    ValueError
        When any name in ruleset_names is not recognized as a standard DICOM
        rule set
    """
    code_per_name = {x.full_name: x for x in E1_1_METHOD_INFO}
    codes = []
    for name in ruleset_names:
        try:  # check whether we know this ruleset as a standard DICOM one
            ruleset_info = code_per_name[name]
        except KeyError as e:
            raise ValueError(
                f'Could not find the code for rule set "{name}". I do'
                f" not know this ruleset"
            ) from e
        # Create the required designation for this dataset
        code_dataset = Dataset()
        code_dataset.CodeValue = ruleset_info.code
        code_dataset.CodingSchemeDesignator = "DCM"
        code_dataset.CodeMeaning = ruleset_info.full_name
        codes.append(code_dataset)

    element = DataElement(
        tag=Tag("DeidentificationMethodCodeSequence"),
        VR=VRs.Sequence.short_name,
        value=Sequence(codes),
    )
    return element


DEFAULT_DEIDENTIFICATION_METHOD = f"idiscore {__version__}"


def get_deidentification_method(
    method: str = DEFAULT_DEIDENTIFICATION_METHOD,
) -> DataElement:
    """Create the element (0012,0063) - DeIdentificationMethod

    A string description of the deidentification method used

    Parameters
    ----------
    method: str, optional
        String representing the deidentification method used. Defaults to
        'idiscore <version>'
    """
    return DataElement(
        tag=Tag("DeidentificationMethod"), VR=VRs.LongString.short_name, value=method
    )


# this element should be inserted by any deidentifier that conforms to PS3.15 E
PATIENT_IDENTITY_REMOVED = DataElement(
    tag=Tag("PatientIdentityRemoved"), VR=VRs.CodeString.short_name, value="YES"
)
