#!/usr/bin/python3
# 5-text_indentation.py
"""Defines a text_indentation function."""


def text_indentation(text):
    """Prints a string with 2 new lines after some characters.

    Args:
        text (str): String to be printed.
    Raises:
        TypeError: text must be a string.
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    c = 0

    while (c < len(text) and text[c] == ' '):
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] in '.?:' or text[c] == '\n':
            if text[c] in '.?:':
                print('\n')
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
