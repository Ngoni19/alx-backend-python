#!/usr/bin/env python3
"""Script -> Tests Module for Utils
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
import requests_mock


class TestAccessNestedMap(unittest.TestCase):
    """Tests the access_nested_map method of utils
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, {"a", }),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Tests the get_json function of utils
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, expected):
        with requests_mock.Mocker() as mock_requests:
            mock_response = expected
            mock_requests.get(url, json=mock_response)

            self.assertEqual(get_json(url), mock_response)
            mock_requests.get.assert_called_once_with(url)
