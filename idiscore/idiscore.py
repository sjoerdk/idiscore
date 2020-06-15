# -*- coding: utf-8 -*-
from typing import List, Set, Union

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
    """Defines what to do with each DICOM tag

    Models a complete deidentification procedure

    Some rules
    * DICOM tags that are not mentioned explicitly in the profile are removed
    * A Profile holds a list of RuleSets. Later Rules overrule earlier
    * A profile's RuleSets can be 'collapsed' to have one operation for each
      tag. Each operation uses only that tag's value; No inspecting the whole
      dataset

    """
    def __init__(self, name: str, rule_sets: List[RuleSet]):
        self.name = name
        self.rule_sets = rule_sets


class Bouncer:
    """Inspects a dataset and either rejects it or lets it in.

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
    """Defines under which circumstances private tags can be considered 'safe'
    Meaning the contain no personally identifiable information


    Has access to the full dataset
    """

    def to_rule_set(self, dataset: Dataset) -> RuleSet:
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

        """
        return RuleSet(name='Safe Private', rules=set())


class BlackOutDefinition:
    """Defines which parts of an image to black out to remove burned in information

    Has access to the full dataset
    """
    pass


class Core:
    """Can deidentify a DICOM dataset. Holds all configuration, filters and
    connections needed to do this
    """

    def __init__(self, bouncers: List[Bouncer],
                 profile: Profile,
                 safe_private: SafePrivateDefinition,
                 black_out: BlackOutDefinition):
        self.profile = profile
        self.bouncers = bouncers
        self.safe_private = safe_private
        self.black_out = black_out

    def deidentify(self, dataset: Dataset):
        #TODO: implement

        # check all bouncers to see whether dataset should be rejected

        # check whether blackout is needed, then check whether a blackout is possible
        # run blackout if required

        # generate safe private ruleset for this dataset

        # add this ruleset to profile and flatten profile

        # run flattened profile (deidentify all tags)

        return dataset


class BouncerException(IDISCoreException):
    pass
