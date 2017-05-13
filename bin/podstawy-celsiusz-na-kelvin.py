#!/usr/bin/env python3

MINIMALNA_TEMPERATURA = -273.15


def przelicz_celsius_na_kelvin(temperatura):
    """
    >>> przelicz_celsius_na_kelvin(1)
    274.15

    >>> przelicz_celsius_na_kelvin(0)
    273.15

    >>> przelicz_celsius_na_kelvin(-300)
    Traceback (most recent call last):
        ...
    ValueError: Nie może być mniejsze niż minimalna temperatura

    >>> przelicz_celsius_na_kelvin('jeden')
    Traceback (most recent call last):
        ...
    ValueError: Temperatura musi być float

    >>> przelicz_celsius_na_kelvin([1.0, 1, 0])
    Traceback (most recent call last):
        ...
    TypeError: Nie obsługiwany typ argumentu
    """

    try:
        temperatura = float(temperatura)
    except ValueError:
        raise ValueError('Temperatura musi być float')
    except TypeError:
        raise TypeError('Nie obsługiwany typ argumentu')

    if temperatura < MINIMALNA_TEMPERATURA:
        raise ValueError('Nie może być mniejsze niż minimalna temperatura')
    else:
        return temperatura - MINIMALNA_TEMPERATURA
