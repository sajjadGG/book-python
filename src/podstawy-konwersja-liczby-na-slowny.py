#!/usr/bin/env python3

LICZBY = {
    1: 'jeden',
    2: 'dwa',
    3: 'trzy',
    4: 'cztery',
    5: 'pięć',
    6: 'sześć',
    7: 'siedem',
    8: 'osiem',
    9: 'dziewięć',
}

# ``input()`` zwraca stringa, symulujemy zachowanie funkcji uzywając ``str()``
liczba_uzytkownika = str('911')


for cyfra in liczba_uzytkownika:
    # indeksy w LICZBA są typu ``int``
    # my iterujemy po ``str`` i cyfra jest typu ``str``
    # rzutujemy cyfrę na ``int`` aby móc odnaleźć ją w LICZBY
    index = int(cyfra)
    print(LICZBY[index])


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
        cyfra = int(cyfra)
        slownie.append(LICZBY[cyfra])

    return ' '.join(slownie)


if __name__ == '__main__':
    liczba_wprowadzona = input('Podaj liczbę: ')
    napis = liczba_slownie(liczba_wprowadzona)
    print(napis)
