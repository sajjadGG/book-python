#!/usr/bin/env python3


ILOSC_POWTORZEN = 5


def rozwiazanie_1(ciag_znakow):
    """
    >>> rozwiazanie_1('10')
    10
    10
    10
    10
    10
    >>> rozwiazanie_1('aa')
    aa
    aa
    aa
    aa
    aa
    >>> rozwiazanie_1(10)
    10
    10
    10
    10
    10
    >>> rozwiazanie_1(['aa'])
    ['aa']
    ['aa']
    ['aa']
    ['aa']
    ['aa']
    """
    for i in range(0, ILOSC_POWTORZEN):
        print(ciag_znakow)


def rozwiazanie_2(ciag_znakow):
    i = 0
    while i < ILOSC_POWTORZEN:
        print(ciag_znakow)
        i += 1


def rozwiazanie_3a(ciag_znakow):
    print((ciag_znakow + '\n') * ILOSC_POWTORZEN)


def rozwiazanie_3b(ciag_znakow):
    print('Alternatywnie')
    print('%s\n' % ciag_znakow * ILOSC_POWTORZEN)


def rozwiazanie_3c(ciag_znakow):
    print('Alternatywnie 2')
    tekst = '{napis}\n'.format(napis=ciag_znakow)
    print(tekst * ILOSC_POWTORZEN)


if __name__ == '__main__':
    ciag_znakow = input('Podaj ciag znakow: ')
    rozwiazanie_1(ciag_znakow)
