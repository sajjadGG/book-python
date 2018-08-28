FILENAME = r'C:\Users\desktop.ini'


with open(FILENAME, mode='w', encoding='utf-8') as file:
    file.write('foobar')


with open(FILENAME, mode='a', encoding='utf-8') as file:
    file.write('foobar')
