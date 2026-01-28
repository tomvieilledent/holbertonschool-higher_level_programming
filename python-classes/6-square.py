#!/usr/bin/python3
"""
This module defines a Square class with size,
position, area, and print functionality.
"""


class Square:
    """
    Square class with private size and position attributes,
    validation, area calculation, and print method.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance with the given size and position.
        Args:
            size (int): The size of the square (default 0).
            position (tuple): The position of the square (default (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def position(self):
        """
        Retrieve the position of the square.
        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, positionValue):
        """
        Set the position of the square with validation.
        Args:
            positionValue (tuple): The new position of the square.
        Raises:
            TypeError: If positionValue is not a tuple of 2 positive integers.
        """
        if (not isinstance(positionValue, tuple) or not len(positionValue) == 2
                or not all(isinstance(x, int) for x in positionValue)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = positionValue

    @property
    def size(self):
        """
        Retrieve the size of the square.
        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, sizeValue):
        """
        Set the size of the square with validation.
        Args:
            sizeValue (int): The new size of the square.
        Raises:
            TypeError: If sizeValue is not an integer.
            ValueError: If sizeValue is less than 0.
        """
        if not isinstance(sizeValue, int):
            raise TypeError("size must be an integer")
        if sizeValue < 0:
            raise ValueError("size must be >= 0")
        self.__size = sizeValue

    def area(self):
        """
        Compute and return the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with '#' characters at the given position.
        Prints an empty line if size is 0.
        """
        if self.__size == 0:
            return
        print(("\n" * self.__position[1]), end="")
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
