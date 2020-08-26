.. _getting_started:

===============
Getting started
===============

Installation
============
.. code-block:: console

    $ pip install idiscore

For more details see :ref:`installation`


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



Choosing a deidentification profile
===================================

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
==================================

Safe private and PII location lists are often needed for more advanced deidentification. They address two special types
of data:

Private DICOM tags
    These are non-standard tags that can be written into a DICOM dataset by any manufacturer. A list of private tags
    considered safe can be passed to an idiscore instance. Without this list idiscore will remove all private tags

PixelData
    In certain types of DICOM datasets, Personally Identifiable information (PII) is burnt into the image itself. This is
    often the case for ultrasound images for example. To handle this a list of known PII locations can be passed to an
    idiscore instance. Without this list, datasets with burnt-in information will be rejected

Here is an example of passing both lists to an idiscore instance:

..  code-block:: python

    from idiscore.defaults import create_default_core
    from idiscore.image_processing import PIILocation, PIILocationList, SquareArea
    from idiscore.private_processing import SafePrivateBlock, SafePrivateDefinition

    safe_private = SafePrivateDefinition(
        blocks=[
            SafePrivateBlock(
                tags=["0023[SIEMENS MED SP DXMG WH AWS 1]10",
                      "0023[SIEMENS MED SP DXMG WH AWS 1]11",
                      "00b1[TestCreator]01",
                      "00b1[TestCreator]02"],
                criterion=lambda x: x.Modality == "CT",
                comment='Some test tags, only valid for CT datasets'),
            SafePrivateBlock(
                tags=["00b1[othercreator]11", "00b1[othercreator]12"],
                comment='Some more test tags, without a criterion')])

    location_list = PIILocationList(
        [PIILocation(
            areas=[SquareArea(5, 10, 4, 12),
                   SquareArea(0, 0, 20, 3)],
            criterion=lambda x: x.Rows == 265 and x.Columns == 512
         ),
         PIILocation(
            areas=[SquareArea(0, 200, 4, 12)],
            criterion=lambda x: x.Rows == 265 and x.Columns == 712
         )]
    )

    core = create_default_core(safe_private_definition=safe_private,
                           location_list=location_list)

.. tip:: When passing a safe private definition, make sure the rule set `Retain Safe Private` is included in your
         profile

For more information on how idiscore works, see :ref:`advanced`.