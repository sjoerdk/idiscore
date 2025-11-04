# History

## 1.3.0 (2025-06-27)
* Drops python 3.8, 3.9 support, moves to 3.12. Using MINOR version bump instead of more usual major because code changes are minimal and I want version 2.0 to signal a real change in paradigm, not just a python version bump.
* Moves from pydicom 2 to pydicom 3
* Updates DICOM Profiles based on updated NEMA table

## 1.2.0 (2024-09-20)
* Updates DICOM Profiles based on updated NEMA table
* Follows NEMA in adding EMPTY_OR_DUMMY action code
* Several dependency updates and package maintenance

## 1.1.0 (2022-09-15)
* Stopped internal deepcopy DICOM files, improving performance and reducing IO issues
* Adopted PEP517 for package management. Using poetry now
* Packaging: push to pypi is now only done on github publish.

## 1.0.0 (2020-08-20)
* Deidentification implementing standard DICOM confidentiality profile and options
* Basic imagedata processing
* Support for safe private tags
* Documentation
* Line coverage over 90%

## 0.3.1 (2020-08-02)
* Alpha development

## 0.1.0 (2020-06-02)
* First release on PyPI.
