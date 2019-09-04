.. _Iterators:

*********
Iterators
*********


Protocol
========
* ``__iter__()``
* ``__next__() -> raise StopIteration``


Iterating over objects
======================

Iterating sequences
-------------------
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

Iterating over ``str``
---------------------
.. code-block:: python

    for character in 'hello':
        print(character)

    # h
    # e
    # l
    # l
    # o


Own Implementation
==================
.. code-block:: python

    class Parking:
        def __init__(self):
            self._parked_cars = list()

        def park(self, car):
            self._parked_cars.append(car)

        def __iter__(self):
            self._current_element = 0
            return self

        def __next__(self):
            if self._current_element >= len(self._parked_cars):
                raise StopIteration

            result = self._parked_cars[self._current_element]
            self._current_element += 1
            return result


    parking = Parking()
    parking.park('Mercedes')
    parking.park('Maluch')
    parking.park('Toyota')


    for car in parking:
        print(car)

    # Mercedes
    # Maluch
    # Toyota


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
    # ...

.. code-block:: python

    from itertools import cycle

    DATA = ['even', 'odd']

    for i, status in enumerate(cycle(DATA)):
        print(i, status)

    # 0, even
    # 1, odd
    # 2, even
    # ...

Example
=======
.. code-block:: python

    def parzyste_f4():
        for x in range(0, 30):
            if x % 2 == 0:
                yield float(x)

    for number in DATA:
        print(number)

    try:

        number = DATA.__next__()
        print(number)

        number = DATA.__next__()
        print(number)

        number = DATA.__next__()
        print(number)

        number = DATA.__next__()
        print(number)

    except StopIteration:
        pass


Assignments
===========

Range
-----
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/iterator_range.py`

:English:
    #. Implement own implementation of a ``range()`` function
    #. Use iterator protocol
    #. Arguments: start, stop, step
    #. How to implement passing only stop argument?

:Polish:
    #. Zaimplementuj własne rozwiązanie ``range()``
    #. Use iterator protocol
    #. Argumenty: początek, koniec, krok
    #. Jak zaimplementować możliwość podawania tylko końca?

Own implementation
------------------
* Complexity level: easy
* Lines of code to write: 20 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/iterator_addressbook.py`

:English:
    #. For input data (see below)
    #. Modify classes to implement iterator

:Polish:
    #. Dla danych wejściowych (patrz poniżej)
    #. Zmodyfikuj klasy aby zaimplementować protokół iterator

:Input:
    .. code-block:: python
        :name: listing-iterators-ksiazka-adresowa
        :caption: Struktury danych książki adresowej

        from dataclasses import dataclass


        @dataclass
        class Contact:
            first_name: str
            last_name: str
            addresses: tuple = ()

        @dataclass
        class Address:
            center: str
            location: str


        DATA = Contact(first_name='Jan', last_name='Twardowski', addresses=(
            Address(center='Johnson Space Center', location='Houston, TX'),
            Address(center='Kennedy Space Center', location='Merritt Island, FL'),
            Address(center='Jet Propulsion Laboratory', location='Pasadena, CA'),
        ))

        for address in DATA:
            print(address)

        # Address(building='Johnson Space Center', location='Houston, TX')
        # Address(building='Kennedy Space Center', location='FL')
        # Address(building='Jet Propulsion Laboratory', location='Pasadena, CA')
