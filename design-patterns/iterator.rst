.. _Iterators:

*********
Iterators
*********


What is iterator?
=================
* ``__iter__()``
* ``__next__() -> raise StopIteration``


Iterowanie po obiektach
=======================

Iterowanie po ``str``
---------------------
.. code-block:: python

    for character in 'hello':
        print(character)

    # h
    # e
    # l
    # l
    # o


Iterowanie po ``list()``, ``dict()``, ``set()``, ``tuple()``
------------------------------------------------------------
.. code-block:: python

    for liczba in [1, 2, 3, 4]:
        print(liczba)

.. code-block:: python

    for key, value in [('a',1), ('b',2), ('c',3)]:
        print(f'{key} -> {value}')

    # a -> 1
    # b -> 2
    # c -> 3

.. code-block:: python

    my_dict = {'a': 1, 'b': 2, 'c': 3}

    for key in my_dict:
        value = my_dict.get(key)
        print(value)

    # 1
    # 2
    # 3


    for key, value in my_dict.items():
        print(f'{key} -> {value}')

    # a -> 1
    # b -> 2
    # c -> 3


Własny iterator
===============
.. code-block:: python

    class Parking:
        def __init__(self):
            self.zaparkowane_samochody = []
            self.index = 0

        def zaparkuj(self, samochod):
            self.zaparkowane_samochody.append(samochod)

        def __iter__(self):
            self.index = 0
            return self

        def __next__(self):
            if self.index >= len(self.zaparkowane_samochody):
                raise StopIteration

            samochod = self.zaparkowane_samochody[self.index]
            self.index += 1
            return samochod


    parking = Parking()
    parking.zaparkuj('Mercedes')
    parking.zaparkuj('Maluch')
    parking.zaparkuj('Toyota')


    for samochod in parking:
        print(samochod)


``itertools``
=============

``chain()``
-----------
.. code-block:: python

    from itertools import chain


    class Numbers:
        def __init__(self, *values):
            self.values = values
            self._iter_index = 0

        def __iter__(self):
            self._iter_index = 0
            return self

        def __next__(self):
            if self._iter_index >= len(self.values):
                raise StopIteration

            element = self.values[self._iter_index]
            self._iter_index += 1
            return element


    class Characters:
        def __init__(self, *values):
            self.values = values
            self._iter_index = 0

        def __iter__(self):
            self._iter_index = 0
            return self

        def __next__(self):
            if self._iter_index >= len(self.values):
                raise StopIteration

            element = self.values[self._iter_index]
            self._iter_index += 1
            return element


    num = Numbers(1, 2, 3)
    chr = Characters('a', 'b', 'c')

    print(chain(num, chr))
    # <itertools.chain object at 0x1008ca0f0>

    print(list(chain(num, chr)))
    # [1, 2, 3, 'a', 'b', 'c']

    for x in chain(num, chr):
        print(x)

    # 1
    # 2
    # 3
    # a
    # b
    # c

``cycle()``
-----------
.. code-block:: python

    from itertools import cycle

    DATA = ['even', 'odd']

    for x in cycle(DATA):
        print(x)

    # even
    # odd
    # even
    # odd
    # even
    # [...]


Przykład
========

.. code-block:: python

    def parzyste_f4():
        for x in range(0, 30):
            if x % 2 == 0:
                yield float(x)


    print(parzyste_f4())
    a = parzyste_f4()

    try:
        print('next1', a.__next__())
        print('next2', a.__next__())
        print('next3', a.__next__())
        print('next4', a.__next__())
    except StopIteration:
        pass


    for liczba in parzyste_f4():
        print(liczba)


Assignments
===========

Range
-----
* Filename: ``design-patterns/iterator_range.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min

#. Zaimplementuj własne rozwiązanie ``range()`` wykorzystując iterator.
#. Początek, koniec, krok (step)

Książka adresowa
----------------
* Filename: ``design-patterns/iterator_addressbook.py``
* Lines of code to write: 20 lines
* Estimated time of completion: 15 min
* Input data: :numref:`listing-iterators-ksiazka-adresowa`

#. spraw aby można było iterować w książce adresowej z poprzednich zadań po adresach użytkownika.

.. literalinclude:: src/iterators-ksiazka-adresowa.py
    :name: listing-iterators-ksiazka-adresowa
    :language: python
    :caption: Struktury danych książki adresowej
