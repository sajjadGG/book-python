"""
>>> sorted(result)  # doctest: +NORMALIZE_WHITESPACE
['bpo-25460', 'bpo-36076', 'bpo-37630', 'bpo-38530', 'bpo-38605', 'bpo-38659',
 'bpo-40849', 'bpo-42333', 'bpo-42854', 'bpo-43362', 'bpo-43641', 'bpo-43669',
 'bpo-43799', 'bpo-43837', 'bpo-43859', 'bpo-43880', 'bpo-43888']
"""

import re
import sys
from datetime import datetime, timezone
import requests


USERNAME = '...'
TOKEN = '...'


DATA_REPOS = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/json/github-python-repos.json'
# DATA_REPOS = 'https://api.github.com/orgs/python/repos?per_page=10000'
DATA_COMMITS = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/json/github-python-commits.json'
# DATA_COMMITS = 'https://api.github.com/repos/python/cpython/commits'

PATTERN = r'bpo-[0-9]+'

commits = list()
result = set()


def GET(url):
    data = requests.get(url, auth=(USERNAME, TOKEN)).json()
    if type(data) is dict and data['message'].startswith('API rate limit exceeded'):
        print('API rate limit exceeded')
        sys.exit(1)
    return data


for repository in GET(DATA_REPOS):
    if repository['name'] == 'cpython':
        DATA_COMMITS = repository['commits_url'].replace('{/sha}', '')
        break


for commit in GET(DATA_COMMITS):
    sha = commit['sha']
    author = commit['commit']['author']['name']
    email = commit['commit']['author']['email']
    date = datetime.strptime(commit['commit']['author']['date'], '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)
    message = commit['commit']['message']

    if issue := re.findall(PATTERN, message):
        result.update(issue)

    commits.append({
        'sha': sha,
        'author': author,
        'email': email,
        'date': date,
        'message': message})
