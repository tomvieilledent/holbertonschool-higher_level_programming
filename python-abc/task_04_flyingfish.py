#!/usr/bin/env python3
"""Module demonstrating multiple inheritance with Fish, Bird, and FlyingFish."""


class Fish:
    """Class representing a fish with swimming and habitat methods."""
    def swim(self):
        """Prints that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Prints the fish's habitat."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird with flying and habitat methods."""
    def fly(self):
        """Prints that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Prints the bird's habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class combining Fish and Bird through multiple inheritance."""
    def fly(self):
        """Prints that the flying fish is soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """Prints that the flying fish is swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Prints the flying fish's dual habitat."""
        print("The flying fish lives both in water and the sky!")