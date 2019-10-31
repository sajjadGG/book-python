***********
Array Shape
***********


Get shape
=========
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    a.shape     # (3,)

.. code-block:: python

    import numpy as np


    b = np.array([[1, 2, 3],
                  [4, 5, 6]])

    b.shape     # (2, 3)

.. code-block:: python

    import numpy as np


    c = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    c.shape     # (3, 3)

.. code-block:: python

    import numpy as np


    d = np.array([[[ 1,  2,  3],
                   [ 4,  5,  6],
                   [ 5,  6,  7]],
                  [[11, 22, 33],
                   [44, 55, 66],
                   [77, 88, 99]]])

    d.shape         # (2, 3, 3)


Reshape
=======
* Returns new array
* Does not modify inplace
* ``a.reshape(1, 2)`` is equivalent to ``a.reshape((1, 2))``


.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    a.reshape(1, 3)
    # array([[1, 2, 3]])

    a.reshape(3, 1)
    # array([[1],
    #        [2],
    #        [3]])

.. code-block:: python

    import numpy as np


    b = np.array([[1, 2, 3],
                  [4, 5, 6]])

    b.reshape(3, 2)
    # array([[1, 2],
    #        [3, 4],
    #        [5, 6]])

    b.reshape(1, 6)
    # array([[1, 2, 3, 4, 5, 6]])

    b.reshape(6, 1)
    # array([[1],
    #        [2],
    #        [3],
    #        [4],
    #        [5],
    #        [6]])

    b.reshape(5, 2)
    # ValueError: cannot reshape array of size 6 into shape (5,2)

.. code-block:: python

    import numpy as np


    a1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])

    a1.reshape(2, 4)
    # array([[1, 2, 3, 4],
    #        [5, 6, 7, 8]])

    a1.reshape(2, 4, 1)
    # array([[[1],
    #         [2],
    #         [3],
    #         [4]],
    #        [[5],
    #         [6],
    #         [7],
    #         [8]]])

    a1.reshape(2, 2, 2)
    # array([[[1, 2],
    #         [3, 4]],
    #        [[5, 6],
    #         [7, 8]]])

    a1.reshape(1, 2, 4)
    # array([[[1, 2, 3, 4],
    #         [5, 6, 7, 8]]])

    a1.reshape(4, 2, 1)
    #array([[[1],
    #        [2]],
    #       [[3],
    #        [4]],
    #       [[5],
    #        [6]],
    #       [[7],
    #        [8]]])

    a1.reshape(1, 8, 1)
    # array([[[1],
    #         [2],
    #         [3],
    #         [4],
    #         [5],
    #         [6],
    #         [7],
    #         [8]]])

    a1.reshape(2, 3, 1)
    # ValueError: cannot reshape array of size 8 into shape (2,3,1)


Flatten
=======
* Returns new array
* Does not modify inplace

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    a.flatten()
    # array([1, 2, 3])

.. code-block:: python

    import numpy as np


    b = np.array([[1, 2, 3],
                  [4, 5, 6]])

    b.flatten()
    # array([1, 2, 3, 4, 5, 6])

.. code-block:: python

    import numpy as np


    c = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    c.flatten()
    # array([1, 2, 3, 4, 5, 6, 7, 8, 9])


Assignments
===========
.. todo:: Create assignments
