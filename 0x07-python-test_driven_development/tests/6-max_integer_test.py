#!/usr/bin/python3
# 6-max_integer_test.py
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestmaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered(self):
        """Test an ordered list of integers."""
        self.assertEqual(max_integer([23, 34, 46, 61, 94]), 94)

    def test_unordered(self):
        """Test an unordered list of integers."""
        self.assertEqual(max_integer([23, 46, 34, 94, 61]), 94)

    def test_max_at_beginning(self):
        """Test a list with max at beginning."""
        self.assertEqual(max_integer([94, 34, 46, 84, 21]), 94)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        """Test a list with one element."""
        self.assertEqual(max_integer([23]), 23)

    def test_floats(self):
        """Test a list of floats."""
        self.assertEqual(max_integer([9.3, 3.4, 45.7, 6.3, 9.5]), 45.7)

    def test_floats_and_ints(self):
        """Test a list of floats and ints."""
        self.assertEqual(max_integer([2.0, 3.5, 46, -61, 9.4]), 46)

    def test_string(self):
        """Test a string."""
        self.assertEqual(max_integer("Tobi"), 'o')

    def test_list_of_strings(self):
        """Test a list of strings."""
        self.assertEqual(max_integer(["How", "are", "you", "today"]), "you")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
