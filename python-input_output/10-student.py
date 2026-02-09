#!/usr/bin/python3
"""Module that defines a Student class with attribute filtering."""


class Student:
    """Represents a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation with optional attribute filtering."""
        if attrs is None or not isinstance(attrs, list) or not all(isinstance(x, str) for x in attrs):
            return vars(self)
        obj_dict = vars(self)
        return {key: obj_dict[key] for key in attrs if key in obj_dict}
