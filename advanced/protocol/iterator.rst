Iterator
========


Rationale
---------
* Used for iterating in a ``for`` loop


Protocol
--------
* ``__iter__(self) -> self``
* ``__next__(self) -> raise StopIteration``
* ``iter(obj)`` -> ``obj.__iter__()``
* ``next(obj)`` -> ``obj.__next__()``

.. code-block:: python

    class Iterator:
        def __iter__(self):
            self._current = 0
            return self

        def __next__(self):
            if self._current >= len(self.values):
                raise StopIteration
            element = self.values[self._current]
            self._current += 1
            return element


Example
-------
.. code-block:: python

    class Crew:
        def __init__(self):
            self.members = list()

        def __iadd__(self, other):
            self.members.append(other)
            return self

        def __iter__(self):
            self._current = 0
            return self

        def __next__(self):
            if self._current >= len(self.members):
                raise StopIteration
            result = self.members[self._current]
            self._current += 1
            return result


    crew = Crew()
    crew += 'Mark Watney'
    crew += 'Jose Jimenez'
    crew += 'Melissa Lewis'

    for member in crew:
        print(member)

    # Mark Watney
    # Jose Jimenez
    # Melissa Lewis


Loop and Iterators
------------------
For loop:

.. code-block:: python

    DATA = [1, 2, 3]

    for current in DATA:
        print(current)

Intuitive implementation of the ``for`` loop:

.. code-block:: python

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

Intuitive implementation of the ``for`` loop:

.. code-block:: python

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
-----------------------
Iterating ``str``:

.. code-block:: python

    for character in 'hello':
        print(character)

    # h
    # e
    # l
    # l
    # o

Iterating sequences:

.. code-block:: python

    for number in [1, 2, 3]:
        print(number)

    # 1
    # 2
    # 3

Iterating ``dict``:

.. code-block:: python

    DATA = {'a': 1, 'b': 2, 'c': 3}

    for element in DATA:
        print(element)

    # a
    # b
    # c

Iterating ``dict``:

.. code-block:: python

    for key, value in DATA.items():
        print(f'{key} -> {value}')

    # a -> 1
    # b -> 2
    # c -> 3

Iterating nested sequences:

.. code-block:: python

    for key, value in [('a',1), ('b',2), ('c',3)]:
        print(f'{key} -> {value}')

    # a -> 1
    # b -> 2
    # c -> 3


Use Cases
---------
Iterator implementation:

.. code-block:: python

    class Parking:
        def __init__(self):
            self._parked_cars = list()

        def park(self, car):
            self._parked_cars.append(car)

        def __iter__(self):
            self._current = 0
            return self

        def __next__(self):
            if self._current >= len(self._parked_cars):
                raise StopIteration
            element = self._parked_cars[self._current]
            self._current += 1
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


Assignments
-----------
.. literalinclude:: assignments/protocol_iterator_a.py
    :caption: :download:`Solution <assignments/protocol_iterator_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/protocol_iterator_b.py
    :caption: :download:`Solution <assignments/protocol_iterator_b.py>`
    :end-before: # Solution
