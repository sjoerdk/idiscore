"""Classes and methods to annotate a DICOM file with respect to deidentification.
which elements contain personally identifiable information? which elements should
definitely not be touched?

Design requirements
===================
* 1 example = Self contained file. An AnnotatedDataset should contain all data
  and annotations. This makes it easy to add examples to a repository and
  to denote which examples a certain test uses.

* Annotations can be edited by text editor. DICOM files that still contain PII are
  often encountered on servers where a terminal is the only communication channel.
  It should be possible to annotate directly, and not face tricky hurdles to adding
  an example to an example library

"""
import json
from os import PathLike
from typing import Dict, List, Type

from dicomgenerator.importer import to_json
from pydicom.dataset import Dataset
from pydicom.tag import BaseTag, Tag

from idiscore.exceptions import AnnotationValidationFailed, IDISCoreException
from idiscore.delta import Delta, DeltaStatusCodes


class Annotation:
    """Information about a single DICOM element"""

    key = "annotation"  # short key for serialization, no spaces
    description = "A basic annotation"  # for humans

    def __init__(
        self, tag: BaseTag, tag_info: str = "", explanation: str = "",
    ):
        """A comment about about a DICOM tag.

        Parameters
        ----------
        tag: BaseTag
            The tag that this annotation is for
        tag_info: str, optional
            Human readable information about this tag. For example its value
            in the current dataset. Makes the serialized version of this annotation
            easier to annotated
        explanation: str, optional
            Why is this annotation like this? For example for a MUST_NOT_CHANGE
            annotation: 'because this is needed for loading in application X'.
            Optional, defaults to empty string

        """
        self.tag = tag
        self.tag_info = tag_info
        self.explanation = explanation

    def __str__(self):
        output = f"{self.tag} - {self.key}"
        if self.explanation:
            output += f" ({self.explanation})"
        return output

    @property
    def tag_key(self) -> str:
        """Convert DICOM Tag to a hex key like 0x00100010
        For serialization. Tag(tag.tag_key) = tag

        """
        return f"{self.tag:08X}"

    def to_dict(self) -> Dict:
        return {
            "tag": self.tag_key,  # key only, 0x00100010 for example
            "tag_info": str(self.tag_info),  # key, name and VR
            "annotation_type": self.key,
            "explanation": self.explanation,
        }

    @staticmethod
    def from_dict(dict_in) -> "Annotation":
        """Cast to correct child class of Annotation"""

        cls = AnnotationTypes.from_key(key=dict_in["annotation_type"])
        return cls(
            tag=Tag(dict_in["tag"]),
            tag_info=dict_in["tag_info"],
            explanation=dict_in.get("explanation"),
        )

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)

    def assert_conformance(self, delta: Delta) -> None:
        """Raises exception if delta goes against what validator wants

        For example, if annotation is 'do not change patient ID', and the delta shows
        a changed patient ID

        Raises
        ------
        AnnotationValidationFailed
            If delta does not conform to this validator. For example when an element
            contains PII, but the value is unchanged in delta
        """
        pass  # if not implemented in child class, just always pass


class MustNotChange(Annotation):

    key = "must_not_change"
    description = "This tag's value must not be deidentified"

    def assert_conformance(self, delta: Delta):
        if not delta.status == DeltaStatusCodes.UNCHANGED:
            raise AnnotationValidationFailed(
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
            raise AnnotationValidationFailed(
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
        except KeyError:
            raise UnknownAnnotationType(
                f'Unknown annotation type "{key}". '
                f"Known types: {list(cls.ALL.keys())}"
            )


class AnnotatedDataset:
    """A full DICOM dataset with annotations

    Notes
    -----
    * Should be serializable
    * Serialised, should be readable / editable in a text editor. It should
      be possible to create an a DICOM example from a command prompt



    """

    def __init__(
        self,
        dataset: Dataset,
        annotations: List[Annotation],
        description="No description",
    ):
        self.dataset = dataset
        self.annotations = annotations
        self.description = description

    def to_dict(self) -> Dict:
        """Serializable representation of this annotated dataset.
        Insert NO_ANNOTATION type annotations for each DICOM element, so that
        annotations can easily be added in a text editor

        """
        annotations_dict = {x.tag: x.to_dict() for x in self.annotations}
        for element in self.dataset:
            if element.tag not in annotations_dict:
                # No annotation for this tag. Add an empty one to help json editors
                annotation = EmptyAnnotation(tag=element.tag, tag_info=str(element))
                annotations_dict[annotation.tag_key] = annotation.to_dict()

        return {
            "dataset": to_json(self.dataset),
            "annotations": list(annotations_dict.values()),
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, dict_in) -> "AnnotatedDataset":
        """Load AnnotatedDataset from dict

        Will disregard any NO_ANNOTATION type annotations
        """

        annotations = []
        for annotation_dict in dict_in["annotations"]:

            if annotation_dict["annotation_type"] == EmptyAnnotation.key:
                # do not load NO_ANNOTATION, only useful in json representation
                pass
            else:
                annotations.append(Annotation.from_dict(annotation_dict))

        return AnnotatedDataset(
            dataset=Dataset.from_json(dict_in["dataset"]),
            annotations=annotations,
            description=dict_in["description"],
        )

    @classmethod
    def from_path(cls, path: PathLike) -> "AnnotatedDataset":
        """Load AnnotatedDataset from a json file"""

        with open(path, "r") as f:
            return AnnotatedDataset.from_dict(json.loads(f.read()))

    def to_json(self):
        return to_json(self.dataset)


class UnknownAnnotationType(IDISCoreException):
    pass
