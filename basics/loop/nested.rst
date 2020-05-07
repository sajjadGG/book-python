.. _Loop Nested Sequences:

*********************
Loop Nested Sequences
*********************


Nested sequence of objects of one type
======================================
.. code-block:: python
    :caption: Iterating over sequence

    DATA = [1, 2, 3]

    for obj in DATA:
        print(obj)

    # 1
    # 2
    # 3

.. code-block:: python
    :caption: Iterating over nested sequence

    DATA = [(...), (...), (...)]

    for obj in DATA:
        print(obj)

    # (...)
    # (...)
    # (...)

.. code-block:: python
    :caption: Iterating over nested sequence

    DATA = [
        ('a', 1),
        ('b', 2),
        ('c', 3),
    ]

    for obj in DATA:
        print(obj)

    # ('a', 1)
    # ('b', 2)
    # ('c', 3)

.. code-block:: python
    :caption: Iterating over nested sequence

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ]

    for row in DATA:
        print(row)

    # (5.1, 3.5, 1.4, 0.2, 'setosa')
    # (5.7, 2.8, 4.1, 1.3, 'versicolor')
    # (6.3, 2.9, 5.6, 1.8, 'virginica')


Nested sequence of objects of many types
========================================
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
        if isinstance(obj, (list, set, tuple)):
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

Mean
----
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/loop_nested_mean.py`

:English:
    #. Use ``DATA`` from "Input" section (see below)
    #. Separate header from data
    #. Calculate mean `Sepal length` value

:Polish:
    #. Użyj ``DATA`` z sekcji "Input" (patrz poniżej)
    #. Oddziel nagłówek od danych
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

:The whys and wherefores:
    * Iterating over nested structure

Unique keys from schema-less database
-------------------------------------
* Complexity level: medium
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/loop_nested_unique_keys.py`

:English:
    #. Use ``DATA`` from "Input" section (see below)
    #. Collect keys from all rows in one sequence ``result``
    #. Sort ``result``
    #. Print unique keys

:Polish:
    #. Użyj ``DATA`` z sekcji "Input" (patrz poniżej)
    #. Zbierz klucze z wszystkich wierszy w jednej sekwencji ``result``
    #. Posortuj ``result``
    #. Wypisz unikalne klucze

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
    * ``for key in row.keys()``
    * Compare solutions with :numref:`Micro-benchmarking use case`
