
"""
Zadanie:
    Napisz program, który wczyta od użytkownika liczbę i wyświetli informację, czy jest to liczba całkowita,
    czy niecałkowita.

Podpowiedź:
    Liczba całkowita to taka, której część dziesiętna nie występuje (int) lub jest równa zero float.
"""

def calkowita(liczba):
    """
    >>> calkowita(1)
    True
    >>> calkowita(0)
    True
    >>> calkowita(-1)
    True
    >>> calkowita(1.5)
    False
    >>> calkowita(1.0)
    True
    """
    if isinstance(liczba, (int, float)) and int(liczba) == liczba:
        return True
    else:
        return False