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
from pathlib import Path
from typing import Dict, Type

import pydicom
from dicomgenerator.annotation import AnnotatedDataset
from dicomgenerator.persistence import JSONSerializable

from idiscore.delta import Delta, DeltaStatusCodes
from idiscore.dicom import ActionCodes
from idiscore.exceptions import AnnotationValidationFailedError, IDISCoreError
from idiscore.logging import get_module_logger

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


class FileExampleDataset(ExampleDataset):
    """An example dataset linked to a source DICOM file on disk

    Makes conversion (DICOM -> Example DICOM) cleaner
    """

    def __init__(self, dataset, source_file_path):
        super().__init__(dataset)
        self.source_file_path = source_file_path

    @classmethod
    def from_path(cls, source_file_path):
        logger.info(f"Reading DICOM dataset from {source_file_path}")
        return cls(
            dataset=pydicom.dcmread(source_file_path), source_file_path=source_file_path
        )

    def save(self, save_path=None):
        if save_path:
            save_path = Path(save_path)
        else:
            source = Path(self.source_file_path)
            save_path = source.parent / (source.stem + "_template.json")
        with open(save_path, "w") as f:
            super().save(f)
        logger.info(f"Wrote DICOM example to {save_path}")


def annotate(dicom_example: ExampleDataset, profile):
    """Add annotations to example dataset based on a profile
    Parameters
    ----------
    dicom_example: ExampleDataset
        Annotate this dataset
    profile: Profile
        Annotate tags that this profile says should be changed
    """
    actions_indicating_pii = (
        ActionCodes.REMOVE,
        ActionCodes.DUMMY,
        ActionCodes.EMPTY,
        ActionCodes.CLEAN,
    )

    def might_have_pii(rule):
        if not rule:
            return False
        else:
            return rule.operation.nema_action_code in actions_indicating_pii

    for element in dicom_example.dataset:
        rule = profile.get_rule(element)
        if might_have_pii(rule):
            dicom_example.annotations[element.tag] = ContainsPII(
                f"Basic Profile mandates action "
                f"{rule.operation.nema_action_code.var_name} for "
                f"this tag"
            )
    return dicom_example


class UnknownAnnotationType(IDISCoreError):
    pass
