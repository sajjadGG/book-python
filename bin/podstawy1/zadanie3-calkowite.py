def calkowita(liczba):
    """
    >>> calkowita(1)
    True
    >>> calkowita(2)
    True
    >>> calkowita(0)
    True
    >>> calkowita(-1)
    True
    >>> calkowita(1.5)
    False
    >>> calkowita(2j+1)
    False
    >>> calkowita(1.0)
    True
    """
    if isinstance(liczba, (int, float)) and liczba == int(liczba):
        return True
    else:
        return False
