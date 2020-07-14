"""Classes and methods to check whether deidentification X works as expected

This differs from regular testing, as there is no one-size-fits all definition
of what a deidentification method should do.

The validation approach is as follows:
* Open a DICOMExample (annotated DICOM file). This indicates what is expected
  for the elements in that file
* Deidentify with method X (for example a certain idiscore.Core instance)
* Compare before and after deidentification with respect to the annotations
* Repeat for as many examples as you want
* Produce a report specifying the method and the validation results per example

"""
from copy import deepcopy
from typing import Dict, List

from pydicom.dataset import Dataset
from pydicom.tag import BaseTag

from idiscore.annotation import AnnotatedDataset, Annotation, ContainsPII, MustNotChange
from idiscore.exceptions import IDISCoreException


class Deidentifier:
    """Something that has a deidentify() method that processes pydicom datasets"""

    def deidentify(self, dataset: Dataset) -> Dataset:
        raise NotImplementedError


def crop_string(string_in: str, max_length: int = 40) -> str:
    """If string is more than max_length, cut and add ..."""
    if len(string_in) > max_length:
        return string_in[: (max_length - 3)] + "..."
    else:
        return string_in


class AnnotationCheckResult:
    """The outcome of checking a single annotation"""

    def __init__(self, message: str, has_succeeded: bool, annotation: Annotation):
        self.message = message
        self.has_succeeded = has_succeeded
        self.annotation = annotation

    def __str__(self):
        if self.has_succeeded:
            return "Success"
        else:
            return f"Failed: {crop_string(self.message)}"


class ValidationResult:
    """The outcome of running one or more examples through a deidentifier"""

    def __init__(
        self,
        deidentifier_description: str,
        results: Dict[AnnotatedDataset, List[AnnotationCheckResult]],
    ):
        """

        Parameters
        ----------
        deidentifier_description: str
            Human readable description of the deidentifier that was validated
        results: Dict[AnnotatedDataset, List[AnnotationCheckResult]])
            For each DICOM example, a list of results after checking

        """
        self.deidentifier_description = deidentifier_description
        self.results = results

    def get_successful_examples(self) -> List[AnnotatedDataset]:
        return [x for x, y in self.results.items() if all(z.has_succeeded for z in y)]

    def get_failed_examples(self) -> List[AnnotatedDataset]:
        return [
            x for x, y in self.results.items() if not all(z.has_succeeded for z in y)
        ]

    def has_failed_checks(self) -> bool:
        """At least one check on on example failed"""
        return self.get_failed_examples() != []

    def summarize(self) -> str:
        output = f"Validation of '{self.deidentifier_description}'\n"
        output += f"On {len(self.results)} DICOM examples\n\n"

        output += f"Results per example:\n"
        for example, results in self.results.items():
            errors = [x.message for x in results if not x.has_succeeded]
            if errors:
                output += f"* {example.description} - NOT OK " f"({','.join(errors)})\n"
            else:
                output += f"* {example.description} - OK\n"

        succes = len(self.get_successful_examples())
        fail = len(self.get_failed_examples())
        total = len(self.results)

        output += f"{succes}/{total} succeeded, {fail}/{total} failed\n"
        return output


class Validation:
    """Which DICOM examples to run through a deidentifier"""

    def __init__(self, deidentifier: Deidentifier, examples: List[AnnotatedDataset]):
        self.deidentifier = deidentifier
        self.examples = examples

    def run(self) -> ValidationResult:
        """Run all datasets through deidentifier and record results"""
        results = {x: check(self.deidentifier, x) for x in self.examples}
        return ValidationResult(
            deidentifier_description=str(self.deidentifier), results=results
        )


def assert_annotation(annotation: Annotation, before: Dataset, after: Dataset) -> None:
    """Check whether the annotation has been heeded

    Parameters
    ----------
    annotation: Annotation
        Annotation to check
    before: Dataset
        DICOM dataset before deidentification
    after: Dataset
        Dicom dataset after deidentification

    Raises
    ------
    AnnotationValidationFailed
        When an element containing PII has not been cleaned, or an essential
        element has been removed

    Notes
    -----
    Currently this implementation cannot handle tags inside groups. Only top-level
    tags are checked
    """
    # what element is this about?
    value_before = before[annotation.tag].value
    try:
        value_after = after[annotation.tag].value
    except KeyError:
        # Element has been removed completely. This is possibly OK
        value_after = None

    if type(annotation) == ContainsPII:
        # Element contained PII before. This should now have changed
        if value_before == value_after:
            raise AnnotationValidationFailed(
                f"{annotation.tag} contained PII "
                f"(explanation:'{annotation.explanation}') but was not changed or "
                f"removed. The value is still {value_after}"
            )
    elif type(annotation) == MustNotChange:
        if not value_before == value_after:
            raise AnnotationValidationFailed(
                f"{annotation.tag} had value {value_before} and should not change"
                f"(reason: '{annotation.explanation}'). However it was changed to"
                f"'{value_after}'"
            )

    else:
        raise ValueError()


def check(
    deidentifier: Deidentifier, annotated_dataset: AnnotatedDataset
) -> List[AnnotationCheckResult]:
    """Does this deidentifier handle all DICOM elements according this example?

    Removing tags that should be removed, leaving tags that should be left, etc.
    """
    # extract dataset from example and run this through deidentifier
    before = deepcopy(annotated_dataset.dataset)  # deepcopy to compare before and after
    after = deidentifier.deidentify(dataset=before)

    # have all the annotations been heeded?
    results = []
    for annotation in annotated_dataset.annotations:
        try:
            assert_annotation(annotation, before, after)
            results.append(
                AnnotationCheckResult("OK", has_succeeded=True, annotation=annotation)
            )
        except AnnotationValidationFailed as e:
            results.append(
                AnnotationCheckResult(
                    message=str(e), has_succeeded=False, annotation=annotation
                )
            )

    return results


class DeltaStatusCodes:
    """How has a DICOM element changed?"""

    UNCHANGED = "UNCHANGED"
    CHANGED = "CHANGED"
    REMOVED = "REMOVED"
    EMPTIED = "EMPTIED"
    CREATED = "CREATED"

    ALL = {UNCHANGED, CHANGED, REMOVED, EMPTIED, CREATED}


class Delta:
    """A change in a DICOM element value after deidentification"""

    def __init__(self, tag: BaseTag, before, after):
        self.tag = tag
        self.before = before
        self.after = after

    @property
    def status(self) -> str:
        if not self.has_changed():
            return DeltaStatusCodes.UNCHANGED
        else:
            if self.after is None:
                return DeltaStatusCodes.REMOVED
            elif self.after == "":
                return DeltaStatusCodes.EMPTIED
            elif self.before is None:
                return DeltaStatusCodes.CREATED
            else:
                return DeltaStatusCodes.CHANGED

    def __str__(self):
        return f"{self.tag} - {self.status}"

    def has_changed(self) -> bool:
        """Has changed or has been removed after deidentification"""
        return self.before != self.after

    def full_description(self) -> str:
        """Full human-readable description of the change that happened"""
        return f"{self.tag} - {self.status}: {self.before} -> {self.after}"


def extract_signature(deidentifier: Deidentifier, dataset: Dataset) -> List[Delta]:
    """Specify exactly what happens to each tag when deidentifying

    Returns
    -------
    List[Delta]
        The change that occurred in each element of dataset
    """
    before = deepcopy(dataset)  # deepcopy to compare before and after
    after = deidentifier.deidentify(dataset=dataset)

    deltas = []
    for element in before:  # go over all original elements to find changes
        tag = element.tag
        val_before = element.value
        if tag_after := after.get(tag):
            val_after = tag_after.value
        else:
            val_after = None  # element was removed
        deltas.append(Delta(tag=tag, before=val_before, after=val_after))

    # find tags that might have been inserted
    inserted_tags = {x.tag for x in after} - {x.tag for x in before}
    for tag in inserted_tags:
        deltas.append(Delta(tag=tag, before=None, after=after[tag]))

    return deltas


# TODO: USE extract_signature in assert_annotation


class AnnotationValidationFailed(IDISCoreException):
    pass
