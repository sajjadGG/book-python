FILE = r'../data/etc-hosts.txt'
output = []


with open(FILE) as file:
    for line in file:
        line = line.strip()

        if not line:
            continue

        if line.startswith('#'):
            continue

        ip, *hosts = line.split()

        for record in output:
            if record['ip'] == ip:
                record['hostnames'].update(hosts)
                break
        else:
            output.append({
                'hostnames': set(hosts),
                'protocol': 'IPv4' if '.' in ip else 'IPv6',
                'ip': ip,
            })

print(output)

## Alternative solution
# found = False
#
# for x in hosts:
#     if output['ip'] == ip:
#         found = True
#         output['hostnames'].update(hosts)
#
# if not found:
#     output.append({
#         'ip': ip,
#         'hostnames': set(hostnames),
#         'protocol': 'IPv4' if '.' in ip else 'IPv6'
#     })
#
