.. _Sequence Nesting:

****************
Sequence Nesting
****************


``list`` of ``tuple``
=====================

Getting elements
----------------
.. code-block:: python

    DATA = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]

    DATA[2]
    # (7.6, 3.0, 6.6, 2.1, 'virginica')

    DATA[2][1]
    # 3.0

Appending elements
------------------
.. code-block:: python

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
    #  4.9,
    #  2.5,
    #  4.5,
    #  1.7,
    #  'virginica']

Length
------
.. code-block:: python

    DATA = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]

    len(DATA)
    # 3

    len(DATA[2])
    # 5

Type Annotation
---------------
.. code-block:: python

    from typing import List


    DATA: List[tuple] = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]

.. code-block:: python

    from typing import List, Tuple


    DATA: List[Tuple[float, float, float, float, str]] = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]


``list`` of ``list``
====================
.. highlights::
    * Multidimensional lists

.. code-block:: python

    DATA = [[1,2,3],[4,5,6],[7,8,9]]

.. code-block:: python

    DATA = [[1,2,3], [4,5,6], [7,8,9]]

.. code-block:: python

    DATA = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

.. code-block:: python

    DATA = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

Getting elements
----------------
.. code-block:: python

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

Length
------
.. code-block:: python

    DATA = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    len(DATA)
    # 3

    len(DATA[2])
    # 3

Type Annotations
----------------
.. code-block:: python

    from typing import List

    DATA: List[list] = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

.. code-block:: python

    from typing import List

    DATA: List[List[int]] = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]


Mixed types
===========

Getting elements
----------------
.. code-block:: python

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

Length
------
.. code-block:: python

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

Type Annotations
----------------
.. code-block:: python

    from typing import Set, List, Union, Tuple


    DATA: List[Union[List[int], Tuple[int, int, int], Set[int]]] = [
        [1, 2, 3],
        (4, 5, 6),
        {7, 8, 9},
    ]

.. code-block:: python

    from typing import List


    DATA: List[Union[list, tuple, set]] = [
        [1, 2, 3],
        (4, 5, 6),
        {7, 8, 9},
    ]


Assignments
===========
.. todo:: Create assignments
