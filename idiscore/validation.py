"""Classes and methods to check whether deidentification X works as expected

This differs from regular testing, as there is no one-size-fits all definition
of what a deidentification method should do.

The validation approach is as follows:

* Open an ExampleDataset. This can have annotations per DICOM element, indicating
  which definitely should be removed, which should be kept, etc.

* Deidentify with method X

* Compare before and after deidentification with respect to the annotations

* Repeat for as many examples as you want

* Produce a report specifying the method and the validation results per example

"""
from copy import deepcopy
from typing import Dict, List

from pydicom.dataset import Dataset

from idiscore.annotation import Annotation, ExampleDataset
from idiscore.core import Deidentifier
from idiscore.delta import Delta
from idiscore.exceptions import AnnotationValidationFailedError


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
        results: Dict[ExampleDataset, List[AnnotationCheckResult]],
    ):
        """

        Parameters
        ----------
        deidentifier_description: str
            Human readable description of the deidentifier that was validated
        results: Dict[ExampleDataset, List[AnnotationCheckResult]])
            For each DICOM example, a list of results after checking

        """
        self.deidentifier_description = deidentifier_description
        self.results = results

    def get_successful_examples(self) -> List[ExampleDataset]:
        return [x for x, y in self.results.items() if all(z.has_succeeded for z in y)]

    def get_failed_examples(self) -> List[ExampleDataset]:
        return [
            x for x, y in self.results.items() if not all(z.has_succeeded for z in y)
        ]

    def has_failed_checks(self) -> bool:
        """At least one check on on example failed"""
        return self.get_failed_examples() != []

    def summarize(self) -> str:
        output = f"Validation of '{self.deidentifier_description}'\n"
        output += f"On {len(self.results)} DICOM examples\n\n"

        output += "Results per example:\n"
        for example, results in self.results.items():
            errors = [x.message for x in results if not x.has_succeeded]
            if errors:
                output += f"* {example.description} - NOT OK " f"{','.join(errors)}\n"
            else:
                output += f"* {example.description} - OK\n"

        succes = len(self.get_successful_examples())
        fail = len(self.get_failed_examples())
        total = len(self.results)

        output += f"{succes}/{total} succeeded, {fail}/{total} failed\n"
        return output


class Validation:
    """A deidentifier with a collection of DICOM examples"""

    def __init__(self, deidentifier: Deidentifier, examples: List[ExampleDataset]):
        self.deidentifier = deidentifier
        self.examples = examples

    def run(self) -> ValidationResult:
        """Run all datasets through deidentifier and record results"""
        results = {x: check(self.deidentifier, x) for x in self.examples}
        return ValidationResult(
            deidentifier_description=str(self.deidentifier), results=results
        )


def check(
    deidentifier: Deidentifier, annotated_dataset: ExampleDataset
) -> List[AnnotationCheckResult]:
    """Does this deidentifier handle all DICOM elements according this example?

    Removing tags that should be removed, leaving tags that should be left, etc.
    """
    # Find out all changes made by deidentifier on this dataset
    signature = extract_signature(
        deidentifier=deidentifier, dataset=annotated_dataset.dataset
    )
    deltas = {delta.tag: delta for delta in signature}  # easy lookup later

    # Check whether these changes fit with the annotations
    results = []
    for tag, annotation in annotated_dataset.annotations.items():
        if delta := deltas.get(tag):
            try:
                annotation.assert_conformance(delta)
                results.append(
                    AnnotationCheckResult(
                        "OK", has_succeeded=True, annotation=annotation
                    )
                )
            except AnnotationValidationFailedError as e:
                results.append(
                    AnnotationCheckResult(
                        message=str(e), has_succeeded=False, annotation=annotation
                    )
                )
        else:
            pass  # no delta for this annotation, can't say anything more

    return results


def extract_signature(deidentifier: Deidentifier, dataset: Dataset) -> List[Delta]:
    """Specify exactly what happens to each tag when deidentifying

    Returns
    -------
    List[Delta]
        The change that occurred in each element of dataset
    """
    dataset_copy = deepcopy(dataset)  # deepcopy to compare before and after
    after = deidentifier.deidentify(dataset=dataset_copy)

    deltas = []
    for element in dataset:  # go over all original elements to find changes
        tag = element.tag
        val_before = element.value
        if tag_after := after.get(tag):
            val_after = tag_after.value
        else:
            val_after = None  # element was removed
        deltas.append(Delta(tag=tag, before=val_before, after=val_after))

    # find tags that might have been inserted
    inserted_tags = {x.tag for x in after} - {x.tag for x in dataset}
    for tag in inserted_tags:
        deltas.append(Delta(tag=tag, before=None, after=after[tag]))

    return deltas
