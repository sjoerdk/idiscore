"""
    Extract and store main tags that identify the DICOM before pseudonymization.
    Otherwise, apply basic profile 
"""

import os
import pydicom
import uuid

from idiscore.core import Core, Profile
from idiscore.defaults import get_dicom_rule_sets
from idiscore.identifiers import RepeatingGroup, SingleTag
from idiscore.operators import Hash, Remove, ReplaceAndStore, BijectiveDummyGenerator
from idiscore.rules import Rule, RuleSet

# Define and instantiate a generator
class BijectiveDummyFileGenerator():
    # BijectiveDummyGenerator that stores the mapping of dummy values and sensitive PHI to a file

    def __init__(self, filename: str):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                pass

    def store_value(self, element: pydicom.DataElement) -> str:
        """Checks file for existing dummy; if missing, creates and saves one."""
        # Check for existing
        with open(self.filename, "r") as f:
            for line in f:
                if line.strip() and "," in line:
                    saved_val, saved_dummy = line.strip().split(",", 1)
                    if saved_val == element.tag:
                        return saved_dummy

        # Not found? Create a new one based on VR constraints
        new_dummy = str(uuid.uuid4().hex)
        if element.VR == "SH":
            new_dummy = new_dummy[:16]
        elif element.VR in ["PN", "LO"]:
            new_dummy = new_dummy[:64]

        # Save it
        with open(self.filename, "a") as f:
            f.write(f"{element.tag},{new_dummy}\n")
        
        return new_dummy


# Custom rules that will hash the patient name and remove all curve data
my_ruleset = RuleSet(
    rules=[
        Rule(SingleTag("PatientID"), ReplaceAndStore()),
        Rule(SingleTag("StudyInstanceUID"), ReplaceAndStore()),
        Rule(SingleTag("AccessionNumber"), ReplaceAndStore()),
    ],
    name="My Custom RuleSet",
)

sets = get_dicom_rule_sets()  # Contains official DICOM deidentification rules
profile = Profile(  # add custom rules to basic profile
    rule_sets=[sets.basic_profile, my_ruleset]
)
core = Core(profile)  # Create an deidentification core

# read a DICOM dataset from file and write to another
core.deidentify(pydicom.dcmread("my_file.dcm")).save_as("deidentified.dcm")