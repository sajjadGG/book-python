"""
* Assignment: OOP Constructor Passwd
* Complexity: easy
* Lines of code: 21 lines
* Time: 13 min

English:
    TODO: English translation
    X. Run doctests - all must succeed

Polish:
    1. Iteruj po liniach w `DATA` i podziel linię po dwukropku
    2. Stwórz klasę `Account`, która zwraca instancje klas
       `UserAccount` lub `SystemAccount` w zależności od wartości pola UID
    3. User ID (UID) to trzecie pole, np.
       `root:x:0:0:root:/root:/bin/bash` to UID jest równy `0`
    4. Jeżeli UID jest:
       a. poniżej 1000, to konto jest systemowe (`SystemAccount`)
       b. 1000 lub więcej, to konto użytkownika (`UserAccount`)
    5. Stwórz repr wyświetlający informacje o klasie w formacie:
       `SystemAccount(username='root', uid=0)`
    6. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `str.splitlines()`
    * `str.split()`
    * `str.strip()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [SystemAccount(username='root', uid=0),
     SystemAccount(username='bin', uid=1),
     SystemAccount(username='daemon', uid=2),
     SystemAccount(username='adm', uid=3),
     SystemAccount(username='shutdown', uid=6),
     SystemAccount(username='halt', uid=7),
     SystemAccount(username='nobody', uid=99),
     SystemAccount(username='sshd', uid=74),
     UserAccount(username='twardowski', uid=1000),
     UserAccount(username='jimenez', uid=1001),
     UserAccount(username='ivanovic', uid=1002),
     UserAccount(username='lewis', uid=1002)]
"""

DATA = """root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
nobody:x:99:99:Nobody:/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
twardowski:x:1000:1000:Jan Twardowski:/home/twardowski:/bin/bash
jimenez:x:1001:1001:José Jiménez:/home/jimenez:/bin/bash
ivanovic:x:1002:1002:Иван Иванович:/home/ivanovic:/bin/bash
lewis:x:1002:1002:Melissa Lewis:/home/lewis:/bin/bash"""


# list[Account]: parse DATA and convert to UserAccount or SystemAccount
result = ...

# Solution
from dataclasses import dataclass


@dataclass
class Account:
    username: str
    uid: int

    def __new__(cls, username: str, uid: int):
        if uid < 1000:
            return object.__new__(SystemAccount)
        else:
            return object.__new__(UserAccount)


class UserAccount(Account):
    pass

class SystemAccount(Account):
    pass


result = [Account(username, int(uid))
          for line in DATA.splitlines()
          if (record := line.strip().split(':'))
          if (username := record[0])
          and (uid := record[2])]
