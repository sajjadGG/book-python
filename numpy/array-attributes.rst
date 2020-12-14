****************
Array Attributes
****************


Size
====
* Number of elements

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    b = np.array([[1, 2, 3],
                  [4, 5, 6]])

    c = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    d = np.array([[[ 1,  2,  3],
                   [ 4,  5,  6],
                   [ 5,  6,  7]],

                  [[11, 22, 33],
                   [44, 55, 66],
                   [77, 88, 99]]])

    a.size
    # 3
    b.size
    # 6
    c.size
    # 9
    d.size
    # 18


Shape
=====
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    b = np.array([[1, 2, 3],
                  [4, 5, 6]])

    c = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    d = np.array([[[ 1,  2,  3],
                   [ 4,  5,  6],
                   [ 5,  6,  7]],

                  [[11, 22, 33],
                   [44, 55, 66],
                   [77, 88, 99]]])

    a.shape
    # (3,)
    b.shape
    # (2, 3)
    c.shape
    # (3, 3)
    d.shape
    # (2, 3, 3)


NDim
====
* Number of Dimensions
* ``len(ndarray.shape)``

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    b = np.array([[1, 2, 3],
                  [4, 5, 6]])

    c = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    d = np.array([[[ 1,  2,  3],
                   [ 4,  5,  6],
                   [ 5,  6,  7]],

                  [[11, 22, 33],
                   [44, 55, 66],
                   [77, 88, 99]]])

    a.ndim
    # 1
    b.ndim
    # 2
    c.ndim
    # 2
    d.ndim
    # 3


Length
======
* Number of elements in first dimension
* ``ndarray.shape[0]``

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    b = np.array([[1, 2, 3],
                  [4, 5, 6]])

    c = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    d = np.array([[[ 1,  2,  3],
                   [ 4,  5,  6],
                   [ 5,  6,  7]],

                  [[11, 22, 33],
                   [44, 55, 66],
                   [77, 88, 99]]])

    len(a)
    # 2
    len(b)
    # 2
    len(c)
    # 2
    len(d)
    # 2


Itemsize
========
* ``int64`` takes 64 bits (8 bytes of memory)

.. code-block:: python

    import numpy as np

    a = np.array([1, 2, 3], dtype=np.int16)
    b = np.array([1, 2, 3], dtype=np.int32)
    c = np.array([1, 2, 3], dtype=np.int64)

    a.itemsize
    # 2
    b.itemsize
    # 4
    c.itemsize
    # 8

.. code-block:: python

    import numpy as np

    a = np.array([1, 2, 3], dtype=np.float16)
    b = np.array([1, 2, 3], dtype=np.float32)
    c = np.array([1, 2, 3], dtype=np.float64)

    a.itemsize
    # 2
    b.itemsize
    # 4
    c.itemsize
    # 8


Strides
=======
* ``int64`` takes 64 bits (8 bytes of memory)
* Strides inform how many bytes numpy has to jump to access values in each dimensions

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    b = np.array([[1, 2, 3],
                  [4, 5, 6]])

    c = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    d = np.array([[[ 1,  2,  3],
                   [ 4,  5,  6],
                   [ 5,  6,  7]],

                  [[11, 22, 33],
                   [44, 55, 66],
                   [77, 88, 99]]])

    a.strides
    # (8,)
    b.strides
    # (24, 8)
    c.strides
    # (24, 8)
    d.strides
    # (72, 24, 8)


Data
====
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    a.shape
    # (3,)
    a.itemsize
    # 8
    a.strides
    # (8,)
    a.data
    # <memory at 0x10cdfaa10>

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.shape
    # (2, 3)
    a.itemsize
    # 8
    a.strides
    # (24, 8)
    a.data
    # <memory at 0x10caefbb0>


.. code-block:: python

    import numpy as np


    a = np.array([[[ 1,  2,  3],
                   [ 4,  5,  6],
                   [ 5,  6,  7]],

                  [[11, 22, 33],
                   [44, 55, 66],
                   [77, 88, 99]]])

    a.shape
    # (2, 3, 3)
    a.itemsize
    # 8
    a.strides
    # (72, 24, 8)
    a.data
    # <memory at 0x107933c70>


Assignments
===========

.. literalinclude:: assignments/numpy_attributes.py
    :caption: :download:`Solution <assignments/numpy_attributes.py>`
    :end-before: # Solution
