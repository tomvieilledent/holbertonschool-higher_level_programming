#!/usr/bin/python3
"""
This module defines MyList class that inherits from list.
"""


class MyList(list):
    """
    MyList class that inherits from list with a print_sorted method.
    """

    def print_sorted(self):
        """
        Print the list in ascending sorted order.
        """
        print(sorted(self))

