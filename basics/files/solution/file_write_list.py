FILE = r'/tmp/file_write_newline.txt'
DATA = ['hello', 'world']
result = '\n'.join(DATA) + '\n'

with open(FILE, mode='wt') as file:
    file.write(result)
