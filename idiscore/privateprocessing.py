"""Classes and methods for handling private DICOM elements

Is a private tag is safe to keep? This can not be answered with regular rules of
the form tag -> operation. Sometimes you need to inspect the entire dataset, for
example to check modality or vendor.
"""

from typing import Callable, Iterable, List, Optional, Set

from pydicom.dataelem import DataElement
from pydicom.dataset import Dataset

from idiscore.exceptions import SafePrivateException
from idiscore.identifiers import TagIdentifier
from idiscore.imageprocessing import CriterionException


class SafePrivateBlock:
    """Defines when one or more private DICOM elements can be considered 'safe'

    Safe as in 'not containing personally identifiable information'
    """

    def __init__(
        self,
        tags: Iterable[TagIdentifier],
        criterion: Optional[Callable[[Dataset], bool]] = None,
        comment: str = "",
    ):
        """

        Parameters
        ----------
        tags: Iterable[TagIdentifier]
            One ore more Tags of private DICOM elements
        criterion: Callable[[Dataset], bool], optional
            Function that is fed a Dataset instance. Returns True if the private
            elements are safe to keep in the dataset. May raise CriterionException
            if a True or False answer cannot be given. Defaults to None, in which
            case the elements are always considered safe
        comment: str
            human readable explanation of why these tags are safe, or the domain in
            which they are safe (only in this hospital, only for these machines etc.)
        """
        self.tags = tags
        self.criterion = criterion
        self.comment = comment

    def get_safe_private_tags(self, dataset: Dataset) -> Set[TagIdentifier]:
        """The private tags that are safe to keep, given this dataset

        Raises
        ------
        CriterionException
            If no True or False response can be given for this dataset
        """
        if self.tags_are_safe(dataset):
            return {x for x in self.tags}
        else:
            return set()

    def tags_are_safe(self, dataset: Dataset) -> bool:
        """True if these private tags are safe to keep in this dataset"""
        if self.criterion:
            try:
                return self.criterion(dataset)
            except AttributeError as e:
                raise CriterionException(f'Error while checking criterion: "{e}"')
        else:
            return True  # no criterion. Assume tags are always safe


class SafePrivateDefinition:
    """Holds all information on which private tags can be considered safe

    Contains one or more SafePrivateBlocks
    """

    def __init__(self, blocks: List[SafePrivateBlock]):
        self.blocks = blocks

    def is_safe(self, element: DataElement, dataset: Dataset) -> bool:
        """True if the given private element in the given dataset is safe to keep

        Raises
        ------
        SafePrivateException
            If for some reason it cannot be determined whether this is safe
        """
        return any(x.matches(element) for x in self.safe_identifiers(dataset))

    def safe_identifiers(self, dataset: Dataset) -> List[TagIdentifier]:
        """All tags that are safe to keep given this dataset

        Raises
        ------
        SafePrivateException
            If safe identifiers cannot be determined
        """
        identifiers = []
        for definition in self.blocks:
            try:
                identifiers += definition.get_safe_private_tags(dataset)
            except CriterionException as e:
                raise SafePrivateException(e)
        return identifiers
