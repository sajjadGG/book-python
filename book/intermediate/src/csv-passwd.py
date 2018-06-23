import csv

FILENAME = r'../contrib/etc-passwd.txt'


with open(FILENAME) as file:
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
        # ivanovic -> Ivan Ivanovic with HOME="/home/ivanovic"
