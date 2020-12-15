"""
* Assignment: File Passwd
* Filename: file_passwd.py
* Complexity: medium
* Lines of code: 100 lines
* Time: 21 min

English:
    1. Use data from "Given" section (see below)
    2. Save listings content to files:
        a. ``etc_passwd.txt``
        b. ``etc_shadow.txt``
        c. ``etc_group.txt``
    3. Copy also comments and empty lines
    4. Parse files and convert it to ``result: list[dict]``
    5. Return list of users with ``UID`` greater than 1000
    6. User dict should contains data collected from all files
    7. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zapisz treści listingów do plików:
        a. ``etc_passwd.txt``
        b. ``etc_shadow.txt``
        c. ``etc_group.txt``
    3. Skopiuj również komentarze i puste linie
    4. Sparsuj plik i przedstaw go w formacie ``result: list[dict]``
    5. Zwróć listę użytkowników, których ``UID`` jest większy niż 1000
    6. Dict użytkownika powinien zawierać dane z wszystkich plików
    7. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. literalinclude:: data/etc-passwd.txt
        :name: code-exam-etc-passwd
        :language: text
        :caption: Przykładowa zawartość pliku ``/etc/passwd``

    .. literalinclude:: data/etc-shadow.txt
        :name: code-exam-etc-shadow
        :language: text
        :caption: Przykładowa zawartość pliku ``/etc/shadow``

    .. literalinclude:: data/etc-group.txt
        :name: code-exam-etc-group
        :language: text
        :caption: Przykładowa zawartość pliku ``/etc/group``

Tests:
    >>> result  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    [{'username': 'twardowski',
      'uid': 1001,
      'gid': 1001,
      'home': '/home/twardowski',
      'shell': '/bin/bash',
      'algorithm': 'SHA-512',
      'password': 'tgfvvFWJJ5...k4kijuhE50',
      'salt': 'P9zn0KwR',
      'groups': {'astronauts', 'sysadmin'},
      'last_changed': datetime.date(2015, 7, 16),
      'locked': False},
    ...]

"""


# Given
from datetime import date


FILE_GROUP = r'../data/etc-group.txt'
FILE_SHADOW = r'../data/etc-shadow.txt'
FILE_PASSWD = r'../data/etc-passwd.txt'

SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR

ALGORITHMS = {
    '1': 'MD5',
    '2a': 'Blowfish',
    '2y': 'Blowfish',
    '5': 'SHA-256',
    '6': 'SHA-512',
}

result_group = {}
result_shadow = {}
result_passwd = {}
result = []


# Solution
try:
    with open(FILE_GROUP, encoding='utf-8') as file:
        etc_groups = file.readlines()
except FileNotFoundError:
    print('File does not exist')
except PermissionError:
    print('Permission denied')


try:
    with open(FILE_SHADOW, encoding='utf-8') as file:
        etc_shadow = file.readlines()
except FileNotFoundError:
    print('File does not exist')
except PermissionError:
    print('Permission denied')


try:
    with open(FILE_PASSWD, encoding='utf-8') as file:
        etc_passwd = file.readlines()
except FileNotFoundError:
    print('File does not exist')
except PermissionError:
    print('Permission denied')


for line in etc_groups:
    line = line.strip()

    if not line or line.startswith('#'):
        continue

    group_name, _, _, members, *_ = line.split(':')

    if not members:
        continue

    for member in members.split(','):
        if member not in result_group.keys():
            result_group[member] = set()

        result_group[member].add(group_name)


for line in etc_shadow:
    line = line.strip()

    if not line or line.startswith('#'):
        continue

    username, password, last_change, *_ = line.split(':')
    timestamp = int(last_change) * DAY
    last_change = date.fromtimestamp(timestamp)

    if password.startswith('$'):
        locked = False
        password = password.split('$')
        password_algorithm = ALGORITHMS[password[1]]
        password_salt = password[2]
        password_password = password[3]
    else:
        locked = True
        password_algorithm = None
        password_salt = None
        password_password = None

    result_shadow[username] = {
        'password': password_password,
        'salt': password_salt,
        'algorithm': password_algorithm,
        'last_change': last_change,
        'locked': locked,
    }


for line in etc_passwd:
    line = line.strip()

    if not line or line.startswith('#'):
        continue

    record = line.split(':')
    username = record[0]

    result_passwd[username] = {
        'password': record[1],
        'uid': int(record[2]),
        'gid': int(record[3]),
        'gecos': record[4],
        'home': record[5],
        'shell': record[6],
    }


for user in result_passwd:
    passwd = result_passwd.get(user)
    groups = result_group.get(user)
    shadow = result_shadow.get(user)

    if passwd['uid'] < 1000:
        continue

    result.append({
        'username': user,
        'uid': passwd['uid'],
        'gid': passwd['gid'],
        'home': passwd['home'],
        'shell': passwd['shell'],
        'algorithm': shadow['algorithm'],
        'password': shadow['password'],
        'groups': groups,
        'last_changed': shadow['last_change'],
        'locked': shadow['locked'],
    })
