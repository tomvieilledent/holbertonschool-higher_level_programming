#!/usr/bin/python3
"""Module to save object to JSON file."""

import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation."""
    with open(filename, 'w', encoding='utf-8') as file:
        return json.dump(my_obj, file)
