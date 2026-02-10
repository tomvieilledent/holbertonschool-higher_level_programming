#!/usr/bin/python3

import pickle


class CustomObject:
    """Serializable object with age, name, and student status."""

    def __init__(self, age, name, is_student):
        """Initialize with age (int), name (str), is_student (bool)."""
        if type(age) is not int:
            raise TypeError('age must be an int')
        if type(name) is not str:
            raise TypeError('name must be a str')
        if type(is_student) is not bool:
            raise TypeError('is_student must be a bool')

        self.age = age
        self.name = name
        self.is_student = is_student

    def display(self):
        """Print object attributes."""
        file = vars(self)
        for key in file:
            print("{}: {}".format(key, file[key]))

    def serialize(self, filename):
        """Save object to file using pickle."""
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """Load object from file using pickle."""
        with open(filename, 'rb') as file:
            return pickle.load(file)
