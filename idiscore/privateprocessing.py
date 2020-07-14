"""Classes and methods for handling private DICOM elements

Is a private tag is safe to keep? This can not be answered with regular rules of
the form tag -> operation. Sometimes you need to inspect the entire dataset, for
example to check modality and vendor.
"""

from typing import Callable, Iterable, List, Optional, Set

from pydicom.dataset import Dataset
from pydicom.tag import Tag

from idiscore.core import RuleSet
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
    ):
        """

        Parameters
        ----------
        tags: Iterable[TagIdentifier]
            One ore more Tags of private DICOM elements
        criterion: Callable[[Dataset], bool], optional
            Function that returns True if these private Elements are safe to keep
            in the given dataset. May return CriterionException if a True or
            False answer cannot be given. Defaults to None, in which case the tags
            are always considered safe
        """
        self.tags = tags
        self.criterion = criterion

    def get_safe_private_tags(self, dataset: Dataset) -> Set[TagIdentifier]:
        """The private tags that are safe to keep, given this dataset

        Raises
        ------
        CriterionException
            If no True or False response can be given for this dataset
        """
        if self.criterion and self.criterion(dataset):
            return {x for x in self.tags}
        else:
            return set()


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
                rules={x for x in self.definitions if x.is_safe(dataset)},
            )
        except CriterionException as e:
            raise PrivateProcessorException(e)
