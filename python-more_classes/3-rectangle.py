#!/usr/bin/python3
"""
This module defines a Rectangle class with area, perimeter, and string representation.
"""

class Rectangle:
    """
    Represents a rectangle with methods to compute area, perimeter, and display as a string.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance with width and height.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, widthValue):
        if not isinstance(widthValue, int):
            raise TypeError("width must be an integer")
        if widthValue < 0:
            raise ValueError("width must be >= 0")
        self.__width = widthValue

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, heightValue):
        if not isinstance(heightValue, int):
            raise TypeError("height must be an integer")
        if heightValue < 0:
            raise ValueError("height must be >= 0")
        self.__height = heightValue

    def area(self):
        area = self.__width * self.__height
        return area

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])
