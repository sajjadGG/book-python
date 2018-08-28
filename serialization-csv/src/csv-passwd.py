import csv

FILENAME = r'etc-passwd.txt'
"""
root:x:0:0:root:/root:/bin/bash
peck:x:1000:1000:Max Peck:/home/peck:/bin/bash
jimenez:x:1001:1001:José Jiménez:/home/jimenez:/bin/bash
ivanovic:x:1002:1002:Иван Иванович:/home/ivanovic:/bin/bash
"""

with open(FILENAME, encoding='utf-8') as file:
    fieldnames = ['username', 'password', 'uid', 'gid', 'full_name', 'home', 'shell']
    data = csv.DictReader(file, fieldnames=fieldnames, delimiter=':')

    for row in data:
        username = row['username']
        full_name = row['full_name']
        home = row['home']

        print(f'{username} -> {full_name} with HOME="{home}" ')
        # root -> root with HOME="/root"
        # peck -> Max Peck with HOME="/home/peck"
        # jimenez -> José Jiménez with HOME="/home/jimenez"
        # ivanovic -> Иван Иванович with HOME="/home/ivanovic"
