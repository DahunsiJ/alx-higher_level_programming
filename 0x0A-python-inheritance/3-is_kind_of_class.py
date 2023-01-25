#!/usr/bin/python3
# 3-is_kind_of_class.py
"""Define function that checks if obj isinstance of class."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a class or its inheritance.

    Args:
        obj (any): The object
        a_class (type): The class to match the type of obj to.

    Return:
        If obj is exactly an instance or inheritance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return (True)
    return (False)
