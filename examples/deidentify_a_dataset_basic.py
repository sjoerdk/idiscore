"""Basic example of deidentifying a single file"""

import pydicom

from idiscore.core import Core, Profile
from idiscore.defaults import get_dicom_rule_sets

sets = get_dicom_rule_sets()  # Contains official DICOM deidentification rules
profile = Profile(  # Choose which rule sets to use
    rule_sets=[sets.basic_profile, sets.retain_modified_dates, sets.retain_device_id]
)
core = Core(profile)  # Create an deidentification core

# read a DICOM dataset from file and write to another

# pydicom.dcmread("/tmp/idis/a_dicom_file").save_as("/tmp/idis/deidentified")
core.deidentify(pydicom.dcmread("/tmp/idis/a_dicom_file")).save_as(
    "/tmp/idis/deidentified"
)
