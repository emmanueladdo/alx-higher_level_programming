#!/usr/bin/python3
"""File IO module that defines a JSON file writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object into text file using JSON representation."""
    with open(filename, mode="w", encoding="utf-8") as fd:
        fd.write(json.dumps(my_obj))
