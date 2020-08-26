.. _advanced:

========
Advanced
========
More in-depth discussion of on certain issues. Intended for people interested in customising what idiscore does

.. _how_does_idiscore_deidentify_a_dataset:

How idiscore deidentifies a dataset
===================================

Getting a sense of what the method :func:`idiscore.core.Core.deidentify` actually does. Starting at the very specific.

* A dataset is fed into :func:`idiscore.core.Core.deidentify` on a :func:`default idiscore instance<idiscore.defaults.create_default_core>`.
  What will happen?
* Suppose that the dataset contains the DICOM element `0010, 0010 (PatientName) - Jane Smith`
* An :func:`idiscore.operators.Operator` is applied to this element. In the default case this is :func:`idiscore.operators.Empty`.
  This will keep the element, but remove its value.
* the :func:`Empty <idiscore.operators.Empty>` operator was applied because the :ref:`default profile<default_core_description>`
  has the :func:`Rule<idiscore.rules.Rule>` `0010, 0010 (PatientName) - Empty`

Overview
--------

* :func:`idiscore.core.Core.deidentify` deidentifies a dataset in 4 steps:

    #. :func:`idiscore.core.Core.apply_bouncers` Can reject a dataset if it is considered too hard to deidentify.

    #. :func:`idiscore.core.Core.apply_pixel_processing` Removes part of the image data if required. If image data
       is unknown or something else goes wrong the dataset is rejected

    #. :func:`idiscore.core.Core.apply_rules` Process all DICOM elements. Remove, replace, keep, according to the profile
       that was set. See for example all rules for the :ref:`idiscore default profile<default_core_description>`. This
       step is the most involved of the steps listed here. It will be

    #. Insert any new elements into the dataset. :func:`idiscore.insertions.get_deidentification_method` for example
       generates an element that indicates what method was used for deidentification


How to modify and extend processing
===================================

Custom profile
--------------
.. literalinclude:: ../../examples/custom_profile.py

Each :func:`Rule<idiscore.rules.Rule>` above consists of two parts: an :func:`Identifier<idiscore.identifiers.TagIdentifier>`
which designates what this rule applies to, and an :func:`Operator<idiscore.operators.Operator>` which defines what the rule does

Custom processing
-----------------
If the existing :func:`Operators<idiscore.operators.Operator>` in :mod:`idiscore.operators` are not enough, you can define
your own by extending :func:`idiscore.operators.Operator`. If these operators could be useful for other users as well,
please consider creating a pull request (see :doc:`contributing`)