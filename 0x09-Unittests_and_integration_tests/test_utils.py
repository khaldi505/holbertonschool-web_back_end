#!/usr/bin/env python3
"""
unittest class to asure that
Access nested map function
works as expected
"""
import utils
from utils import access_nested_map, get_json, memoize
import unittest
from unittest.mock import patch
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
        Assert the output is
        equal to the expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
       ({}, ('a', )),
       ({'a': 1}, ('a', 'b'))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        test if the nested map function
        raises the KeyError when an
        argument, expected result is missing.
        also makes sure that the exception message
        is as expected
        """
        self.assertRaises(KeyError,  access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    test get json
    """
    @parameterized.expand([
        ("http://example.com", {"test_payload": True}),
        ("http://holberton.io", {"test_payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
            patch the requests.get
            to return a fake payload
            assert that we're getting
            the expected result
        """
        with patch('requests.get') as mc:
            mc.return_value.json.return_value = test_payload
            response = get_json(test_url)
            self.assertEqual(response, test_payload)
            mc.assert_called_once()


class TestMemoize(unittest.TestCase):
    """
    a class that tests the
    test_memoize method
    """
    def test_memoize(self):
        """
        test memoize
        """
        class TestClass:
            """
            testclass"""
            def a_method(self):
                """a_met"""
                return 42

            @memoize
            def a_property(self):
                """
                aprperty"""
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mc:
            obj = TestClass()
            self.assertEqual(obj.a_property, mc.return_value)
            self.assertEqual(obj.a_property, mc.return_value)
            mc.assert_called_once()
