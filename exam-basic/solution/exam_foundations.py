from datetime import date
from pprint import pprint

ETC_SHADOW = '../src/etc-shadow.txt'
ETC_PASSWD = '../src/etc-passwd.txt'
ETC_GROUP = '../src/etc-group.txt'

users = list()
groups = dict()
ALGORITHMS = {
    '1': 'MD5',
    '2a': 'Blowfish',
    '2y': 'Blowfish',
    '5': 'SHA-256',
    '6': 'SHA-512',
}

def is_clean(line):
    if line.isspace() or line.startswith('#'):
        return False
    else:
        return True


with open(ETC_GROUP) as group:
    for line in group:
        if is_clean(line):
            groupname, password, gid, users = line.split(':')

            for user in users.split(','):
                user = user.strip()

                if not user:
                    continue

                if user not in groups.keys():
                    groups[user] = [groupname]
                else:
                    groups[user].append(groupname)


with open(ETC_SHADOW) as shadow:
    for line in shadow:
        if is_clean(line):
            username, password, lastchanged, *_ = line.split(':')
            lastchanged = date.fromtimestamp(int(lastchanged))

            if password in ('*', '!', '!!'):
                locked = True
            else:
                locked = False
                _, algorithm, salt, password = password.split('$')
                algorithm = ALGORITHMS[algorithm]

        # 'algorithm': algorithm,
        # 'password': password,

        # 'locked': locked,
        # 'lastchanged': lastchanged,


with open(ETC_PASSWD, encoding='utf-8') as passwd:
    for line in passwd:
        if is_clean(line):
            username, password, uid, gid, fullname, home, shell = line.split(':')
            users.append({'login': username, 'uid': uid, 'gid': gid, 'home': home, 'shell': shell})


pprint(users)
