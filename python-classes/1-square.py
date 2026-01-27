#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute.
"""

class Square:
    """
    Square class that stores a private size attribute.
    """
    def __init__(self, size):
        """
        Initialize a new Square instance with the given size.
        Args:
            size (int): The size of the square.
        """
        self.__size = size
