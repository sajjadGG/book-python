"""
* Assignment: JSON Object Dataclass
* Complexity: easy
* Lines of code: 15 lines
* Time: 13 min

English:
    1. `DATA` is a JSON downloaded from https://api.github.com/users
    3. Model data as class `User`
    4. Iterate over records and create instances of this class
    5. Collect all instances to one list
    6. Run doctests - all must succeed

Polish:
    1. `DATA` to JSON pobrany z https://api.github.com/users
    3. Zamodeluj dane za pomocą klasy `User`
    4. Iterując po rekordach twórz instancje tej klasy
    5. Zbierz wszystkie instancje do jednej listy
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result)
    <class 'list'>
    >>> len(result) > 0
    True
    >>> all(type(row) is User
    ...     for row in result)
    True
    >>> result[0]  # doctest: +NORMALIZE_WHITESPACE
    User(login='myuser',
         id=1,
         node_id='MDQ6VXNlcjE=',
         avatar_url='https://avatars.githubusercontent.com/u/1?v=4',
         gravatar_id='',
         url='https://api.github.com/users/myuser',
         html_url='https://github.com/myuser',
         followers_url='https://api.github.com/users/myuser/followers',
         following_url='https://api.github.com/users/myuser/following',
         gists_url='https://api.github.com/users/myuser/gists{/gist_id}',
         starred_url='https://api.github.com/users/myuser/starred',
         subscriptions_url='https://api.github.com/users/myuser/subscriptions',
         organizations_url='https://api.github.com/users/myuser/orgs',
         repos_url='https://api.github.com/users/myuser/repos',
         events_url='https://api.github.com/users/myuser/events{/privacy}',
         received_events_url='https://api.github.com/users/myuser',
         type='User',
         site_admin=False)
"""
import json


DATA = (
    '[{"login":"myuser","id":1,"node_id":"MDQ6VXNlcjE=","avatar_url":"http'
    's://avatars.githubusercontent.com/u/1?v=4","gravatar_id":"","url":"ht'
    'tps://api.github.com/users/myuser","html_url":"https://github.com/myu'
    'ser","followers_url":"https://api.github.com/users/myuser/followers",'
    '"following_url":"https://api.github.com/users/myuser/following","gist'
    's_url":"https://api.github.com/users/myuser/gists{/gist_id}","starred'
    '_url":"https://api.github.com/users/myuser/starred","subscriptions_ur'
    'l":"https://api.github.com/users/myuser/subscriptions","organizations'
    '_url":"https://api.github.com/users/myuser/orgs","repos_url":"https:/'
    '/api.github.com/users/myuser/repos","events_url":"https://api.github.'
    'com/users/myuser/events{/privacy}","received_events_url":"https://api'
    '.github.com/users/myuser","type":"User","site_admin":false},{"login":'
    '"defunkt","id":2,"node_id":"MDQ6VXNlcjI=","avatar_url":"https://avata'
    'rs.githubusercontent.com/u/2?v=4","gravatar_id":"","url":"https://api'
    '.github.com/users/defunkt","html_url":"https://github.com/defunkt","f'
    'ollowers_url":"https://api.github.com/users/defunkt/followers","follo'
    'wing_url":"https://api.github.com/users/defunkt/following","gists_url'
    '":"https://api.github.com/users/defunkt/gists{/gist_id}","starred_url'
    '":"https://api.github.com/users/defunkt/starred","subscriptions_url":'
    '"https://api.github.com/users/defunkt/subscriptions","organizations_u'
    'rl":"https://api.github.com/users/defunkt/orgs","repos_url":"https://'
    'api.github.com/users/defunkt/repos","events_url":"https://api.github.'
    'com/users/defunkt/events{/privacy}","received_events_url":"https://ap'
    'i.github.com/users/defunkt","type":"User","site_admin":false},{"login'
    '":"pjhyett","id":3,"node_id":"MDQ6VXNlcjM=","avatar_url":"https://ava'
    'tars.githubusercontent.com/u/3?v=4","gravatar_id":"","url":"https://a'
    'pi.github.com/users/pjhyett","html_url":"https://github.com/pjhyett",'
    '"followers_url":"https://api.github.com/users/pjhyett/followers","fol'
    'lowing_url":"https://api.github.com/users/pjhyett/following","gists_u'
    'rl":"https://api.github.com/users/pjhyett/gists{/gist_id}","starred_u'
    'rl":"https://api.github.com/users/pjhyett/starred","subscriptions_url'
    '":"https://api.github.com/users/pjhyett/subscriptions","organizations'
    '_url":"https://api.github.com/users/pjhyett/orgs","repos_url":"https:'
    '//api.github.com/users/pjhyett/repos","events_url":"https://api.githu'
    'b.com/users/pjhyett/events{/privacy}","received_events_url":"https://'
    'api.github.com/users/pjhyett","type":"User","site_admin":false}]')


class User:
    def __repr__(self):
        result = []
        for attrname, attrvalue in vars(self).items():
            if type(attrvalue) is str:
                result.append(f"{attrname}='{attrvalue}'")
            else:
                result.append(f"{attrname}={attrvalue}")
        result = ', '.join(result)
        return f"User({result})"


# JSON decoded DATA
result = ...


# Solution
class User:
    def __init__(self, login, id, node_id, avatar_url, gravatar_id, url,
                 html_url, followers_url, following_url, gists_url,
                 starred_url, subscriptions_url, organizations_url,
                 repos_url, events_url, received_events_url, type,
                 site_admin):

        self.login = login
        self.id = id
        self.node_id = node_id
        self.avatar_url = avatar_url
        self.gravatar_id = gravatar_id
        self.url = url
        self.html_url = html_url
        self.followers_url = followers_url
        self.following_url = following_url
        self.gists_url = gists_url
        self.starred_url = starred_url
        self.subscriptions_url = subscriptions_url
        self.organizations_url = organizations_url
        self.repos_url = repos_url
        self.events_url = events_url
        self.received_events_url = received_events_url
        self.type = type
        self.site_admin = site_admin

    def __repr__(self):
        result = []
        for attrname, attrvalue in vars(self).items():
            if type(attrvalue) is str:
                result.append(f"{attrname}='{attrvalue}'")
            else:
                result.append(f"{attrname}={attrvalue}")
        result = ', '.join(result)
        return f"User({result})"


def decoder(obj: dict) -> User:
    return User(**obj)


result = json.loads(DATA, object_hook=decoder)

# Solution 2
from dataclasses import dataclass


@dataclass
class User:
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    site_admin: bool


def decoder(obj: dict) -> User:
    return User(**obj)


result = json.loads(DATA, object_hook=decoder)
