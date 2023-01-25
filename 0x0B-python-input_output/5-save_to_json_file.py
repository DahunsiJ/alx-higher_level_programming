#!/usr/bin/python3
# 5-save_to_json_file.py
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a text file.

    Args:
        my_obj (any): The object.
        filename (str): The name of the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
