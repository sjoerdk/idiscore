"""Command line interface code

Examples
--------
idiscore convert to_example <dcm file in>
idiscore convert to_dicom <json file in>
"""
import logging
from pathlib import Path

import click
from dicomgenerator.export import export
from dicomgenerator.tools import replace_pixel_data

from idiscore import logs
from idiscore.annotation import (
    ExampleDataset,
    FileExampleDataset,
    annotate,
    create_default_scrambler,
)
from idiscore.defaults import get_dicom_rule_sets
from idiscore.logs import get_module_logger

logger = get_module_logger("cli")


@click.group()
@click.option("-v", "--verbose", count=True)
def main(verbose):
    configure_logging(verbose)


def configure_logging(verbose):
    logging.basicConfig(level=logging.INFO)
    root_logger = logging.getLogger(logs.ROOT_LOGGER_NAME)
    if verbose == 0:
        root_logger.setLevel(logging.INFO)
    elif verbose == 1:
        root_logger.setLevel(logging.DEBUG)
    else:
        root_logger.setLevel(logging.DEBUG)


@click.group(name="convert")
def convert():
    """Convert between DICOM and Example files"""
    pass


@click.command()
@click.argument("dicom_file", type=click.Path())
@click.option("--output_file", type=click.Path(), default=None)
@click.option(
    "--replace-image-data/--no_replace-image_data",
    default=True,
    help="Replace pixel data with tiny dummy image",
)
@click.option(
    "--seed-annotations/--no-seed-annotations",
    default=True,
    help="Place PII annotations according to DICOM basic profile",
)
@click.option(
    "--scramble/--no-scramble",
    default=True,
    help="Replace PII values according to DICOM basic profile with random values",
)
def to_example(dicom_file, output_file, replace_image_data, seed_annotations, scramble):
    """Convert given DICOM file to an example file"""
    example = FileExampleDataset.from_dicom_path(dicom_file)
    if replace_image_data:
        example.dataset = replace_pixel_data(example.dataset)
    if seed_annotations:
        profile = get_dicom_rule_sets().basic_profile
        example.json_dataset = annotate(example.json_dataset, profile)
    if scramble:
        create_default_scrambler().scramble(example.dataset)

    example.save_to_path(output_file)


@click.command()
@click.argument("json_file", type=click.Path())
@click.option("--output_file", type=click.Path(), default=None)
def to_dicom(json_file, output_file):
    """Convert example file to a DICOM file"""
    if not output_file:
        json_file = Path(json_file)
        output_file = json_file.parent / (json_file.stem + ".dcm")
    with open(json_file) as f:
        example = ExampleDataset.load(f)

    logger.info(f"Writing DICOM dataset to {output_file}")
    export(example.dataset, path=output_file)


main.add_command(convert)
convert.add_command(to_example)
convert.add_command(to_dicom)
