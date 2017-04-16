Programowanie funkcyjne
=======================

lambda
------

.. code-block:: python

    def czy_parzysta(x):
        if x % 2 == 0:
            return True
        else:
            return False

    parzyste = filter(czy_parzysta, liczby)


    foo = lambda x: x*x
    print(foo(10))

    liczby = [1, 2, 3, 4]
    parzyste = filter(lambda x: x % 2 == 0, liczby)



closure
-------

.. code-block:: python

    def f(x):
        def g(y):
            return x + y
        return g


złożenia funkcji
----------------

``map()``
---------

.. code-block:: python

    lista = [1, 2, 3]

    def inkrementuj(y):
        return 1 + y

    map(inkrementuj, lista)
    map(lambda y: 1 + y, l)


.. code-block:: python

    def kwadrat(x):
        return pow(x, 2)

    potegi1 = map(kwadrat, dane)
    potegi2 = map(lambda x: pow(x, 2), dane)

    print(list(potegi1))

.. code-block:: python

    import datetime

    def opoznienie(przesuniecie):
        delay = pow(przesuniecie, 2)
        return datetime.datetime.now() + datetime.timedelta(seconds=delay)

    czasy = map(opoznienie, dane)

    print(list(czasy))



``zip()``
---------

.. code-block:: python

    >>> x = [1, 2, 3]
    >>> y = [4, 5, 6]
    >>> zipped = zip(x, y)
    >>> list(zipped)
    [(1, 4), (2, 5), (3, 6)]

.. code-block:: python

    >>> # unzip
    >>> x2, y2 = zip(*zip(x, y))
    >>> x == list(x2) and y == list(y2)
    True

``filter()``
------------

.. code-block:: python

    OSOBY = [
        {'imie': 'Matt', 'wiek': 10},
        {'imie': 'Angelika', 'wiek': 18},
        {'imie': 'Mateusz', 'wiek': 21},
        {'imie': 'Tadeusz', 'wiek': 35},
    ]

    def osoba_pelnoletnia(osoba):
        if osoba['wiek'] >= 18:
            return True
        else:
            return False


    dorosli = filter(osoba_pelnoletnia, OSOBY)
    print(list(dorosli))


.. code-block:: python

    def parzysta(liczba):
        if liczba % 2 == 0:
            return True
        else:
            return False


    dane = range(0, 30)

    parzyste1 = filter(parzysta, dane)
    parzyste2 = filter(lambda x: x % 2 == 0, dane)
    parzyste3 = filter(lambda x: not x % 2, dane)

    print(list(parzyste3))


``all()``
---------

``any()``
---------
