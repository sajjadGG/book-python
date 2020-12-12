**********
Array Sort
**********

Sort
====

One dimensional
---------------
.. code-block:: python

    import numpy as np


    a = np.array([2, 3, 1])
    a.sort()

    a
    # array([1, 2, 3])

Two dimensional - Default axis
------------------------------
.. code-block:: python

    import numpy as np


    a = np.array([[2, 3, 1],
                  [5, 6, 4]])
    a.sort()

    a
    # array([[1, 2, 3],
    #        [4, 5, 6]])

Two dimensional - Columns
-------------------------
.. code-block:: python

    import numpy as np


    a = np.array([[2, 3, 1],
                  [5, 6, 4]])

    a.shape
    # (2, 3)

    a.sort(axis=0)
    # array([[2, 3, 1],
    #        [5, 6, 4]])

    a.sort(axis=1)
    # array([[1, 2, 3],
    #        [4, 5, 6]])

Two dimensional - Rows
----------------------
.. code-block:: python

    import numpy as np

    a = np.array([[9, 1, 8],
                  [2, 3, 1],
                  [5, 6, 4]])

    a.shape
    # (3,3)

    a.sort(axis=0)
    # array([[2, 1, 1],
    #        [5, 3, 4],
    #        [9, 6, 8]])

    a.sort(axis=1)
    # array([[1, 8, 9],
    #        [1, 2, 3],
    #        [4, 5, 6]])


Flip
====
* Does not modify inplace
* Returns new ``np.ndarray``
* Reverse the order of elements in an array along the given axis

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    # array([1, 2, 3])

    np.flip(a)
    # array([3, 2, 1])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.flip()
    # array([[6, 5, 4],
    #        [3, 2, 1]])

    np.flip(a, axis=0)
    # array([[4, 5, 6],
    #        [1, 2, 3]])

    np.flip(a, axis=1)
    # array([[3, 2, 1],
    #        [6, 5, 4]])


Assignments
===========

.. todo:: Convert assignments to literalinclude

Numpy Sort
----------
* Assignment: Numpy Sort
* Filename: :download:`assignments/numpy_sort.py`
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Sort ``result`` columns
    3. Flip ``result`` rows
    4. Print ``result``

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Posortuj kolumny ``result``
    3. Flipnij wiersze ``result``
    4. Wypisz ``result``

Given:
    .. code-block:: python

        DATA = np.array([[44, 47, 64, 67],
                         [67,  9, 83, 21],
                         [36, 87, 70, 88]])

Tests:

    >>> type(result)
    np.ndarray
    >>> result
    array([[36, 70, 87, 88],
           [ 9, 21, 67, 83],
           [44, 47, 64, 67]])
