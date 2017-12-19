FILENAME = '/etc/hostname'


with open(FILENAME) as file:
    for line in file:
        print(line)


with open(FILENAME) as file:
    content = file.read()


with open(FILENAME) as file:
    content = file.readlines()


with open(FILENAME) as file:
    for line in file.readlines()[30:50]:
        print(line)