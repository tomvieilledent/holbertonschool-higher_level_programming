#!/usr/bin/python3
"""Module that defines abstract Shape class and its implementations."""

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    """Abstract base class for geometric shapes."""
    @abstractmethod
    def area(self):
        """Returns the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Returns the perimeter of the shape."""
        pass

class Circle(Shape):
    """Circle class that inherits from Shape."""

    def __init__(self, radius):
        """Initializes a circle with given radius."""
        self.radius = radius

    def area(self):
        """Returns the area of the circle."""
        return pi * (self.radius ** 2)
    
    def perimeter(self):
        """Returns the perimeter of the circle."""
        return 2 * pi * self.radius

class Rectangle(Shape):
    """Rectangle class that inherits from Shape."""

    def __init__(self, width, height):
        """Initializes a rectangle with given width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height
    
    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)
    
def shape_info(shape):
    """Prints the area and perimeter of a shape."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
    

