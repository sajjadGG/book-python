import csv

FILENAME = r'C:\Users\Matt Harasymczuk\Desktop\passwd.txt'

with open(FILENAME) as csvfile:
    fieldnames = ['user', 'password', 'uid', 'gid', 'name', 'home', 'shell']
    data = csv.DictReader(csvfile, fieldnames=fieldnames, delimiter=':')

    for row in data:
        print(row)

# OrderedDict([('user', 'root'), ('password', 'x'), ('uid', '0'), ('gid', '0'), ('name', 'root'), ('home', '/root'), ('shell', '/bin/bash')])
# OrderedDict([('user', 'bin'), ('password', 'x'), ('uid', '1'), ('gid', '1'), ('name', 'bin'), ('home', '/bin'), ('shell', '/sbin/nologin')])