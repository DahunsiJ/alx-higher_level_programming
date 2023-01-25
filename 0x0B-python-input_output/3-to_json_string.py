#!/usr/bin/python3
# 3-to_json_string.py
"""Defines a function that returns the JSON rep of an object(string)."""
import json


def to_json_string(my_obj):
    """Function that converts an object to JSON string.

    Args:
        my_obj (any): The object to convert.
    Returns:
        The JSON representation of the object.
    """
    return (json.dumps(my_obj))
