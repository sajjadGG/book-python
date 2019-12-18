FILE = r'../data/etc-hosts.txt'
OUTPUT = []


with open(FILE) as file:
    for line in file:
        line = line.strip()

        if not line:
            continue

        if line.startswith('#'):
            continue

        ip, *hosts = line.split()

        for record in OUTPUT:
            if record['ip'] == ip:
                record['hostnames'].update(hosts)
                break
        else:
            OUTPUT.append({
                'hostnames': set(hosts),
                'protocol': 'IPv4' if '.' in ip else 'IPv6',
                'ip': ip,
            })

print(OUTPUT)

## Alternative solution
# found = False
#
# for x in hosts:
#     if OUTPUT['ip'] == ip:
#         found = True
#         OUTPUT['hostnames'].update(hosts)
#
# if not found:
#     OUTPUT.append({
#         'ip': ip,
#         'hostnames': set(hostnames),
#         'protocol': 'IPv4' if '.' in ip else 'IPv6'
#     })
#
