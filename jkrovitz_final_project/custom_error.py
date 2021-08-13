# defining Python user-defined exceptions
class Error(Exception):
    """BAse class that will be used for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised while the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass
