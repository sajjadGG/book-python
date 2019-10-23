*****
Slice
*****


1-dimensional Array
===================
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3, 4], float)
    # array([1., 2., 3., 4.])

    a[:2]
    # array([1., 2.])

    a[1:3]
    # array([2., 3.])

    a[-2:]
    # array([3., 4.])


2-dimensional Array - Rows
==========================
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]])

    a[:]
    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]])

    a[1:]
    # array([[4, 5, 6],
    #        [7, 8, 9]])

    a[:1]
    # array([[1., 2., 3.]])

    a[1:2]
    # array([[4, 5, 6]])


2-dimensional Array - Columns
=============================
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]])

    a[:,0]
    # array([1, 4, 7])

    a[:,1]
    # array([2, 5, 8])

    a[:,2]
    # array([3, 6, 9])

    a[:,-1]
    # array([3, 6, 9])

    a[:,0:1]
    # array([[1],
    #        [4],
    #        [7]])

    a[:,0:2]
    # array([[1, 2],
    #        [4, 5],
    #        [7, 8]])


2-dimensional Array - Rows and Columns
======================================
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]])

    a[0:1,0:1]
    # array([[1]])

    a[0:2,0:2]
    # array([[1, 2],
    #        [4, 5]])

    a[-1:,-2:]
    # array([[8, 9]])


Assignments
===========
