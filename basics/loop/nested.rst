.. _Loop Nested Sequences:

*********************
Loop Nested Sequences
*********************


Convention
==========
* ``row`` - best for nested loops with sequence inside
* Conventions for rows and columns:

    * ``row`` - row (all elements)
    * ``column`` - current column element from ``row`` sequence
    * ``i`` - row number
    * ``j`` - column number
    * ``x`` - row number
    * ``y`` - column number
    * ``outer`` - for outer loop element
    * ``inner`` - for inner loop element

* Note that ``i`` may interfere with ``i`` used as loop counter


Vector
======
.. highlights::
    * Suggested variable name: ``value``

.. code-block:: python

    DATA = [
        'a',
        'b',
        'c',
    ]

    for obj in DATA:
        print(obj)

    # a
    # b
    # c


List of Pairs
=============
.. highlights::
    * Suggested variable name: ``pair``

.. code-block:: python

    DATA = [
        ('a', 1),
        ('b', 2),
        ('c', 3),
    ]

    for obj in DATA:
        first = obj[0]
        second = obj[1]

        print(first, '->', second)

    # a -> 1
    # b -> 2
    # c -> 3


List of Sequence
================
.. highlights::
    * Suggested variable name: ``row`` or ``line``

.. code-block:: python

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ]

    for obj in DATA:
        sepal_length = obj[0]
        sepal_width = obj[1]
        petal_length = obj[2]
        petal_width = obj[3]
        species = obj[4]

        total = sepal_length + sepal_width + petal_length + petal_width
        print(species, '->', sepal_length)

    # setosa -> 10.2
    # versicolor -> 13.9
    # virginica -> 16.599999999999998

.. code-block:: python

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ]

    for row in DATA:
        features = row[0:4]
        label = row[4]
        print(f'{label} -> {sum(features)}')

    # setosa -> (5.1, 3.5, 1.4, 0.2)
    # versicolor -> (5.7, 2.8, 4.1, 1.3)
    # virginica -> (6.3, 2.9, 5.6, 1.8)


Matrix
======
.. highlights::
    * Suggested variable name: ``row``

.. code-block:: python

    DATA = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    for obj in DATA:
        col1 = obj[0]
        col2 = obj[1]
        col3 = obj[2]

        print(col1, '->', col2, '->', col3)

    # 1 -> 2 -> 3
    # 4 -> 5 -> 6
    # 7 -> 8 -> 9


Mixed
=====
.. highlights::
    * Suggested variable name: ``outer`` and ``inner``

.. code-block:: python
    :caption: Iterating over ``list`` with scalar and vector values - simple loop

    DATA = [('Jan', 'Twardowski'), 'Watney', 42, 13.37, {True, None, False}]

    for obj in DATA:
        print(obj)

    # ('Jan', 'Twardowski')
    # Watney
    # 42
    # 13.37
    # {False, True, None}

.. code-block:: python
    :caption: Iterating over ``list`` with scalar and vector values - nested loop

    DATA = [('Jan', 'Twardowski'), 'Watney', 42, 13.37, {True, None, False}]

    for obj in DATA:
        for inner in obj:
            print(inner)

    # Jan
    # Twardowski
    # W
    # a
    # t
    # n
    # e
    # y
    # Traceback (most recent call last):
    #   File "<input>", line 4, in <module>
    # TypeError: 'int' object is not iterable

.. code-block:: python
    :caption: Iterating over ``list`` with scalar and vector values - smart loop

    DATA = [('Jan', 'Twardowski'), 'Watney', 42, 13.37, {True, None, False}]


    for obj in DATA:
        if isinstance(obj, (list, tuple, set, frozenset)):
            for inner in obj:
                print(inner)
        else:
            print(obj)

    # Jan
    # Twardowski
    # Watney
    # 42
    # 13.37
    # False
    # True
    # None


Assignments
===========

Loop Nested Mean
----------------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/loop_nested_mean.py`

:English:
    #. Use data from "Input" section (see below)
    #. Separate header from data
    #. Calculate mean `Sepal length` value

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Odseparuj nagłówek od danych
    #. Wylicz średnią wartość `Sepal length`

:Input:
    .. code-block:: python

        DATA = [
            ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 2.9, 5.6, 1.8, 'virginica'),
            (6.4, 3.2, 4.5, 1.5, 'versicolor'),
            (4.7, 3.2, 1.3, 0.2, 'setosa'),
            (7.0, 3.2, 4.7, 1.4, 'versicolor'),
            (7.6, 3.0, 6.6, 2.1, 'virginica'),
            (4.6, 3.1, 1.5, 0.2, 'setosa'),
        ]

:Output:
    .. code-block:: python

        result: float
        # 5.911111111111111

:The whys and wherefores:
    * Iterating over nested structure

Loop Nested Unique Keys
-----------------------
* Complexity level: medium
* Lines of code to write: 5 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/loop_nested_unique_keys.py`

:English:
    #. Use data from "Input" section (see below)
    #. Collect keys from all rows in one sequence ``result``
    #. Sort ``result``
    #. Print unique keys
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zbierz klucze z wszystkich wierszy w jednej sekwencji ``result``
    #. Posortuj ``result``
    #. Wypisz unikalne klucze
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        DATA = [
            {'Sepal length': 5.1, 'Sepal width': 3.5, 'Species': 'setosa'},
            {'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
            {'Sepal length': 6.3, 'Petal width': 1.8, 'Species': 'virginica'},
            {'Sepal length': 5.0, 'Petal width': 0.2, 'Species': 'setosa'},
            {'Sepal width': 2.8, 'Petal length': 4.1, 'Species': 'versicolor'},
            {'Sepal width': 2.9, 'Petal width': 1.8, 'Species': 'virginica'},
        ]

:Output:
    .. code-block:: text

        Petal length
        Petal width
        Sepal length
        Sepal width
        Species

:The whys and wherefores:
    * Generating ``set``
    * Deduplication
    * Accessing ``dict`` keys
    * Iterating over nested structure
    * Updating ``set``

:Hint:
    * ``row.keys()``
    * Compare solutions with :ref:`Micro-benchmarking use case`
