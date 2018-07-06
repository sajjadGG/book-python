#!/usr/bin/env python3
import datetime

DISSABLED_SHADOW_ENTRY = {'!', '!!', '*'}

ETC_PASSWD = '../data/etc-passwd.txt'
ETC_SHADOW = '../data/etc-shadow.txt'
ETC_GROUP = '../data/etc-group.txt'

ALGORITHMS = {
    '$1$': 'MD5',
    '$2a$': 'Blowfish',
    '$2y$': 'Blowfish',
    '$5$': 'SHA-256',
    '$6$': 'SHA-512',
}

"""
users = [{
    'login': 'jimenez',
    'uid': 1001,
    'gid': 1001,
    'home': '/home/jimenez',
    'shell': '/bin/bash',
    'algorithm': 'SHA-512',
    'password': 'P9zn0KwR...k4kijuhE50',
    'groups': ['staff', 'sysadmin'],
    'lastchanged': datetime.date(2015, 7, 16),
    'locked': False,
}, ...]
"""

users = []

with open(ETC_PASSWD) as passwd, \
     open(ETC_GROUP) as group, \
     open(ETC_SHADOW) as shadow:

        etc_passwd = passwd.readlines()
        etc_group = group.readlines()
        etc_shadow = shadow.readlines()

for line in etc_passwd:
    if not line.isspace() and not line.startswith('#'):
        login, password, uid, gid, gecos, home, shell = line.strip().split(':')

        if int(uid) < 1000:
            continue

        groups = []
        locked = False
        algorithm = None
        lastchanged = None

        for line in etc_group:
            if not line.isspace() and not line.startswith('#'):
                gr_name, gr_passwd, gr_gid, gr_members = line.strip().split(':')

                if login in gr_members.split(','):
                    groups.append(gr_name)

        for line in etc_shadow:
            if not line.isspace() and not line.startswith('#'):
                shadow_login, shadow_password, shadow_lastchanged, *_ = line.strip().split(':')

                if shadow_login != login:
                    continue

                shadow_lastchanged = int(shadow_lastchanged) * 60 * 60 * 24
                lastchanged = datetime.date.fromtimestamp(shadow_lastchanged)

                if shadow_password in DISSABLED_SHADOW_ENTRY:
                    locked = True
                    password = None
                    break

                for string in ALGORITHMS.keys():
                    if shadow_password.startswith(string):
                        algorithm = ALGORITHMS.get(string)
                        password = shadow_password.replace(string, '')

        users.append({
            'login': login,
            'uid': uid,
            'gid': gid,
            'home': home,
            'shell': shell,
            'algorithm': algorithm,
            'password': password,
            'groups': groups,
            'lastchanged': lastchanged,
            'locked': locked
        })

from pprint import pprint
pprint(users)