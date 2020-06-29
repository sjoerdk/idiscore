"""Ways to designate a DICOM tag or a group of dicom tags"""

from functools import total_ordering
from typing import Union

from pydicom._dicom_dict import RepeatersDictionary
from pydicom.datadict import dictionary_keyword, mask_match
from pydicom.dataelem import DataElement
from pydicom.tag import Tag


@total_ordering
class TagIdentifier:
    """Identifies a single DICOM tag or repeating group like (50xx,xxx)


    Using just DICOM tags is too limited for defining deidentification. We want
    to be able to represent for example:
    * all curves (50xx,xxxx)
    * a private tag with a variable group ([PrivateCreatorName]01,0010)
    """

    def matches(self, element: DataElement) -> bool:
        """The given element matches this identifier"""
        return False

    def key(self) -> str:
        """String used for comparison operators"""
        return str(id(self))

    def name(self) -> str:
        """Human readable name for this tag"""
        return "BaseTagIdentifier"

    #   Override comparisons to be able to compare and order different
    #   child classes
    def __le__(self, other):
        """Return ``True`` if `self`  is less than or equal to `other`"""
        return self.key() >= other.key()

    def __eq__(self, other):
        if isinstance(other, TagIdentifier):
            return self.key() == other.key()
        else:
            return False

    def __hash__(self):
        # TagIdentifiers are used as dictionary keys
        return hash(self.key())


class SingleTag(TagIdentifier):
    """Matches a single DICOM tag like (0010,0010) or 'PatientName'"""

    def __init__(self, tag: Tag):
        self.tag = tag

    def __str__(self):
        return str(self.tag)

    def name(self) -> str:
        """Human readable name for this tag"""
        return dictionary_keyword(self.tag)

    def matches(self, element: DataElement) -> bool:
        """The given element matches this identifier"""
        return element.tag == self.tag

    def key(self) -> str:
        return str(self.tag)

    def as_python(self) -> str:
        """For special export. Python code that recreates this instance"""
        return f"SingleTag('{self.key()}')"


class RepeatingTag:
    """Dicom tag with x's in it to denote wildcards, like (50xx,xxxx) for curve data

    See http://dicom.nema.org/medical/dicom/current/output/chtml/part05/sect_7.6.html

    Raises
    ------
    ValueError
        on init if tag cannot be parsed as a DICOM repeater group

    Notes
    -----
    I would prefer to take any pydicom way of working with repeater tags, but
    the current version of pydicom (2.0) only offers limited lookup support
    as far as I can see
    """

    def __init__(self, tag: str):
        # check input
        try:
            self.tag = RepeatingTag.parse_tag_string(tag)
        except ValueError as e:
            raise ValueError(
                f'Invalid format "{tag}":{e}. Examples of valid tag '
                f'strings: "(0010,xx10)", "0010,xx10", "0010xx10"'
            )

    def __str__(self):
        """Output format matches pydicom.tag.Tag.__str__()"""
        return f"({self.tag[:4]}, {self.tag[4:]})"

    @staticmethod
    def parse_tag_string(tag: str) -> str:
        """Cleans tag string and outputs it in standard format.
        Raises ValueError if tag is not of the correct format like
        (0010,10xx).

        Returns
        -------
        str
            standard format, 8 character hex string with 'x' for wildcard bytes.
            like 0010xx10 or 75f300xx
        """
        # remove potential brackets and comma. Make lower case to reduce clutter
        tag = tag.replace("(", "").replace(")", "").replace(",", "").lower()
        if len(tag) != 8:
            raise ValueError(f"Tag should be 8 characters long")
        # check whether this is a valid hex string if you discount the x's
        try:
            int(f'0x{tag.replace("x","0")}', 0)
        except ValueError:
            raise ValueError(f'Non "x" parts of this tag are not hexadecimal')

        return tag

    def name(self) -> str:
        """Human readable name for this repeater tag, from pydicom lists"""
        key = mask_match(self.static_component())
        if key:
            return RepeatersDictionary[key][4]  # 4th item in tuple is no-space name
        else:
            return f"Unknown Repeater tag {self.tag}"

    def as_mask(self) -> int:
        """Byte mask that can remove the byte positions that have value 'x'

        RepeatingTag('0010,xx10').as_mask() -> 0xffff00ff
        RepeatingTag('50xx,xxxx').as_mask() -> 0xff000000
        """
        hex_string = f"0x{''.join(map(lambda x: '0' if x=='x' else 'f', self.tag))}"
        return int(hex_string, 0)

    def static_component(self) -> int:
        """The int value of all bytes of this tag that are not 'x'
        RepeatingTag('0010,xx10').static_component() -> 0x00100010
        RepeatingTag('50xx,xxxx').static_component() -> 0x50000000
        """
        return int(f'0x{self.tag.replace("x", "0")}', 0)


class RepeatingGroup(TagIdentifier):
    """A DICOM tag where not all elements are filled. Like (50xx,xxxx)"""

    def __init__(self, tag: Union[str, RepeatingTag]):
        if isinstance(tag, str):  # allow string init for convenience
            tag = RepeatingTag(tag.replace(" ", ""))  # allow (xxxx, xxxx)
        self.tag = tag

    def __str__(self):
        return str(self.tag)

    def matches(self, element: DataElement) -> bool:
        """True if the element's tag matches the tag string, ignoring any part
        of the tag_string where there are x marks
        """
        # Following pydicom in using byte operations for this
        return element.tag & self.tag.as_mask() == self.tag.static_component()

    def key(self) -> str:
        """For sane sorting, make sure this matches the key format of other
        identifiers
        """
        return str(self.tag)

    def name(self) -> str:
        """Human readable name for this tag"""
        return self.tag.name()

    def as_python(self) -> str:
        """For special export. Python code that recreates this instance"""
        return f"RepeatingGroup('{self.key()}')"


class PrivateTags(TagIdentifier):
    """Matches any private DICOM tag. A private tag has an uneven group number"""

    def __str__(self):
        return self.key()

    def matches(self, element: DataElement) -> bool:
        return element.tag.is_private()

    def key(self) -> str:
        return "PrivateAttributes"

    def name(self) -> str:
        return "Private Attributes"

    @staticmethod
    def as_python() -> str:
        """For special export. Python code that recreates this instance"""
        return f"PrivateTags()"
