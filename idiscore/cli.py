"""Command line interface code

Examples
--------
dicomgen convert to_json <dcm file in>
dicomgen convert to_dicom <json file in>
"""
import logging

import click

from idiscore.tools import to_annotated_dataset


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
    "--replace-image-data/--no_replace_image_data",
    default=True,
    help="Replace pixel data with tiny dummy image",
)
def to_dicom_example(dicom_file, output_file, replace_image_data):
    to_annotated_dataset(
        input_path=dicom_file,
        replace_image_data=replace_image_data,
        output_path=output_file,
    )


main.add_command(convert)
convert.add_command(to_dicom_example)
