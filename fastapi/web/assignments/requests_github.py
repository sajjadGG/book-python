"""
>>> sorted(result)  # doctest: +NORMALIZE_WHITESPACE
['bpo-34311', 'bpo-38530', 'bpo-41515', 'bpo-41661', 'bpo-42248', 'bpo-42904',
 'bpo-43080', 'bpo-43680', 'bpo-43712', 'bpo-43723', 'bpo-43731', 'bpo-43760',
 'bpo-43770', 'bpo-43774', 'bpo-43777', 'bpo-43785', 'bpo-43787', 'bpo-43797',
 'bpo-43799', 'bpo-43811', 'bpo-43816']
"""

import re
from datetime import datetime, timezone
import requests


USERNAME = '...'
TOKEN = '...'

AUTH = (USERNAME, TOKEN)
commits = list()
result = set()

PATTERN = r'bpo-[0-9]+'

DATA_REPOS = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/json/github-python-repos.json'
# DATA_REPOS = 'https://api.github.com/orgs/python/repos?per_page=10000'
DATA_COMMITS = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/json/github-python-commits.json'
# DATA_COMMITS = 'https://api.github.com/repos/python/cpython/commits'


for repository in requests.get(DATA_REPOS, auth=AUTH).json():
    if repository['name'] == 'cpython':
        url = repository['commits_url']
        url = url.replace('{/sha}', '')
        break


for commit in requests.get(url, auth=AUTH).json():
    hash = commit['sha']
    author = commit['commit']['author']['name']
    email = commit['commit']['author']['email']
    date = commit['commit']['author']['date']
    date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)
    message = commit['commit']['message']

    if issue := re.findall(PATTERN, message):
        result.update(issue)

    commits.append({
        'hash': hash,
        'author': author,
        'email': email,
        'date': date,
        'message': message})
