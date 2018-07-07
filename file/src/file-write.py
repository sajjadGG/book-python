FILENAME = '/etc/hostname'


with open(FILENAME, mode='w') as file:
    file.write('foobar')


with open(FILENAME, mode='a') as file:
    file.write('foobar')


with open(FILENAME, mode='w', encoding='utf-8') as file:
    file.write('foobar')
