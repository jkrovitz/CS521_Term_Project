"""
Jeremy Krovitz
Class: CS 521 - Summer 2
Date: 08/21/2021
Description of File: This file defines custom, user-defined Python exceptions.
"""


class Error(Exception):
    """Base class that will be used for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised while the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass


class AlreadyExistsError(Error):
    """Raised when attempting to create an id that already exists."""
    pass
