**************
Array Indexing
**************


Index
=====

Flat
----
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.flat[0]   # 1
    a.flat[1]   # 2
    a.flat[2]   # 3
    a.flat[3]   # 4
    a.flat[4]   # 5
    a.flat[5]   # 6

Multidimensional
----------------
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a[0,0]      # 1
    a[0,1]      # 2
    a[0,2]      # 3
    a[1,0]      # 4
    a[1,1]      # 5
    a[1,2]      # 6


Selecting items
===============

1-dimensional Array
-------------------
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    # array([1, 2, 3])

    a[0]        # 1
    a[1]        # 2
    a[2]        # 3
    a[3]        # IndexError: index 3 is out of bounds for axis 0 with size 3
    a[-1]       # 3

2-dimensional Array
-------------------
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a[0]        # array([1, 2, 3])
    a[1]        # array([4, 5, 6])
    a[2]        # IndexError: index 2 is out of bounds for axis 0 with size 2

    a[0,0]      # 1
    a[0,1]      # 2
    a[0,2]      # 3

    a[1,0]      # 4
    a[1,1]      # 5
    a[1,2]      # 6

    a[2,0]      # IndexError: index 2 is out of bounds for axis 0 with size 2

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a[0]        # array([1, 2, 3])
    a[1]        # array([4, 5, 6])
    a[2]        # IndexError: index 2 is out of bounds for axis 0 with size 2

    a[0,0]      # 1
    a[0,1]      # 2
    a[0,2]      # 3

    a[1,0]      # 4
    a[1,1]      # 5
    a[1,2]      # 6

    a[2,0]      # 7
    a[2,1]      # 8
    a[2,2]      # 9

3-dimensional Array
-------------------
.. code-block:: python

    import numpy as np


    a = array([[[ 1,  2,  3],
                [ 4,  5,  6],
                [ 5,  6,  7]],
               [[11, 22, 33],
                [44, 55, 66],
                [77, 88, 99]]])

    a[0,0,0]    # 1
    a[0,0,1]    # 2
    a[0,0,2]    # 3
    a[0,0,3]    # IndexError: index 3 is out of bounds for axis 2 with size 3

    a[0,1,2]    # 6
    a[0,2,1]    # 6
    a[2,1,0]    # IndexError: index 2 is out of bounds for axis 0 with size 2


Substituting items
==================

1-dimensional Array
-------------------
* Will type cast values to ``ndarray.dtype``

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    a[0] = 99
    # array([99,  2,  3])

    a[-1] = 88
    # array([99,  2,  88])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3], float)

    a[0] = 99.9
    # array([99.9,  2.,  3.])

    a[-1] = 11.1
    # array([99.9,  2.,  11.1])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3], int)

    a[0] = 99.9
    # array([99,  2,  3])

    a[-1] = 11.1
    # array([99,  2,  11])

2-dimensional Array
-------------------
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a[0,0] = 99
    # array([[99,  2,  3],
    #        [ 4,  5,  6]])

    a[1,2] = 88
    # array([[99,  2,  3],
    #        [ 4,  5, 88]])


Assignments
===========

Index
-----
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/numpy_indexing.py`

:English:
    #. Create ``output: ndarray``
    #. Add to ``output`` elements from ``INPUT`` (see below) at indexes:

        - row 0, column 2
        - row 2, column 2
        - row 0, column 0
        - row 1, column 0

    #. ``output`` size must be 2x2
    #. ``output`` type must be float

:Polish:
    #. Stwórz ``output: ndarray``
    #. Dodaj do ``output`` elementy z ``INPUT`` (patrz sekcja input) o indeksach:

        - wiersz 0, kolumna 2
        - wiersz 2, kolumna 2
        - wiersz 0, kolumna 0
        - wiersz 1, kolumna 0

    #. Rozmiar ``output`` musi być 2x2
    #. Typ ``output`` musi być float

:Input:
    .. code-block:: python

        INPUT = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])

:Output:
    .. code-block:: python

        output: ndarray
        # array([[3, 9],
        #        [1, 4]])

:The whys and wherefores:
    * Defining ``ndarray``
    * Indexing ``ndarray``

:Hint:
    * ``np.zeros(shape, dtype)``
