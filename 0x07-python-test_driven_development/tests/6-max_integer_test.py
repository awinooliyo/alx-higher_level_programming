#!/usr/bin/python3
"""Unittest for the max_integer module"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """The series of test cases for the max_integer function"""

    def test_max_at_the_end(self):
        """Test for a list with max value at the end."""
        max_at_the_end = [1, 2, 3, 4]
        self.assertEqual(max_integer(max_at_the_end), 4)

    def test_max_at_beginning(self):
        """Test for a list with max value at the beginning."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Testcase for the empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [2, 1, 4, 3]
        self.assertEqual(max_integer(unordered_list), 4)

    def test_unique_element(self):
        """Test a list with a single element."""
        unique_element = [80]
        self.assertEqual(max_integer(unique_element), 80)

    def test_float_list(self)
        """Test for a list of floats."""
        float = [1.48, 1.23, 4.99, 7.88, 9.99, -8.93]
        self.assertEqual(max_integer(float), 9.99)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [-9, 1.47, 2.43, 9, 23.5, 6, 8]
        self.assertEqual(max_integer(ints_and_floats), 23.5)

    def test_neg_float_list(self):
        """Tests a list with negative floats."""
        neg_float = [-12.67, -2.3, -66.9, -10, -111.1)
        self.assertEqual(max_integer(neg_float), -2.3)

    def test_string_list(self):
        """Test a string."""
        string = "Erick"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Baidoo", "is", "my", "mentor"]
        self.assertEqual(max_integer(strings), "my")

    def test_empty_string(self):
        """Tests an empty string."""
        self.assertEqual(max_integer(""), None)

    def test_diff_data_types(self):
        """Tests different data types."""
        with self.assertRaises(TypeError):
            max_integer([1, "1"])

    def test_list_list(self):
        """Test a nested list."""
        list = [[1, 4], [2, 9]]
        self.assertEqual(max_integer(list), [2, 9])

if __name__ == "__main__":
    unittest.main()
