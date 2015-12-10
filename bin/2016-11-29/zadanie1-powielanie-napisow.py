#!/usr/bin/env python3

"""
Zadanie 1:
Napisz program, który wczyta od użytkownika pewien napis,
a następnie wyświetli 30 kopii tego napisu, każda w osobnej linii.

Zadanie 2:
Napisz trzy wersje tego programu:

- wykorzystując range()
- wykorzystując pętlę while
- wykorzystując właściwości mnożenia stringów

Zadanie 3:
- Napisz doctest do takiej funkcji.

Podpowiedź:
- print('ciag znakow' * 30)
"""

ILOSC_WYSWIETLEN = 5

def print1(napis):
    """
    >>> print1('asd')
    asd
    asd
    asd
    asd
    asd
    """
    for i in range(ILOSC_WYSWIETLEN):
        print(napis)


def print2(napis):
    """
    >>> print2('asd')
    asd
    asd
    asd
    asd
    asd
    """
    i = 0
    while i < ILOSC_WYSWIETLEN:
        print(napis)
        i += 1


def print3(napis):
    """
    >>> print3('asd')
    asd
    asd
    asd
    asd
    asd
    <BLANKLINE>
    """
    print((napis+'\n') * ILOSC_WYSWIETLEN)


def print4(napis):
    """
    >>> print4('asd')
    asd
    asd
    asd
    asd
    asd
    """
    output = [napis] * ILOSC_WYSWIETLEN
    output = '\n'.join(output)
    print(output)



if __name__ == '__main__':
    napis = input('Wprowadz ciag znakow: ')
    #print1(napis)
    #print2(napis)
    #print3(napis)
    #print4(napis)