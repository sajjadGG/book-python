#!/usr/bin/env python3

DANE = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'


def pierwsze_trzy_litery(text):
    """
    >>> pierwsze_trzy_litery(DANE)
    'Lor'
    >>> pierwsze_trzy_litery('Sages')
    'Sag'
    """
    return text[0:3]


def ostatnie_trzy_litery(text):
    """
    >>> ostatnie_trzy_litery('Sages')
    'ges'
    >>> ostatnie_trzy_litery('Przerwa')
    'rwa'
    """
    return text[-3:]


if __name__ == '__main__':
    import doctest
    doctest.testmod()


    # pierwsze_trzy_litery(DANE)
