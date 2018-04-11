import csv

FILENAME = r'../../../data/file-etc-passwd.txt'


with open(FILENAME) as file:
    fieldnames = ['user', 'password', 'uid', 'gid', 'name', 'home', 'shell']
    data = csv.DictReader(file, fieldnames=fieldnames, delimiter=':')

    for row in data:
        print(row)

# OrderedDict([('user', '# User Database'), ('password', None), ('uid', None), ('gid', None), ('name', None), ('home', None), ('shell', None)])

# OrderedDict([('user', 'jimenez'), ('password', 'x'), ('uid', '1001'), ('gid', '1001'), ('name', 'Jose Jimenez'), ('home', '/home/jimenez'), ('shell', '/bin/bash')])

# OrderedDict([('user', 'ivanovic'), ('password', 'x'), ('uid', '1002'), ('gid', '1002'), ('name', 'Ivan Ivanovic'), ('home', '/home/ivanovic'), ('shell', '/bin/bash')])