***********
Array Index
***********


1-dimensional Array
===================
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    # array([1, 2, 3])

    a[0]        # 1
    a[1]        # 2
    a[2]        # 3
    a[3]        # IndexError: index 3 is out of bounds for axis 0 with size 3
    a[-1]       # 3


2-dimensional Array
===================
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    a[0]        # array([1, 2, 3])
    a[1]        # array([4, 5, 6])
    a[2]        # IndexError: index 2 is out of bounds for axis 0 with size 2

    a[0,0]      # 1
    a[0,1]      # 2
    a[0,2]      # 3

    a[1,0]      # 4
    a[1,1]      # 5
    a[1,2]      # 6

    a[2,0]      # IndexError: index 2 is out of bounds for axis 0 with size 2


Assignments
===========
.. todo:: Create assignments
