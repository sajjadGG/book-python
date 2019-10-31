****************
Array Arithmetic
****************

.. glossary::

    Vectorized Operations
        Single statement without a loop that explains a looping concept:

            .. code-block:: python

                import numpy as np


                a = np.array([1, 2, 3])
                a ** 2
                # array([1, 4, 9])


Addition
========
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    a + 2
    # array([[3, 4, 5],
    #        [6, 7, 8]])

    a + a
    # array([[ 2,  4,  6],
    #        [ 8, 10, 12]])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    b = np.array([4, 5])

    a + b
    # ValueError: operands could not be broadcast together with shapes (3,) (2,)


Subtraction
===========
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    a - 2
    # array([[-1,  0,  1],
    #        [ 2,  3,  4]])

    a - a
    # array([[0, 0, 0],
    #        [0, 0, 0]])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    b = np.array([4, 5])

    a - b
    # ValueError: operands could not be broadcast together with shapes (3,) (2,)


Division
========
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    a / 2
    # array([[0.5, 1. , 1.5],
    #        [2. , 2.5, 3. ]])

    a / a
    # array([[1., 1., 1.],
    #        [1., 1., 1.]])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    b = np.array([4, 5])

    a / b
    # ValueError: operands could not be broadcast together with shapes (3,) (2,)

Square Root
===========
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    np.sqrt(a)
    # array([[1., 1.41421356, 1.73205081],
    #        [2., 2.23606798, 2.44948974]])


Modulo
======
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    a % 2
    # array([[1, 0, 1],
    #        [0, 1, 0]])

    a % a
    # array([[0, 0, 0],
    #        [0, 0, 0]])

    a // a
    # array([[1, 1, 1],
    #        [1, 1, 1]])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    b = np.array([4, 5])

    a % b
    # ValueError: operands could not be broadcast together with shapes (3,) (2,)

    a // b
    # ValueError: operands could not be broadcast together with shapes (3,) (2,)


Multiplication
==============
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    a * 2
    # array([[ 2,  4,  6],
    #        [ 8, 10, 12]])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    b = np.array([4, 5])

    a * b
    # ValueError: operands could not be broadcast together with shapes (3,) (2,)


Power
=====
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    a ** 2
    # array([[ 1,  4,  9],
    #        [16, 25, 36]])

    a * a
    # array([[ 1,  4,  9],
    #        [16, 25, 36]])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    b = np.array([4, 5])

    a ** b
    # ValueError: operands could not be broadcast together with shapes (3,) (2,)


Array Multiplication
====================
.. warning:: For two-dimensional arrays, multiplication ``*`` remains elementwise and does not correspond to matrix multiplication.

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])

    a * b
    # array([[ 5, 12],
    #        [21, 32]])


Matrix Multiplication
=====================
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])

    a.dot(b)
    # array([[19, 22],
    #        [43, 50]])

.. code-block:: text

    import numpy as np


    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])

    a @ b
    # array([[19, 22],
    #        [43, 50]])

.. code-block:: text

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.array([7, 8])

    a @ b
    # ValueError: matmul: Input operand 1 has a mismatch in its core dimension 0, with gufunc signature (n?,k),(k,m?)->(n?,m?) (size 2 is different from 3)

    a.dot(b)
    # ValueError: shapes (3,) and (2,) not aligned: 3 (dim 0) != 2 (dim 0)


Assignments
===========

Matrix multiplication
---------------------
* Complexity level: easy
* Lines of code to write: 2 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/numpy_matmul.py`

:English:
    #. Multiply two ``np.array``
    #. Compare output of ``@`` and ``*``
    #. Why it differs?

:Polish:
    #. Pomnóż dwa ``np.array``
    #. Porównaj wynik ``@`` oraz ``*``
    #. Dlaczego się różnią?

.. code-block:: python

    def matrix_multiplication(A, B):
        """
        >>> import numpy as np

        >>> A = np.array([[1, 0], [0, 1]])
        >>> B = [[4, 1], [2, 2]]
        >>> matrix_multiplication(A, B)
        array([[4, 1],
               [2, 2]])

        >>> A = [[1,0,1,0], [0,1,1,0], [3,2,1,0], [4,1,2,0]]
        >>> B = np.array([[4,1], [2,2], [5,1], [2,3]])
        >>> matrix_multiplication(A, B)
        array([[ 9,  2],
               [ 7,  3],
               [21,  8],
               [28,  8]])
        """
        return ...
