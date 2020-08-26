.. _concepts:

========
Concepts
========

Things in idiscore that are not necessarily code but require more explanation nonetheless

.. _glossary:

Glossary
========
Terms used throughout this documentation

IDIS core
    Library that implements basic deidentification. Requires configuration before it can actually be used or deployed.
    Implements each of the standard DICOM confidentiality options.

DICOM deidentification option
    `DICOM Confidentiality options <http://dicom.nema.org/medical/dicom/current/output/chtml/part15/sect_E.3.html>`_ are
    a part of the DICOM standard which helps describe to which extent data is deidentified. In addition to a compulsory
    Basic profile there are 10 modifier options which either remove additional data, such as 'Clean Pixel Data' or which
    remove less data, such as 'Retain Patient Characteristics'.

IDIS core configuration
    All information needed by IDIS core to actually deidentify a DICOM dataset. Safe private tag definitions,
    the Confidentiality options to use, Pixel data definitions, and any custom additional options.

IDIS core instance
    A specific version of the IDIS core library combined with a specific configuration. This can be deployed and used as is.
    This is the object that can be validated and tested against a collection of DICOM examples.

DICOM example
    An annotated DICOM dataset. The annotations indicate for one or more DICOM tags whether the tag contains personal
    information or not. A DICOM example can be used to verify deidentification

IDIS verify
    A library that can run one or more DICOM examples through an IDIS core instance and test whether deidentification
    is correct according to each example. Produces a Data Certificate
    Potentially also determines which

Data certificate
    A list of DICOM examples which have been successfully passed through a IDIS Core instance IDIS Verify. For these
    examples the Core Instance is 'certified' to work properly. The data certificate can also be used to determine
    whether new data can be processed or not

DICOM example library
    A collection of DICOM examples

DICOM example tool
    CLI tool that makes it easy to collect, anonymize and annotate DICOM examples

PII
    Personally Identifiable Information. Information in a DICOM dataset that can be used to trace back the dataset to
    a single person. Deidentification attempts to remove all such information
