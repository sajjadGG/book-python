.. _Loop Nested Sequences:

*********************
Loop Nested Sequences
*********************


Iterating over nested ``list`` items
====================================
.. code-block:: python
    :caption: Iterating over nested ``list`` items

    DATA = [1, 2, 3]

    for obj in DATA:
        print(obj)

    # 1
    # 2
    # 3

.. code-block:: python
    :caption: Iterating over nested ``list`` items

    DATA = [(...), (...), (...)]

    for obj in DATA:
        print(obj)

    # (...)
    # (...)
    # (...)

.. code-block:: python
    :caption: Iterating over nested ``list`` items

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


Unpacking values in loop
========================

Recap information about unpacking
---------------------------------
.. code-block:: python
    :caption: Unpacking values

    a, b = 1, 2
    a, b = (1, 2)
    k, v = (1, 2)
    key, value = (1, 2)

Unpacking ``list`` of pairs
---------------------------
.. code-block:: python
    :caption: Unpacking values in loop

    DATA = [
        ('a', 1),
        ('b', 2),
        ('c', 3),
    ]

    for key, value in DATA:
        print(f'{key} -> {value}')

    # a -> 1
    # b -> 2
    # c -> 3

.. code-block:: python
    :caption: Unpacking values in loop

    DATA = [
        (1, 2),
        ('name', 'Jan Twardowski'),
        ('species', ['setosa', 'versicolor', 'virginica']),
        ((1, 2), ['Johnson Space Center', 'Kennedy Space Center']),
    ]

    for key, value in DATA:
        print(f'{key} -> {value}')

    # 1 -> 2
    # name -> Jan Twardowski
    # species -> ['setosa', 'versicolor', 'virginica']
    # (1, 2) -> ['Johnson Space Center', 'Kennedy Space Center']

Unpacking ``list`` of sequences
-------------------------------
.. code-block:: python
    :caption: Unpacking values in loop

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ]

    # sepal_len, sepal_wid, petal_len, petal_wid, species = (5.1, 3.5, 1.4, 0.2, 'setosa')

    for sepal_len, sepal_wid, petal_len, petal_wid, species in DATA:
        print(f'{species} -> {sepal_len}')

    # setosa -> 5.1
    # versicolor -> 5.7
    # virginica -> 6.3

``list`` of ``dict``
--------------------
.. code-block:: python
    :caption: ``list`` of ``dict``

    DATA = [
        {'Sepal length': 5.1, 'Sepal width': 3.5, 'Petal length': 1.4, 'Petal width': 0.2, 'Species': 'setosa'},
        {'Sepal length': 5.7, 'Sepal width': 2.8, 'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
        {'Sepal length': 6.3, 'Sepal width': 2.9, 'Petal length': 5.6, 'Petal width': 1.8, 'Species': 'virginica'},
    ]

    for row in DATA:
        sepal_length = row['Sepal length']
        species = row['Species']
        print(f'{species} -> {sepal_length}')

    # setosa -> 5.1
    # versicolor -> 5.7
    # virginica -> 6.3


Enumerating and item index
==========================
.. code-block:: python
    :caption: Enumerating and item index

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ]

    for i, row in enumerate(DATA):
        print(f'{i} -> {row}')

    # 0 -> (5.1, 3.5, 1.4, 0.2, 'setosa')
    # 1 -> (5.7, 2.8, 4.1, 1.3, 'versicolor')
    # 2 -> (6.3, 2.9, 5.6, 1.8, 'virginica')


Iterating complex types
=======================
.. code-block:: python
    :caption: Iterating over ``list`` with scalar and vector values - simple loop

    DATA = [('Jan', 'Twardowski'), 'Watney', 42, 13.37, {True, None, False}]

    for element in DATA:
        print(element})

    # ('Jan', 'Twardowski')
    # Watney
    # 42
    # 13.37
    # {False, True, None}

.. code-block:: python
    :caption: Iterating over ``list`` with scalar and vector values - nested loop

    DATA = [('Jan', 'Twardowski'), 'Watney', 42, 13.37, {True, None, False}]

    for outer in DATA:
        for inner in outer:
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


    for outer in DATA:
        if isinstance(outer, (list, set, tuple)):
            for inner in outer:
                print(inner)
        else:
            print(outer)

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

Get elements from nested data structure
---------------------------------------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/for_nested.py`

:English:
    #. For input data (see below)
    #. Separate header from data
    #. Iterate over data
    #. Print species names ending with "ca" or "sa"

:Polish:
    #. Dla danych wejściowych (patrz poniżej)
    #. Oddziel nagłówek od danych
    #. Iteruj po danych
    #. Wypisz nazwy gatunków kończące się na "ca" lub "sa"

:Input:
    .. code-block:: python

        INPUT = [
            ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, {'virginica'}),
            (5.1, 3.5, 1.4, 0.2, {'setosa'}),
            (5.7, 2.8, 4.1, 1.3, {'versicolor'}),
            (6.3, 2.9, 5.6, 1.8, {'virginica'}),
            (6.4, 3.2, 4.5, 1.5, {'versicolor'}),
            (4.7, 3.2, 1.3, 0.2, {'setosa'}),
            (7.0, 3.2, 4.7, 1.4, {'versicolor'}),
            (7.6, 3.0, 6.6, 2.1, {'virginica'}),
            (4.6, 3.1, 1.5, 0.2, {'setosa'}),
        ]

:The whys and wherefores:
    * Accessing ``dict`` keys
    * Iterating over nested structure

Unique keys from schema-less database
-------------------------------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/loop_unique_keys.py`

:English:
    #. For input data (see below)
    #. Collect unique keys in one sequence
    #. Print the sequence

:Polish:
    #. Dla danych wejściowych (patrz poniżej)
    #. Zbierz unikalne klucze w jednej sekwencji
    #. Wypisz sekwencję

:Input:
    .. code-block:: python

        INPUT = [
            {'Sepal length': 5.1, 'Sepal width': 3.5, 'Species': 'setosa'},
            {'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
            {'Sepal length': 6.3, 'Petal width': 1.8, 'Species': 'virginica'},
            {'Sepal length': 5.0, 'Petal width': 0.2, 'Species': 'setosa'},
            {'Sepal width': 2.8, 'Petal length': 4.1, 'Species': 'versicolor'},
            {'Sepal width': 2.9, 'Petal width': 1.8, 'Species': 'virginica'},
        ]

:The whys and wherefores:
    * Generating ``set``
    * Deduplication
    * Accessing ``dict`` keys
    * Iterating over nested structure
    * Updating ``set``

:Hint:
    * Compare solutions with :numref:`Micro-benchmarking use case`
