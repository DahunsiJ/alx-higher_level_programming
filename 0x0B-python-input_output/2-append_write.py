#!/usr/bin/python3
# 2-write_file.py
"""Defines a function that appends a string at the end of a text file."""


def append_write(filename="", text=""):
    """Function that writes a text to a file.

    Args:
        filename (str): Name of the file to open.
        text (str): The string of text to write to a file.
    Returns:
        The number of characters written.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
