FILENAME = r'C:\Users\desktop.ini'

try:
    with open(FILENAME, mode='w', encoding='utf-8') as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print('File does not exist')

except PermissionError:
    print('Permission denied')
