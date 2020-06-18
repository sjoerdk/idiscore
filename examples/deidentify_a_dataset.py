import pydicom

from idiscore.core import Core


# Basic deidentification
core = Core()
deidentified_ds = core.deidentify(pydicom.read("myfile.dcm"))
deidentified_ds.save_as("deidentified.dcm")


# Alter settings
# TODO: write
