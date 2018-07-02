#!/usr/bin/env python3
from typing import Union

STEP = 5
MAX = 41
MIN = -20


def celsius_to_fahrenheit(degree: Union[int, float]) -> float:
    """
    Celsius to Fahrenheit: (°C * 1.8) + 32 = °F
    >>> celsius_to_fahrenheit(0)
    32.0
    >>> celsius_to_fahrenheit(1)
    33.8
    >>> celsius_to_fahrenheit(-1)
    30.2
    >>> celsius_to_fahrenheit(100)
    212.0
    >>> celsius_to_fahrenheit([0, 1, 2])
    Traceback (most recent call last):
        ...
    TypeError: can't multiply sequence by non-int of type 'float'
    """
    return degree * 1.8 + 32


for celsius in range(MIN, MAX, STEP):
    fahrenheit = celsius_to_fahrenheit(celsius)

    print(f'Temperatura {celsius:=+8}C to {fahrenheit:_^+10.0f}F')
