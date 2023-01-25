#!/usr/bin/python3
# 4-from_json_string.py
"""Defines a function that returns an object(data struct) rep by JSON."""
import json


def from_json_string(my_str):
    """Function that converts JSON string back to Object

    Args:
        my_str (string): The string(JSON) to convert back.
    Returns:
        The Object represented in JSON
    """
    return (json.loads(my_str))
