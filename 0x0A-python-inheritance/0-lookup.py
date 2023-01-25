#!/usr/bin/python3
# 0-lookup.py
"""Define function that looks up an object's identity"""


def lookup(obj):
    """ Function returns the list of attributes and methods of an object.

    Arg:
        obj (object): The object whose identity is returned.
    Return:
        list of available attributes and methods in obj
    """
    return (dir(obj))
