.. _Sequence Nesting:

****************
Sequence Nesting
****************


``list`` of ``tuple``
=====================
.. code-block:: python
    :caption: Get elements from ``list`` of ``tuple``

    DATA = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]

    DATA[2]
    # (7.6, 3.0, 6.6, 2.1, 'virginica')

    DATA[2][1]
    # 3.0

.. code-block:: python
    :caption: Append elements using ``list.append()``

    DATA = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]

    row = (4.9, 2.5, 4.5, 1.7, 'virginica')
    DATA.append(row)
    # [(4.7, 3.2, 1.3, 0.2, 'setosa'),
    #  (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    #  (7.6, 3.0, 6.6, 2.1, 'virginica'),
    #  (4.9, 2.5, 4.5, 1.7, 'virginica')]

.. code-block:: python
    :caption: Append elements using ``list.extend()``

    DATA = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]

    row = (4.9, 2.5, 4.5, 1.7, 'virginica')
    DATA.extend(row)
    # [(4.7, 3.2, 1.3, 0.2, 'setosa'),
    #  (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    #  (7.6, 3.0, 6.6, 2.1, 'virginica'),
    #  4.9,
    #  2.5,
    #  4.5,
    #  1.7,
    #  'virginica']

.. code-block:: python
    :caption: ``list`` of ``tuple`` length

    DATA = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]

    len(DATA)
    # 3

    len(DATA[2])
    # 5


``list`` of ``list``
====================
.. highlights::
    * Multidimensional lists

.. code-block:: python
    :caption: Lists ``a``, ``b``, ``c``, ``d`` contains the same values, but readability differs depending on whitespaces.

    a = [[1,2,3],[4,5,6],[7,8,9]]

    b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    c = [[1,2,3], [4,5,6], [7,8,9]]

    d = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

.. code-block:: python
    :caption: Get elements from ``list`` of ``list``

    DATA = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    DATA[0][0]
    # 1

    DATA[0][2]
    # 3

    DATA[2][1]
    # 8

.. code-block:: python
    :caption: ``list`` of ``list`` length

    DATA = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    len(DATA)
    # 3

    len(DATA[2])
    # 3


Unions
======
.. code-block:: python
    :caption: Get elements from union

    DATA = [
        [1, 2, 3],
        (4, 5, 6),
        {7, 8, 9},
    ]

    DATA[1]
    # (4, 5, 6)

    DATA[1][2]
    # 6

    DATA[2]
    # {7, 8, 9}

.. code-block:: python
    :caption: Union length

    DATA = [
        [1, 2],
        (3, 4, 5, 6),
        {7, 8, 9, 10, 11},
    ]

    len(DATA)
    # 3

    len(DATA[0])
    # 2

    len(DATA[1])
    # 4

    len(DATA[2])
    # 5


Assignments
===========

Nesting Create
--------------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/sequence_nesting_create.py`

:English:
    #. Create nested sequence ``result`` with elements:

        * tuple: 1, 2, 3
        * list: 1.1, 2.2, 3.3
        * set: 'Mark Watney', 'Melissa Lewis', 'Jan Twardowski'

    #. Print ``result``
    #. Print number of elements in ``result``

:Polish:
    #. Stwórz zagnieżdżoną sekwencję ``result`` z elementami:

        * krotka: 1, 2, 3
        * lista: 1.1, 2.2, 3.3
        * zbiór: 'Mark Watney', 'Melissa Lewis', 'Jan Twardowski'

    #. Wypisz ``result``
    #. Wypisz liczbę elementów ``result``
