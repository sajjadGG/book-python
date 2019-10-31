***********
Array Slice
***********


1-dimensional Array
===================
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3, 4])
    # array([1, 2, 3, 4])

    a[0:2]
    # array([1, 2])

    a[:2]
    # array([1, 2])

    a[1:3]
    # array([2, 3])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3, 4])
    # array([1., 2., 3., 4.])

    a[-2:]
    # array([3, 4])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3, 4])
    # array([1., 2., 3., 4.])

    a[::2]
    # array([1, 3])

    a[1::2]
    # array([2, 4])


2-dimensional Array
===================

All
---
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a[:]
    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]])

Rows
----
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a[1:]
    # array([[4, 5, 6],
    #        [7, 8, 9]])

    a[:1]
    # array([[1, 2, 3]])

    a[1:3]
    # array([[4, 5, 6],
    #        [7, 8, 9]])

    a[::2]
    # array([[1, 2, 3],
    #        [7, 8, 9]])

    a[1::2]
    # array([[4, 5, 6]])

Columns
-------
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a[:, 0]
    # array([1, 4, 7])

    a[:, 1]
    # array([2, 5, 8])

    a[: ,2]
    # array([3, 6, 9])

    a[:, -1]
    # array([3, 6, 9])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a[:, 0:1]
    # array([[1],
    #        [4],
    #        [7]])

    a[:, 0:2]
    # array([[1, 2],
    #        [4, 5],
    #        [7, 8]])

    a[:, :2]
    # array([[1, 2],
    #        [4, 5],
    #        [7, 8]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a[:, ::2]
    # array([[1, 3],
    #        [4, 6],
    #        [7, 9]])

    a[:, 1::2]
    # array([[2],
    #        [5],
    #        [8]])

Rows and Columns
----------------
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a[0:1, 0:1]
    # array([[1]])

    a[0:1, 0:2]
    # array([[1, 2]])

    a[0:1, 0:3]
    # array([[1, 2, 3]])

    a[0:2, 0:2]
    # array([[1, 2],
    #        [4, 5]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a[-1:, -2:]
    # array([[8, 9]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a[::2, ::2]
    # array([[1, 3],
    #        [7, 9]])

    a[1::2, 1::2]
    # array([[5]])


Newaxis
=======
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    a[:, np.newaxis]
    # array([[1],
    #        [2],
    #        [3]])

    a[np.newaxis, :]
    # array([[1, 2, 3]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a[:, np.newaxis]
    # array([[[1, 2, 3]],
    #        [[4, 5, 6]]])

    a[np.newaxis, :]
    # array([[[1, 2, 3],
    #         [4, 5, 6]]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a[:, np.newaxis, 1]
    # array([[2],
    #        [5],
    #        [8]])

    a[np.newaxis, :, 1]
    # array([[2, 5, 8]])

    a[1, np.newaxis, :]
    # array([[4, 5, 6]])


Assignments
===========

Array Slicing
-------------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/numpy_slice.py`

:English:
    #. Use input ndarray (see below)
    #. Select inner 3x3 and save to ``OUTPUT: ndarray``
    #. Print ``OUTPUT``

:Polish:
    #. Użyj wejściowej ndarray (patrz poniżej)
    #. Wybierz wewnętrzne 3x3 i zapisz do ``OUTPUT: ndarray``
    #. Wypisz ``OUTPUT``

:Input:
    .. code-block:: python

        INPUT = np.array([
            [7, 5, 3, 4, 5],
            [2, 2, 8, 1, 5],
            [3, 8, 8, 4, 4],
            [5, 5, 5, 2, 5],
            [0, 1, 0, 6, 0],
        ])

:Output:
    .. code-block:: python

        print(OUTPUT)
        # [[2 8 1]
        #  [8 8 4]
        #  [5 5 2]]

:The whys and wherefores:
    * Defining ``np.array``
    * Generating random ``np.array``

Sum of inner elements
---------------------
* Complexity level: medium
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/numpy_inner_sum.py`

:English:
    #. Use only random module from ``numpy`` module
    #. Set random seed to zero
    #. Generate ``outer: ndarray`` with 16x16 random digits (0-9 inclusive)
    #. Calculate sum of inner 4x4 elements
    #. Inner matrix is exactly in the middle of outer

:Polish:
    #. Używaj tylko modułu random z modułu ``numpy``
    #. Ustaw ziarno losowości na zero
    #. Wygeneruj ``outer: ndarray`` z 16x16 losowych cyfr (0-9 włącznie)
    #. Policz sumę środkowych 4x4 elementów
    #. Środkowa macierz jest dokładnie w środku większej

.. figure:: img/random-inner-sum.png
    :scale: 25%
    :align: center

    Sum of inner elements

:Hint:
    * ``np.array.sum()``
