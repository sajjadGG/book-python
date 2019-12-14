temperature = input('Type temperature: ')

try:
    temperature = float(temperature)
except ValueError:
    print('Invalid temperature')


print(temperature)
