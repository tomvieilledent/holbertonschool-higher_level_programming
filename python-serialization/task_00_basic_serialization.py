#!/usr/bin/python3
"""Module for basic serialization with JSON."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to a JSON file."""

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load and deserialize data from a JSON file."""

    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
