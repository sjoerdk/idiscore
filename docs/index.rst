Welcome to IDIS Core's documentation!
======================================

IDIS core de-identifies DICOM datasets. It does this by removing or replacing certain DICOM tags, and by removing
voxels in the DICOM image data if needed.

Goals
=====
* Deidentify DICOM datasets in conformance to the DICOM standard.
* Configuration is an extra, not a requirement. With minimal configuration IDIS core should deidentify a dataset 'well'
  This means IDIS core will include opinions on deidentification.
* Python all the way. No custom configuration languages, no installers, just scripts and pip. IDIS core assumes you can
  write python and leverages class inheritance, docstrings, pytest, variable annotations. This keeps things clean,
  testable and unambiguous

Non-Goals
=========
* Deidentification pipeline. IDIS core deidentifies a DICOM dataset. It does not care where this dataset came from or
  where it is going to.
* Handling DICOM files. Internally IDIS core only works with pydicom datasets. Reading and writing of datasets is expedited
  to pydicom. Thank you pydicom.

Alternatives
============
Alternative methods of de-identification

CTP
    `MIRC CTP <http://mircwiki.rsna.org/index.php?title=MIRC_CTP>`_ is a widely used, extensive, java-based framework
    for deidentification and data aggragation. It has many plugins and can be configured using several scripting languages.
    All in all it is a very good choice for many people. For me as a programmer developing mostly python-based software,
    I have found it to have some drawbacks however:

    * It is difficult to integrate into a test suite properly. This is first of all because it is file-based, requiring an
      actual file on disk for each type of DICOM you might want to verify the deidentification of. Second, because the pipeline
      is configured with several different custom scripts it is difficult to set up the correct context for tests.
    * I found it tricky to integrate into my python-based infrastructure. Again, because the pipeline is java based and
      file-based there is no easy way to access the state of files in the pipeline. Is a file done? Has something gone wrong?
      Getting this information would require either checking all possible output, stage and quarantine folders. I was really
      missing exceptions I could catch.
    * Because it is an installable pipeline, I found it difficult to integrate into smaller, non-server based applications like
      a command line tool that locally deidentifies some data for a user.

deid
    `pydicom deid <https://github.com/pydicom/deid>`_ is a pydicom based best-effort anonymizer for medical image data.
    It is part of the pydicom family. It has `extensive and friendly documentation <https://pydicom.github.io/deid/>`_
    and get several concepts right.
    Reasons for not expanding on this library and instead starting a new one:

    * There seems to have been little development since the libraries start in 2017
    * Seems to be quite file-based in places, often requiring input and output folders for initializing objects
    * No test coverage monitoring, uses unittest for testing which is hard to maintain and expand on
    * Uses `custom scripting <https://pydicom.github.io/deid/examples/recipe/>`_ language for configuring the anonymization. This
      is useful for non-coding end-users, but adds a layer of indirectness to testing.


Concepts
========
In this documentation, the following terms are used often:

IDIS core
    Library that implements basic deidentification. Requires configuration before it can actually be used or deployed.
    Implements each of the standard DICOM confidentiality options.

DICOM deidentification option
    `DICOM Confidentiality options <http://dicom.nema.org/medical/dicom/current/output/chtml/part15/sect_E.3.html>`_ are
    a part of the DICOM standard which helps describe to which extent data is deidentified. In addition to a compulsary
    Basic profile there are 10 modifier options which either remove additional data, such as 'Clean Pixel Data' or which
    remove less data, such as 'Retain Patient Characteristics'.

IDIS core configuration
    All information needed by IDIS core to actually deidentify a DICOM dataset. Safe private tag definitions,
    the Confidentiality options to use, Pixel data definitions, and any custom additional options.

IDIS core instance
    A specific version of the IDIS core library combined with a specific configuration. This can be deployed an used as is.
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

DICOM data type
    A 'kind' of DICOM data. Given the heterogeneity of DICOM this is a very tricky / impossible thing to define.
    In the context of deidentification it can, however, be meaningfully defined with respect to a specific
    IDIS core instance

    .. code-block:: console

        For a given DICOM data type and IDIS core instance, it should
        always be possible to answer the question
        'can this data type be deidentified correctly by this IDIS instance?'
        with yes or no.

    If the answer is 'it depends' then the data type is too broad and needs to be split into smaller types.
    The question in the definition is also the main reason for having DICOM data types. If new data is presented, can you
    reasonably assume that it will be deidentified correctly?

    Technically, the definition of a data type will probably be some kind of function of values for DICOM tags such as
    Modality, Vendor, SopClassUID, et cetera. However it is not necessarily constrained to DICOM tags only. One can imagine for
    example a hospital that is known to sometimes put patient information in StudyDescription tags. This knowledge is
    not encoded in DICOM tags but does impact the definition above. In this case DICOM data type should be expanded to use
    this knowledge.


DICOM example library
    A collection of DICOM examples

DICOM example tool
    CLI tool that makes it easy to collect, anonymize and annotate DICOM examples



.. toctree::
   :maxdepth: 2
   :caption: Contents:

   readme
   installation
   usage
   modules
   contributing
   history

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
