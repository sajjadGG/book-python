#!/usr/bin/env python3

import json
from pprint import pprint
import urllib.request
import unittest
import unittest.mock


RESPONSE = '''
{
  "id": 4164482,
  "name": "django",
  "full_name": "django/django",
  "owner": {
    "login": "django",
    "id": 27804,
    "avatar_url": "https://avatars.githubusercontent.com/u/27804?v=3",
    "gravatar_id": "",
    "url": "https://api.github.com/users/django",
    "html_url": "https://github.com/django",
    "followers_url": "https://api.github.com/users/django/followers",
    "following_url": "https://api.github.com/users/django/following{/other_user}",
    "gists_url": "https://api.github.com/users/django/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/django/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/django/subscriptions",
    "organizations_url": "https://api.github.com/users/django/orgs",
    "repos_url": "https://api.github.com/users/django/repos",
    "events_url": "https://api.github.com/users/django/events{/privacy}",
    "received_events_url": "https://api.github.com/users/django/received_events",
    "type": "Organization",
    "site_admin": false
  },
  "private": false,
  "html_url": "https://github.com/django/django",
  "description": "The Web framework for perfectionists with deadlines.",
  "fork": false,
  "url": "https://api.github.com/repos/django/django",
  "forks_url": "https://api.github.com/repos/django/django/forks",
  "keys_url": "https://api.github.com/repos/django/django/keys{/key_id}",
  "collaborators_url": "https://api.github.com/repos/django/django/collaborators{/collaborator}",
  "teams_url": "https://api.github.com/repos/django/django/teams",
  "hooks_url": "https://api.github.com/repos/django/django/hooks",
  "issue_events_url": "https://api.github.com/repos/django/django/issues/events{/number}",
  "events_url": "https://api.github.com/repos/django/django/events",
  "assignees_url": "https://api.github.com/repos/django/django/assignees{/user}",
  "branches_url": "https://api.github.com/repos/django/django/branches{/branch}",
  "tags_url": "https://api.github.com/repos/django/django/tags",
  "blobs_url": "https://api.github.com/repos/django/django/git/blobs{/sha}",
  "git_tags_url": "https://api.github.com/repos/django/django/git/tags{/sha}",
  "git_refs_url": "https://api.github.com/repos/django/django/git/refs{/sha}",
  "trees_url": "https://api.github.com/repos/django/django/git/trees{/sha}",
  "statuses_url": "https://api.github.com/repos/django/django/statuses/{sha}",
  "languages_url": "https://api.github.com/repos/django/django/languages",
  "stargazers_url": "https://api.github.com/repos/django/django/stargazers",
  "contributors_url": "https://api.github.com/repos/django/django/contributors",
  "subscribers_url": "https://api.github.com/repos/django/django/subscribers",
  "subscription_url": "https://api.github.com/repos/django/django/subscription",
  "commits_url": "https://api.github.com/repos/django/django/commits{/sha}",
  "git_commits_url": "https://api.github.com/repos/django/django/git/commits{/sha}",
  "comments_url": "https://api.github.com/repos/django/django/comments{/number}",
  "issue_comment_url": "https://api.github.com/repos/django/django/issues/comments{/number}",
  "contents_url": "https://api.github.com/repos/django/django/contents/{+path}",
  "compare_url": "https://api.github.com/repos/django/django/compare/{base}...{head}",
  "merges_url": "https://api.github.com/repos/django/django/merges",
  "archive_url": "https://api.github.com/repos/django/django/{archive_format}{/ref}",
  "downloads_url": "https://api.github.com/repos/django/django/downloads",
  "issues_url": "https://api.github.com/repos/django/django/issues{/number}",
  "pulls_url": "https://api.github.com/repos/django/django/pulls{/number}",
  "milestones_url": "https://api.github.com/repos/django/django/milestones{/number}",
  "notifications_url": "https://api.github.com/repos/django/django/notifications{?since,all,participating}",
  "labels_url": "https://api.github.com/repos/django/django/labels{/name}",
  "releases_url": "https://api.github.com/repos/django/django/releases{/id}",
  "deployments_url": "https://api.github.com/repos/django/django/deployments",
  "created_at": "2012-04-28T02:47:18Z",
  "updated_at": "2016-07-06T12:10:51Z",
  "pushed_at": "2016-07-06T12:49:25Z",
  "git_url": "git://github.com/django/django.git",
  "ssh_url": "git@github.com:django/django.git",
  "clone_url": "https://github.com/django/django.git",
  "svn_url": "https://github.com/django/django",
  "homepage": "https://www.djangoproject.com/",
  "size": 199624,
  "stargazers_count": 20172,
  "watchers_count": 20172,
  "language": "Python",
  "has_issues": false,
  "has_downloads": true,
  "has_wiki": false,
  "has_pages": false,
  "forks_count": 8127,
  "mirror_url": null,
  "open_issues_count": 97,
  "forks": 8127,
  "open_issues": 97,
  "watchers": 20172,
  "default_branch": "master",
  "organization": {
    "login": "django",
    "id": 27804,
    "avatar_url": "https://avatars.githubusercontent.com/u/27804?v=3",
    "gravatar_id": "",
    "url": "https://api.github.com/users/django",
    "html_url": "https://github.com/django",
    "followers_url": "https://api.github.com/users/django/followers",
    "following_url": "https://api.github.com/users/django/following{/other_user}",
    "gists_url": "https://api.github.com/users/django/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/django/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/django/subscriptions",
    "organizations_url": "https://api.github.com/users/django/orgs",
    "repos_url": "https://api.github.com/users/django/repos",
    "events_url": "https://api.github.com/users/django/events{/privacy}",
    "received_events_url": "https://api.github.com/users/django/received_events",
    "type": "Organization",
    "site_admin": false
  },
  "network_count": 8127,
  "subscribers_count": 1198
}
'''


class Rectangle:

    def __init__(self, a, b):
        if a <= 0 or b <= 0:
            raise ValueError('Dlugosc boku musi być liczbą dodatnią')

        self.bok_a = a
        self.bok_b = b

    def get_data_from_internet(self):
        url = 'https://api.github.com/repos/django/django'
        response = urllib.request.urlopen(url).read()
        return json.loads(response.decode('utf-8'))

    def pole(self):
        return self.bok_a * self.bok_b

    def obwod(self):
        return (self.bok_a + self.bok_b) * 2

    def __str__(self):
        return 'Prostokat(a={a}, b={b})'.format(a=self.bok_a, b=self.bok_b)


class TestDict:

    @staticmethod
    def github_stub():
        return json.loads(RESPONSE)

    def dict_contains_dict(self, small, large):
        for key, value in large.items():
            if key in small.keys() and value == small.get(key):
                return True
        raise AssertionError('Dict does not contains subset')


class TestRectangle(unittest.TestCase, TestDict):

    @classmethod
    def setUpClass(cls):
        cls.rectangle = Rectangle(a=5, b=10)
        cls.old_data_function = cls.rectangle.get_data_from_internet
        cls.rectangle.get_data_from_internet = cls.github_stub

    def test_dlugosci_boku_a(self):
        self.assertEqual(self.rectangle.bok_a, 5)

    def test_dlugoci_boku_b(self):
        self.assertEqual(self.rectangle.bok_b, 10)

    def test_obliczania_pola(self):
        self.assertEqual(self.rectangle.pole(), 50)

    def test_obliczania_obwodu(self):
        self.assertEqual(self.rectangle.obwod(), 30)

    def test_wyswietlanie(self):
        self.assertEqual(str(self.rectangle), 'Prostokat(a=5, b=10)')

    def test_poprawnej_dlugosci_boku_a(self):
        with self.assertRaises(ValueError):
            Rectangle(a=-1, b=10)

    def test_poprawnej_dlugosci_boku_b(self):
        with self.assertRaises(ValueError):
            Rectangle(a=5, b=-1)

    def test_poprawnej_dlugosci_bokow(self):
        with self.assertRaises(ValueError):
            Rectangle(a=-1, b=-1)

    def test_co_przechowuje(self):
        contains = self.dict_contains_dict({'name': 'django'}, self.rectangle.get_data_from_internet())
        self.assertTrue(contains)

    @classmethod
    def tearDownClass(cls):
        cls.rectangle.get_data_from_internet = cls.old_data_function
        del cls.old_data_function


if __name__ == '__main__':
    unittest.main()