#!/usr/bin/env python3
"""Script-> A module for testing the client module.
"""
import unittest
from typing import Dict, List, Optional, Tuple, Union
from unittest.mock import MagicMock, Mock, PropertyMock, patch

import requests
from parameterized import parameterized, parameterized_class

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Tests the `GithubOrgClient` class."""

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch.object(requests.Session, "get")
    def test_org(
        self,
        org: str,
        resp: Dict,
        mocked_get: MagicMock,
    ) -> None:
        """Tests the `org` method."""
        mocked_get.return_value.json.return_value = resp
        gh_org_client = GithubOrgClient(org)
        self.assertEqual(gh_org_client.org(), resp)
        mocked_get.assert_called_once_with(
            f"https://api.github.com/orgs/{org}",
        )

    def test_public_repos_url(self) -> None:
        """Tests the `_public_repos_url` property."""
        with patch.object(
            GithubOrgClient,
            "org",
            new_callable=PropertyMock,
        ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @patch.object(requests.Session, "get")
    def test_public_repos(
        self,
        mock_get: MagicMock,
    ) -> None:
        """Tests the `public_repos` method."""
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ]
        }
        mock_get.return_value.json.return_value = test_payload["repos"]
        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new_callable=PropertyMock,
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                [
                    "episodes.dart",
                    "kratu",
                ],
            )
            mock_public_repos_url.assert_called_once()
        mock_get.assert_called_once()

    @parameterized.expand([
        (
            {'license': {'key': "bsd-3-clause"}},
            "bsd-3-clause",
            True,
        ),
        (
            {'license': {'key': "bsl-1.0"}},
            "bsd-3-clause",
            False,
        ),
    ])
    def test_has_license(
        self,
        repo: Dict,
        key: str,
        expected: bool,
    ) -> None:
        """Tests the `has_license` method."""
        gh_org_client = GithubOrgClient("google")
        client_has_licence = gh_org_client.has_license(repo, key)
        self.assertEqual(client_has_licence, expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Performs integration tests for the `GithubOrgClient` class."""

    @classmethod
    def setUpClass(cls) -> None:
        """Sets up class fixtures before running tests."""
        cls.session = requests.Session()
        cls.route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in cls.route_payload:
                return Mock(
                    **{'json.return_value': cls.route_payload[url]},
                )
            return HTTPError

        cls.session.get = MagicMock(side_effect=get_payload)

    def test_public_repos(self) -> None:
        """Tests the `public_repos` method."""
        self.assertEqual(
            GithubOrgClient("google", session=self.session).public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """Tests the `public_repos` method with a license."""
        self.assertEqual(
            GithubOrgClient(
                "google",
                session=self.session,
            ).public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Removes the class fixtures after running all tests."""
        cls.session.close()
