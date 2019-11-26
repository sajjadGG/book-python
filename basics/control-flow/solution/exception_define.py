temperature = input('Type temperature: ')
temperature = float(temperature)


class NegativeKelvinError(Exception):
    pass


if temperature < 0:
    raise NegativeKelvinError
