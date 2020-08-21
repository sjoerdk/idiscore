import hashlib
import random

from copy import copy
from datetime import timedelta
from datetime import datetime
from dicomgenerator.dicom import VRs
from dicomgenerator.factory import DataElementFactory
from hashlib import md5
from idiscore.exceptions import IDISCoreException
from idiscore.private_processing import SafePrivateDefinition
from idiscore.settings import IDIS_CORE_ROOT_UID
from pydicom.dataelem import DataElement
from pydicom.dataset import Dataset
from typing import Optional, Tuple, Union


class Operator:
    """Base class for something that can change a DICOM data element.

    Like changing the value, hashing it, removing the entire element, etc.
    Takes care of input validation, raising exceptions when needed

    Notes
    -----
    Responsibilities

    An Operator:

    * Can change the single DICOM data element that is fed to it
    * Can inspect the dataset that is passed to it
    * Can take init arguments and connect to external resources if needed
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
        copied.value = None
        return copied


class TimeDeltaProvider:
    """Generates a random shift in time to use when cleaning dates.

    Returns the same output for data sets in the same study
    """

    def __init__(self):
        self.generated = {}

    @staticmethod
    def generate_random_delta() -> timedelta:
        """Anything from 0 up to 5 years and 23:59 and 59 seconds"""
        return timedelta(
            days=random.randint(0, 1825),  # 365 * 5
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59),
            seconds=random.randint(0, 59),
        )

    def get_delta(self, dataset: Dataset) -> timedelta:
        """Returns the same delta if a dataset belongs to a series already seen

        If series cannot be determined, return random delta
        """
        try:
            key = self.extract_key(dataset)
        except ValueError:
            return self.generate_random_delta()

        if key not in self.generated:
            self.generated[key] = self.generate_random_delta()

        return self.generated[key]

    @staticmethod
    def extract_key(dataset: Dataset) -> str:
        """Extracts a key from dataset. Data sets with the same key will be
        given the same delta

        Raises
        ------
        ValueError
            If key cannot be generated
        """
        try:
            return dataset.StudyInstanceUID
        except AttributeError:
            raise ValueError(
                "Cannot determine key. This dataset has no" " StudyInstanceUID"
            )


class Clean(Operator):
    """Replace with values of similar meaning known not to contain identifying
    information and consistent with the VR

    'similar meaning' is open to interpretation.

    Also handles private tags
    """

    name = "Clean"

    def __init__(
        self,
        safe_private: SafePrivateDefinition = None,
        delta_provider: TimeDeltaProvider = None,
    ):
        """

        Parameters
        ----------
        safe_private: SafePrivateDefinition, optional
            For cleaning private tags. Defines which private tags are safe to keep.
            Defaults to None, in which case all private elements are removed
        delta_provider: TimeDeltaProvider, optional
            For cleaning dates. Determines how much to shift dates and times.
            Defaults to None, in which case time shift will be random, but
            the same for data sets from the same study.
        """
        self.safe_private = safe_private
        if not delta_provider:
            delta_provider = TimeDeltaProvider()  # initialize default
        self.delta_provider = delta_provider

    def apply(
        self, element: DataElement, dataset: Optional[Dataset] = None
    ) -> DataElement:
        vr = VRs.short_name_to_vr(element.VR)

        if element.tag.is_private:
            return self.clean_private(element, dataset)
        elif vr in VRs.date_like:
            return self.clean_date_time(element, dataset)
        elif vr in VRs.string_like:
            return DataElement(tag=element.tag, VR=element.VR, value="CLEANED")
        elif vr == VRs.Sequence:
            return copy(element)  # sequence elements are processed later. pass
        else:
            # too difficult. Cannot do it
            raise ValueError(
                f"Cannot clean {element}. I don't know how to handle "
                f"tags of type '{vr}'"
            )

    def clean_private(self, element: DataElement, dataset: Dataset) -> DataElement:
        """Clean private DICOM element"""
        if self.is_safe(element=element, dataset=dataset):
            return copy(element)  # Nothing needs to be done. Keep.
        else:
            raise ElementShouldBeRemoved()  # not safe. Remove

    def clean_date_time(self, element: DataElement, dataset: Dataset) -> DataElement:
        """Clean a DICOM date or time

        Do this by subtracting a random increment from it
        """
        delta = self.delta_provider.get_delta(dataset)
        date_format, parsed = self.parse_date_time(element.value)
        return DataElement(
            tag=element.tag, VR=element.VR, value=(parsed - delta).strftime(date_format)
        )

    @staticmethod
    def parse_date_time(value: str) -> Tuple[str, datetime]:
        """Parse DICOM date, datetime or time string

        Parameters
        ----------
        value: str
            A dicom date datetime or time string

        Returns
        -------
        Tuple[str, datetime]
            strptime date format string, parsed datetime instance

        Raises
        ------
        ValueError
            If value cannot be parsed

        """
        formats = ["%Y%m%d%H%M%S", "%Y%m%d", "%H%M%S", "%H%M%S.%f", "%H%M%S.%f%z"]
        while formats:
            date_format = formats.pop()
            try:
                return date_format, datetime.strptime(value, date_format)
            except ValueError:
                continue  # try next format

        raise ValueError(f"Value {value} did not fit any" f" of the formats {formats}")

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


class HashUID(Operator):
    """Replace element with a valid UID"""

    name = "HashUID"

    def __init__(self, root_uid: str = None):
        """

        Parameters
        ----------
        root_uid: str, optional
            UID to prepend to all hashes. For example 1.2.826.0.1.3680043.10.566.
            Defaults to using idiscore's own root UID.
        """
        if not root_uid:
            root_uid = IDIS_CORE_ROOT_UID
        self.root_uid = root_uid

    def apply(
        self, element: DataElement, dataset: Optional[Dataset] = None
    ) -> DataElement:
        return DataElement(
            tag=element.tag,
            VR=element.VR,
            value=self.ctp_hash_uid(prefix=self.root_uid, uid=element.value),
        )

    @staticmethod
    def ctp_hash_uid(prefix: str, uid: str):
        """Implementation of CTP function hashUID(prefix, uid)

        Generates a hash of the given UID with the given prefix. Modelled as
        closely as possible to the java function
        https://mircwiki.rsna.org/index.php?title=The_CTP_DICOM_Anonymizer
        #.40hashuid.28root.2CElementName.29

        Parameters
        ----------
        prefix: str
            DICOM prefix for your organization to prepend in output.
        uid: str
            original UID

        Returns
        -------
        str
            hashed UID

        """
        prefix = prefix.strip()
        if prefix and not prefix.endswith("."):
            prefix += "."
        hash_string = str(
            int.from_bytes(hashlib.md5(uid.encode("utf-8")).digest(), byteorder="big")
        )
        if hash_string.startswith("0"):
            hash_string = "9" + hash_string
        new_uid = prefix + hash_string
        new_uid = new_uid[:64]
        return new_uid


class Hash(Operator):
    """Replace value with an MD5 hash of that value"""

    name = "Hash"

    def apply(
        self, element: DataElement, dataset: Optional[Dataset] = None
    ) -> DataElement:
        copied = copy(element)
        copied.value = md5(str(element.value).encode("utf8")).hexdigest()
        return copied


class SetFixedValue(Operator):
    """Replace element with a fixed value from a list of tag-value pairs"""

    name = "SetFixedValue"

    def __init__(self, value: Union[str, int, object]):
        """

        Parameters
        ----------
        value: Union[str, int, object])
            DICOM element value to set. Anything that is valid for DataElement.value
        """
        self.value = value

    def apply(
        self, element: DataElement, dataset: Optional[Dataset] = None
    ) -> DataElement:
        return DataElement(tag=element.tag, VR=element.VR, value=self.value)


class ElementShouldBeRemoved(IDISCoreException):
    pass
