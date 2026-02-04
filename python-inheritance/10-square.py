#!/usr/bin/python3
"""Module that defines BaseGeometry, Rectangle, and Square classes."""


class BaseGeometry:
    """Base class for geometry with validation."""

    def area(self):
        """Raises an Exception indicating area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer."""
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes a rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns string representation of the rectangle."""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initializes a square with validated size."""
        super().__init__(size, size)
