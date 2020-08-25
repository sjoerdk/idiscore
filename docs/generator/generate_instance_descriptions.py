"""Generates full descriptions for the default idiscore instance.
What is done to which tags?
"""
from pathlib import Path

from idiscore.defaults import create_default_core

destination = Path("../sphinx/default_core_description.rst")

with open(destination, "w+") as f:
    f.write(".. _default_core_description:\n\n")
    f.write(create_default_core().description(text_format="rst"))

print(f"description written to {destination}")
