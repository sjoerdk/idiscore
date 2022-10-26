"""Classes and methods to annotate a DICOM file with respect to deidentification.
which elements contain personally identifiable information? which elements should
definitely not be touched?

Design requirements
===================
* 1 example = Self contained file. An ExampleDataset should contain all data
  and annotations. This makes it easy to add examples to a repository and
  to denote which examples a certain test uses.

* Annotations can be edited by text editor. DICOM files that still contain PII are
  often encountered on servers where a terminal is the only communication channel.
  It should be possible to annotate directly, and not face tricky hurdles to adding
  an example to an example library

"""
import collections
from typing import Any, Callable, Dict, Optional, Type

from dicomgenerator.annotation import AnnotatedDataset
from dicomgenerator.dicom import VRs
from dicomgenerator.generators import DataElementFactory
from dicomgenerator.persistence import FileJSONDataset, JSONSerializable
from pydicom.dataelem import DataElement
from pydicom.dataset import Dataset

from idiscore.defaults import get_dicom_rule_sets
from idiscore.delta import Delta, DeltaStatusCodes
from idiscore.dicom import ActionCodes
from idiscore.exceptions import AnnotationValidationFailedError, IDISCoreError
from idiscore.logs import get_module_logger

logger = get_module_logger("annotation")


class Annotation(JSONSerializable):
    """Information about a single DICOM element"""

    key = "annotation"  # short key for serialization, no spaces
    description = "A basic annotation"  # for humans

    def __init__(
        self,
        explanation: str = "",
    ):
        """A comment about a DICOM tag.

        Parameters
        ----------
        explanation: str, optional
            Why is this annotation like this? For example for a MUST_NOT_CHANGE
            annotation: 'because this is needed for loading in application X'.
            Optional, defaults to empty string

        """
        self.explanation = explanation

    def __str__(self):
        return f"{type(self).__name__}({self.explanation})"

    def to_json_dict(self) -> Dict:
        return {
            "annotation_type": self.key,
            "explanation": self.explanation,
        }

    @classmethod
    def from_json_dict(cls, dict_in) -> "Annotation":
        """Cast to correct child class of Annotation"""

        klass = AnnotationTypes.from_key(key=dict_in["annotation_type"])
        return klass(
            explanation=dict_in.get("explanation"),
        )

    def assert_conformance(self, delta: Delta) -> None:
        """Raises exception if delta goes against what validator wants

        For example, if annotation is 'do not change patient ID', and the delta shows
        a changed patient ID

        Raises
        ------
        AnnotationValidationFailedError
            If delta does not conform to this validator. For example when an element
            contains PII, but the value is unchanged in delta
        """
        pass  # if not implemented in child class, just always pass


class MustNotChange(Annotation):

    key = "must_not_change"
    description = "This tag's value must not be deidentified"

    def assert_conformance(self, delta: Delta):
        if not delta.status == DeltaStatusCodes.UNCHANGED:
            raise AnnotationValidationFailedError(
                f"{delta.tag} had value {delta.before} and should not change"
                f"(reason: '{self.explanation}'). However it was changed to"
                f"'{delta.after}'"
            )


class ContainsPII(Annotation):

    key = "contains_pii"
    description = "this tag contains personally identifiable information"

    def assert_conformance(self, delta: Delta):
        if delta.status not in [
            DeltaStatusCodes.REMOVED,
            DeltaStatusCodes.EMPTIED,
            DeltaStatusCodes.CHANGED,
        ]:
            raise AnnotationValidationFailedError(
                f"{delta.tag} contained PII (explanation:'{self.explanation}') "
                f"but was not changed or removed. The value is still {delta.after}"
            )


class EmptyAnnotation(Annotation):
    """For representing empty annotation in json. Can then be easily filled by
    editing json with text editor
    """

    key = "no_annotation"
    description = "No annotation for this tag"


class AnnotationTypes:
    """Lists all annotation types. Helps with serialization"""

    ALL = {
        MustNotChange.key: MustNotChange,
        ContainsPII.key: ContainsPII,
        EmptyAnnotation.key: EmptyAnnotation,
    }

    @classmethod
    def from_key(cls, key: str) -> Type[Annotation]:
        try:
            return cls.ALL[key]
        except KeyError as e:
            raise UnknownAnnotationType(
                f'Unknown annotation type "{key}". '
                f"Known types: {list(cls.ALL.keys())}"
            ) from e


class ExampleDataset(AnnotatedDataset):
    def __init__(self, dataset, description="No description", annotations=None):
        """A full DICOM dataset with annotations

        Builds on dicomgenerator.ExampleDataset, adds more elaborate annotations

        Parameters
        ----------
        dataset: Dataset
            The pydicom dataset
        description: str
            Description of this dataset
        annotations: Dict[TagLike, Annotation]
            Annotations per tag. TagLike can be DICOM tag name such as 'PatientID'
            ,hex such as '0x0010,0x0012' or a Tag object. JsonSerializable is
            anything that you can put in json.dumps()
        """
        super().__init__(
            dataset=dataset, description=description, annotations=annotations
        )

    @classmethod
    def parse_annotation(cls, annotation_json_obj):
        """Process raw annotation object. For overwriting in child classes"""
        return Annotation.from_json_dict(annotation_json_obj)


class FileExampleDataset(FileJSONDataset):
    """An example dataset linked to a source DICOM file on disk

    Makes conversion (DICOM -> Example DICOM) cleaner
    """

    json_dataset_class = ExampleDataset


def create_pii_filter(profile):
    """Filter to use with Scrambler.scramble()"""

    def might_contain_pii(element):
        return bool(get_cleaning_rule(element, profile))

    return might_contain_pii


def get_cleaning_rule(element, profile):
    """Profile indicates that this element should be cleaned or removed
    Returns
    -------
    Optional[Rule]:
        The cleaning or removing rule for this element, or None if there is no
        rule of the rule is not a cleaning or removing rule

    """
    actions_indicating_pii = (
        ActionCodes.REMOVE,
        ActionCodes.DUMMY,
        ActionCodes.EMPTY,
        ActionCodes.CLEAN,
    )
    rule = profile.get_rule(element)
    if not rule:
        return None
    elif rule.operation.nema_action_code in actions_indicating_pii:
        return rule
    else:
        return None


def annotate(dicom_example: ExampleDataset, profile):
    """Add annotations to example dataset based on a profile
    Parameters
    ----------
    dicom_example: ExampleDataset
        Annotate this dataset
    profile: Profile
        Annotate tags that this profile says should be changed
    """

    logger.info(f"Annotating using {profile}")
    new_annotations = {}
    for element in dicom_example.dataset:
        rule = get_cleaning_rule(element, profile)
        if rule:
            new_annotations[element.tag] = ContainsPII(
                f"Basic Profile mandates action "
                f"{rule.operation.nema_action_code.var_name} for "
                f"this tag"
            )
    logger.info(f"Added {len(new_annotations)} annotations")
    dicom_example.annotations.update(new_annotations)
    return dicom_example


class Scrambler:
    def __init__(
        self, element_filter: Optional[Callable[[DataElement], bool]] = lambda x: True
    ):
        """

        Parameters
        ----------
        element_filter: optional
            Callable that takes a DataElement in and returns True for scramble or False
            for skip and leave unaltered. Defaults to scrambling all

        """
        self.replacements: Dict[str, Any] = {}
        self.element_filter = element_filter

    def reset_replacements(self):
        self.replacements = {}

    def scramble(self, dataset: Dataset):
        """Replace the most identifiable data in dataset

        Main purpose is to save a user from manually replacing 100+ dicom elements,
        while still keeping the dataset 'realistic'. This balance is struck by
        replacing only some elements:
        * The most annoying to replace elements like UIDs (annoying to keep consistent)
        * The most glaringly PII containing tags like Patient and Physician Names

        Does not remove or add any dicom elements. Internal consistency is maintained
        by mapping each string in dataset to a random value that is randomized for
        each run.

        Desired functions:
        * Deidentify data for use as example data in deidentification validation
        * Maintain original data structure as much as possible, even if original data
          is not valid DICOM. This is to ensure real-life examples for validation,
          not just ideal pydicom-generated proper datasets. Real DICOM can be very
          bad. We don't want to sugarcoat things.

        Parameters
        ----------
        dataset:
            dataset to scramble elements of

        Warnings
        --------
        This is not a full deidentification. After scrambling there might still be PII
        in the dataset. Do a manual check before committing anything
        """
        if self.element_filter:
            elements_to_scramble = [x for x in dataset if self.element_filter(x)]
        else:
            elements_to_scramble = list(dataset)  # don't filter

        logger.info(
            f"Scrambling {len(elements_to_scramble)} elements of "
            f"{len([x for x in dataset])} in dataset"
        )

        for element in elements_to_scramble:
            if element.VR == VRs.Sequence.short_name:  # recurse into sequences
                for ds in element:
                    self.scramble(ds)
            else:
                self.scramble_element(element)
        self.reset_replacements()

    def scramble_element(self, element):
        """Scramble given element, trying to give the same scrambled value"""

        if isinstance(element.value, collections.abc.Hashable):
            value = element.value
        else:
            value = str(element.value)  # not very clean, but it's a scramble function..

        if value == "":
            return  # don't fill in empty values with gibberish

        previous_replacement = self.replacements.get((element.VR, value))
        if previous_replacement is None:
            replacement = DataElementFactory(VR=element.VR).value
            element.value = replacement
            self.replacements[(element.VR, value)] = replacement

            logger.debug(f"Replacing '{truncate(value,200)}' with '{replacement}'")
        else:
            element.value = previous_replacement


def truncate(value, length):
    value = str(value)
    if len(value) > length - 14:
        return value[: length - 14] + "...<truncated>"
    else:
        return value


def create_default_scrambler():
    """A scrambler that scrambles all tags containing PII according to
    DICOM basic deidentificaion profile
    """
    return Scrambler(
        element_filter=create_pii_filter(profile=get_dicom_rule_sets().basic_profile)
    )


class UnknownAnnotationType(IDISCoreError):
    pass
