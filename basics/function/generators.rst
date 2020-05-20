.. _Function Generators:

*******************
Function Generators
*******************


Range
=====
.. highlights::
    * optional ``start``, inclusive, default: ``0``
    * required ``stop``, exclusive,
    * optional ``step``, default: ``1``

.. code-block:: python
    :caption: ``range()`` syntax

    range([start], <stop>, [step])

.. code-block:: python
    :caption: ``range()`` definition

    range(0,3)
    # range(0, 3)

    list(range(0,3))
    # [0, 1, 2]

    tuple(range(0,3))
    # (0, 1, 2)

    set(range(0,3))
    # {0, 1, 2}

    frozenset(range(0,3))
    # frozenset({0, 1, 2})

.. code-block:: python

    list(range(4, 11, 2))
    # [4, 6, 8, 10]

.. code-block:: python

    header = ['a', 'b', 'c']
    data = [1, 2, 3]
    result = {}

    for i in range(len(header)):
        key = header[i]
        value = data[i]
        result[key] = value

    print(result)
    # {'a': 1, 'b': 2, 'c': 3}


Zip
===
.. code-block:: python
    :caption: ``zip()`` syntax

    zip(<sequence>, <sequence>, ...)

.. code-block:: python
    :caption: ``zip()`` definition

    header = ['a', 'b', 'c']
    data = [1, 2, 3]

    zip(header, data)
    # <zip object at 0x11cf54b90>

    list(zip(header, data))
    # [('a', 1), ('b', 2), ('c', 3)]

    tuple(zip(header, data))
    # (('a', 1), ('b', 2), ('c', 3))

    set(zip(header, data))
    # {('b', 2), ('a', 1), ('c', 3)}

    frozenset(zip(header, data))
    # frozenset({('b', 2), ('a', 1), ('c', 3)})

    dict(zip(header, data))
    # {'a': 1, 'b': 2, 'c': 3}

.. code-block:: python
    :caption: ``zip()`` adjust to shortest sequence

    header = ['a', 'b', 'c']
    data = [1, 2, 3, 4, 5, 6]

    result = zip(header, data)

    print(list(result))
    # [('a', 1), ('b', 2), ('c', 3)]

.. code-block:: python
    :caption: ``zip()`` examples

    header = ['a', 'b', 'c']
    data = [1, 2, 3]
    row = [77, 88, 99]

    result = [(h,d,r) for h,d,r in zip(header, data, row)]

    print(result)
    # [('a', 1, 77), ('b', 2, 88), ('c', 3, 99)]


Enumerate
=========
.. code-block:: python
    :caption: ``enumerate()`` syntax

    enumerate(<sequence>)

.. code-block:: python
    :caption: ``enumerate()`` definition

    header = ['a', 'b', 'c']

    list(enumerate(header))
    # [(0, 'a'), (1, 'b'), (2, 'c')]

    dict(enumerate(header))
    # {0: 'a', 1: 'b', 2: 'c'}

    dict((v,k) for k,v in enumerate(data))
    # {'a': 0, 'b': 1, 'c': 2}

    {v:k for k,v in enumerate(data, start=5)}
    # {'a': 5, 'b': 6, 'c': 7}

.. code-block:: python
    :caption: ``enumerate()`` example

    header = ['a', 'b', 'c']
    data = [1, 2, 3]
    result = {}

    for i, _ in enumerate(header):
        key = header[i]
        value = data[i]
        result[key] = value

    print(result)
    # {'a': 1, 'b': 2, 'c': 3}

.. code-block:: python

    header = ['a', 'b', 'c']
    data = [1, 2, 3]
    result = {}

    for i, header in enumerate(header):
        result[header] = data[i]

    print(result)
    # {'a': 1, 'b': 2, 'c': 3}


Map
===
.. code-block:: python
    :caption: ``map()`` syntax

    map(<callable>, <sequence>)

.. code-block:: python
    :caption: ``map()`` definition

    data = [1, 2, 3]

    map(float, data)
    # <map object at 0x11d15a190>

    list(map(float, data))
    # [1.0, 2.0, 3.0]

    tuple(map(float, data))
    # (1.0, 2.0, 3.0)

    set(map(float, data))
    # {1.0, 2.0, 3.0}

    frozenset(map(float, data))
    # frozenset({1.0, 2.0, 3.0})

.. code-block:: python
    :caption: ``map()`` examples

    def square(x):
        return x ** 2


    data = [1, 2, 3]
    result = map(square, data)

    list(result)
    # [1, 4, 9]


Filter
======
.. code-block:: python
    :caption: ``filter()`` syntax

    filter(<callable>, <sequence>)

.. code-block:: python
    :caption: ``filter()`` example

    def is_even(x):
        if x % 2 == 0:
            return True
        else:
            return False


    data = [1, 2, 3, 4, 5, 6]

    filter(is_even, data)
    # <filter object at 0x11d182990>

    result = filter(is_even, data)
    list(result)
    # [2, 4, 6]

.. code-block:: python

    def is_even(x):
        return x % 2 == 0


    data = [1, 2, 3, 4, 5, 6]
    result = filter(is_even, data)

    list(result)
    # [2, 4, 6]

.. code-block:: python
    :caption: ``filter()`` example


    def adult(person):
        if person['age'] >= 21:
            return True
        else:
            return False


    people = [
        {'age': 21, 'name': 'Jan Twardowski'},
        {'age': 25, 'name': 'Mark Watney'},
        {'age': 18, 'name': 'Melissa Lewis'}]

    result = filter(adult, people)

    print(list(result))
    # [{'age': 21, 'name': 'Jan Twardowski'},
    #  {'age': 25, 'name': 'Mark Watney'}]

.. code-block:: python
    :caption: ``filter()`` example

    def astronaut(person):
        return person['is_astronaut']


    people = [
        {'is_astronaut': False, 'name': 'Jan Twardowski'},
        {'is_astronaut': True, 'name': 'Mark Watney'},
        {'is_astronaut': True, 'name': 'Melissa Lewis'}]

    result = filter(astronaut, people)

    print(list(result))
    # [{'is_astronaut': True, 'name': 'Mark Watney'},
    #  {'is_astronaut': True, 'name': 'Melissa Lewis'}]


Assignments
===========

Function Generator Chain
------------------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/function_generators_chain.py`

:English:
    #. Use generator expression to create ``numbers: List[int]``
    #. In generator use ``range()`` to get numbers from 1 to 33 (inclusive) divisible by 3
    #. Use ``filter()`` to get odd numbers from ``numbers``
    #. Use ``map()`` to cube all numbers in ``numbers``
    #. Create ``result: float`` with arithmetic mean of ``numbers``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj wyrażenia generatorowego do stworzenia ``numbers: List[int]``
    #. W generatorze użyj ``range()`` aby otrzymać liczby od 1 do 33 (włącznie) podzielne przez 3
    #. Użyj ``filter()`` aby otrzymać liczby nieparzyste z ``numbers``
    #. Użyj ``map()`` aby podnieść wszystkie liczby w ``numbers`` do sześcianu
    #. Stwórz ``result: float`` ze średnią arytmetyczną z ``numbers``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: python

        result: float
        # 11502.0

:Hint:
    * ``mean = sum(...) / len(...)``
    * type cast to ``list()`` before calculating mean to expand generator
