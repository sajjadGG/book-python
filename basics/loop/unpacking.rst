.. _Loop Unpacking Sequences:

************************
Loop Unpacking Sequences
************************


Recap
=====
.. code-block:: python
    :caption: Recap information about unpacking

    a, b = 1, 2
    a, b = (1, 2)
    k, v = (1, 2)
    key, value = (1, 2)


List of pairs
=================
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


List of sequence
================
.. code-block:: python

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ]

    for sepal_len, sepal_wid, petal_len, petal_wid, species in DATA:
        print(f'{species} -> {sepal_len}')

    # setosa -> 5.1
    # versicolor -> 5.7
    # virginica -> 6.3

.. code-block:: python

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ]

    for sl, sw, pl, pw, s in DATA:
        print(f'{s} -> {sl}')

    # setosa -> 5.1
    # versicolor -> 5.7
    # virginica -> 6.3

.. code-block:: python

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ]

    for row in DATA:
        featuers = row[0:4]
        label = row[4]
        print(f'{label} -> {featuers}')

    # setosa -> (5.1, 3.5, 1.4, 0.2)
    # versicolor -> (5.7, 2.8, 4.1, 1.3)
    # virginica -> (6.3, 2.9, 5.6, 1.8)

.. code-block:: python

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ]

    for row in DATA:
        *featuers, label = row
        print(f'{label} -> {featuers}')

    # setosa -> [5.1, 3.5, 1.4, 0.2]
    # versicolor -> [5.7, 2.8, 4.1, 1.3]
    # virginica -> [6.3, 2.9, 5.6, 1.8]

.. code-block:: python

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ]

    for *featuers, label in DATA:
        print(f'{label} -> {featuers}')

    # setosa -> [5.1, 3.5, 1.4, 0.2]
    # versicolor -> [5.7, 2.8, 4.1, 1.3]
    # virginica -> [6.3, 2.9, 5.6, 1.8]

.. code-block:: python

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ]

    for *X,y in DATA:
        print(f'{y} -> {X}')

    # setosa -> [5.1, 3.5, 1.4, 0.2]
    # versicolor -> [5.7, 2.8, 4.1, 1.3]
    # virginica -> [6.3, 2.9, 5.6, 1.8]

.. code-block:: python

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ]

    for sepal_length, *_, species in DATA:
        print(f'{species} -> {sepal_length}')

    # setosa -> 5.1
    # versicolor -> 5.7
    # virginica -> 6.3


Nested
======
.. code-block:: python
    :caption: Unpacking nested sequence

    DATA = [
        (1, 2),
        ('name', 'Jan Twardowski'),
        ('species', ['setosa', 'versicolor', 'virginica']),
        ((1, 2), ['Johnson Space Center', 'Kennedy Space Center']),
        (['NASA', 'ESA', 'Roscosmos'], 1),
    ]

    for key, value in DATA:
        print(f'{key} -> {value}')

    # 1 -> 2
    # name -> Jan Twardowski
    # species -> ['setosa', 'versicolor', 'virginica']
    # (1, 2) -> ['Johnson Space Center', 'Kennedy Space Center']
    # ['NASA', 'ESA', 'Roscosmos'] -> 1


List of Dicts
=============
.. code-block:: python
    :caption: Unpacking ``list`` of ``dict``

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


Assignments
===========

Unpacking
---------
* Complexity level: medium
* Lines of code to write: 3 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/loop_unpacking_endswith.py`

:English:
    #. Use data from "Input" section (see below)
    #. Separate header from data
    #. Iterating over data unpack row to ``*features`` and ``label``
    #. Print species names ending with "ca" or "osa"

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Oddziel nagłówek od danych
    #. Iterując po danych rozpakuj wiersz do ``*features`` oraz ``label``
    #. Wypisz nazwy gatunków kończące się na "ca" lub "osa"

:Input:
    .. code-block:: python

        DATA = [
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
    * Accessing ``set`` items
    * Iterating over nested structure
    * Unpacking in ``for`` loop

:Hint:
    * ``str.endswith()``
    * ``set.pop()``
    * ``isinstance`` or ``type``
