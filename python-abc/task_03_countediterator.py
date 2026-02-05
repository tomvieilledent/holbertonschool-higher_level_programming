#!/usr/bin/python3
"""Module that defines CountedIterator class for counting iterations."""


class CountedIterator:
    """Iterator class that counts the number of elements iterated."""

    def __init__(self, data):
        """Initializes the iterator with data."""
        self.iterator = iter(data)
        self.i = 0

    def get_count(self):
        """Returns the number of items iterated."""
        return self.i

    def __next__(self):
        """Returns next item and increments count."""
        itered = next(self.iterator)
        self.i += 1
        return itered