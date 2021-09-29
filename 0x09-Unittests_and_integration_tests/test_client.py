#!/usr/bin/env python3
"""
unittest class to asure that
Access nested map function
works as expected
"""
import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """nyes
        """
        with patch(
            'client.GithubOrgClient.org', new_callable=PropertyMock
                ) as mc:
            mc.return_value = {'repos_url': 'test.io'}
            org_client = client
            org_client = org_client.GithubOrgClient('test_org')
            self.assertEqual(
                org_client.org['repos_url'], org_client._public_repos_url
                    )

    @patch("client.get_json", return_value={'key': '55548798'})
    def test_public_repos(self, get_json_mock):
        """
        """
        get_json_mock()
        with patch(
            'client.GithubOrgClient._public_repos_url',
                new_callable=PropertyMock) as mcp:
            mcp.return_value = {'key': '55548798'}
            test_obj = client
            test_obj = test_obj.GithubOrgClient('another_test')
            ex = test_obj._public_repos_url
            self.assertEqual(
                ex, mcp.return_value
            )
            get_json_mock.assert_called_once()
            mcp.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, dict_license, key_license, expc_result):
        """
        """

        self.assertEqual(
            client.GithubOrgClient.has_license(dict_license, key_license),
            expc_result
        )
