****************
Array Attributes
****************


Data type
=========
* Array can have only one data type (``dtype``)
* Type can be "non-primitive" - any class

int
---
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    # array([1, 2, 3])

    type(a)
    # <class 'numpy.ndarray'>

    a.dtype
    # dtype('int64')

float
-----
.. code-block:: python

    import numpy as np


    a = np.array([1., 2., 3.])
    # array([1., 2., 3.])

    type(a)
    # <class 'numpy.ndarray'>

    a.dtype
    # dtype('float64')

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    a.dtype
    # dtype('int64')

    a.astype(float)
    # array([[1., 2., 3.],
    #        [4., 5., 6.]])

    a.dtype
    # dtype('int64')

    b = a.astype(float)
    # array([[1., 2., 3.],
    #        [4., 5., 6.]])

    b.dtype
    # dtype('float64')

complex
-------
.. code-block:: python

    import numpy as np


    a = np.array([1+2j])
    # array([1.+2.j])

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
    # array([1, 2, 3])

    a.ndim          # 1
    a.size          # 3
    a.shape         # (3,)
    len(a)          # 3

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    a.ndim          # 2
    a.shape         # (2, 3)
    a.size          # 6
    len(a)          # 2

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]])

    a.ndim          # 2
    a.shape         # (3, 3)
    a.size          # 9
    len(a)          # 3

Data
====
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    # array([1, 2, 3])

    a.itemsize      # 8
    a.data          # <memory at 0x10cdfaa10>
    list(a.data)    # NotImplementedError: multi-dimensional sub-views are not implemented

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    a.itemsize      # 8
    a.data          # <memory at 0x10caefbb0>

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]])

    a.itemsize      # 8
    a.data          # <memory at 0x10cf92210>


.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], float)
    # array([[1., 2., 3.],
    #        [4., 5., 6.],
    #        [7., 8., 9.]])

    a.itemsize      # 8
    a.data          # <memory at 0x10caefbb0>


Assignments
===========
.. todo:: Create assignments
