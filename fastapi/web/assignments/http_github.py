"""
>>> date
datetime.datetime(2021, 1, 23, 17, 51, 48, tzinfo=datetime.timezone.utc)
>>> name
'Florian Apolloner'
>>> result
{'1'}
"""

import re
import json
from http.client import HTTPSConnection
from http import HTTPStatus
from base64 import b64encode
from datetime import datetime

PATTERN = r'#([0-9]+)'

USERNAME = 'your username'
TOKEN = 'your password'


auth = bytes(f'{USERNAME}:{TOKEN}', 'utf-8')
auth = b64encode(auth).decode('ascii')

headers = {
    'Authorization': f'Basic {auth}',
    'User-Agent': 'Python http.client',
    'Accept': 'application/json'
}

conn = HTTPSConnection(host="api.github.com", port=443)


def GET(url):
    conn.request('GET', url, headers=headers)
    response = conn.getresponse()

    if response.status == HTTPStatus.OK:
        body = response.read().decode()
        return json.loads(body)
    else:
        raise ConnectionError(response.reason)


for repository in GET('/orgs/django/repos'):
    if repository['name'] == 'django/django':
        break


url = repository['commits_url']
url = url.replace('{/sha}', '')
url = url.replace('https://api.github.com', '')

commits = GET(url)
date = commits[0]['commit']['author']['date']
name = commits[0]['commit']['author']['name']
messages = [commit['commit']['message'] for commit in commits]
date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z')

result = set()

for msg in messages:
    tickets = re.findall(PATTERN, msg, flags=re.MULTILINE)
    result.update(tickets)

conn.close()
