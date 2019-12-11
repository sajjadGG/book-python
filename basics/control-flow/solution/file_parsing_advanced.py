FILE = r'../data/etc-hosts.txt'
OUTPUT = []


try:
    with open(FILE) as file:
        hosts_file = file.readlines()

except FileNotFoundError:
    print('File does not exist')

except PermissionError:
    print('Permission denied')


for line in hosts_file:
    line = line.strip()

    if line == '' or line.startswith('#'):
        continue

    ip, *hostnames = line.split()
    found = False

    for host in OUTPUT:
        if host['ip'] == ip:
            host['hostnames'] += hostnames
            found = True
            break

    if not found:
        hostnames.append({
            'ip': ip,
            'hostnames': hostnames,
            'protocol': 'IPv4' if '.' in ip else 'IPv6'
        })

print(OUTPUT)


## Alternative solution
# for record in OUTPUT:
#     if record['ip'] == ip:
#         record['hostnames'].update(hostnames)
#         break
# else:
#     OUTPUT.append({
#         'hostnames': set(hostnames),
#         'protocol': 'IPv4' if '.' in ip else 'IPv6',
#         'ip': ip,
#     })
