#!/usr/bin/python3
# 4-print_square.py
"""Function that prints a square with #."""


def print_square(size):
    """Prints a square.

    Args:
        size (int): The size(height/width) of the square.
    Raises:
        TypeError: size must be an integer.
        ValueError: size must be >= 0.
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for a in range(size):
            print("#", end="")
        print("")
