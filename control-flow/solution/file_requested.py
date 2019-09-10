FILE = input('File to open: ').strip()


try:

    with open(FILE, mode='r') as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print('File does not exists')

except PermissionError:
    print('Permission denied')
