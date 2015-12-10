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


FILENAME = '../../tmp/etc-passwd.txt'


def passwd1():
    """
    Zwraca informacje na temat kont systemowych
    """
    technical_accouts = []

    with open(FILENAME) as file:

        for line in file:

            if not line.startswith('#'):
                username = line.split(':')[0]
                uid = int(line.split(':')[2])

                if uid < 1000:
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


"""
def make_html1(lista):
    html = '<table>'

    for element in lista:
        html += '<tr><td>%s</td></tr>' % element
    html += '</table>'

    return html


def make_html2(lista):
    html = ['<table>']
    for element in lista:
        html.append('<tr><td>%s</td></tr>' % element)
    html.append('</table>')
    return '\r\n'.join(html)
"""

if __name__ == '__main__':
    konta1 = passwd1()
    konta2 = passwd2()

    print(sys.getsizeof(konta1))
    print(sys.getsizeof(konta2))
