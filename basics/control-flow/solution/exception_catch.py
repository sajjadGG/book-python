temperature = input('Type temperature: ')

try:
    temperature = float(temperature)
    print(temperature)
except ValueError:
    print('Invalid temperature')

