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

FILENAME = '../data/hosts.txt'
hosts = []


with open(FILENAME) as file:
    for line in file:
        if line.isspace() or line.startswith('#'):
            continue

        # ip, *hostnames = line.split()
        ip = line.split()[0]
        hostnames = line.split()[1:]

        hosts.append({
            'ip': ip,
            'hostnames': hostnames,
            'protocol': 'ipv4' if '.' in ip else 'ipv6',
        })


from pprint import pprint
pprint(hosts)
