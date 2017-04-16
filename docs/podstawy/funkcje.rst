*******
Funkcje
*******

Definiowanie funkcji
====================

.. code-block:: python

    def hello():
        print('hello world')

Konwencja nazewnicza funkcji
============================

* CamelCase? Nie?! Używanie ``_`` w nazwach
* Funkcje o nazwie zaczynającej się od ``_`` przez konwencję są traktowane jako prywatne (w Pythonie nie ma private/protected/public).
* Funkcje o nazwie zaczynającej się od ``__`` i kończących się na ``__`` przez konwencję są traktowane jako systemowe.
* Nazwy opisowe funkcji

Argumenty do funkcji
====================

.. code-block:: python

    >>> def dodaj(a, b):
    ...    return a + b

    >>> dodaj(1, 2)
    3


Argumenty nazwane
-----------------

.. code-block:: python

    >>> def dodaj(a, b):
    ...    return a + b

    >>> dodaj(a=1, b=2)
    3

Argumenty z wartością domyślną
------------------------------

.. code-block:: python

    >>> def hello(tekst='hello world'):
    ...     print(tekst)

    >>> hello(tekst='ehlo')
    ehlo

    >>> hello()
    hello world

Zwracanie wartości
==================

Zwracanie wartości prostych
---------------------------

.. code-block:: python

    def foo1():
        return True

    def foo2():
        return None

    def foo3():
        return 'bar'

    def foo4():
        return [10, 20]

    def foo5():
        return foo1

    def foo6():
        pass

    def foo7():
        return 10, 20, 30, 5, 'a'

    def foo8():
        return {'imie': 'Matt', 'nazwisko': 'Harasymczuk'}


Zwracanie typów złożonych
-------------------------

.. code-block:: python

    def foo9():
        return [
            {'imie': 'Matt', 'nazwisko': 'Harasymczuk'},
            {'imie': 'Matt', 'nazwisko': 'Harasymczuk'},
            {'imie': 'Matt', 'nazwisko': 'Harasymczuk'}]

Rozpakowywanie wartości zwracanych
----------------------------------

.. code-block:: python

    >>> napiece, natezenie, *args = foo7()
    >>> napiecie, *_ = foo7()

.. code-block:: python

    >>> value, _ = function()
    >>> value, *args = function()


Operator ``*`` i ``**``
=======================


Argumenty ``*args``, ``**kwargs``
---------------------------------

.. code-block:: python

    def foo(a, b, *args, **kwargs):
        print(locals())

Przy wywołaniu funkcji
----------------------

.. code-block:: python

    foo(1, 2, **{'napiecie':10, 'natezenie': 20, 'moc': 3})

    foo(
        1,
        2,
        napiecie=10,
        natezenie=20,
        moc=3)


    def bar():
        return range(0, 5)

    jeden, dwa, *reszta = bar()

    print(jeden, dwa, reszta)


    def foobar(a, b, *args):
        print(locals())

    foobar(1, 2, 5, 7)


    def foobar(a, b, **kwargs):
        print(locals())

    foobar(1, 2, 5, 7)


Przykładowe zastosowanie
------------------------

.. code-block:: python

    class Osoba:
        first_name = 'Matt'
        last_name = 'Harasymczuk'

        def __str__(self):
            return '{first_name} {last_name}'.format(**self.__dict__)

.. code-block:: python

    def create_or_update():
        return True, [
            {'id': 1, 'imie': 'matt', 'nazwisko': 'harasymczuk'},
            {'id': 2, 'imie': 'matt', 'nazwisko': 'asd'},
        ], 10, str('asd')


    czy_utworzone, *args  = create_or_update()

    print(czy_utworzone)


Lambda - funkcje anonimowe
==========================

.. code-block:: python

    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


    def parzystosc(x):
        if x % 2 == 0:
            return True
        else:
            return False


    parzyste1 = filter(lambda x: x % 2 == 0, lista)
    parzyste2 = filter(parzystosc, lista)

    print(list(parzyste1))
    print(list(parzyste2))
