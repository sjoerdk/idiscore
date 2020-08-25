"""How mark safe private tags and known PII locations"""

import pydicom
from idiscore.core import Core, Profile
from idiscore.defaults import get_dicom_rule_sets

sets = get_dicom_rule_sets()  # Contains official DICOM deidentification rules
profile = Profile(  # Choose which rule sets to use
    rule_sets=[sets.basic_profile, sets.retain_modified_dates, sets.retain_device_id]
)
core = Core(profile)  # Create an deidentification core

# read a DICOM dataset from file and write to another
core.deidentify(pydicom.read("my_file.dcm")).save_as("deidentified.dcm")
