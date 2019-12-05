************
Array Create
************


Array Declaration
=================

1-dimensional Array
-------------------
.. code-block:: python

    import numpy as np


    np.array([1, 2, 3])

.. code-block:: python

    import numpy as np


    np.array([1.0, 2.0, 3.0])
    # array([1., 2., 3.])

    np.array([1.1, 2.2, 3.3])
    # array([1.1, 2.2, 3.3])

    np.array([1, 2, 3], float)
    # array([ 1., 2., 3.])

    np.array([1, 2, 3], dtype=float)
    # array([ 1., 2., 3.])

2-dimensional Array
-------------------
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])


Array str vs repr
=================
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    str(a)
    # '[[1 2 3]\n [4 5 6]\n [7 8 9]]'

    print(a)
    # [[1 2 3]
    #  [4 5 6]
    #  [7 8 9]]

    repr(a)
    # 'array([[1, 2, 3],\n       [4, 5, 6],\n       [7, 8, 9]])'

    a
    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]])

    print(repr(a))
    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]])

Array Generation
================

Array from ``range()``
----------------------
.. code-block:: python

    import numpy as np


    np.array(range(5))
    # array([0, 1, 2, 3, 4])

    np.array(range(5), float)
    # array([ 0., 1., 2., 3., 4.])

.. code-block:: python

    import numpy as np


    np.array(range(5, 10))
    # array([5, 6, 7, 8, 9])

    np.array(range(5, 10), float)
    # array([5., 6., 7., 8., 9.])

.. code-block:: python

    import numpy as np


    np.array(range(5, 10, 2))
    # array([5, 7, 9])

    np.array(range(5, 10, 2), float)
    # array([5., 7., 9.])

Array from ``np.arange()``
--------------------------
* similar to ``range()``
* array-range

.. code-block:: python

    import numpy as np


    np.arange(5)
    # array([0, 1, 2, 3, 4])

    np.arange(5, dtype=float)
    # array([0., 1., 2., 3., 4.])

    np.arange(5.0)
    # array([0., 1., 2., 3., 4.])

.. code-block:: python

    import numpy as np


    np.arange(5, 10)
    # array([5, 6, 7, 8, 9])

    np.arange(5, 10, step=2)
    # array([5, 7, 9])

    np.arange(start=5, stop=10, step=2)
    # array([5, 7, 9])

    np.arange(start=5, stop=10, step=2, dtype=float)
    # array([5., 7., 9.])

.. code-block:: python

    import numpy as np


    np.arange(0.0, 1.0, 0.1)
    # array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])

    np.arange(0.0, 1.0, 0.2)
    # array([0. , 0.2, 0.4, 0.6, 0.8])

    np.arange(0.0, 1.0, 0.3)
    # array([0. , 0.3, 0.6, 0.9])

Zeros and zeros-like
--------------------
.. code-block:: python

    import numpy as np


    np.zeros((2, 3))
    # array([[0., 0., 0.],
    #       [0., 0., 0.]])

    np.zeros(shape=(2, 3))
    # array([[0., 0., 0.],
    #        [0., 0., 0.]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    np.zeros_like(a)
    # array([[0, 0, 0],
    #        [0, 0, 0]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]], float)

    np.zeros_like(a)
    # array([[0., 0., 0.],
    #        [0., 0., 0.]])

Ones and ones-like
------------------
.. code-block:: python

    import numpy as np


    np.ones((3, 2))
    # array([[1., 1.],
    #        [1., 1.],
    #        [1., 1.]])

    np.ones(shape=(3, 2))
    # array([[1., 1.],
    #        [1., 1.],
    #        [1., 1.]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    np.ones_like(a)
    # array([[1, 1, 1],
    #        [1, 1, 1]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]], float)

    np.ones_like(a)
    # array([[1., 1., 1.],
    #        [1., 1., 1.]])

Empty and empty-like
--------------------
* Garbage from memory
* Will reuse previous if given shape was already created

.. code-block:: python

    import numpy as np


    np.empty((3,4))
    # array([[ 2.31584178e+077,  1.29073692e-231,  2.96439388e-323, 0.00000000e+000],
    #       [-2.32034891e+077,  2.68678047e+154,  2.18018101e-314, 2.18022275e-314],
    #       [ 0.00000000e+000,  2.18023445e-314,  1.38338381e-322, 9.03690495e-309]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    np.empty((2,3))
    # array([[1., 2., 3.],
    #        [4., 5., 6.]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    np.empty_like(a)
    # array([[1, 2, 3],
    #        [4, 5, 6]])

Identity
--------
.. code-block:: python

    import numpy as np


    np.identity(2)
    # array([[1., 0.],
    #        [0., 1.]])

    np.identity(3)
    # array([[1., 0., 0.],
    #        [0., 1., 0.],
    #        [0., 0., 1.]])

    np.identity(4, int)
    # array([[1, 0, 0, 0],
    #        [0, 1, 0, 0],
    #        [0, 0, 1, 0],
    #        [0, 0, 0, 1]])


Assignments
===========

Create
------
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/numpy_create_arange.py`

:English:
    #. Create ``a: ndarray`` with even numbers from 0 to 100
    #. Numbers must be ``float`` type

:Polish:
    #. Stwórz ``a: ndarray`` z liczbami parzystymi od 0 do 100
    #. Liczby muszą być typu ``float``

:The whys and wherefores:
    * Defining ``ndarray``

Create Random
-------------
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/numpy_create_random.py`

:English:
    #. Set random seed to zero
    #. Create ``a: ndarray`` with size 16x16
    #. Structure must contains random integers (0-9)
    #. Print ``a``

:Polish:
    #. Ustaw ziarno losowości na zero
    #. Stwórz ``a: ndarray`` o rozmiarze 16x16
    #. Struktura musi zawierać losowe liczby (0-9)
    #. Wypisz ``a``

:The whys and wherefores:
    * Defining ``ndarray``
    * Using ``np.random.seed()``
    * Generating random ``np.array``
