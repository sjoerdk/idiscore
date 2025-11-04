# idiscore

[![CI](https://github.com/sjoerdk/idiscore/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/sjoerdk/idiscore/actions/workflows/build.yml?query=branch%3Amain)
[![PyPI](https://img.shields.io/pypi/v/idiscore)](https://pypi.org/project/idiscore/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/idiscore)](https://pypi.org/project/idiscore/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

Deidentification of DICOM images using Attribute Confidentiality Options

* Free software: GPLv3 License
* Documentation: https://idiscore.readthedocs.io.


## Installation
```
pip install idiscore
```

## Features
* Pure-python de-identification using pydicom
* Useful even without configuration - offers reasonable de-identification out of the box.
* Uses standard `DICOM Confidentiality options <http://dicom.nema.org/medical/dicom/current/output/chtml/part15/sect_E.3.html>`_
  to define de-identification that is to be performed

## Non-features
* No pipeline management, No special input and output handling. Only pydicom dataset in -> pydicom dataset out.
