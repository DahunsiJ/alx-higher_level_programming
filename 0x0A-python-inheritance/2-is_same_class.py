#!/usr/bin/python3
# 2-is_same_class.py
"""Define function that checks if obj isinstance of class."""


def is_same_class(obj, a_class):
    """Function that checks if obj isinstance of a_class.

    Args:
        obj (object): The object
        a_class (class): The class

    Return:
        If obi is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return (True)
    return (False)
