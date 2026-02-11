#!/usr/bin/python3

import pickle


class CustomObject:
    """Serializable object with name, age, and student status."""

    def __init__(self, name, age, is_student):
        """Initialize object attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print object attributes in required format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize object to file."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize object from file."""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None
