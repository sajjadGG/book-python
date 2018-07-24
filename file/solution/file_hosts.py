hosts = []


with open(r'../src/etc-hosts.txt', encoding='utf-8') as file:
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
