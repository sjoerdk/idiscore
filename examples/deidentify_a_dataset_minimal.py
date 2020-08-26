"""Minimal example of deidentifying a single file"""

import pydicom
from idiscore.defaults import create_default_core


core = create_default_core()  # create an idiscore instance

ds = pydicom.read("my_file.dcm")  # load a DICOM dataset
ds = core.deidentify(ds)  # remove patient information
ds.save_as("deidentified.dcm")  # save to disk
