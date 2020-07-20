class IDISCoreException(Exception):
    """Base for all exceptions in IDIS core"""

    pass


class SafePrivateException(IDISCoreException):
    pass


class AnnotationValidationFailed(IDISCoreException):
    pass
