#!/usr/bin/python3
"""Module that defines a Student class with serialization/deserialization."""


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
    
    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance from a dictionary."""
        obj_dict = vars(self)
        for key in ("first_name", "last_name", "age"):
            if key in json:
                obj_dict[key] = json[key]