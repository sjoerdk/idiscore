=========
IDIS Core
=========

.. image:: https://github.com/sjoerdk/idiscore/workflows/build/badge.svg
        :target: https://github.com/sjoerdk/idiscore/actions?query=workflow%3Abuild
        :alt: Build Status

.. image:: https://img.shields.io/pypi/v/idiscore.svg
    :target: https://pypi.python.org/pypi/idiscore

.. image:: https://readthedocs.org/projects/idiscore/badge/?version=latest
        :target: https://idiscore.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://codecov.io/gh/sjoerdk/idiscore/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/sjoerdk/idiscore

.. image:: https://pyup.io/repos/github/sjoerdk/idiscore/shield.svg
     :target: https://pyup.io/repos/github/sjoerdk/idiscore/
     :alt: Updates

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black


Deidentification of DICOM images using Attribute Confidentiality Options


* Free software: GPLv3 License
* Documentation: https://idiscore.readthedocs.io.


Features
--------
* Pure-python de-identification using pydicom
* De-identification is verified by test suite
* Useful even without configuration - offers reasonable de-identification out of the box.
* Uses standard `DICOM Confidentiality options <http://dicom.nema.org/medical/dicom/current/output/chtml/part15/sect_E.3.html>`_
  to define de-identification that is to be performed
* Focus on de-identification, pydicom dataset in -> pydicom dataset out. No pipeline management, No special input and output
  handling.


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
