try:
    with open(r'C:\Users\desktop.ini', mode='w', encoding='utf-8') as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print('File does not exist')

except PermissionError:
    print('Permission denied')
