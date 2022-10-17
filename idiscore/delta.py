from pydicom.tag import BaseTag

from idiscore.identifiers import get_keyword


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

    @property
    def tag_name(self) -> str:
        return get_keyword(self.tag)

    def __str__(self):
        return f"{self.tag} - {self.status}"

    def has_changed(self) -> bool:
        """Has changed or has been removed after deidentification"""
        return self.before != self.after

    def full_description(self) -> str:
        """Full human-readable description of the change that happened"""
        return (
            f"{self.tag} - {self.tag_name} - {self.status}: {self.before} "
            f"-> {self.after}"
        )
