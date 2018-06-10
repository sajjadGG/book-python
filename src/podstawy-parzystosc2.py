#!/usr/bin/env python3
import logging
from typing import Union

"""
Zadanie:
Napisz program, który wczyta od użytkownika ciąg znaków
i wyświetli informację, czy jest to liczba, czy jest parzysta, czy nieparzysta.

Podpowiedź:
- Liczba parzysta, to taka, która po podzieleniu przez dwa nie ma reszty
- Użyj dzielenia modulo % lub divmod()
- Zwróć uwagę, że operator % działa modulo tylko na int oraz na float.
    Przy str ma zupełnie inne znaczenie.
"""

def czy_lista_ma_tylko_parzyste(lista):
    for liczba in lista:

        if not czy_parzysta(liczba):
            return False

    return True


def czy_parzysta(liczba: int) -> bool:
    """
    >>> czy_parzysta1(1)
    False
    >>> czy_parzysta1(2)
    True
    >>> czy_parzysta1(1.5)
    False
    >>> czy_parzysta1(0)
    True
    >>> czy_parzysta1(-1)
    False
    >>> czy_parzysta1(-2)
    True
    >>> czy_parzysta1([2, 4, 6, 8])
    Traceback (most recent call last):
    ...
    TypeError
    >>> czy_parzysta1('two')
    Traceback (most recent call last):
    ...
    TypeError
    >>> czy_parzysta1('2')
    Traceback (most recent call last):
    ...
    TypeError
    """
    if isinstance(liczba, (int, float)):
        return liczba % 2 == 0
    else:
        logging.error('Podany argument jest nieprawidłowy')
        raise TypeError