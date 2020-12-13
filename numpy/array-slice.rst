***********
Array Slice
***********


1-dimensional Array
===================
.. code-block:: python
    :caption: 1-dimensional Array

    import numpy as np


    a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

    a[1:5]          # array([2, 3, 4, 5])
    a[3:8]          # array([4, 5, 6, 7, 8])

    a[0:5]          # array([1, 2, 3, 4, 5])
    a[:5]           # array([1, 2, 3, 4, 5])
    a[5:9]          # array([6, 7, 8, 9])

    a[5:len(a)]     # array([6, 7, 8, 9])
    a[5:]           # array([6, 7, 8, 9])
    a[-2:]          # array([8, 9])
    a[-5:]          # array([5, 6, 7, 8, 9])
    a[-6:-2]        # array([4, 5, 6, 7])

    a[3:8:2]        # array([4, 6, 8])
    a[-8:-3:2]      # array([2, 4, 6])
    a[::2]          # array([1, 3, 5, 7, 9])
    a[1::2]         # array([2, 4, 6, 8])

    a[0:len(a)]     # array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    a[0:]           # array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    a[:len(a)]      # array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    a[:]            # array([1, 2, 3, 4, 5, 6, 7, 8, 9])


2-dimensional Array
===================
.. code-block:: python
    :caption: Rows

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a[:]
    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]])

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

.. code-block:: python
    :caption: Columns

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

    a[:, ::2]
    # array([[1, 3],
    #        [4, 6],
    #        [7, 9]])

    a[:, 1::2]
    # array([[2],
    #        [5],
    #        [8]])

.. code-block:: python
    :caption: Rows and Columns

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

    a[::2, ::2]
    # array([[1, 3],
    #        [7, 9]])

    a[1::2, 1::2]
    # array([[5]])

    a[[2,1], ::2]
    # array([[7, 9],
    #        [4, 6]])


Assignments
===========

.. literalinclude:: assignments/numpy_slice_1.py
    :caption: :download:`Solution <assignments/numpy_slice_1.py>`
    :end-before: # Solution

.. literalinclude:: assignments/numpy_slice_2.py
    :caption: :download:`Solution <assignments/numpy_slice_2.py>`
    :end-before: # Solution

.. figure:: img/random-inner-sum.png

    Inner 4x4 elements
