#!/usr/bin/python3
# 1-write_file.py
"""Defines a function that writes to a text file."""


def write_file(filename="", text=""):
    """Function that writes a text to a file.

    Args:
        filename (str): Name of the file to open.
        text (str): The string of text to write to a file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
