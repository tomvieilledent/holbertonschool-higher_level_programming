#!/usr/bin/python3
"""
This module defines a Square class with size validation and an area method.
"""

class Square:
    """
    Square class with private size attribute, validation, and area calculation.
    """
    def __init__(self, size=0):
        """
        Initialize a new Square instance with the given size.
        Args:
            size (int): The size of the square (default 0).
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Compute and return the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
