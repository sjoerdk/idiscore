"""Classes and methods for handling private DICOM elements

Is a private tag is safe to keep? This can not be answered with regular rules of
the form tag -> operation. Sometimes you need to inspect the entire dataset, for
example to check modality or vendor.
"""

from typing import Callable, Iterable, List, Optional, Set

from pydicom.dataset import Dataset

from idiscore.rules import RuleSet
from idiscore.exceptions import PrivateProcessorException
from idiscore.identifiers import TagIdentifier
from idiscore.imageprocessing import CriterionException


class SafePrivateDefinition:
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
            elements are safe to keep in this instance. May raise CriterionException
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


class PrivateProcessor:
    """Uses SafePrivateDefinitions to determine all private DICOM elements that
    can be kept for any given dataset

    """

    def __init__(self, definitions: List[SafePrivateDefinition]):
        self.definitions = definitions

    def get_rule_set(self, dataset: Dataset) -> RuleSet:
        """Given this dataset, which private elements can be kept?

        Parameters
        ----------
        dataset: Dataset
            The DICOM dataset to inspect

        Returns
        -------
        RuleSet
            Rules for all private DICOM elements that are safe for the
            given dataset

        Raises
        ------
        PrivateProcessorException
            When rule set cannot be found properly
        """
        try:
            return RuleSet(
                name="safe private",
                rules={x.get_safe_private_tags(dataset) for x in self.definitions},
            )
        except CriterionException as e:
            raise PrivateProcessorException(e)
