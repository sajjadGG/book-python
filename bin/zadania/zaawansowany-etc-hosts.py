#!/usr/bin/env python3

""" /etc/hosts
##
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting.  Do not change this entry.
##
127.0.0.1       localhost
255.255.255.255 broadcasthost
::1             localhost


127.0.0.1 matt python air
"""

"""
hosts = [
    {'ip': '127.0.0.1', 'hostnames': ['localhost'], 'protocol': 'ipv4'},
    {'ip': '255.255.255.255', 'hostnames': ['broadcasthost'], 'protocol': 'ipv4'},
    {'ip': '::1', 'hostnames': ['localhost'], 'protocol': 'ipv6'},
    {'ip': '127.0.0.1', 'hostnames': ['matt', 'python', 'air'], 'protocol': 'ipv4'},
]
"""

FILENAME = '../../tmp/etc-hosts'
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
