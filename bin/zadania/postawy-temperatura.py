#!/usr/bin/env python3


def celsiusz_na_farenheit(celsiusze):
    """
    Celsius to Fahrenheit: (°C * 1.8) + 32 = °F
    >>> celsiusz_na_farenheit(0)
    32.0
    >>> celsiusz_na_farenheit(1)
    33.8
    >>> celsiusz_na_farenheit(-1)
    30.2
    >>> celsiusz_na_farenheit(100)
    212.0
    """
    return celsiusze * 1.8 + 32


for stopien in range(-20, 41, 5):
    celsiusz = "{0:+5d}".format(stopien)
    farenheit = "{0:+5.0f}".format(celsiusz_na_farenheit(stopien))
    print(celsiusz, farenheit)

