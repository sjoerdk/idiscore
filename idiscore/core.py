import warnings
from typing import List, Optional, Union, Iterable, Tuple

from dicomgenerator.dicom import VRs
from pydicom.dataelem import DataElement
from pydicom.dataset import Dataset
from pydicom.sequence import Sequence

from idiscore import __version__
from idiscore.bouncers import (
    Bouncer,
    DatasetRejected,
    BouncerError,
    determine_bouncer_results,
)
from idiscore.dataset import RequiredTagNotFound
from idiscore.exceptions import IDISCoreError
from idiscore.image_processing import (
    PixelDataProcessorException,
    PixelProcessor,
)
from idiscore.operators import ElementShouldBeRemoved
from idiscore.rules import RuleSet
from idiscore.templates import (
    idiscore_description_rst,
    idiscore_description_txt,
    jinja_env,
    profile_description_rst,
    profile_description_txt,
)

# Used for holding a change to a DataElement (change or remove)
Mutation = Union[DataElement, ElementShouldBeRemoved]


class Profile:
    """Defines what to do with each DICOM tag in a dataset

    Models the complete deidentification of all DICOM elements except for pixel data

    Rules:
    * DICOM tags that are not mentioned explicitly in the profile are kept

    * A Profile holds a list of RuleSets. Later Rules overrule earlier

    * A profile's RuleSets can be 'flattened' to have exactly one operation for
      each tag

    """

    def __init__(self, rule_sets: List[RuleSet], name: str = "Profile"):
        """

        Parameters
        ----------
        rule_sets: List[RuleSet]
            All RuleSets that should be applied. Ordering is important; if two
            RuleSets contain a rule for the same DICOM tag, the RuleSet with the
            higher index takes precedence.
        name: str
            Human-readable name for this profile. Defaults to 'Profile'
        """
        self.rule_sets = rule_sets
        self.name = name

    def __str__(self):
        return f'Profile "{self.name}"'

    def flatten(self, additional_rule_sets: Optional[List[RuleSet]] = None) -> RuleSet:
        """Collapse all rule sets into one, ensuring only one rule per DICOM tag
        If a sets disagree, later sets (higher index in the list) take precedence.

        Parameters
        ----------
        additional_rule_sets: List[RuleSet]
            Append these to the existing rule sets, so they overrule them. Useful
            for one-time additions without changing the profile itself. For example
            when adding dataset-specific safe private rules.

        """
        if not additional_rule_sets:
            additional_rule_sets = []

        output = {}
        for rule_set in self.rule_sets + additional_rule_sets:
            output.update({x.identifier: x for x in rule_set.rules})

        return RuleSet(name="flattened", rules=set(output.values()))

    def description(self, text_format: str = "txt") -> str:
        """A multi-line, human-readable description of this profile

        Parameters
        ----------
        text_format: str,optional
            Format of output. Either 'txt' for flat string description, or 'rst'
            for Sphinx rst. Defaults to txt

        Raises
        ------
        ValueError
            For unknown format
        """
        if text_format == "txt" or not text_format:
            template = profile_description_txt
        elif text_format == "rst":
            template = profile_description_rst
        else:
            raise ValueError(
                f"{text_format} is not a valid format. Allowed:" f' ["txt","rst"]'
            )
        rules = self.flatten().rules
        return jinja_env.from_string(template).render(
            profile_name=self.name,
            rule_set_names=[f"* {x.name}" for x in self.rule_sets],
            rule_strings_by_name=sorted(x.as_human_readable() for x in rules),
            rule_strings_by_tag=sorted(
                f"{x.identifier} ({x.identifier.name()}) - {x.operation}" for x in rules
            ),
        )


class Deidentifier:
    """Something that has a deidentify() method that processes pydicom datasets"""

    def deidentify(self, dataset: Dataset) -> Dataset:
        raise NotImplementedError()


class Core(Deidentifier):
    """Can deidentify a DICOM dataset. Holds all configuration, filters and
    connections needed to do this
    """

    def __init__(
        self,
        profile: Profile,
        insertions: Optional[List[DataElement]] = None,
        bouncers: Optional[List[Bouncer]] = None,
        pixel_processor: Optional[PixelProcessor] = None,
    ):
        """

        Parameters
        ----------
        profile: Profile
            Defines what to do with each DICOM element (except PixelData)
        insertions: List[DataElement]
            DICOM elements to insert into each deidentified dataset
        bouncers: List[Bouncer], optional
            Inspect all incoming data and can reject if it is deemed not fit for
            deidentification. For example rejecting encapsulated PDFs as they are
            too difficult to deidentify. Defaults to empty list (all data allowed)
        pixel_processor: Optional[PrivateProcessor],
            Defines what to do with DICOM image data (the PixelData tag). Can remove
            or black out certain parts of an image. Defaults to None

        """
        self.profile = profile
        self.insertions = insertions if insertions else []  # convert default None
        self.bouncers = bouncers if bouncers else []
        self.pixel_processor = pixel_processor

    def deidentify(self, dataset: Dataset) -> Dataset:
        """Try to remove identifiable information from dataset

        Raises
        ------
        DeidentificationError
            If deidentification fails for any reason

        Warnings
        --------
        Input dataset is passed by reference so will be modified. The output
        of this function is the same object as the input
        >>> original_dataset
        >>> deidentified = core.deidentify(original_dataset)
        >>> original_dataset == deidentified  # True

        """
        # Check bouncers. Ones that might change after pixel cleaning are returned
        try:
            maybe_allow = determine_bouncer_results(self.bouncers, dataset)
        except (DatasetRejected, BouncerError) as e:
            raise DeidentificationError from e

        if maybe_allow:
            # one or more bouncers that currently reject might allow after pixel clean
            dataset = self.apply_pixel_processor(dataset)
        # check again
        self.apply_bouncers(maybe_allow, dataset)

        deidentified = self.apply_rules(rules=self.profile.flatten(), dataset=dataset)

        # add tags if needed
        for element in self.insertions:
            deidentified.add(element)

        return deidentified

    def collect_mutations(self, dataset, rules):
        """Determine mutation for each element in dataset, return non-empty mutations"""

        all_mutations = (
            (x, self.determine_mutation(dataset, x, rules)) for x in dataset
        )
        return (x for x in all_mutations if x[1] is not None)

    def determine_mutation(
        self, dataset: Dataset, element: DataElement, rules: RuleSet
    ) -> Union[None, Mutation]:
        """Find out whether to change, remove or keep the given element.

        Returns
        -------
        DataElement
            element should be changed to this
        ElementShouldBeRemoved
            element should be removed.
        None
            element should be kept as-is.


        Notes
        -----
        This will modify the input Dataset instance. Modification in-place to minimize
        memory footprint.

        """
        if element.VR == VRs.Sequence.short_name:  # recurse into sequences

            new = DataElement(
                tag=element.tag,
                VR=element.VR,
                value=Sequence(
                    [self.apply_rules(rules, sub_dataset) for sub_dataset in element]
                ),
            )
            return new

        elif rule := rules.get_rule(element):  # non-sequence
            try:
                new = rule.operation.apply(element, dataset)
                return new
            except ElementShouldBeRemoved as e:  # Operator signals removal
                return e  # Using Exception instance a signal object.. Smelly?

        else:  # no rule found. Leave this element unchanged.
            return None  # explicit return as it signals 'keep this element'

    @staticmethod
    def get_private_block_from_creator(ds, private_creator_elem):
        """Get a private block from an existing private creator element."""
        group = private_creator_elem.tag.group
        private_creator_name = private_creator_elem.value
        return ds.private_block(group, private_creator_name, create=False)

    @staticmethod
    def get_private_elements_for_block(ds, block):
        """Get all private elements by checking each possible offset."""
        private_elems = []
        for offset in range(0xFF):  # 0x00 to 0xFF
            if offset in block:
                private_elems.append(block[offset])

        return private_elems

    def apply_rules(self, rules: RuleSet, dataset: Dataset) -> Dataset:
        """Apply rules to each element in dataset, recursing into sequence elements

        Notes
        -----
        This will modify the input Dataset instance. Modification in-place to minimize
        memory footprint.
        """

        # at top level of file, process file_meta tags. Mainly for processing
        # MediaStorageSOPInstanceUID (0002,0003)
        if hasattr(dataset, "file_meta"):
            mutations = self.collect_mutations(dataset.file_meta, rules)
            self.apply_mutations(mutations, dataset.file_meta)

        # collect and apply all changes
        mutations = self.collect_mutations(dataset, rules)
        self.apply_mutations(mutations, dataset)

        return dataset

    @classmethod
    def apply_mutations(
        cls, mutations: Iterable[Tuple[DataElement, Mutation]], dataset: Dataset
    ):
        """Apply all mutations to the given dataset.

        Existing elements in data set will be overwritten by mutated ones. If an
        element does not exist, it will be overwritten.
        """

        # exclude private_creators
        private_creator_mutations = []
        for (original, mutation) in mutations:
            if original.tag.is_private_creator:  # process this later
                private_creator_mutations.append((original, mutation))
            elif isinstance(mutation, DataElement):
                dataset.add(mutation)  # add overwrites existing
            elif isinstance(mutation, ElementShouldBeRemoved):
                del dataset[original.tag]
            else:
                raise IDISCoreError(
                    f"Expected new element or remove signal, " f"got {mutation}"
                )

        cls.apply_private_creator_mutations(
            mutations=private_creator_mutations, dataset=dataset
        )

    @classmethod
    def apply_private_creator_mutations(
        cls, mutations: Iterable[Tuple[DataElement, Mutation]], dataset: Dataset
    ):
        """Apply all mutations to the given private creator tags

        Do not apply illegal private creator tag changes

        If a private creator would be removed but there are still private tags that
        reference it, cancel removal. This prevents creating invalid DICOM
        see https://github.com/sjoerdk/idiscore/issues/149#issuecomment-3868214042
        for reasoning.

        Notes
        -----
        Lots of instance creation going on here. Candidate for optimization.
        """

        for (original, mutation) in mutations:
            if isinstance(mutation, DataElement):
                raise IDISCoreError(
                    f"Rules seem to suggest altering private creator"
                    f"tag {original} into {mutation}. This would is too "
                    f"strange to allow."
                )
            elif isinstance(mutation, ElementShouldBeRemoved):
                block = cls.get_private_block_from_creator(dataset, original)
                all = cls.get_private_elements_for_block(dataset, block)
                if all:
                    # removing this would mangle the private block. Don't.
                    warnings.warn(
                        f"Not removing private creator tag {original} as there"
                        f" are still {len(all)} private tags that reference "
                        f"it: {[x for x in all]}",
                        stacklevel=2,
                    )
                else:
                    del dataset[original.tag]
            else:
                raise IDISCoreError(
                    f"Expected new element or remove signal, " f"got {mutation}"
                )

    def apply_pixel_processor(self, dataset):
        """Paint parts of image data black if required

        Raises
        ------
        DeidentificationError
            When dataset can not be processed
        """

        if self.pixel_processor:
            try:
                dataset = self.pixel_processor.clean_pixel_data(dataset)
            except PixelDataProcessorException as e:
                raise DeidentificationError(e) from e
        return dataset

    def description(self, text_format: str = "txt") -> str:
        """A multi-line, human-readable description of this instance

        what happens to each tag, which data will be rejected, etc.

        Parameters
        ----------
        text_format: str,optional
            Format of output. Either 'txt' for flat string description, or 'rst'
            for Sphinx rst. Defaults to txt

        Raises
        ------
        ValueError
            For unknown format
        """
        if text_format == "txt" or not text_format:
            template = idiscore_description_txt
        elif text_format == "rst":
            template = idiscore_description_rst
        else:
            raise ValueError(
                f"{text_format} is not a valid format. Allowed:" f' ["txt","rst"]'
            )

        return jinja_env.from_string(template).render(
            idiscore_lib_version=__version__,
            bouncer_descriptions=[x.description for x in self.bouncers],
            profile_description=self.profile.description(text_format=text_format)
            # if applicable, safe private
        )

    @staticmethod
    def apply_bouncers(bouncers, dataset):
        """Check all bouncers to see whether dataset should be rejected"""

        for bouncer in bouncers:
            try:
                bouncer.inspect(dataset)
            except (DatasetRejected, BouncerError) as e:
                raise DeidentificationError(e) from e


def handle_key_error(func):
    def decorated(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except KeyError as e:
            raise RequiredTagNotFound(f"Required tag not found: {e}") from e

    return decorated


class DeidentificationError(IDISCoreError):
    pass
