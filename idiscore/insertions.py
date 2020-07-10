"""Common DICOM elements you might like to insert into deidentified datasets"""
from typing import List

from dicomgenerator.dicom import VRs
from pydicom.dataelem import DataElement
from pydicom.tag import Tag

from idiscore.nema import E1_1_METHOD_INFO


def get_idis_code_sequence(ruleset_names: List[str]) -> DataElement:
    """Create the required element (0012,0064) - DeIdentificationMethodCodeSequence

    This sequence specifies what kind of anonymization has been performed. It is
    quite free form. This method uses the following format:

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
    code_per_name = {x.full_name: x.code for x in E1_1_METHOD_INFO}
    codes = []
    for name in ruleset_names:
        try:
            codes.append(code_per_name[name])
        except KeyError:
            raise ValueError(
                f'Could not find the code for rule set "{name}". I do'
                f" not know this ruleset"
            )

    element = DataElement(
        tag=Tag("DeidentificationMethodCodeSequence"), VR=VRs.Sequence, value=codes
    )
    return element
