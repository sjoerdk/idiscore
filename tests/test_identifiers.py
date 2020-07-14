import pytest
from dicomgenerator.factory import CTDatasetFactory

from idiscore.identifiers import (
    PrivateBlockTagIdentifier,
    PrivateTags,
    RepeatingGroup,
    RepeatingTag,
    SingleTag,
    TagIdentifier,
)
from pydicom.tag import Tag


def test_identifier_comparison():
    """Tag Identifiers are hashable and should be sortable as well"""
    # these should equal each other
    assert SingleTag(tag=Tag("PatientID")) == SingleTag(tag=Tag("PatientID"))
    # You can use any initialization that pydicom.tag.Tag allows, still equal
    assert SingleTag(tag=Tag(0x0010, 0x0020)) == SingleTag(tag=Tag("PatientID"))

    assert RepeatingGroup(tag="0010,10xx") == RepeatingGroup(tag="0010,10xx")

    # it should be possible to sort them as well
    taglist = [
        SingleTag(tag=Tag("0020000e")),
        SingleTag(tag=Tag("00100020")),
        RepeatingGroup(tag="001010xx"),
    ]

    taglist.sort(reverse=True)
    assert str(taglist[1]) == "(0010, 10xx)"


def test_identifier_matching():

    assert RepeatingGroup("50xx,xxxx").matches(Tag("50100040"))
    assert RepeatingGroup("50xx,xxxx").matches(Tag((0x5010, 0x0040)))
    assert RepeatingGroup("50xx,xxxx").matches(Tag("50ef3340"))
    assert not RepeatingGroup("50xx,xxxx").matches(Tag("51ef3340"))

    assert RepeatingGroup("0010,10xx").matches(Tag("00101000"))
    assert RepeatingGroup("0010,10xx").matches(Tag("001010ef"))
    assert not RepeatingGroup("0010,10xx").matches(Tag("001011ef"))

    assert PrivateTags().matches(Tag("11ef0010"))
    assert not PrivateTags().matches(Tag("12ee201f"))


@pytest.mark.parametrize(
    "tag_string",
    [
        "50xx,xxxx",
        "50xxxxxx",  # comma is optional
        "(50xx,xxxx)",  # so are parenthesis
        "100e,10xx",  # characters hex or 'x'
        "FF10,XXXX",  # case does not matter
    ],
)
def test_repeating_tag_format(tag_string):
    """Valid string for initializing a RepeatingTag"""
    RepeatingTag(tag_string)


@pytest.mark.parametrize(
    "tag_string",
    [
        "50xx,xxxxx",  # too long
        "50xx,xxx",  # too short
        "50xRxxxx",  # strange charactersstarted
    ],
)
def test_repeating_tag_format_exceptions(tag_string):
    """Invalid string for initializing a RepeatingTag. These should not work"""
    with pytest.raises(ValueError):
        RepeatingTag(tag_string)


def test_repeating_tag_masks():
    """Just checking the byte fiddling that RepeatingTag does"""
    # mask should have 0 where there was x
    assert hex(RepeatingTag("00xx,23e3").as_mask()) == hex(0xFF00FFFF)
    assert hex(RepeatingTag("(00xx,23e3)").as_mask()) == hex(0xFF00FFFF)
    assert hex(RepeatingTag("(0034,23e3)").as_mask()) == hex(0xFFFFFFFF)
    assert hex(RepeatingTag("(50xx,xxxx)").as_mask()) == hex(0xFF000000)

    # static_component should just show the non-x parts
    assert hex(RepeatingTag("00xx,23e3").static_component()) == hex(0x000023E3)
    assert hex(RepeatingTag("50xx,xxxx").static_component()) == hex(0x50000000)


def test_identifier_number_of_matchable_tags():
    """A number that can be used to sort identifiers for 'generality'"""

    assert SingleTag((0x0010, 0x10EA)).number_of_matchable_tags() == 1
    assert RepeatingGroup("(0010,00xx)").number_of_matchable_tags() == 16 * 16
    assert RepeatingGroup("(00xx,xxxx)").number_of_matchable_tags() == 16 ** 6
    assert PrivateTags().number_of_matchable_tags() == (16 ** 8) / 2


@pytest.mark.parametrize(
    "tag_identifier_instance",
    [
        SingleTag("PatientID"),
        SingleTag("00100010"),
        SingleTag((0x0010, 0x0010)),
        RepeatingGroup("00xx,00xx"),
        RepeatingGroup("(00xx, xxxx)"),
    ],
)
def test_identifier_keys(tag_identifier_instance: TagIdentifier):
    """You should be able te recreate a TagIdentifier instance using its key"""

    instance = tag_identifier_instance
    assert instance == type(instance)(instance.key())


def test_private_block_identifier():
    dataset = CTDatasetFactory()
    tag_to_match = dataset[(0x0075, 0x1000)]
    tag = PrivateBlockTagIdentifier("0075,[MyCompany]01")
