#!/usr/bin/env python3

"""
1. Liczba parzysta to liczba podzielna przez 2 bez reszty

-> parzysta: liczba % 2 == 0
-> nieparzysta: cos innego

sprawdzanie w IF:
    0 => False
    0.0 => False
    None => False
    '' => False
    [] => False
    {} => False
    () => False

"""


def jest_parzysta(liczba):
    """
    >>> jest_parzysta(10)
    True
    >>> jest_parzysta(11)
    False
    >>> jest_parzysta(0)
    True
    >>> jest_parzysta(-2)
    True
    >>> jest_parzysta(-1)
    False
    >>> jest_parzysta(1.0)
    False
    >>> jest_parzysta(2.0)
    True
    >>> jest_parzysta(2.1)
    False
    >>> jest_parzysta(2.2)
    False
    >>> jest_parzysta('%six')
    False
    >>> jest_parzysta([2][0])
    True
    >>> jest_parzysta([2, 4, 6] + [1])

    """
    # >>> jest_parzysta([2])
    # >>> jest_parzysta('six')
    # False
    # >>> jest_parzysta('')
    # False

    if not liczba % 2:
        return True
    else:
        return False


if jest_parzysta(10):
    print('tak')
else:
    print('nie')
