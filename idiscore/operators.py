from copy import copy
from hashlib import md5
from typing import Optional

from dicomgenerator.dicom import VRs
from dicomgenerator.factory import DataElementFactory
from pydicom.dataelem import DataElement
from pydicom.dataset import Dataset

from idiscore.exceptions import IDISCoreException
from idiscore.privateprocessing import SafePrivateDefinition


class Operator:
    """Base class for something that can change a DICOM data element.

    Like changing the value, hashing it, removing the entire element, etc.
    Takes care of input validation, raising exceptions when needed

    Notes
    -----
    Responsibilities

    An Operator

    * Can change the single DICOM data element that is fed to it
    * Can inspect the dataset that is passed to it
    * Can take init arguments and connect to external resources if needed

    * Should NOT Be stateful. ElementOperation.apply(element) should return the same
      object regardless of what went before. It CAN however rely on external stateful
      sources like a pseudonymization service.
    * Should NOT alter the dataset that is passed to it

    """

    name = "Base Operation"

    def apply(
        self, element: DataElement, dataset: Optional[Dataset] = None
    ) -> DataElement:
        """Perform this operation on the given element.

        Parameters
        ----------
        element: DataElement
            The DICOM element to operate on
        dataset: Dataset, optional
            The DICOM dataset that this element comes from. This can be inspected
            to determine what to do with element. Should not be changed in any way.
            Defaults to None

        Returns
        -------
        DataElement
            A new DataElement instance to replace the given element with

        Raises
        ------
        ValueError
            When this operation cannot be performed on this element. For example
            when the data element has a number ValueType but the operation is for
            a string
        ElementShouldBeRemoved
            Signals that this element should be removed from the dataset. Operators
            cannot do this by themselves as they can only operate on the element
            given

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

    def apply(
        self, element: DataElement, dataset: Optional[Dataset] = None
    ) -> DataElement:
        return copy(element)


class Remove(Operator):
    """Remove the given element completely"""

    name = "Remove"

    def apply(self, element: DataElement, dataset: Optional[Dataset] = None):
        raise ElementShouldBeRemoved()


class Empty(Operator):
    """Make the content of element empty"""

    name = "Empty"

    def apply(
        self, element: DataElement, dataset: Optional[Dataset] = None
    ) -> DataElement:
        copied = copy(element)
        copied.value = ""
        return copied


class Clean(Operator):
    """Replace with values of similar meaning known not to contain identifying
    information and consistent with the VR

    'similar meaning' is open to interpretation.

    Also handles private tags
    """

    name = "Clean"

    def __init__(self, safe_private: SafePrivateDefinition = None):
        """

        Parameters
        ----------
        safe_private: SafePrivateDefinition, optional
            For cleaning private tags. Defines which private tags are safe to keep.
            Defaults to None, in which case all private elements are removed
        """
        self.safe_private = safe_private

    def apply(
        self, element: DataElement, dataset: Optional[Dataset] = None
    ) -> DataElement:
        vr = VRs.short_name_to_vr(element.VR)

        if element.tag.is_private:
            # is this element safe?
            if self.is_safe(element=element, dataset=dataset):
                return copy(element)  # Nothing needs to be done. Keep.
            else:
                raise ElementShouldBeRemoved()  # not safe. Remove

        if vr in VRs.date_like:
            # maybe something can be done for dates. For now just return a random one
            return DataElementFactory(tag=element.tag)
        elif vr in VRs.string_like:
            element.value = "CLEANED"
            return copy(element)
        elif vr == VRs.Sequence:
            return copy(element)  # sequence elements are processed later. pass
        else:
            # too difficult. Cannot do it
            raise ValueError(
                f"Cannot clean {element}. I don't know how to handle "
                f"tags of type '{vr}'"
            )

    def is_safe(self, element: DataElement, dataset: Dataset) -> bool:
        """True if this element is safe according to safe private definition

        Raises
        ------
        SafePrivateException
            If for some reason it cannot be determined whether this is safe
        """
        if not self.safe_private:
            return False
        else:
            return self.safe_private.is_safe(element=element, dataset=dataset)


class Replace(Operator):
    """Replace element with a dummy value"""

    name = "Replace"

    def apply(
        self, element: DataElement, dataset: Optional[Dataset] = None
    ) -> DataElement:
        return DataElementFactory(tag=element.tag)


class GenerateUID(Operator):
    """Replace element with a valid UID"""

    name = "GenerateUID"

    def apply(
        self, element: DataElement, dataset: Optional[Dataset] = None
    ) -> DataElement:
        return DataElementFactory(tag="StudyInstanceUID")


class Hash(Operator):
    """Replace element value with an MD5 hash of that value"""

    name = "Hash"

    def apply(
        self, element: DataElement, dataset: Optional[Dataset] = None
    ) -> DataElement:
        copied = copy(element)
        copied.value = md5(str(element.value).encode("utf8")).hexdigest()
        return copied


class ElementShouldBeRemoved(IDISCoreException):
    pass
