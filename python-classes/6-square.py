#!/usr/bin/python3
"""
This module defines a Square class with size, position, area, and print functionality.
"""

class Square:
    """
    Represents a square with size, position, area calculation, and print functionality.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance with the given size and position.
        Args:
            size: The size of the square (integer, default 0).
            position: The position of the square (tuple of 2 positive integers, default (0, 0)).
        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if not isinstance(position, tuple) or not len(position) == 2 or not all(isinstance(x, int) for x in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    # Define the new square position
    @property
    def position(self):
        return self.__position

    # Set the new square position
    @position.setter
    def position(self, positionValue):
        if not isinstance(self.__position, tuple) or not len(self.__position) == 2 or not all(isinstance(x, int) for x in self.__position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = positionValue

    # Define the new square size
    @property
    def size(self):
        return self.__size

    # Set the new square size
    @size.setter
    def size(self, sizeValue):
        if not isinstance(sizeValue, int):
            raise TypeError("size must be an integer")
        if sizeValue < 0:
            raise ValueError("size must be >= 0")
        self.__size = sizeValue

    # Return the new area of the square
    def area(self):
        area = self.__size ** 2
        return area

    # Print a square with "z" size at the (x,y) position
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print(("\n" * self.__position[1]), end="")
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
