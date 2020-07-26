FILE = r'file_write_hello.txt'
DATA = 'hello\nworld\n'

with open(FILE, mode='wt') as file:
    file.write(DATA)

with open(FILE, mode='rt') as file:
    result = [x.strip() for x in file.readlines()]

print(result)
