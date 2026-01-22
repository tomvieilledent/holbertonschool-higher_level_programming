#!/usr/bin/python3
"""
Module for text indentation.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', ':'.

    Args:
        text: String to format

    Raises:
        TypeError: If text is not a string
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Process each character
    for char in text:
        if char == "." or char == "?" or char == ":":
            print(char)
            print()
        else:
            print(char, end="")
