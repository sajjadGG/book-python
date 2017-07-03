.. _Funkcje:

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
        return {'imie': 'Ivan', 'nazwisko': 'Ivanovic'}


Zwracanie typów złożonych
-------------------------

.. code-block:: python

    def foo9():
        return [
            {'imie': 'Max', 'nazwisko': 'Peck'},
            {'imie': 'Ivan', 'nazwisko': 'Ivanovic'},
            {'imie': 'José', 'nazwisko': 'Jiménez'}]

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

.. todo:: zrobić lepsze przykłady wykorzystania parametrów z gwiazdką
.. todo:: zrobić zadania do rozwiązania dla parametrów z gwiazdką

Argumenty ``*args``, ``**kwargs``
---------------------------------

.. code-block:: python

    def foo(a, b, *args, **kwargs):
        print(locals())

Przy wywołaniu funkcji
----------------------

.. code-block:: python

    >>> foo(1, 2, **{'napiecie':10, 'natezenie': 20, 'moc': 3})

    # jest równoważne z:

    >>> foo(1, 2, napiecie=10, natezenie=20, moc=3)

.. code-block:: python

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
        first_name = 'Max'
        last_name = 'Peck'

        def __str__(self):
            return '{first_name} {last_name}'.format(**self.__dict__)

.. code-block:: python

    def create_or_update():
        return True, [
            {'id': 1, 'imie': 'Ivan', 'nazwisko': 'Ivanovic'},
            {'id': 2, 'imie': 'José', 'nazwisko': 'Jiménez'},
        ], 10, str('asd')


    czy_utworzone, *args  = create_or_update()

    print(czy_utworzone)


Zadania kontrolne
=================

Konwersja liczby na zapis słowny
--------------------------------
Napisz program ``numer.py``, który zamieni wprowadzony przez użytkownika ciąg cyfr na formę tekstową:

* znaki nie będące cyframi mają być ignorowane
* konwertujemy cyfry, nie liczby, a zatem:

  * 911 to "dziewięć jeden jeden"
  * 1100 to "jeden jeden zero zero"

* Napisz testy sprawdzające przypadki brzegowe.

.. code-block:: python

    >>> int_to_str(999)
    'dziewiećset dziewięćdziesiąt dziewięć'
    >>> int_to_str(127.32)
    'sto dwadzieścia siedem i trzydzieści dwa setne'

:Zakres:
    * 6 cyfr przed przecinkiem
    * 5 cyfr po przecinku


Rzymskie
--------
:Zadanie 1:
    Napisz program, który przeliczy wprowadzoną liczbę rzymską na jej postać dziesiętną.

:Zadanie 2:
    Zrób drugą funkcję, która dokona procesu odwrotnego.

