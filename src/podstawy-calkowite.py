"""
Zadanie:
    Napisz program, który wczyta od użytkownika liczbę i wyświetli informację, czy jest to liczba całkowita,
    czy niecałkowita.

Podpowiedź:
    Liczba całkowita to taka, której część dziesiętna nie występuje (int) lub jest równa zero float.
"""

def czy_liczba_jest_calkowita(liczba):
    """
    Zwroc uywage, ze ``input()`` zawsze zwraca ``str()`` wiec trzeba rzutowac na int
    Wtedy tracimy informacje czy byl wczesniej float
    Lub wyskakuje exception gdy podano inny typ

    >>> czy_liczba_jest_calkowita(0)
    True
    >>> czy_liczba_jest_calkowita(1)
    True
    >>> czy_liczba_jest_calkowita(-1)
    True
    >>> czy_liczba_jest_calkowita(1.0)
    True
    >>> czy_liczba_jest_calkowita(1.1)
    False
    """
    if liczba == int(liczba):
        return True
    else:
        return False


if __name__ == '__main__':
    liczba_wprowadzona_przez_uzytownika = input('Podaj liczbę: ')
    wynik = czy_liczba_jest_calkowita(liczba=liczba_wprowadzona_przez_uzytownika)
    print(wynik)
