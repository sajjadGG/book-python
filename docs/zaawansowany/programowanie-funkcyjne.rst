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

decorator
---------

* Modify arguments
* Modify returned value
* Do things before call
* Do things after call
* Avoid calling
* Modify global state
* Metadata

.. code-block:: python

    def my_decorator(f):
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return wrapper

    # usage

    @my_decorator
    def func(x):
        return x

.. code-block:: python

    import os
    import logging


    def if_file_exists(function):

        def check(filename):
            if os.path.exists(filename):
                function(filename)
            else:
                logging.error('File "%(filename)s" does not exists, will not execute!', locals())

        return check


    @if_file_exists
    def print_file(filename):
        with open(filename) as file:
            content = file.read()
            print(content)


    if __name__ == '__main__':
        print_file('/etc/passwd')
        print_file('/tmp/passwd')


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



``all()``
---------

``any()``
---------
