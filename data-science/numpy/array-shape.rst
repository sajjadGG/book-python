***********
Array Shape
***********


Get shape
=========
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    b = np.array([[1, 2, 3], [4, 5, 6]])
    c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    a.shape     # (3,)
    b.shape     # (2, 3)
    c.shape     # (3, 3)


Reshape
=======
* Returns new array
* Does not modify inplace
* ``a.reshape(1, 2)`` is equivalent to ``a.reshape((1, 2))``

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    a.shape
    # (2, 3)

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    a.reshape(3, 2)
    # array([[1, 2],
    #        [3, 4],
    #        [5, 6]])

    a.reshape(1, 6)
    # array([[1, 2, 3, 4, 5, 6]])

    a.reshape(6, 1)
    # array([[1],
    #        [2],
    #        [3],
    #        [4],
    #        [5],
    #        [6]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    a.reshape(5, 2)
    # ValueError: cannot reshape array of size 6 into shape (5,2)

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    a.reshape(1, 6)
    # array([[1, 2, 3, 4, 5, 6]])

    a
    # array([[1, 2, 3],
    #        [4, 5, 6]])


.. code-block:: python

    import numpy as np


    a = np.array(range(6), float)
    # array([0., 1., 2., 3., 4., 5.])

    a.reshape(2, 3, 1)
    # array([[[0.],
    #         [1.],
    #         [2.]],
    #
    #        [[3.],
    #         [4.],
    #         [5.]]])

    a.reshape(2, 3)
    # array([[0., 1., 2.],
    #        [3., 4., 5.]])

Flatten
=======
* Returns new array
* Does not modify inplace

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    a.flatten()
    # array([1, 2, 3, 4, 5, 6])

    a
    # array([[1, 2, 3],
    #        [4, 5, 6]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]])

    a.flatten()
    # array([1, 2, 3, 4, 5, 6, 7, 8, 9])

    a
    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]])


Assignments
===========
