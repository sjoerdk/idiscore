"""Classes and methods to annotate a DICOM file with respect to deidentification.
which elements contain personally identifiable information? which elements should
definitely not be touched?
"""

from typing import Dict

from pydicom.dataset import Dataset
from pydicom.tag import Tag


class Annotation:
    """Information about a single DICOM tag"""

    key = "short_key"  # for serialization, no spaces
    description = "longer description of this class"  # for humans

    def __str__(self):
        return self.description


class ContainsPII(Annotation):
    key = "contains_pii"
    description = "this tag contains personally identifiable information"  # for humans


class MustNotChange(Annotation):

    CONTAINS_PII = (
        "contains_pii"  # this tag contains personally identifiable information
    )
    MUST_NOT_CHANGE = "must_not_change"  # this tag

    def __init__(self, reason: str = ""):
        """Something must not change, with optional reason why.

        Parameters
        ----------
        reason: str, optional
            Why must this not change? For example 'because this is needed for loading
            in application X'. Optional, defaults to empty string

        """
        self.reason = reason

    def __str__(self):
        output = self.description
        if self.reason:
            output += f" ({self.reason})"
        return output


class DICOMExample:
    def __init__(
        self,
        dataset: Dataset,
        annotations: Dict[Tag, Annotation],
        description="No description",
    ):
        self.dataset = dataset
        self.annotations = annotations
        self.description = description

    def to_json(self):
        return [self.dataset]
