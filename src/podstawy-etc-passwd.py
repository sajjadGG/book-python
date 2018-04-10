#!/usr/bin/env python3

"""
The /etc/passwd file is a colon-separated file that contains the following information:
- User name
- Encrypted password
- User ID number (UID)
- User's group ID number (GID)
- Full name of the user (GECOS)
- User home directory
- Login shell
"""

import sys


FILENAME = '../../_tmp/etc-passwd.txt'


def passwd1():
    technical_accouts = []

    with open(FILENAME) as file:

        for line in file:
            if line and not line.startswith('#'):
                line_splitted = line.split(':')
                username = line_splitted[0]
                uid = int(line_splitted[2])

                if uid < 50:
                    technical_accouts.append(username)

    return technical_accouts


def passwd2():
    with open(FILENAME) as file:

        for line in file:

            if not line.startswith('#'):
                username = line.split(':')[0]
                uid = int(line.split(':')[2])

                if uid < 1000:
                    yield username


if __name__ == '__main__':
    konta1 = passwd1()
    konta2 = passwd2()

    print(sys.getsizeof(konta1))
    print(sys.getsizeof(konta2))
