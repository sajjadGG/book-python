*************
Array Slicing
*************


1-dimensional Array
===================
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    a[0:2]
    # array([1, 2])

    a[:2]
    # array([1, 2])

    a[1:3]
    # array([2, 3])

    a[-2:]
    # array([2, 3])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    a[::2]
    # array([1, 3])

    a[1::2]
    # array([2])


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

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

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

    a[:, 2]
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


Assignments
===========

Numpy Slice 1
-------------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/numpy_slice_1.py`

:English:
    #. Use data from "Input" section (see below)
    #. Print inner 2x2 elements
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Wybierz wewnętrzne 2x2 elementy
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        DATA = np.array([
            [2, 8, 1, 5],
            [8, 8, 4, 4],
            [5, 5, 2, 5],
            [1, 0, 6, 0],
        ])

:Output:
    .. code-block:: python

        result: ndarray
        # array([[8, 4],
        #        [5, 2]])

:The whys and wherefores:
    * Defining ``np.array``
    * Generating random ``np.array``

Numpy Slice 2
-------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/numpy_slice_2.py`

:English:
    #. Use only ``random`` module from ``numpy`` library
    #. Set random seed to zero
    #. Generate ``DATA: ndarray`` with 16x16 random digits (0-9 inclusive)
    #. Print inner 4x4 elements
    #. Inner matrix is exactly in the middle of outer

:Polish:
    #. Użyj tylko funkcji z modułu ``random`` biblioteki ``numpy``
    #. Ustaw ziarno losowości na zero
    #. Wygeneruj ``DATA: ndarray`` z 16x16 losowych cyfr (0-9 włącznie)
    #. Wypisz środkowe 4x4 elementy
    #. Środkowa macierz jest dokładnie w środku większej

.. figure:: img/random-inner-sum.png
    :width: 75%
    :align: center

    Inner 4x4 elements
