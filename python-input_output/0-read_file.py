#!/usr/bin/python3
"""Module to read and print file content."""


def read_file(filename=""):
    """Reads and prints the content of a text file."""
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
