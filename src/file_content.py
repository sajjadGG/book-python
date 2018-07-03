
FILENAME = '/etc/passwd'
#FILENAME = input('Podaj nazwę pliku: ')


try:

    with open(FILENAME, 'w') as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print('File does not exists')

except PermissionError:
    print('Brak uprawnien')
