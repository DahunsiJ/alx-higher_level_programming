#!/usr/bin/python3
# 0-add_integer.py
"""Function to add two Integers."""


def add_integer(a, b=98):
    """Function to add two integers together.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The return value

    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
