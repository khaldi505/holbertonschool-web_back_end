#!/usr/bin/env python3
"""
unittest class to asure that
Access nested map function
works as expected
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized, parameterized_class
import client


class TestGithubOrgClient(unittest.TestCase):
    """
    test github org client
    """
    @parameterized.expand([('google', {}), ('abc', {})])
    def test_org(self, test_org, result):
        """
        test org
        """
        with patch("client.get_json") as mc:
            mc.return_value = {}
            orgclient = client
            orgclient = orgclient.GithubOrgClient(test_org)
            self.assertEqual(orgclient.org, result)
            mc.assert_called_once()
