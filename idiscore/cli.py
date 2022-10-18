"""Command line interface code

Examples
--------
dicomgen convert to_json <dcm file in>
dicomgen convert to_dicom <json file in>
"""
import logging

import click
from dicomgenerator.tools import replace_pixel_data

from idiscore.annotation import FileExampleDataset


@click.group()
def main():
    logging.basicConfig(level=logging.INFO)


@click.group(name="convert")
def convert():
    """Convert between DICOM and DICOMExample"""
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
    help="Place PII annotation according to DICOM basic profile",
)
def to_dicom_example_cli(dicom_file, output_file, replace_image_data, seed_annotations):
    example = FileExampleDataset.from_path(dicom_file)
    if replace_image_data:
        example.dataset = replace_pixel_data(example.dataset)
    example.save(output_file)


main.add_command(convert)
convert.add_command(to_dicom_example_cli)
