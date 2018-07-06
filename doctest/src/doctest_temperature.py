from typing import Union


def fahrenheit_to_kelvin(fahrenheit: Union[int, float]) -> float:
    """
    >>> fahrenheit_to_kelvin(1)
    255.92777777777775
    >>> fahrenheit_to_kelvin(0)
    255.3722222222222
    >>> fahrenheit_to_kelvin(-1)
    254.81666666666663
    >>> fahrenheit_to_kelvin(1.4)
    256.15
    >>> fahrenheit_to_kelvin('one')
    Traceback (most recent call last):
        ...
    ValueError: Invalid argument
    >>> fahrenheit_to_kelvin([1, 2])
    Traceback (most recent call last):
        ...
    ValueError: Invalid argument
    """
    if not isinstance(fahrenheit, (float, int)):
        raise ValueError('Invalid argument')

    celsius = (fahrenheit-32) / 1.8
    kelvin = celsius + 273.15
    return kelvin

