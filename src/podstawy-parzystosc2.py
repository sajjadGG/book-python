#!/usr/bin/env python3
from typing import Union


def is_even_number(liczba: Union[int, float]) -> bool:
    """
    >>> is_even_number(1)
    False
    >>> is_even_number(2)
    True
    >>> is_even_number(1.5)
    False
    >>> is_even_number(0)
    True
    >>> is_even_number(-1)
    False
    >>> is_even_number(-2)
    True
    >>> is_even_number([2, 4, 6, 8])
    Traceback (most recent call last):
    ...
    TypeError
    >>> is_even_number('two')
    Traceback (most recent call last):
    ...
    TypeError
    >>> is_even_number('2')
    Traceback (most recent call last):
    ...
    TypeError
    """
    if isinstance(liczba, (int, float)):
        return liczba % 2 == 0
    else:
        raise TypeError