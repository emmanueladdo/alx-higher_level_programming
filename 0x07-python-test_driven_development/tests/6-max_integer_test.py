#!/usr/bin/python3
"""Unittest for max_integer module
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        nums = [1, 2, 3, 2, 7]
        self.assertEqual(max_integer(nums), 7)

    def test_non_integer_values(self):
        nums = ["i", "b", 8]
        self.assertRaises(TypeError, max_integer, nums)

    def test_empty_list(self):
        nums = []
        self.assertIsNone(max_integer(nums))

    def test_negative_values(self):
        nums = [-2, -6, 1]
        self.assertEqual(max_integer(nums), 1)

    def test_mixed_integer_and_float(self):
        nums = [3, 7.2, 2]
        self.assertEqual(max_integer(nums), 7.2)

    def test_non_list_argument(self):
        self.assertRaises(TypeError, max_integer, 5)

    def test_single_value_list(self):
        nums = [8]
        self.assertEqual(max_integer(nums), 8)

    def test_identical_values_list(self):
        nums = [4, 3, 6, 6, 6]
        self.assertEqual(max_integer(nums), 6)

    def test_string_list(self):
        strings = ["Alice", "Bob", "Charlie"]
        self.assertEqual(max_integer(strings), "Charlie")

    def test_none_argument(self):
        self.assertRaises(TypeError, max_integer, None)


if __name__ == '__main__':
    unittest.main()
