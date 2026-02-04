#!/usr/bin/python3
"""Module that checks if an object is an instance of, or inherits from, a specified class."""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or inherits from it."""
    return isinstance(obj, a_class)
