#!/usr/bin/python3
"""Module that defines a list subclass with print_sorted method."""


class MyList(list):
    """List subclass that can print itself in sorted order."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
