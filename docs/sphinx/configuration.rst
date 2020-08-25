=============
Configuration
=============

After :doc:`installation` idiscore should already deidentify to a reasonable extent. In the trade off between
security (remove a lot) and usability (remove little), the default settings lean towards security. This means more
datasets might be rejected and more DICOM elements might be removed then might be necessary for your context.


Changing deidentification
=========================
To extend or alter deidentification, you can extend or alter the python modules that make up core.