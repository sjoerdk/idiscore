"""Functions and classes for turning existing DICOM files into editable datasets
and templates
"""
from pathlib import Path

import pydicom
from dicomgenerator.tools import replace_pixel_data

from idiscore.annotation import ExampleDataset
from idiscore.logging import get_module_logger

logger = get_module_logger("tools")


def dataset_to_json(dataset, replace_image_data=True, description="Converted"):
    """Turn dataset into a template. Replaces image data with tiny dummy image
    by default
    """
    if replace_image_data:
        dataset = replace_pixel_data(dataset)

    return ExampleDataset(dataset=dataset, description=description)


def to_annotated_dataset(
    input_path, output_path=None, description="Converted", replace_image_data=False
):
    """Reads dicom file at path and convert to annotated dataset

    Parameters
    ----------
    input_path: str:
        read dicom file here

    output_path: str, optional
        write annotated set to this path. If not given will write to <input_path>.json

    description: str, optional
        human-readable description of this dataset

    replace_image_data: Bool, optional
        Replace image pixel data with tiny dummy image

    Returns
    -------
    The path that was written to
    """
    input_path = Path(input_path)
    if output_path:
        output_path = Path(output_path)
    else:
        output_path = input_path.parent / (input_path.stem + "_template.json")

    logger.info(f"Reading dataset from {input_path}")
    dataset = pydicom.dcmread(input_path)
    with open(output_path, "w") as f_out:
        dataset_to_json(
            dataset, description=description, replace_image_data=replace_image_data
        ).save(f_out)
        logger.info(f"Wrote json dataset to {output_path}")
    return output_path
