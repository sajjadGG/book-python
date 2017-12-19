FILENAME = '/etc/hostname'


with open(FILENAME, 'w') as file:
    file.write('foobar')


with open(FILENAME, 'a') as file:
    file.write('foobar')