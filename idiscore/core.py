# -*- coding: utf-8 -*-
from typing import Callable, List, Set, Tuple, Union

from pydicom.dataset import Dataset
from pydicom.tag import Tag
from pydicom.uid import UID

from idiscore.exceptions import IDISCoreException
from idiscore.operations import Operation


class Rule:
    """Defines what to do with a single DICOM element"""

    def __init__(self, tag: Tag, operation: Operation):
        self.tag = tag
        self.operation = operation


class RuleSet:
    """Defines what to do to one or more DICOM tags

    Models part of a deidentification procedure, such as the Basic Application
    Level Confidentiality Options in DICOM (e.g. Retain Safe Private Option)
    """
    def __init__(self, name: str, rules: Set[Rule]):
        self.name = name
        self.rules = rules


class Profile:
    """Defines what to do with each DICOM tag in a dataset

    Models the complete deidentification of all DICOM elements except for pixel data

    Rules:
    * DICOM tags that are not mentioned explicitly in the profile are removed
    * A Profile holds a list of RuleSets. Later Rules overrule earlier
    * A profile's RuleSets can be 'collapsed' to have one operation for each
      tag

    """
    def __init__(self, name: str, rule_sets: List[RuleSet]):
        """

        Parameters
        ----------
        name: str
            Human-readable name for this profile
        rule_sets: List[RuleSet]
            All RuleSets that should be applied. Ordering is important; if two
            RuleSets contain a rule for the same DICOM tag, the RuleSet with the
            higher index takes precedence.
        """
        self.name = name
        self.rule_sets = rule_sets

    def flatten(self, extra_rule_sets: List[RuleSet] = None) -> RuleSet:
        """Find a single rule for each DICOM tag. This means that we take
        all rules in the first RuleSet, then look at the second. For any conflicting
        rule the definition in the second RuleSet takes precedence

        """
        pass


class Bouncer:
    """Inspects a dataset and either rejects it or lets it through

    """
    def inspect(self, dataset: Dataset):
        """Check given dataset, raise exception if it should be rejected

        Parameters
        ----------
        dataset: Dataset
            The DICOM dataset to inspect

        Returns
        -------
        None

        Raises
        ------
        BouncerException
            When this dataset cannot be deidentified for any reason

        """
        pass


class RejectKOGSPS(Bouncer):

    def inspect(self, dataset: Dataset):
        """ This bouncer rejects three types of DICOM objects:
        1.2.840.10008.5.1.4.1.1.11.1 - GrayscaleSoftcopyPresentationStateStorage
        1.2.840.10008.5.1.4.1.1.88.59 - KeyObjectSelectionDocument
        1.2.840.10008.5.1.4.1.1.11.2 - ColorSoftcopyPresentationStateStorage
        These often contain ids and physician names in their SeriesDescription.
        See ticket #8465

        Raises
        ------
        BouncerException
            When the dataset is one of these types

        """
        black_list = [UID('1.2.840.10008.5.1.4.1.1.11.1'),
                      UID('1.2.840.10008.5.1.4.1.1.88.59'),
                      UID('1.2.840.10008.5.1.4.1.1.11.2')]

        def is_annotation(ds) -> bool:
            return ds['SeriesDescription'] == 'Annotation'

        for uid in black_list:
            if dataset['SopClassUID'] == uid and not is_annotation(dataset):
                raise BouncerException(
                    f'Datasets of type {uid.name} ({uid}) are not allowed as '
                    f'they often contain physician information')


class SafePrivateDefinition:
    """Defines when one or more private DICOM elements can be considered 'safe'
    Safe as in 'not containing personally identifiable information'
    """
    def __init__(self, tags:List[Tag], criterion: Callable[[Dataset], bool]):
        """

        Parameters
        ----------
        tags: List[Tag]
            One ore more Tags of private DICOM elements
        criterion: Callable[[Dataset], bool]
            Function that returns True if these private Elements are safe to keep
            in the given dataset. May return CriterionException if a True or
            False answer cannot be given
        """
        self.tags = tags
        self.criterion = criterion

    def is_safe(self, dataset: Dataset) -> bool:
        """These private tags are safe to keep in the given dataset

        Raises
        ------
        CriterionException
            If no True or False response can be given for this dataset
        """
        return self.criterion(dataset)


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
            return [x for x in self.definitions if x.is_safe(dataset)]
        except CriterionException as e:
            raise PrivateProcessorException(e)


class SquareArea:
    """A 2D square in pixel coordinates
    """
    def __init__(self, origin_x:int, origin_y:int, width: int, height: int):
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.width = width
        self.height = height


class PIILocation:
    """One or more areas in a DICOM image slice that might contain Personally
    Identifiable Information (PPI)

    Notes
    -----
    A PIILocation is 2D. Cleaning will be done on each slice individually.

    Responsibilities:
    * Holds location information. Does not alter PixelData itself
    * Determine whether it applies to a given Dataset

    """
    def __init__(self,
                 name: str,
                 criterion: Callable[[Dataset], bool],
                 areas: List[SquareArea]
                 ):
        """

        Parameters
        ----------
        name: str
            Human-readable name for this location
        criterion: Callable[[Dataset], bool]
            Function that return True if this PIILocation exists in the given dataset
            May return CriterionException if a True or False answer cannot be given
        areas: List[SquareArea]
            The
        """
        self.name = name
        self.criterion = criterion
        self.areas = areas

    def exists_in(self, dataset: Dataset) -> bool:
        """True if the given PII location exists in the given dataset

        Raises
        ------
        CriterionException
            If for some reason no True or False response can be given for this
            dataset
        """
        return self.criterion(dataset)


class PixelProcessor:
    """Finds and removes burned-in sensitive information in images

    Notes
    -----
    Responsibilities:
    * Checking whether a dataset needs cleaning of its pixel data
    * Checking whether redaction can be performed
    * Actually performing the blackout
    """
    def __init__(self, locations: List[PIILocation]):
        """

        Parameters
        ----------
        locations: List[PIILocation]
            Information on all potentials locations containing personally
            identifiable information

        """
        self.locations = locations

    @staticmethod
    def needs_cleaning(dataset: Dataset) -> bool:
        """Whether this dataset should be rejected as unsafe without cleaning

        Made this into a separate method as for many DICOM datasets you can
        reasonably skip the slow redaction process all together
        """
        # TODO: check separate criteria for suspicion! not get PPILocations
        return True

    def get_locations(self, dataset: Dataset) -> List[PIILocation]:
        """Get all locations with person information in the current dataset

        Raises
        ------
        PixelDataProcessorException
            When locations cannot be found properly
        """
        try:
            return [x for x in self.locations if x.exists_in(dataset)]
        except CriterionException as e:
            raise PixelDataProcessorException(e)

    def clean_pixel_data(self, dataset: Dataset) -> Dataset:
        """Remove pixel data in all PII locations and mark the dataset as safe

        Raises
        ------
        PixelDataProcessorException
            If cleaning pixeldata fails for any reason

        """
        for location in self.get_locations(dataset):
            #TODO: implement
            for area in location:
                print(f'Removing {area} in {dataset}')
        return dataset


class Core:
    """Can deidentify a DICOM dataset. Holds all configuration, filters and
    connections needed to do this
    """

    def __init__(self, bouncers: List[Bouncer],
                 profile: Profile,
                 safe_private: PrivateProcessor,
                 pixel_processor: PixelProcessor):
        self.profile = profile
        self.bouncers = bouncers
        self.safe_private = safe_private
        self.pixel_processor = pixel_processor

    def deidentify(self, dataset: Dataset):
        #TODO: implement

        # check all bouncers to see whether dataset should be rejected
        for bouncer in self.bouncers:
            bouncer.inspect(dataset)

        # check whether blackout is needed, then check whether a blackout is possible
        # run blackout if required
        if self.pixel_processor.needs_cleaning(dataset):
            dataset = self.pixel_processor.clean_pixel_data(dataset)

        # generate safe private ruleset for this dataset
        safe_private = self.safe_private.get_rule_set(dataset)

        # add this ruleset to profile and then flatten

        # run flattened profile (deidentify all tags)

        return dataset


class BouncerException(IDISCoreException):
    pass


class CriterionException(IDISCoreException):
    pass


class PixelDataProcessorException(IDISCoreException):
    pass


class PrivateProcessorException(IDISCoreException):
    pass
