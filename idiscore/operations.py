from hashlib import md5

from dicomgenerator.factory import DataElementFactory
from pydicom.dataelem import DataElement


class Operation:
    """Base class for any operation on a DICOM data element

    Like changing the tag value, or removing it, hashing, etc.
    Takes care of input validation, raising exceptions when needed

    Notes
    -----
    Responsibilties

    An ElementOperation

    * Can change a single DICOM data element
    * Can use the content or value representation of the input argument
    * Can take init arguments

    * Should NOT Depend on the value of other DataElements. If more complicated logic
      is needed it should be dealt with higher up the execution stack
    * Should NOT Be stateful. ElementOperation.apply(element) should return the same
      object regardless of what went before.

    """

    def apply(self, element: DataElement) -> DataElement:
        """
        Raises
        ------
        ValueError
            When this operation cannot be performed on this element. For example
            when the data element has a number ValueType but the operation is for
            a string

        """
        return element


class Keep(Operation):
    """Keep the given element as is. Make no changes
    """
    pass


class Remove(Operation):
    """Remove the given element completely
    """

    def apply(self, element: DataElement) -> DataElement:
        return None


class Replace(Operation):
    """Replace element with a dummy value"""

    def apply(self, element: DataElement) -> DataElement:
        return DataElementFactory(tag=element.tag)


class Hash(Operation):
    """Replace element value with an MD5 hash of that value"""

    def apply(self, element: DataElement) -> DataElement:
        element.value = md5(str(element.value).encode('utf8')).hexdigest()


#TODO: Implement all of these operations:
"""
from http://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_E.html#table_E.1-1 

D - replace with a non-zero length value that may be a dummy value and consistent with the VR
Z - replace with a zero length value, or a non-zero length value that may be a dummy value and consistent with the VR
X - remove
K - keep (unchanged for non-sequence attributes, cleaned for sequences)
C - clean, that is replace with values of similar meaning known not to contain identifying information and consistent with the VR
U - replace with a non-zero length UID that is internally consistent within a set of Instances
Z/D - Z unless D is required to maintain IOD conformance (Type 2 versus Type 1)
X/Z - X unless Z is required to maintain IOD conformance (Type 3 versus Type 2)
X/D - X unless D is required to maintain IOD conformance (Type 3 versus Type 1)
X/Z/D - X unless Z or D is required to maintain IOD conformance (Type 3 versus Type 2 versus Type 1)
X/Z/U* - X unless Z or replacement of contained instance UIDs (U) is required to maintain IOD conformance (Type 3 versus Type 2 versus Type 1 sequences containing UID references)


"""
