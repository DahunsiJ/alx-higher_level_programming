#!/usr/bin/python3
# 3-say_my_name.py
"""Defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """Prints a person's name.

    Args:
        first_name (str): The first name.
        last_name (str): The last name.
    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
