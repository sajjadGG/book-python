def celsius_to_fahrenheit(stopnie):
    return (stopnie * 1.8) + 32


def fahrenheit_to_celsius(stopnie):
    return (stopnie - 32) / 1.8


for temp in range(-20, 40, 5):
    print('Temperatura {celsius}C to {fahrenheit}F'.format(
        celsius=temp,
        fahrenheit=celsius_to_fahrenheit(temp)
    ))