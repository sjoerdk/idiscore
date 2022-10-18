"""Additions to the pydicom Dataset object"""
from pydicom.dataset import Dataset

from idiscore.exceptions import IDISCoreError


class RequiredDataset(Dataset):
    """A pydicom Dataset,that raises distinctive errors when accessing missing keys

    Made this to specifically handle missing keys on a dataset. By default, a Dataset
    instance raises KeyError and AttributeError. These are too general to safely
    catch over larger pieces of code. Putting try-except blocks around each individual
    dict key access is ugly and annoying.

    Raises
    ------
    RequiredTagNotFound
        When a requested key is not found in this dataset. Either through attribute
        access, like dataset.PatientID or through dict access like
        dataset['PatientID']

    Notes
    -----
    Init like this:

    >>> ds = Dataset()
    >>> rds = RequiredDataset(ds)

    Now you can handle missing keys cleanly without accidentally catching other
    KeyErrors:

    >>> try:
    >>>     important_dataset_check(rds)
    >>> except RequiredTagNotFound:
    >>>     print('check failed due to missing information')

    """

    def __getattr__(self, name):
        try:
            return super().__getattr__(name)
        except AttributeError as e:
            raise RequiredTagNotFound(f"Required tag not found: {e}") from e

    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError as e:
            raise RequiredTagNotFound(f"Required tag not found: {e}") from e


class RequiredTagNotFound(IDISCoreError):
    pass
