#!/usr/bin/python3

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV to JSON and save to data.json."""
    list = []
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_data = csv.DictReader(csv_file)
            for line in csv_data:
                list.append(line)

        with open('data.json', 'w', encoding='utf-8') as csv_file:
            json.dump(list, csv_file, indent=4)
        return True

    except FileNotFoundError:
        return False
