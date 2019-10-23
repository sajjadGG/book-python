******************
Array Modification
******************


1-dimensional Array
===================
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    # array([1, 2, 3])

    a[0] = 99
    # array([99,  2,  3])

    a[-1] = 88
    # array([99,  2,  88])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3], float)
    # array([1., 2., 3.])

    a[0] = 99.9
    # array([99.9,  2.,  3.])

    a[-1] = 11.1
    # array([99.9,  2.,  11.1])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3], int)
    # array([1, 2, 3])

    a[0] = 99.9
    # array([99,  2,  3])

    a[-1] = 11.1
    # array([99,  2,  11])


2-dimensional Array
===================
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    a[0,0] = 99
    # array([[99,  2,  3],
    #        [ 4,  5,  6]])

    a[1,2]
    # array([[99,  2,  3],
    #        [ 4,  5, 88]])


Fill
====
* Modifies inplace

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    # array([1, 2, 3])

    a.fill(0)
    # array([0, 0, 0])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    a.fill(0)
    # array([[0, 0, 0],
    #        [0, 0, 0]])


Transpose
=========
* ``a.transpose()`` or ``a.T``
* ``a.transpose()`` is preferred

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    # array([1, 2, 3])

    a.transpose()
    # array([1, 2, 3])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

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


    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]])

    a.transpose()
    # array([[1, 4, 7],
    #        [2, 5, 8],
    #        [3, 6, 9]])


Newaxis
=======
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    # array([1, 2, 3])

    a[:,np.newaxis]
    # array([[1],
    #        [2],
    #        [3]])

    a[np.newaxis,:]
    # array([[1, 2, 3]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    a[:,np.newaxis]
    # array([[[1, 2, 3]],
    #        [[4, 5, 6]]])

    a[np.newaxis,:]
    # array([[[1, 2, 3],
    #         [4, 5, 6]]])


Assignments
===========
