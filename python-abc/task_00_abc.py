#!/usr/bin/env python3
"""Module that defines abstract Animal class with sound method."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""
    @abstractmethod
    def sound(self):
        """Returns the sound of the animal."""
        pass


class Dog(Animal):
    """Dog class that inherits from Animal."""
    def sound(self):
        """Returns the dog's sound."""
        return "Bark"


class Cat(Animal):
    """Cat class that inherits from Animal."""
    def sound(self):
        """Returns the cat's sound."""
        return "Meow"
