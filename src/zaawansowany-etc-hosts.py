#!/usr/bin/env python3

""" /etc/hosts
##
# Host Database
#   - Unix: /etc/hosts
#   - Windows: C:/Windows/System32/drivers/etc/hosts
##

127.0.0.1       localhost
127.0.0.1       astromatt
10.13.37.1      nasa.gov esa.int roscosmos.ru
255.255.255.255 broadcasthost
::1             localhost
"""

FILENAME = '../../_tmp/etc-hosts'
hosts = []


with open(FILENAME) as file:
    for line in file.readlines():
        if not line.isspace() and not line.startswith('#'):
            ip, *hostnames = line.split()

            hosts.append({
                'ip': ip,
                'hostnames': hostnames,
                'protocol': 'ipv4' if '.' in ip else 'ipv6',
            })

from pprint import pprint
pprint(hosts)

""" Powinniśmy uzyskać efekt podobny do:
[
    {'ip': '127.0.0.1', 'hostnames': ['localhost'], 'protocol': 'ipv4'},
    {'ip': '127.0.0.1', 'hostnames': ['astromatt'], 'protocol': 'ipv4'},
    {'ip': '10.13.37.1', 'hostnames': ['nasa.gov', 'esa.int', 'roscosmos.ru'], 'protocol': 'ipv4'},
    {'ip': '255.255.255.255', 'hostnames': ['broadcasthost'], 'protocol': 'ipv4'},
    {'ip': '::1', 'hostnames': ['localhost'], 'protocol': 'ipv6'},
]
"""
