#!/usr/bin/env python3

""" /etc/hosts
##
# Host Database
##

127.0.0.1       localhost
127.0.0.1       mycomp
10.13.37.1      facebook.com google.com microsoft.com
255.255.255.255 broadcasthost
::1             localhost
"""

FILENAME = '../../_tmp/etc-hosts'
hosts = []


with open(FILENAME) as file:
    for line in file:
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

{'ip': '127.0.0.1', 'hostnames': ['localhost'], 'protocol': 'ipv4'},
{'ip': '127.0.0.1', 'hostnames': ['mycomp'], 'protocol': 'ipv4'},
{'ip': '10.13.37.1', 'hostnames': ['facebook.com', 'google.com', 'microsoft.com'], 'protocol': 'ipv4'},
{'ip': '255.255.255.255', 'hostnames': ['broadcasthost'], 'protocol': 'ipv4'},
{'ip': '::1', 'hostnames': ['localhost'], 'protocol': 'ipv6'},
"""
