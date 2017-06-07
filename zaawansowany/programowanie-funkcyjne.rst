***********************
Programowanie funkcyjne
***********************

lambda
======

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



Closure
=======

.. code-block:: python

    def f(x):
        def g(y):
            return x + y
        return g

Monady
======

złożenia funkcji
================

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


``all(iterable)``
-----------------

Return True if all elements of the iterable are true (or if the iterable is empty). Equivalent to:

.. code-block:: python

    def all(iterable):
        for element in iterable:
            if not element:
                return False
        return True

``any(iterable)``
-----------------

Return True if any element of the iterable is true. If the iterable is empty, return False. Equivalent to:

.. code-block:: python

    def any(iterable):
        for element in iterable:
            if element:
                return True
        return False

``enumerate(iterable, start=0)``
--------------------------------
Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration. The __next__() method of the iterator returned by enumerate() returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating over iterable.

.. code-block:: python

    >>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    >>> list(enumerate(seasons))
    [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
    >>> list(enumerate(seasons, start=1))
    [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

Equivalent to:

.. code-block:: python

    def enumerate(sequence, start=0):
        n = start
        for elem in sequence:
            yield n, elem
            n += 1


``functools``
=============


``memoize``
-----------

.. code-block:: python

    import functools

    @functools.lru_cache(maxsize=None)
    def fib(num):
        if num < 2:
            return num
        else:
            return fib(num-1) + fib(num-2)

.. code-block:: python

    def fact(n):
        if not hasattr(fact, 'mem'):
            fact.mem = {1: 1}
        if not n in fact.mem:
            fact.mem[n] = n * fact(n - 1)
        return fact.mem[n]

.. code-block:: python

    def memoize(function):
        from functools import wraps

        memo = {}

        @wraps(function)
        def wrapper(*args):
            if args in memo:
                return memo[args]
            else:
                rv = function(*args)
                memo[args] = rv
                return rv
        return wrapper


    @memoize
    def fibonacci(n):
        if n < 2: return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    fibonacci(25)

Zadania kontrolne
=================

``map()``, ``filter()`` i ``lambda``
------------------------------------
Używając generatora zbuduj listę zawierającą wszystkie liczby podzielne przez 3 z zakresu od 1 do 33:

* Używając funkcji ``filter()`` usuń z niej wszystkie liczby parzyste
* Używając wyrażenia ``lambda`` i funkcji ``map()`` podnieś wszystkie elementy tak otrzymanej listy do sześcianu
* Odpowiednio używając funkcji ``sum()``  i ``len()`` oblicz średnią arytmetyczną z elementów tak otrzymanej listy.
