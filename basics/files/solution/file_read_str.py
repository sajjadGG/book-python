FILE = r'/tmp/file_write_hello.txt'
DATA = 'hello'

with open(FILE, mode='wt') as file:
    file.write(DATA)

with open(FILE, mode='rt') as file:
    result = file.read()

print(result)
