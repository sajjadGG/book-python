**********
Array Axis
**********


About Axis
==========
* ``axis`` is an index in ``a.shape``
* Columns are always last


One Dimensional
===============
.. code-block:: python

    import numpy

    a = np.array([1, 2, 3])

    a.shape                 # (3,)

    a[0]                    # 1
    a[1]                    # 2
    a[2]                    # 3

    a.take(0, axis=0)       # 1
    a.take(1, axis=0)       # 2
    a.take(2, axis=0)       # 3

    a.take(0, axis=-1)      # 1
    a.take(1, axis=-1)      # 2
    a.take(2, axis=-1)      # 3

    a[:, 1]                 # IndexError: too many indices for array
    a.take(0, axis=1)       # AxisError: axis 1 is out of bounds for array of dimension 1


Two Dimensional
===============

Rows
----
.. code-block:: python

    import numpy


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a.shape                 # (3, 3)

    a[0, :]                 # array([1, 2, 3])
    a[1, :]                 # array([4, 5, 6])
    a[2, :]                 # array([7, 8, 9])

    a.take(0, axis=0)       # array([1, 2, 3])
    a.take(1, axis=0)       # array([4, 5, 6])
    a.take(2, axis=0)       # array([7, 8, 9])

Columns
-------
.. code-block:: python

    import numpy


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a.shape                 # (3, 3)

    a[:, 0]                 # array([1, 4, 7])
    a[:, 1]                 # array([2, 5, 8])
    a[:, 2]                 # array([3, 6, 9])

    a.take(0, axis=1)       # array([1, 4, 7])
    a.take(1, axis=1)       # array([2, 5, 8])
    a.take(2, axis=1)       # array([3, 6, 9])

    a.take(0, axis=-1)      # array([1, 4, 7])
    a.take(1, axis=-1)      # array([2, 5, 8])
    a.take(2, axis=-1)      # array([3, 6, 9])


Three Dimensional
=================

Depth
-----
.. code-block:: python

    import numpy

    a = np.array([[[ 1,  2,  3],
                   [ 4,  5,  6],
                   [ 5,  6,  7]],

                  [[11, 22, 33],
                   [44, 55, 66],
                   [77, 88, 99]]])

    a.shape
    # (2, 3, 3)

    a[0,:,:]
    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [5, 6, 7]])

    a[1,:,:]
    # array([[11, 22, 33],
    #        [44, 55, 66],
    #        [77, 88, 99]])

    a[2,:,:]
    # IndexError: index 2 is out of bounds for axis 0 with size 2

    a.take(0, axis=0)
    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [5, 6, 7]])

    a.take(1, axis=0)
    # array([[11, 22, 33],
    #        [44, 55, 66],
    #        [77, 88, 99]])

    a.take(2, axis=0)
    # IndexError: index 2 is out of bounds for size 2

Rows
----
.. code-block:: python

    import numpy

    a = np.array([[[ 1,  2,  3],
                   [ 4,  5,  6],
                   [ 5,  6,  7]],

                  [[11, 22, 33],
                   [44, 55, 66],
                   [77, 88, 99]]])

    a.shape
    # (2, 3, 3)

    a[:,0,:]
    # array([[ 1,  2,  3],
    #        [11, 22, 33]])

    a[:,1,:]
    # array([[ 4,  5,  6],
    #        [44, 55, 66]])

    a[:,2,:]
    # array([[ 5,  6,  7],
    #        [77, 88, 99]])

    a.take(0, axis=1)
    # array([[ 1,  2,  3],
    #        [11, 22, 33]])

    a.take(1, axis=1)
    # array([[ 4,  5,  6],
    #        [44, 55, 66]])

    a.take(2, axis=1)
    # array([[ 5,  6,  7],
    #        [77, 88, 99]])

Columns
-------
.. code-block:: python

    import numpy

    a = np.array([[[ 1,  2,  3],
                   [ 4,  5,  6],
                   [ 5,  6,  7]],

                  [[11, 22, 33],
                   [44, 55, 66],
                   [77, 88, 99]]])

    a.shape
    # (2, 3, 3)

    a[:,:,0]
    # array([[ 1,  4,  5],
    #        [11, 44, 77]])

    a[:,:,1]
    # array([[ 2,  5,  6],
    #        [22, 55, 88]])

    a[:,:,2]
    # array([[ 3,  6,  7],
    #        [33, 66, 99]])

    a.take(0, axis=2)
    # array([[ 1,  4,  5],
    #        [11, 44, 77]])

    a.take(1, axis=2)
    # array([[ 2,  5,  6],
    #        [22, 55, 88]])

    a.take(2, axis=2)
    # array([[ 3,  6,  7],
    #        [33, 66, 99]])

    a.take(0, axis=-1)
    # array([[ 1,  4,  5],
    #        [11, 44, 77]])

    a.take(1, axis=-1)
    # array([[ 2,  5,  6],
    #        [22, 55, 88]])

    a.take(2, axis=-1)
    # array([[ 3,  6,  7],
    #        [33, 66, 99]])


``n`` Dimensional
=================
* ``axis`` is an index in ``a.shape``
* Columns are always last
