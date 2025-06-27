=========
IDIS Core
=========


.. image:: https://github.com/sjoerdk/idiscore/actions/workflows/build.yml/badge.svg?branch=main
        :target: https://github.com/sjoerdk/idiscore/actions/workflows/build.yml?query=branch%3Amain
        :alt: Build Status

.. image:: https://img.shields.io/pypi/v/idiscore.svg
    :target: https://pypi.python.org/pypi/idiscore

.. image:: https://readthedocs.org/projects/idiscore/badge/?version=latest
        :target: https://idiscore.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black

.. image:: http://www.mypy-lang.org/static/mypy_badge.svg
    :target: http://mypy-lang.org/
    :alt: Checked with mypy



Deidentification of DICOM images using Attribute Confidentiality Options


* Free software: GPLv3 License
* Documentation: https://idiscore.readthedocs.io.


Features
--------
* Pure-python de-identification using pydicom
* Useful even without configuration - offers reasonable de-identification out of the box.
* Uses standard `DICOM Confidentiality options <http://dicom.nema.org/medical/dicom/current/output/chtml/part15/sect_E.3.html>`_
  to define de-identification that is to be performed

Non-features
------------
* No pipeline management, No special input and output handling. Only pydicom dataset in -> pydicom dataset out.


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
