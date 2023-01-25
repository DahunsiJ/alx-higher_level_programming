#!/usr/bin/python3
# 100-my_int.py
"""Defines class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, val):
        """Override == operator with != behaviour."""
        return (self.real != val)

    def __ne__(self, val):
        """Override != operator with == behaviour."""
        return (self.real == val)
