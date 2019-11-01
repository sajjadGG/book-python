****************
Array Statistics
****************


Sum
===
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.sum()
    # 21

    a.sum(axis=0)
    # array([5, 7, 9])

    a.sum(axis=1)
    # array([ 6, 15])


Product
=======
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.prod()
    # 720


Mean
====
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.mean()
    # 3.5

    a.mean(axis=0)
    # array([2.5, 3.5, 4.5])

    a.mean(axis=1)
    # array([2., 5.])


Variance
========
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.var()
    # 2.9166666666666665

    a.var(axis=0)
    # array([2.25, 2.25, 2.25])

    a.var(axis=1)
    # array([0.66666667, 0.66666667])


Standard Deviation
==================
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.std()
    # 1.707825127659933

    a.std(axis=0)
    # array([1.5, 1.5, 1.5])

    a.std(axis=1)
    # array([0.81649658, 0.81649658])


Minimal Value
=============
 * ``ndarray.argmin()`` index of an ``a.min()`` element in array

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.min()
    # 1

    a.min(axis=0)
    # array([1, 2, 3])

    a.min(axis=1)
    # array([1, 4])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.argmin()
    # 0

    a.argmin(axis=0)
    # array([0, 0, 0])

    a.argmin(axis=1)
    # array([0, 0])


Maximal Value
=============
 * ``ndarray.argmax()`` index of an ``a.max()`` element in array

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.max()
    # 6

    a.max(axis=0)
    # array([4, 5, 6])

    a.max(axis=1)
    # array([3, 6])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.argmax()
    # 5

    a.argmax(axis=1)
    # array([2, 2])

    a.argmax(axis=0)
    # array([1, 1, 1])


Assignments
===========
.. todo:: Create assignments
