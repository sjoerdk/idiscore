Welcome to IDIS Core's documentation!
======================================

IDIS core de-identifies DICOM datasets. It does this by removing or replacing DICOM elements when needed. All DICOM
processing is based on `pydicom <https://pydicom.github.io/pydicom/stable/>`_. It processes in accordance to the
`DICOM deidentification profile and options <http://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_E.html#table_E.1-1>`_.


It works like this:

.. code-block:: python

    import pydicom
    from idiscore.defaults import create_default_core

    core = create_default_core()      # create an idiscore instance

    ds = pydicom.read("my_file.dcm")  # load a DICOM dataset
    ds = core.deidentify(ds)          # remove patient information
    ds.save_as("deidentified.dcm")    # save to disk

See :ref:`getting_started` to start using idiscore

Goals
=====
* Deidentify DICOM datasets in conformance to the DICOM standard
* Configuration is an extra, not a requirement. With minimal configuration IDIS core should deidentify a dataset 'well'
  This means IDIS core will include opinions on deidentification
* Python all the way. No custom configuration languages, no installers, just scripts and pip. IDIS core assumes you can
  write python and leverages class inheritance, docstrings, pytest, variable annotations. This keeps things clean,
  testable and unambiguous

Non-Goals
=========
* No deidentification pipeline. IDIS core deidentifies DICOM datasets. It does not want to know where this dataset comes
  from or where it is going to. It does not offer any installable or server to send files to. It could be used to create
  such a server, but this is out of this project's scope
* Reading and Writing DICOM files. Internally IDIS core only works with `pydicom <https://pydicom.github.io/pydicom/stable/>`_ datasets. Reading and writing of DICOM datasets is
  to pydicom


Alternatives
============
Alternative methods of de-identification

CTP
    `MIRC CTP <http://mircwiki.rsna.org/index.php?title=MIRC_CTP>`_ is a widely used, extensive, java-based framework
    for deidentification and data aggragation. It has many plugins and can be configured using several scripting languages.
    All in all it is a very good choice for many people. For me as a programmer developing mostly python-based software,
    I struggled with certain aspects however:

    * It is difficult to integrate into a test suite properly. This is first of all because it is file-based, requiring an
      actual file on disk for each type of DICOM you might want to verify the deidentification of. Second, because the pipeline
      is configured with several different file-based custom scripts it is difficult to set up the correct context for tests.
    * I found it tricky to integrate into my python-based infrastructure. Again, because the pipeline is java-based and
      file-based there is no easy way to access the state of files in the pipeline. Is a file done? Has something gone wrong?
      Getting this information would require either checking all possible output, stage and quarantine folders. I was really
      missing exceptions I could catch.
    * Because it is an installable pipeline, I found it difficult to integrate into smaller, non-server based applications like
      a command line tool that locally deidentifies some data for a user.

deid
    `pydicom deid <https://github.com/pydicom/deid>`_ is a pydicom based best-effort anonymizer for medical image data.
    It is part of the pydicom family. It has `extensive and friendly documentation <https://pydicom.github.io/deid/>`_
    and get several concepts right. Reasons for not expanding on this library and instead starting a new one:

    * There seems to have been little development since the libraries start in 2017
    * Seems to be quite file-based in places, often requiring input and output folders for initializing objects
    * No test coverage monitoring, uses unittest for testing which is hard to maintain and expand on
    * Uses `custom scripting <https://pydicom.github.io/deid/examples/recipe/>`_ language for configuring the
      anonymization. This is useful for non-coding end-users, but adds a layer of indirectness to automated testing.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   readme
   getting_started
   advanced
   concepts
   modules
   contributing
   history

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
