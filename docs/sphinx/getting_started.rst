.. _getting_started:

===============
Getting started
===============

Installation
============
.. code-block:: console

    $ pip install idiscore

For more details see `installation`_


How to run idiscore
===================
Idiscore is meant to be used within a python script:

.. code-block:: python

    import pydicom
    from idiscore.defaults import create_default_core

    core = create_default_core()      # create an idiscore instance

    ds = pydicom.read("my_file.dcm")  # load a DICOM dataset
    ds = core.deidentify(ds)          # remove patient information
    ds.save_as("deidentified.dcm")    # save to disk


Configuration
=============

Choosing a deidentification profile
-----------------------------------

Deidentification is based on the DICOM standard deidentification profile and one or more
`DICOM Confidentiality options <http://dicom.nema.org/medical/dicom/current/output/chtml/part15/sect_E.3.html>`_.
The minimal example above uses the :ref:`idiscore default profile<default_core_description>` which uses some of these
options (defined as 'rule sets').

To select DICOM confidentiality options yourself, initialise a core instance like this:

..  code-block:: python

    import pydicom
    from idiscore.core import Core, Profile
    from idiscore.defaults import get_dicom_rule_sets

    sets = get_dicom_rule_sets()  # Contains official DICOM deidentification rules
    profile = Profile(            # Choose which rule sets to use
        rule_sets=[sets.basic_profile,
                   sets.retain_modified_dates,
                   sets.retain_device_id]
    )
    core = Core(profile)          # Create an deidentification core

The rule sets in idiscore implement the rules in
`DICOM PS3.15 table E.1-1 <http://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_E.html>`_.

Safe Private and PII location list
----------------------------------
The rule sets determine how to process each DICOM element. There are two areas however that require extra consideration:

Private DICOM tags
    These are non-standard tags that can be written into a DICOM dataset by any manufacturer. A list of private tags
    considered safe can be passed to an idiscore instance. Without this list idiscore will remove all private tags

PixelData
    In certain types of DICOM datasets, Personally Identifiable information (PII) is burnt into the image itself. This is
    often the case for ultrasound images for example. To handle this a list of known PII locations can be passed to an
    idiscore instance. Without this list, datasets with burnt-in information will be rejected

Here is an example of passing both lists to an idiscore instance::

Sometimes you want to keep these tags however. To do so make sure you use the
    'Retain safe private' rule set, and add the tags you consider safe to






In many cases two extra lists are required for useful

In addition to the rule sets
Two areas of To deidentify a DICOM dataset properly

Two lists are usually needed



Examples

Advanced
    - How DICOM elements are processed
    - How to modify and extend processing