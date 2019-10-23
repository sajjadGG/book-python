************
Array Create
************


1-dimensional Array
===================
.. code-block:: python

    import numpy as np


    np.array([1, 2, 3])
    # array([1, 2, 3])

.. code-block:: python

    import numpy as np


    np.array([1.0, 2.0, 3.0])
    # array([1., 2., 3.])

    np.array([1.1, 2.2, 3.3])
    # array([1.1, 2.2, 3.3])

.. code-block:: python

    import numpy as np


    np.array([1, 2, 3], dtype=float)
    # array([ 1., 2., 3.])

    np.array([1, 2, 3], float)
    # array([ 1., 2., 3.])

.. code-block:: python

    import numpy as np


    np.array(['a', 'b', 'c'])
    # array(['a', 'b', 'c'], dtype='<U1')

    np.array(['one', 'two', 'three'])
    # array(['one', 'two', 'three'], dtype='<U5')


2-dimensional Array
===================
.. code-block:: python

    import numpy as np


    np.array([[1,2], [3,4]])
    # array([[1, 2],
    #        [3, 4]])

    np.array([[1,2], [3,4]], float)
    # array([[1., 2.],
    #        [3., 4.]])

.. code-block:: python

    import numpy as np


    np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]])


Array Generation
================
.. code-block:: python

    import numpy as np


    np.array(range(10))
    # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    np.array(range(10), float)
    # array([ 0., 1., 2., 3., 4., 5., 6., 7., 8., 9.])


Arange
======
* similar to ``range()``
* array-range

int
---
.. code-block:: python

    import numpy as np


    np.arange(5)
    # array([0, 1, 2, 3, 4])

    np.arange(1, 5)
    # array([1, 2, 3, 4])

    np.arange(1, 10, step=2)
    # array([1, 3, 5, 7, 9])

float
-----
.. code-block:: python

    import numpy as np


    np.arange(5.0)
    # array([0., 1., 2., 3., 4.])

.. code-block:: python

    import numpy as np


    np.arange(start=2, stop=10, step=2, dtype=float)
    # array([2., 4., 6., 8.])

.. code-block:: python

    import numpy as np


    np.arange(0.0, 1.0, 0.1)
    # array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])


Zeros
=====
.. code-block:: python

    import numpy as np


    np.zeros((2, 3))
    # array([[0., 0., 0.],
    #       [0., 0., 0.]])


.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])

    np.zeros_like(a)
    # array([[0, 0, 0],
    #        [0, 0, 0]])


Ones
====
.. code-block:: python

    import numpy as np


    np.ones((3, 2))
    # array([[1., 1.],
    #        [1., 1.],
    #        [1., 1.]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])

    np.ones_like(a)
    # array([[1, 1, 1],
    #        [1, 1, 1]])


Empty
=====
* Garbage from memory
* Very small numbers (``1e-312``, ``1e-313``, ``1e-322``)
* Will reuse previous if given shape was already created

.. code-block:: python

    import numpy as np


    np.empty((3,4))
    # array([[ 2.31584178e+077,  1.29073692e-231,  2.96439388e-323, 0.00000000e+000],
    #       [-2.32034891e+077,  2.68678047e+154,  2.18018101e-314, 2.18022275e-314],
    #       [ 0.00000000e+000,  2.18023445e-314,  1.38338381e-322, 9.03690495e-309]])

.. code-block:: python

    import numpy as np


    np.zeros((2, 3))
    #array([[0., 0., 0.],
    #       [0., 0., 0.]])

    np.empty((2, 3))
    #array([[0., 0., 0.],
    #       [0., 0., 0.]])


Random
======
.. code-block:: python

    import numpy as np


    np.random.rand(2, 3)
    # array([[0.12840072, 0.14798816, 0.94352656],
    #        [0.24807979, 0.6355252 , 0.65943694]])

.. code-block:: python

    import numpy as np


    a = np.random.randint(10, size=(2, 3))
    # array([[9, 5, 0],
    #        [7, 0, 6]])


Identity
========
.. code-block:: python

    import numpy as np


    np.identity(3)
    # array([[1., 0., 0.],
    #        [0., 1., 0.],
    #        [0., 0., 1.]])

    np.identity(4, int)
    # array([[1, 0, 0, 0],
    #        [0, 1, 0, 0],
    #        [0, 0, 1, 0],
    #        [0, 0, 0, 1]])


Copy
====
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    # array([1, 2, 3])

    b = a
    # array([1, 2, 3])

    c = a.copy()
    # array([1, 2, 3])

    a[0] = 0
    # array([0, 2, 3])

    b
    # array([0, 2, 3])

    c
    # array([1, 2, 3])


Assignments
===========
.. todo:: Create assignments
