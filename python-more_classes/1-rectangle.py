#!/usr/bin/python3
"""
This module defines a Rectangle class with private width and height attributes.
"""

class Rectangle:
    """
    Represents a rectangle with private width and height attributes.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance with optional width and height.
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
