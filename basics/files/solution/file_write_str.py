FILE = r'/tmp/file_write_hello.txt'
DATA = 'hello'
result = DATA + '\n'

with open(FILE, mode='wt') as file:
    file.write(result)
