****************
Array Attributes
****************


Data type
=========
* Array can have only one data type (``dtype``)
* Type can be "non-primitive" - any class

int
---
* Signed (positive and negative):

    * ``np.int``
    * ``np.int0``
    * ``np.int8``
    * ``np.int16``
    * ``np.int32``
    * ``np.int64``

* Unsigned (non-negative only):

    * ``np.uint0``
    * ``np.uint8``
    * ``np.uint16``
    * ``np.uint32``
    * ``np.uint64``

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    type(a)
    # <class 'numpy.ndarray'>

    a.dtype
    # dtype('int64')

.. code-block:: python

    import numpy as np


    a = np.array([[1., 2., 3.],
                  [4., 5., 6.]])

    a.astype(int)
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    a.astype(np.int0)
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    a.astype(np.int8)
    # array([[1, 2, 3],
    #        [4, 5, 6]], dtype=int8)

float
-----
* ``np.float``
* ``np.float16``
* ``np.float32``
* ``np.float64``
* ``np.float128``

.. code-block:: python

    import numpy as np


    a = np.array([1., 2., 3.])

    type(a)
    # <class 'numpy.ndarray'>

    a.dtype
    # dtype('float64')

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.astype(float)
    # array([[1., 2., 3.],
    #        [4., 5., 6.]])

    a.astype(np.float64)
    # array([[1., 2., 3.],
    #        [4., 5., 6.]])

    a.astype(np.float128)
    # array([[1., 2., 3.],
    #        [4., 5., 6.]], dtype=float128)

complex
-------
* ``np.complex``
* ``np.complex64``
* ``np.complex128``
* ``np.complex256``

.. code-block:: python

    import numpy as np


    a = np.array([1+2j])

    a.dtype
    # dtype('complex128')

.. code-block:: python

    import numpy as np


    a = np.array([1.1+2.2j])
    # array([1.1+2.2j])

    a.dtype
    # dtype('complex128')


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
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    a.itemsize      # 8
    a.data          # <memory at 0x10cdfaa10>
    list(a.data)    # NotImplementedError: multi-dimensional sub-views are not implemented

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.itemsize      # 8
    a.data          # <memory at 0x10caefbb0>

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a.itemsize      # 8
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
    #. Create ``np.array`` with size 16x16
    #. Structure must contains random integers (0-9)
    #. Print number of:

        - dimensions
        - columns
        - rows
        - element count

:Polish:
    #. Ustaw ziarno losowości na zero
    #. Stwórz ``np.array`` o rozmiarze 16x16
    #. Struktura musi zawierać losowe liczby (0-9)
    #. Wypisz liczbę:

        - wymiarów
        - kolumn
        - wierszy
        - ilość elementów

:The whys and wherefores:
    * Defining ``np.array``
    * Using ``np.random.seed()``
    * Generating random ``np.array``
