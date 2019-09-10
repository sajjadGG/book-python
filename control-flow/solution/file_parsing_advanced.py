FILE = r'../data/etc-hosts.txt'
output = []


try:
    with open(FILE) as file:
        content = file.readlines()

except FileNotFoundError:
    print('File does not exist')

except PermissionError:
    print('Permission denied')


for line in content:
    if line.startswith('#'):
        continue
    if line.isspace():
        continue

    line = line.strip().split()
    ip = line[0]
    hosts = line[1:]

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

"""
found = False

for x in hosts:
    if x['ip'] == ip:
        found = True
        x['hostnames'] += hostnames

if not found:
    hosts.append({
        'ip': ip,
        'hostnames': hostnames,
        'protocol': 'IPv4' if '.' in ip else 'IPv6'
    })
"""
