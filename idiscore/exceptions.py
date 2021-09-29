class IDISCoreError(Exception):
    """Base for all exceptions in IDIS core"""

    pass


class SafePrivateError(IDISCoreError):
    pass


class AnnotationValidationFailedError(IDISCoreError):
    pass
