*************
Array Methods
*************


Copy
====
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    b = a
    c = a.copy()

    a[0] = 99

    a
    # array([99, 2, 3])

    b
    # array([99, 2, 3])

    c
    # array([1, 2, 3])


Put
===

One dimensional
---------------
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3, 4, 5, 6])

    a.put([0, 2, 5], 99)

    a
    # array([99,  2, 99,  4,  5, 99])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3, 4, 5, 6])
    at_index = [0, 2, 5]

    a.put(at_index, 99)

    a
    # array([99,  2, 99,  4,  5, 99])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3, 4, 5, 6])
    b = np.array([99, 88, 77, 66, 55, 44, 33, 22])
    at_index = [0, 2, 5]

    a.put(at_index, b)

    a
    # array([99,  2, 88,  4,  5, 77])

Two dimensional
---------------
* Equivalent to ``a.flat[indexes] = value``

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    b = np.array([99, 88, 77, 66, 55, 44, 33, 22])
    at_index = [0, 2, 5]

    a.put(at_index, b)

    a
    # array([[99,  2, 88],
    #        [ 4,  5, 77],
    #        [ 7,  8,  9]])


Fill
====
* Modifies inplace

Fill all
--------
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    a.fill(0)
    # array([0, 0, 0])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.fill(0)
    # array([[0, 0, 0],
    #        [0, 0, 0]])

Fill slice
----------
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a[:, 0].fill(0)
    # array([[0, 2, 3],
    #        [0, 5, 6],
    #        [0, 8, 9]])

Fill NaN
--------
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a[:, 0].fill(np.nan)

    a
    # array([[-9223372036854775808, 2, 3],
    #        [-9223372036854775808, 5, 6],
    #        [-9223372036854775808, 8, 9]])

.. code-block:: python

    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]], dtype=float)

    a[:, 0].fill(np.nan)

    a
    # array([[nan,  2.,  3.],
    #        [nan,  5.,  6.],
    #        [nan,  8.,  9.]])


Full
====
.. code-block:: python

    import numpy as np


    np.full((2, 2), np.inf)
    # array([[inf, inf],
    #        [inf, inf]])

    np.full((2, 2), 10)
    # array([[10, 10],
    #        [10, 10]])


Transpose
=========
* ``a.transpose()`` or ``a.T``
* ``a.transpose()`` is preferred

One dimensional
---------------
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    a.transpose()
    # array([1, 2, 3])

Two dimensional
---------------
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.transpose()
    # array([[1, 4],
    #        [2, 5],
    #        [3, 6]])

    a.T
    # array([[1, 4],
    #        [2, 5],
    #        [3, 6]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a.transpose()
    # array([[1, 4, 7],
    #        [2, 5, 8],
    #        [3, 6, 9]])


To list
=======

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.tolist()
    # [[1, 2, 3], [4, 5, 6]]


Assignments
===========

Array Methods
-------------
* Complexity level: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/numpy_methods.py`

:English:
    #. Set random seed to zero
    #. Generate ``a: ndarray`` of 12 random integers from 0 to 100 (exclusive)
    #. Reshape ``a`` to 3x4
    #. Print ``a``

:Polish:
    #. Ustaw ziarno losowości na zero
    #. Wygeneruj ``a: ndarray`` z 12 losowymi liczbami całkowitymi od 0 do 100 (rozłącznie)
    #. Zmień kształt na 3x4
    #. Transponuj ``a``
    #. Wypisz ``a``
