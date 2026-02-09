#!/usr/bin/python3
"""Module to convert class instance to dictionary."""


def class_to_json(obj):
    """Returns the dictionary description of an object for JSON serialization."""
    return vars(obj)