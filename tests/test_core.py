"""Tests for `idiscore` package."""
from io import BytesIO

import pytest
from dicomgenerator.generators import DataElementFactory as DatEF, quick_dataset
from pydicom import dcmread
from pydicom.dataset import Dataset, FileMetaDataset
from pydicom.tag import Tag
from pydicom.uid import CTImageStorage

from dicomgenerator.templates import CTDatasetFactory

from idiscore.bouncers import ProtocolFilterBouncer
from idiscore.core import Core, Profile
from idiscore.defaults import create_default_core
from idiscore.identifiers import PrivateTags, RepeatingGroup, SingleTag
from idiscore.image_processing import (
    PIILocation,
    SquareArea,
    PIILocationList,
    PixelProcessor,
)
from idiscore.operators import Clean, Hash, Keep, Remove
from idiscore.private_processing import SafePrivateDefinition, SafePrivateBlock
from idiscore.rules import Rule, RuleSet
from idiscore.validation import extract_signature


def test_idiscore_deidentify_basic(a_dataset, a_core_with_some_rules):
    """Send a dataset through a full Core instance"""

    # check before processing
    assert Tag(0x5010, 0x3000) in a_dataset
    assert Tag(0x1013, 0x0001) in a_dataset
    assert a_dataset.PatientID == "12345"
    assert a_dataset.PatientName == "Martha"
    assert len(a_dataset.items()) == 8

    # now apply the rules to the dataset
    core = a_core_with_some_rules
    deidentified = core.deidentify(a_dataset)

    # check whether that worked as expected
    assert Tag(0x5010, 0x3000) not in deidentified  # removed by 50xx,xxxx rule
    assert Tag(0x1013, 0x0001) not in deidentified  # removed by PrivateTags() rule
    assert deidentified.PatientID == "12345"  # not touched. No rule for this
    assert deidentified.PatientName != "Martha"  # should have been hashed
    assert len(deidentified.items()) == 4


@pytest.fixture
def some_pid_rules():
    return [
        Rule(SingleTag("PatientID"), Hash()),
        Rule(SingleTag("PatientID"), Remove()),
        Rule(SingleTag("PatientID"), Keep()),
    ]


def test_profile_flatten(some_pid_rules):
    """A profile can have multiple rule sets, but with flatten you should end up
    with one rule per DICOM tag
    """
    hash_name = Rule(SingleTag("PatientName"), Hash())

    # initial set
    set1 = RuleSet(rules=[some_pid_rules[0], hash_name])
    # set with a different rule for PatientID
    set2 = RuleSet(rules=[some_pid_rules[1], Rule(SingleTag("Modality"), Remove())])

    profile = Profile(rule_sets=[set1, set2])

    # The PatientID rule of set2 should be chosen when flattening
    assert some_pid_rules[1] in profile.flatten().rules
    assert some_pid_rules[0] not in profile.flatten().rules

    # if another set is added, the rules from this should overrule earlier
    set3 = RuleSet(name="another set", rules=[some_pid_rules[2]])
    assert some_pid_rules[2] in profile.flatten(additional_rule_sets=[set3]).rules
    # but any original rule that was not overwritten should still be present
    assert hash_name in profile.flatten(additional_rule_sets=[set3]).rules


def test_rule_precedence():
    """Rules are applied in order of generality - most specific first. Verify"""

    # Some rules with a potentially ambivalent order
    rule_a = Rule(PrivateTags(), Remove())  # Remove all private tags
    rule_b = Rule(Tag(0x1301, 0x0000), Keep())  # but keep this private tag
    rule_c = Rule(RepeatingGroup("50xx,xxxx"), Hash())  # match all these
    rule_d = Rule(Tag(0x5002, 0x0002), Keep())  # but specifically remove this
    rule_e = Rule(SingleTag("PatientName"), Hash())  # and one regular rule
    rules = RuleSet(rules=[rule_a, rule_b, rule_c, rule_d, rule_e])

    # now in all these cases, the most specific rule should be returned:
    assert rules.get_rule(DatEF(tag=(0x1301, 0x0000))) == rule_b  # also matches a
    assert rules.get_rule(DatEF(tag=(0x5002, 0x0002))) == rule_d  # also matches c
    assert rules.get_rule(DatEF(tag=(0x5002, 0x0001))) == rule_c
    assert rules.get_rule(DatEF(tag=(0x5001, 0x0001))) == rule_c  # also matches a
    assert rules.get_rule(DatEF(tag=(0x0010, 0x0010))) == rule_e
    assert rules.get_rule(DatEF(tag="Modality")) is None

    # For rules with identical generality, just keep the order of input
    rule_1 = Rule(RepeatingGroup("50xx,xxxx"), Hash())
    rule_2 = Rule(RepeatingGroup("xx10,xxxx"), Hash())
    rules = RuleSet(rules=[rule_1, rule_2])

    assert rules.get_rule(DatEF(tag=(0x5010, 0x0000))) == rule_1  # also matches a
    assert rules.get_rule(DatEF(tag=(0x5110, 0x0000))) == rule_2  # also matches a


def test_rule_set_human_readable(some_rules):

    as_string = RuleSet(some_rules).as_human_readable_list()
    assert "PatientName - (0010,0010)" in as_string
    assert "Unknown Repeater tag" in as_string


def test_core_deidentify_safe_private():
    """Private elements marked as safe should not be removed by Clean()"""

    def get_dataset():
        # Set up a dataset with a single private creator and two private elements
        ds = Dataset()
        block = ds.private_block(0x00B1, "a_producer", create=True)
        block.add_new(0x01, "UN", b"value")  # add private tag '00b1[a_producer]01'
        block.add_new(0x02, "LO", 1)  # add private tag '00b1[a_producer]02'
        return ds

    ds = get_dataset()
    # sanity check, these elements should have been created
    assert Tag("00b10010") in ds  # a private creator tag
    assert Tag("00b11001") in ds  # and a private tag
    assert Tag("00b11002") in ds  # and another

    ds.Modality = "CT"
    # A core instance that should clean() private tags. One tag is deemed safe on
    # CT datasets
    ruleset = RuleSet(
        [
            Rule(
                PrivateTags(),
                Clean(
                    safe_private=SafePrivateDefinition(
                        blocks=[
                            SafePrivateBlock(
                                tags=["00b1[a_producer]01"],
                                criterion=lambda x: x.Modality == "CT",
                            )
                        ]
                    )
                ),
            )
        ]
    )  # this nesting is nasty
    core = Core(profile=Profile([ruleset]))

    # but only so long as dataset has modality is CT. Now this is no longer true
    ds = get_dataset()
    ds.Modality = "US"

    deltas = extract_signature(deidentifier=core, dataset=ds)

    # nothing is not deemed safe. Clean() should remove all, including private creator
    assert {x.tag: x for x in deltas}[Tag("00b11001")].status == "REMOVED"
    assert {x.tag: x for x in deltas}[Tag("00b11002")].status == "REMOVED"
    assert {x.tag: x for x in deltas}[Tag("00b10010")].status == "REMOVED"


def test_deidentify_uids():
    """Recreates issue from #145"""

    core = create_default_core()  # create an idiscore instance
    values = {
        "SOPInstanceUID": "111.1",
        "StudyInstanceUID": "222.2",
        "SeriesInstanceUID": "333.3",
    }
    ds = quick_dataset(**(values | {"SOPClassUID": CTImageStorage}))
    for name, value in values.items():
        assert ds[name].value == value

    ds_after = core.deidentify(ds)  # remove patient information

    for name, value in values.items():
        assert ds_after[name].value != value


def test_file_meta_processing():
    """Exposes issue #147. Any element in file_meta (0002,xxxx) tags is not processed"""
    # generate realistic example: a dicom file that has been written to disk and
    # loaded again.

    ds: Dataset = CTDatasetFactory()

    dicom_file = create_dummy_disk_file(ds)

    original = dcmread(dicom_file)
    value_before = original.file_meta.MediaStorageSOPInstanceUID

    # Create core that only hashes MediaStorageSOPInstanceUID
    profile = Profile(
        rule_sets=[
            RuleSet(
                rules=[Rule(SingleTag("MediaStorageSOPInstanceUID"), Hash())],
                name="test_ruleset",
            )
        ]
    )
    core = Core(profile)

    processed = core.deidentify(original)
    value_after = processed.file_meta.MediaStorageSOPInstanceUID

    # now this should hash MediaStorageSOPInstanceUID
    assert value_before != value_after


def create_dummy_disk_file(ds):
    """Save dataset to BytesIO. This mimics a DICOM file written to disk.

    Note: the transfer syntax and storage SOP class are just random and might not be
    valid. I just want ot make the save work at the moment.
    """
    dicom_file = BytesIO()
    ds.is_little_endian = True
    ds.is_implicit_VR = False
    ds.file_meta = FileMetaDataset()
    ds.file_meta.TransferSyntaxUID = "1.2.840.10008.1.2.1"
    ds.file_meta.MediaStorageSOPClassUID = "1.2.3"
    ds.file_meta.MediaStorageSOPInstanceUID = "4.5.6"
    ds.save_as(dicom_file, enforce_file_format=True)
    dicom_file.seek(0)
    return dicom_file


def test_deferred_elements_processing():
    """Exposes very nasty bug #149. Somewhere inside the deidentify() method, private
    tags with VR UN (Unknown) are lost.

    Notes
    -----
    This bug is very hard to debug because it involves pydicom deferred / lazy loading.
    This means that certain attributes of certain DICOM DataElements are not loaded
    initially. They are loaded as soon as any access to __attr__ is made. This has the
    effect that viewing any of these objects in a standard IDE debug window will make
    the bug disappear. Calling str() on the Dataset instance will make the bug
    disappear. Printing certain values will make the bug disappear.
    """

    def load_dataset():
        """Create a minimal dataset that is read from disk, meaning pydicom will use
        deferred loading on unknown bytes elements
        """
        ds = Dataset()
        block = ds.private_block(0x000B, "a_company", create=True)
        block.add_new(0x01, "UN", b"12325")  # add private tag '00b[a_company]01'
        file = create_dummy_disk_file(ds)
        ds = dcmread(file)
        ds.SOPClassUID = "1.2.840.10008.5.1.4.1.1.1"
        return ds

    # create a core that has 000b[a_company]01 in its safe-private definition
    core = create_default_core(
        safe_private_definition=SafePrivateDefinition(
            blocks=[
                SafePrivateBlock(
                    tags=["000b[a_company]00", "000b[a_company]01"],
                    criterion=lambda x: True,
                )
            ]
        )
    )

    # load the dataset containing 000b[a_company]01 from disk (deferred loading happens)
    ds = load_dataset()
    # deidentify with 000b[a_company]01 in the safe list
    ds_after = core.deidentify(ds)
    # the private element 000b[a_company]01 should still be in the processed dataset
    assert ds_after.get(0x000B1001)


def test_bouncer_pixel_processing_interplay():
    """Asserts correct behaviour of bouncers and pixel processor together
    see https://github.com/sjoerdk/idiscore/issues/152
    """
    # create a dataset with pixel data and burnedininfo = True, or non existant
    dataset_a = CTDatasetFactory()
    dataset_a.BurnedInAnnotations = True

    # create a bouncer that refuses this dataset
    bouncer = ProtocolFilterBouncer(
        criterion="Modality.equals('CT') and not BurnedInAnnotation.equals('False')",
        justification="CT is not to be trusted without explicit burned in "
        "annotation = False",
    )

    # create a pixel filter that fixes this

    # todo: remove PIILocation list. its not a useful object.. just use list
    processor = PixelProcessor(
        location_list=PIILocationList(
            [
                PIILocation(
                    areas=[SquareArea(5, 10, 4, 12), SquareArea(0, 0, 20, 3)],
                    criterion=lambda x: x.Modality
                    == "CT",  # TODO: replace this by dicomcriterion
                )
            ]
        )
    )

    # add these to a deidentifier
    core = Core(
        profile=Profile(
            rule_sets=[
                RuleSet(
                    rules=[Rule(SingleTag("PatientID"), Hash())],
                    name="test_ruleset",
                )
            ]
        ),
        bouncers=[bouncer],
        pixel_processor=processor,
    )

    # run dataset through deidentifier
    result = core.deidentify(dataset_a)

    # check whether dataset gets through
    assert result
