.. _Iterators:

*********
Iterators
*********


Protocol
========
* ``__iter__(self) -> self``
* ``__next__(self) -> raise StopIteration``

.. code-block:: python

    class Iterator:
        def __iter__(self):
            self._iter_index = 0
            return self

        def __next__(self):
            if self._iter_index >= len(self.values):
                raise StopIteration

            element = self.values[self._iter_index]
            self._iter_index += 1
            return element


Mechanism
=========
.. code-block:: python
    :caption: For loop

    DATA = [1, 2, 3]

    for current in DATA:
        print(current)

.. code-block:: python
    :caption: Intuitive implementation of the ``for`` loop

    DATA = [1, 2, 3]

    iterator = iter(DATA)

    try:

        current = next(iterator)
        print(current)

        current = next(iterator)
        print(current)

        current = next(iterator)
        print(current)

        current = next(iterator)
        print(current)

    except StopIteration:
        pass

.. code-block:: python
    :caption: Intuitive implementation of the ``for`` loop

    DATA = [1, 2, 3]

    iterator = DATA.__iter__()

    try:

        current = iterator.__next__()
        print(current)

        current = iterator.__next__()
        print(current)

        current = iterator.__next__()
        print(current)

        current = iterator.__next__()
        print(current)

    except StopIteration:
        pass


Built-in Type Iteration
=======================
.. code-block:: python
    :caption: Iterating ``str``

    for character in 'hello':
        print(character)

    # h
    # e
    # l
    # l
    # o

.. code-block:: python
    :caption: Iterating sequences

    for number in [1, 2, 3]:
        print(number)

    # 1
    # 2
    # 3

.. code-block:: python
    :caption: Iterating nested sequences

    for key, value in [('a',1), ('b',2), ('c',3)]:
        print(f'{key} -> {value}')

    # a -> 1
    # b -> 2
    # c -> 3

.. code-block:: python
    :caption: Iterating ``dict``

    DATA = {'a': 1, 'b': 2, 'c': 3}

    for element in DATA:
        print(element)

    # a
    # b
    # c

.. code-block:: python
    :caption: Iterating ``dict``

    for key, value in DATA.items():
        print(f'{key} -> {value}')

    # a -> 1
    # b -> 2
    # c -> 3


Implementation
==============
.. code-block:: python
    :caption: Iterator implementation

    class Parking:
        def __init__(self):
            self._parked_cars = list()

        def park(self, car):
            self._parked_cars.append(car)

        def __iter__(self):
            self._iter_index = 0
            return self

        def __next__(self):
            if self._iter_index >= len(self._parked_cars):
                raise StopIteration

            element = self._parked_cars[self._iter_index]
            self._iter_index += 1
            return element


    parking = Parking()
    parking.park('Mercedes')
    parking.park('Maluch')
    parking.park('Toyota')

    for car in parking:
        print(car)


    # Mercedes
    # Maluch
    # Toyota


Standard Library Itertools
==========================
* ``import itertools``

.. code-block:: python
    :caption: ``itertools.chain()``

    keys = ['a', 'b', 'c']
    values = [1, 2, 3]

    for x in chain(keys, values):
        print(x)

    # a
    # b
    # c
    # 1
    # 2
    # 3

.. code-block:: python
    :caption: ``itertools.chain()``

    from itertools import chain


    class Iterator:
        def __iter__(self):
            self._iter_index = 0
            return self

        def __next__(self):
            if self._iter_index >= len(self.values):
                raise StopIteration

            element = self.values[self._iter_index]
            self._iter_index += 1
            return element


    class Character(Iterator):
        def __init__(self, *values):
            self.values = values


    class Number(Iterator):
        def __init__(self, *values):
            self.values = values


    chars = Character('a', 'b', 'c')
    nums = Number(1, 2, 3)

    print(chain(chars, nums))
    # <itertools.chain object at 0x116166970>

    print(list(chain(chars, nums)))
    # [1, 2, 3, 'a', 'b', 'c']

    for x in chain(chars, nums):
        print(x)

    # a
    # b
    # c
    # 1
    # 2
    # 3

.. code-block:: python
    :caption: ``itertools.cycle()``

    from itertools import cycle

    DATA = ['even', 'odd']

    for x in cycle(DATA):
        print(x)

    # even
    # odd
    # even
    # odd
    # even
    # ...

.. code-block:: python
    :caption: ``itertools.cycle()``

    from itertools import cycle

    DATA = ['even', 'odd']

    for i, status in enumerate(cycle(DATA)):
        print(i, status)

        if i == 3:
            break

    # 0, even
    # 1, odd
    # 2, even
    # 3, odd


Assignments
===========

Protocol Iterator Implementation
--------------------------------
* Complexity level: easy
* Lines of code to write: 9 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/protocol_iterator_implementation.py`

:English:
    #. Use data from "Input" section (see below)
    #. Modify classes to implement iterator
    #. Iterate over object using ``for`` loop
    #. Print data
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj data z sekcji "Input" (patrz poniżej)
    #. Zmodyfikuj klasy aby zaimplementować protokół iterator
    #. Iteruj po obiekcie używając pętli ``for``
    #. Wypisz dane
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        from dataclasses import dataclass


        @dataclass
        class Astronaut:
            first_name: str
            last_name: str
            missions: tuple = ()

        @dataclass
        class Mission:
            year: int
            name: str


        twardowski = Astronaut('Jan', 'Twardowski', missions=(
            Mission(1969, 'Apollo 11'),
            Mission(2024, 'Artemis 3'),
            Mission(2035, 'Ares 3'),
        ))

:Output:
    .. code-block:: python

        Mission(year=1969, name='Apollo 11')
        Mission(year=2024, name='Artemis 3')
        Mission(year=2035, name='Ares 3')

Protocol Iterator Range
-----------------------
* Complexity level: medium
* Lines of code to write: 25 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/protocol_iterator_range.py`

:English:
    #. Use code from "Input" section (see below)
    #. Write own implementation of a ``range()`` function
    #. Use iterator protocol
    #. Arguments: start, stop, step
    #. How to implement passing only stop argument?

:Polish:
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Zaimplementuj własne rozwiązanie ``range()``
    #. Use iterator protocol
    #. Argumenty: początek, koniec, krok
    #. Jak zaimplementować możliwość podawania tylko końca?

:Input:
    .. code-block:: python

        class Range:
            """
            >>> list(Range(0, 10, 2))
            [0, 2, 4, 6, 8]

            >>> list(Range(0, 5))
            [0, 1, 2, 3, 4]

            >>> list(Range(5))
            [0, 1, 2, 3, 4]

            >>> list(Range())
            Traceback (most recent call last):
              ...
            ValueError: Invalid arguments

            >>> list(Range(1,2,3,4))
            Traceback (most recent call last):
              ...
            ValueError: Invalid arguments
            """
