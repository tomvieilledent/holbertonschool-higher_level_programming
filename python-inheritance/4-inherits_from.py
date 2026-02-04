#!/usr/bin/python3
"""Module that checks if an object inherits from a specified class."""


def inherits_from(obj, a_class):
    """Returns True if obj inherits from a_class (but not if it's exactly a_class)."""
    return isinstance(obj, a_class) and type(obj) is not a_class
