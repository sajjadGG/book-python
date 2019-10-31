*************
Array Methods
*************


Copy
====
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    b = a
    c = a.copy()

    a[0] = 99

    repr(a)
    # array([99, 2, 3])

    repr(b)
    # array([99, 2, 3])

    repr(c)
    # array([1, 2, 3])


Put
===
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    a.put([0, 2], 99)
    # array([99,  2, 99])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    at_index = [0, 2]

    a.put(at_index, 99)
    # array([99,  2, 99])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    b = np.array([99, 88, 77])
    at_index = [0, 2]

    a.put(at_index, b)
    # array([99,  2, 88])


Fill
====
* Modifies inplace

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    a.fill(0)
    # array([0, 0, 0])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

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

    a.transpose()
    # array([1, 2, 3])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

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


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    a.transpose()
    # array([[1, 4, 7],
    #        [2, 5, 8],
    #        [3, 6, 9]])


Sort
====
.. code-block:: python

    import numpy as np


    a = np.array([2, 3, 1])

    sorted(a)
    # [1, 2, 3]

    a.sort()
    # array([1, 2, 3])

.. code-block:: python

    import numpy as np


    a = np.array([[2, 3, 1],
                   [5, 6, 4]])

    sorted(a)
    # ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

    a.sort()
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    a.sort(axis=0)
    # array([[2, 3, 1],
    #        [5, 6, 4]])

    a.sort(axis=1)
    # array([[1, 2, 3],
    #        [4, 5, 6]])


Flip
====
* Does not modify inplace
* Returns new ``ndarray``
* Reverse the order of elements in an array along the given axis

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    # array([1, 2, 3])

    np.flip(a)
    # array([3, 2, 1])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.flip()
    # array([[6, 5, 4],
    #        [3, 2, 1]])

    np.flip(a, axis=0)
    # array([[4, 5, 6],
    #        [1, 2, 3]])

    np.flip(a, axis=1)
    # array([[3, 2, 1],
    #        [6, 5, 4]])


To list
=======

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.tolist()
    # [[1, 2, 3], [4, 5, 6]]

Assignments
===========
.. todo:: Create assignments
