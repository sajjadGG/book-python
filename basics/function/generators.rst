*******************
Built-in Generators
*******************


``range()``
===========
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
    # range(0,3)

    list(range(0,3))
    # [0, 1, 2]

    tuple([0, 1, 2])
    # (0, 1, 2)

.. code-block:: python
    :caption: ``range()`` examples

    for number in range(4, 11, 2):
        print(number)

    # 4
    # 6
    # 8
    # 10


``zip()``
=========
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

    dict(zip(header, data))
    # {'a': 1, 'b': 2, 'c': 3}

    tuple(zip(header, data))
    # (('a', 1), ('b', 2), ('c', 3))

.. code-block:: python
    :caption: ``zip()`` examples

    header = ['a', 'b', 'c']
    data = [1, 2, 3]
    row = [77,88,99]

    [(k,v,r) for k,v,r in zip(header, data, row)]
    # [('a', 1, 77), ('b', 2, 88), ('c', 3, 99)]


``map()``
=========
.. code-block:: python
    :caption: ``map()`` syntax

    map(<callable>, <sequence>)

.. code-block:: python
    :caption: ``map()`` definition

    data = [1, 2, 3]

    list(map(float, data))
    # [1.0, 2.0, 3.0]

.. code-block:: python
    :caption: ``map()`` examples

    map(float, [1, 2, 3])
    # <map object at 0x11d15a190>

    list(map(float, [1, 2, 3]))
    # [1.0, 2.0, 3.0]

    tuple(map(float, [1, 2, 3]))
    # (1.0, 2.0, 3.0)


``filter()``
============
.. code-block:: python
    :caption: ``filter()`` syntax

    filter(<callable>, <sequence>)

.. code-block:: python
    :caption: ``filter()`` definition

    list(filter(lambda x: x % 2 == 0, data))
    # [2, 4, 6]

.. code-block:: python
    :caption: ``filter()`` example

    DATA = [
        {'name': 'Jan Twardowski', 'age': 21},
        {'name': 'Mark Watney', 'age': 25},
        {'name': 'Melissa Lewis', 'age': 18},
    ]

    def is_adult(person):
        if person['age'] >= 21:
            return True
        else:
            return False


    output = filter(is_adult, DATA)
    print(list(output))
    # [
    #   {'name': 'Jan Twardowski', 'age': 21},
    #   {'name': 'Mark Watney', 'age': 25},
    # ]

.. code-block:: python
    :caption: ``filter()`` example

    data = [1, 2, 3, 4, 5, 6]

    def is_even(x):
        if x % 2 == 0:
            return True
        else:
            return False

    filter(is_even, data)
    # <filter object at 0x11d182990>

    list(filter(is_even, data))
    # [2, 4, 6]


``enumerate()``
===============
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

.. code-block:: python
    :caption: ``enumerate()`` example

    header = ['a', 'b', 'c']
    data = [1, 2, 3]
    output = {}

    for i, _ in enumerate(header):
        key = header[i]
        value = data[i]
        output[key] = value

    print(output)
    # {'a': 1, 'b': 2, 'c': 3}


``all()``
=========
Return True if all elements of the iterable are true (or if the iterable is empty). Equivalent to:

.. code-block:: python

    def all(iterable):
        if not iterable:
            return False

        for element in iterable:
            if not element:
                return False

        return True


``any()``
=========
Return True if any element of the iterable is true. If the iterable is empty, return False. Equivalent to:

.. code-block:: python

    def any(iterable):
        if not iterable:
            return False

        for element in iterable:
            if element:
                return True

        return False


Assignments
===========

Built-in Generators
-------------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 15 min
* Solution: :download:`solution/generators_task.py`

:English:
    #. Using comprehension generate ``output: List[int]`` with numbers from 1 to 33 which are divisible by 3
    #. Filter ``output`` to contain only odd numbers
    #. Cube all numbers in ``output``
    #. Calculate arithmetic mean from ``output``

:Polish:
    #. Używając comprehension wygeneruj ``output: List[int]`` z liczbami z zakresu 1 do 33 podzielnymi przez 3
    #. Przefiltruj ``output`` aby zawierał tylko liczby nieparzyste
    #. Podnieś wszystkie liczby w ``output`` do sześcianu
    #. Oblicz średnią arytmetyczną z ``output``

:Hint:
    * ``mean = sum(...) / len(...)``
