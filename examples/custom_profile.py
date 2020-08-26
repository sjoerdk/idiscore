"""You can set your own rules for specific DICOM tags. Be aware that this might

mean the deidentification is no longer DICOM-complient
"""

import pydicom
from idiscore.core import Core, Profile
from idiscore.defaults import get_dicom_rule_sets
from idiscore.identifiers import RepeatingGroup, SingleTag
from idiscore.operators import Hash, Remove
from idiscore.rules import Rule, RuleSet

# Custom rules that will hash the patient name and remove all curve data
my_ruleset = RuleSet(
    rules=[
        Rule(SingleTag("PatientName"), Hash()),
        Rule(RepeatingGroup("50xx,xxxx"), Remove()),
    ],
    name="My Custom RuleSet",
)

sets = get_dicom_rule_sets()  # Contains official DICOM deidentification rules
profile = Profile(  # add custom rules to basic profile
    rule_sets=[sets.basic_profile, my_ruleset]
)
core = Core(profile)  # Create an deidentification core

# read a DICOM dataset from file and write to another
core.deidentify(pydicom.read("my_file.dcm")).save_as("deidentified.dcm")
