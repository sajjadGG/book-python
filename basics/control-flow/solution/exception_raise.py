age = input('Type age: ')
age = float(age)

if age >= 18:
    raise PermissionError('Only for kids')
