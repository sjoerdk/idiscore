#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["pydicom==2.*", "dicomgenerator"]

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Sjoerd Kerkstra",
    author_email="sjoerd.kerkstra@radboudumcn.nl",
    python_requires="~=3.8",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
    ],
    description="Pure-python deidentification of DICOM images conforming to using "
    "Attribute Confidentiality Options",
    install_requires=requirements,
    license="GPLv3",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="idiscore",
    name="idiscore",
    packages=find_packages(include=["idiscore", "idiscore.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/sjoerdk/idiscore",
    version="1.0.0",
    zip_safe=False,
)
