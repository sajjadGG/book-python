*********
Iteratory
*********

Czym jest iterator?
===================

* ``__iter__()``
* ``__next__()``
* ``raise StopIteration``

Iterowanie po obiektach
=======================

Iterowanie po stringu
---------------------

.. code-block:: python

    for znak in 'python':
        print(znak)


Iterowanie po ``list()``, ``dict()``, ``set()``, ``tuple()``
------------------------------------------------------------

.. code-block:: python

    for liczba in [1, 2, 3, 4]:
        print(liczba)

.. code-block:: python

    for key, value in [(0, 0), (1, 1), (1, 2)]:
        print('%s -> %s' % (key, value))

.. code-block:: python

    slownik = {'x': 1, 'y': 2}

    for key in slownik:
        print(slownik.get(key))

    for key, value in slownik.items():
        print(key, value)

Własny iterator
===============

.. code-block:: python

    class ListaFigurGeometrycznych:
        lista = []
        aktualny_elemtent = 0

        def __iter__(self):
            return self

        def push(self, figura):
            self.lista.append(figura)

        def __next__(self):
            try:
                element = self.lista[self.aktualny_elemtent]
                self.aktualny_elemtent += 1
                return element
            except IndexError:
                raise StopIteration


    figury = ListaFigurGeometrycznych()

    figury.push('kwadrat')
    figury.push('prostokat')
    figury.push('trojkat')


    for figura in figury:
        print(figura)


``itertools``
=============

Przykład
========

.. code-block:: python

    def parzyste_f4():
        for x in range(0, 30):
            if x % 2 == 0:
                yield float(x)


    print(parzyste_f4())
    a = parzyste_f4()

    print('next1', a.__next__())
    print('next2', a.__next__())
    print('next3', a.__next__())
    print('next4', a.__next__())


    for liczba in parzyste_f4():
        print(liczba)

Zadania kontrolne
=================

Range
-----
#. Zaimplementuj własne rozwiązanie ``range()`` wykorzystując iterator.
#. Początek, koniec, krok (step)

Książka adresowa
----------------
#. spraw aby można było iterować w książce adresowej z poprzednich zadań po adresach użytkownika.
