****************
Array Attributes
****************


Dimensions
==========
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    a.ndim          # 1
    a.size          # 3
    a.shape         # (3,)
    len(a)          # 3

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.ndim          # 2
    a.shape         # (2, 3)
    a.size          # 6
    len(a)          # 2

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a.ndim          # 2
    a.shape         # (3, 3)
    a.size          # 9
    len(a)          # 3

.. code-block:: python

    import numpy as np


    a = np.array([[[ 1,  2,  3],
                   [ 4,  5,  6],
                   [ 5,  6,  7]],
                  [[11, 22, 33],
                   [44, 55, 66],
                   [77, 88, 99]]])

    a.ndim          # 3
    a.shape         # (2, 3, 3)
    a.size          # 18
    len(a)          # 2


Data
====
* ``int64`` takes 64 bits (8 bytes of memory)
* strides inform how many bytes numpy has to jump to access values in each dimensions

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    a.itemsize      # 8
    a.strides       # (8,)
    a.data          # <memory at 0x10cdfaa10>
    list(a.data)    # NotImplementedError: multi-dimensional sub-views are not implemented

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.itemsize      # 8
    a.strides       # (24, 8)
    a.data          # <memory at 0x10caefbb0>

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a.itemsize      # 8
    a.strides       # (24, 8)
    a.data          # <memory at 0x10cf92210>


Assignments
===========

Create
------
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/numpy_astype.py`

:English:
    #. Set random seed to zero
    #. Create ``a: ndarray`` with size 16x16
    #. Structure must contains random integers (0-9)
    #. Print number of:

        - dimensions
        - columns
        - rows
        - element count

:Polish:
    #. Ustaw ziarno losowości na zero
    #. Stwórz ``a: ndarray`` o rozmiarze 16x16
    #. Struktura musi zawierać losowe liczby (0-9)
    #. Wypisz liczbę:

        - wymiarów
        - kolumn
        - wierszy
        - ilość elementów

:The whys and wherefores:
    * Defining ``ndarray``
    * Using ``np.random.seed()``
    * Generating random ``np.array``
