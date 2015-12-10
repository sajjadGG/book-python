"""
Napisz program, który wczyta od użytkownika liczbę całkowitą i wyświetli informację, czy jest to liczba parzysta, czy nieparzysta.
"""


def czy_liczba_jest_parzysta(liczba):
    """
    >>> czy_liczba_jest_parzysta(1)
    Liczba jest nieparzysta
    False
    >>> czy_liczba_jest_parzysta(2)
    Liczba jest parzysta
    True
    >>> czy_liczba_jest_parzysta(0)
    Liczba nie jest parzysta i nie jest nieparzysta
    >>> czy_liczba_jest_parzysta('a')
    Podana liczba nie jest liczbą całkowitą
    >>> czy_liczba_jest_parzysta([])
    Podana liczba nie jest liczbą całkowitą
    >>> czy_liczba_jest_parzysta(-1)
    Liczba jest nieparzysta
    False
    >>> czy_liczba_jest_parzysta(-2)
    Liczba jest parzysta
    True
    >>> czy_liczba_jest_parzysta(1.0)
    Liczba jest nieparzysta
    False
    >>> czy_liczba_jest_parzysta(2.0)
    Liczba jest parzysta
    True
    """
    if not isinstance(liczba, int) and not isinstance(liczba, float):
        print('Podana liczba nie jest liczbą całkowitą')
        return None
    elif liczba == 0:
        print('Liczba nie jest parzysta i nie jest nieparzysta')
        return None
    elif liczba % 2 == 0:
        print('Liczba jest parzysta')
        return True
    else:
        print('Liczba jest nieparzysta')
        return False


if __name__ == '__main__':
    liczba_podana_przez_uzytkownika = int(input('Podaj liczbę całkowitą: '))
    czy_liczba_jest_parzysta(liczba_podana_przez_uzytkownika)
