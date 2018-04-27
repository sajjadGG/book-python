#!/usr/bin/env python3

LICZBY = {
    '1': 'jeden',
    '2': 'dwa',
    '3': 'trzy',
    '4': 'cztery',
    '5': 'pięć',
    '6': 'sześć',
    '7': 'siedem',
    '8': 'osiem',
    '9': 'dziewięć',
}

# liczba_wprowadzona = input('Podaj liczbę: ')
liczba_wprowadzona = str(911)  # ``input`` zawsze zwraca ``str``

for cyfra in liczba_wprowadzona:
    print(LICZBY[cyfra])


# Alternatywnie
def liczba_slownie(liczba: int) -> str:
    """
    >>> liczba_slownie(123)
    'jeden dwa trzy'

    >>> liczba_slownie(456)
    'cztery pięć sześć'
    """
    slownie = []

    for cyfra in str(liczba):
        slownie.append(LICZBY[cyfra])

    return ' '.join(slownie)


if __name__ == '__main__':
    # liczba_wprowadzona = input('Podaj liczbę: ')
    liczba_wprowadzona = str(911)  # ``input`` zawsze zwraca ``str``
    napis = liczba_slownie(liczba_wprowadzona)
    print(napis)
