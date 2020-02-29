FILE = r'hosts-adv.txt'
output = []


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

    for host in output:
        if host['ip'] == ip:
            host['hostnames'].update(hostnames)
            found = True
            break

    if not found:
        output.append({
            'ip': ip,
            'hostnames': set(hostnames),
            'protocol': 'IPv4' if '.' in ip else 'IPv6'
        })

print(output)


## Alternative solution
# for record in output:
#     if record['ip'] == ip:
#         record['hostnames'].update(hostnames)
#         break
# else:
#     output.append({
#         'hostnames': set(hostnames),
#         'protocol': 'IPv4' if '.' in ip else 'IPv6',
#         'ip': ip,
#     })

