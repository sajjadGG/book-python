"""
* Assignment: Unpack Assignement Expression
* Complexity: medium
* Lines of code: 6 lines
* Time: 13 min

English:
    1. Split `DATA` by lines and then by colon `:`
    2. Extract system accounts (users with UID [third field] is less than 1000)
    3. Return list of system account logins
    4. Implement solution using list comprehension and assignment expression
    5. Mind the `root` user who has `uid == 0` (whether is not filtered-out in if statement)
    6. Run doctests - all must succeed

Polish:
    1. Podziel `DATA` po liniach a następnie po dwukropku `:`
    2. Wyciągnij konta systemowe (użytkownicy z UID [trzecie pole] mniejszym niż 1000)
    3. Zwróć listę loginów użytkowników systemowych
    4. Zaimplementuj rozwiązanie wykorzystując list comprehension i assignment expression
    5. Zwróć uwagę na użytkownika `root`, który ma `uid == 0` (czy nie jest odfiltrowany w instrukcji if)
    6. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * `str.splitlines()`
    * `str.strip()`
    * `str.split()`
    * `int()`
    * `bool(0) == False`
    * `bool('0') == True`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert len(result) > 0, \
    'Variable `result` cannot be empty'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert all(type(x) is str for x in result), \
    'All rows in `result` should be str'

    >>> result
    ['root', 'bin', 'daemon', 'adm', 'shutdown', 'halt', 'nobody', 'sshd']
"""

DATA = """root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
nobody:x:99:99:Nobody:/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
watney:x:1000:1000:Mark Watney:/home/watney:/bin/bash
lewis:x:1001:1001:Melissa Lewis:/home/lewis:/bin/bash
martinez:x:1002:1002:Rick Martinez:/home/martinez:/bin/bash"""


# list[str]: system account usernames (UID [third field] is less than 1000)
result = ...

# Solution
result = [username
          for row in DATA.splitlines()
          if (values := row.strip().split(':'))
          and (username := values[0])
          and (uid := values[2])
          and int(uid) < 1000]
