temperature = input('Type temperature: ')

try:
    temperature = float(temperature)
except ValueError:
    print('Invalid temperature')


class NegativeKelvinError(Exception):
    pass


if temperature < 0:
    raise NegativeKelvinError
