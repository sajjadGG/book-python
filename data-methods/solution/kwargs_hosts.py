from pprint import pprint

FILE = '../data/etc-hosts.txt'


hosts = {}

with open(FILE) as file:
    for line in file:

        if line.startswith('#'):
            continue
        if line.isspace():
            continue

        ip, *hostnames = line.split()

        if ip in hosts:
            hosts[ip] += hostnames
        else:
            hosts[ip] = hostnames

pprint(hosts)
