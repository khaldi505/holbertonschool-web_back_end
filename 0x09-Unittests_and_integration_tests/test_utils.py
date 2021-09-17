#!/usr/bin/env python3
"""
unittest class to asure that
Access nested map function
works as expected
"""
from utils import access_nested_map
import unittest
from parameterized import parameterized, parameterized_class


class TestAccessNestedMap(unittest.TestCase):
    """
    the test access nested map
    test cases class.
    """

    @parameterized.expand([
                        ({"a": 1}, ("a",), 1),
                        ({"a": {"b": 2}}, ("a", ), {"b": 2}),
                        ({"a": {"b": 2}}, ("a", "b"), 2)
                            ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        test something
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
