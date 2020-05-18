filename = input('Type filename: ')

try:
    with open(filename) as file:
        print(file.read())

except FileNotFoundError:
    print('Sorry, file not found')

except PermissionError:
    print('Sorry, not permitted')
