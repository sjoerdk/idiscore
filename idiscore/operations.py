from hashlib import md5

from dicomgenerator.dicom import VRs
from dicomgenerator.factory import DataElementFactory
from pydicom.dataelem import DataElement


class Operator:
    """Base class for something that can change a DICOM data element.

    Like changing the value, hashing it, removing the entire element, etc.
    Takes care of input validation, raising exceptions when needed

    Notes
    -----
    Responsibilities

    An Operator

    * Can change a single DICOM data element that is fed to it
    * Can use the content or value representation of the input argument
    * Can take init arguments and connect to external resources if needed

    * Should NOT Depend on the value of other DataElements. If more complicated logic
      is needed it should be dealt with higher up the execution stack
    * Should NOT Be stateful. ElementOperation.apply(element) should return the same
      object regardless of what went before. It CAN however rely on external sources
      like a pseudonymization service.
    * Should NOT alter anything besides the element that is fed to it

    """

    name = "Base Operation"

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

    def __str__(self):
        if self.name:
            return self.name
        else:
            return super().__str__()


class Keep(Operator):
    """Keep the given element as is. Make no changes"""

    name = "Keep"

    def apply(self, element: DataElement) -> DataElement:
        return element


class Remove(Operator):
    """Remove the given element completely"""

    name = "Remove"

    def apply(self, element: DataElement) -> DataElement:
        return None


class Empty(Operator):
    """Make the content of element empty"""

    name = "Empty"

    def apply(self, element: DataElement) -> DataElement:
        return DataElementFactory(tag=element.tag, value=None)


class Clean(Operator):
    """Replace with values of similar meaning known not to contain identifying
    information and consistent with the VR

    'similar meaning' is open to interpretation.
    """

    name = "Clean"

    def apply(self, element: DataElement) -> DataElement:
        vr = VRs.short_name_to_vr(element.VR)
        if vr in VRs.date_like:
            # maybe something can be done for dates. For now just return a random one
            return DataElementFactory(tag=element.tag)
        else:
            # too difficult. Cannot do it
            raise ValueError(
                f"Cannot clean {element}. I don't know how to handle "
                f"tags of type '{vr}'"
            )


class Replace(Operator):
    """Replace element with a dummy value"""

    name = "Replace"

    def apply(self, element: DataElement) -> DataElement:
        return DataElementFactory(tag=element.tag)


class GenerateUID(Operator):
    """Replace element with a valid UID"""

    name = "Replace"

    def apply(self, element: DataElement) -> DataElement:
        # not so pretty, but works
        element.value = DataElementFactory(tag="PatientID").value


class Hash(Operator):
    """Replace element value with an MD5 hash of that value"""

    name = "Hash"

    def apply(self, element: DataElement) -> DataElement:
        element.value = md5(str(element.value).encode("utf8")).hexdigest()
