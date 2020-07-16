from dataclasses import dataclass
from pprint import pprint

FILE = r'/tmp/etc-passwd.txt'

DATA = """##
# User Database
#   - User name
#   - Encrypted password
#   - User ID number (UID)
#   - User's group ID number (GID)
#   - Full name of the user (GECOS)
#   - User home directory
#   - Login shell
##

root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
nobody:x:99:99:Nobody:/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
peck:x:1000:1000:Max Peck:/home/peck:/bin/bash
jimenez:x:1001:1001:José Jiménez:/home/jimenez:/bin/bash
ivanovic:x:1002:1002:Ivan Иванович:/home/ivanovic:/bin/bash
"""

with open(FILE, mode='w') as file:
    file.write(DATA)


@dataclass
class Account:
    username: str


class SystemAccount(Account):
    pass


class UserAccount(Account):
    pass


class Parse:
    def __new__(cls, *args, **kwargs):
        with open(FILE, encoding='utf-8') as file:
            for line in file:
                line = line.strip()

                if len(line) == 0 or line.startswith('#'):
                    continue

                username, _, uid, *_ = line.split(':')

                if int(uid) >= 1000:
                    yield UserAccount(username)
                else:
                    yield SystemAccount(username)


result = Parse()
pprint(list(result))
