****************
Array Arithmetic
****************

.. glossary::

    Vectorized Operations
        Single statement without a loop that explains a looping concept.
        Applies operation to each element.

            .. code-block:: python

                import numpy as np


                a = np.array([1, 2, 3])

                a ** 2
                # array([1, 4, 9])


Broadcasting Rules
==================
* Source :cite:`NumpyBroadcastingRules`

#. Operations between multiple array objects are first checked for proper shape match
#. Mathematical operators (``+``, ``-``, ``*``, ``/``, ``exp``, ``log``, ...) apply element by element, on values
#. Reduction operations (``mean``, ``std``, ``skew``, ``kurt``, ``sum``, ``prod``, ...) apply to whole array, unless an axis is specified
#. Missing values propagate, unless explicitly ignored (``nanmean``, ``nansum``, ...)


Addition
========
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

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


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

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


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

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


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    np.sqrt(a)
    # array([[1., 1.41421356, 1.73205081],
    #        [2., 2.23606798, 2.44948974]])


Modulo
======
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

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


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

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


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

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


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    b = np.array([[4, 5, 6],
                  [7, 8, 9]])

    a * b
    # array([[ 4, 10, 18],
    #        [ 7, 16, 27]])


Matrix Multiplication
=====================
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    b = np.array([[4, 5, 6],
                  [7, 8, 9]])

    a.dot(b)
    # ValueError: shapes (3,) and (2,3) not aligned: 3 (dim 0) != 2 (dim 0)

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    b = np.array([[1, 2],
                  [3, 4],
                  [5, 6]])

    a.dot(b)
    # array([[22, 28],
    #        [49, 64]])

.. code-block:: python
    :force:

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    b = np.array([[1, 2],
                  [3, 4],
                  [5, 6]])

    a @ b
    # array([[22, 28],
    #        [49, 64]])

.. code-block:: python
    :force:

    import numpy as np


    a = np.array([1, 2, 3])
    b = np.array([[4, 5, 6],
                  [7, 8, 9]])

    a @ b
    # ValueError: matmul: Input operand 1 has a mismatch in its core dimension 0, with gufunc signature (n?,k),(k,m?)->(n?,m?) (size 2 is different from 3)

    a.dot(b)
    # ValueError: shapes (3,) and (2,3) not aligned: 3 (dim 0) != 2 (dim 0)

* ``np.dot()``
* If either a or b is 0-D (scalar), it is equivalent to ``multiply`` and using ``numpy.multiply(a, b)`` or ``a * b`` is preferred.
* If both a and b are 1-D arrays, it is inner product of vectors (without complex conjugation).
* If both a and b are 2-D arrays, it is matrix multiplication, but using ``matmul`` or ``a @ b`` is preferred.
* If a is an N-D array and b is a 1-D array, it is a sum product over the last axis of a and b.
* If a is an N-D array and b is an M-D array (where ``M>=2``), it is a sum product over the last axis of a and the second-to-last axis of b: ``dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])``

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3], float)
    b = np.array([0, 1, 1], float)

    np.dot(a, b)
    # 5.0

.. code-block:: python

    import numpy as np


    a = np.array([[0, 1], [2, 3]], float)
    b = np.array([2, 3], float)
    c = np.array([[1, 1], [4, 0]], float)

    a
    # array([[ 0., 1.],
    #        [ 2., 3.]])

    np.dot(b, a)
    # array([ 6., 11.])

    np.dot(a, b)
    # array([ 3., 13.])

    np.dot(a, c)
    # array([[ 4., 0.],
    #        [ 14., 2.]])

    np.dot(c, a)
    # array([[ 2., 4.],
    #        [ 0., 4.]])


Assignments
===========

Arithmetic operations
---------------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/numpy_arithmetic.py`

:English:
    #. For given: ``a: ndarray``, ``b: ndarray``, ``c: ndarray`` (see below)
    #. Calculate square root of each element in ``a`` and ``b``
    #. Calculate second power (square) of each element in ``c``
    #. Add elements from ``a`` to ``b``
    #. Multiply the result by ``c``

:Polish:
    #. Dla danych: ``a: ndarray``, ``b: ndarray``, ``c: ndarray`` (patrz sekcja input)
    #. Oblicz pierwiastek kwadratowy każdego z elementu w ``a`` i ``b``
    #. Oblicz drugą potęgę (kwadrat) każdego z elementu w ``c``
    #. Dodaj elementy z ``a`` do ``b``
    #. Przemnóż wynik przez ``c``

:Input:
    .. code-block:: python

        a = np.array([[0, 1], [2, 3]], float)
        b = np.array([2, 3], float)
        c = np.array([[1, 1], [4, 0]], float)

:Output:
    .. code-block:: python

        array([[0.34657359, 1.00505254],
               [3.81230949,       -inf]])

Addition
--------
* Complexity level: easy
* Lines of code to write: 2 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/numpy_arithmetic_add.py`

:English:
    #. Add ``a`` and ``b``
    #. Add ``b`` and ``a``
    #. What happened?

:Polish:
    #. Dodaj ``a`` i ``b``
    #. Dodaj ``b`` i ``a``
    #. Co się stało?

.. code-block:: python

        import numpy as np

        a = np.array([[1, 0], [0, 1]])
        b = [[4, 1], [2, 2]]

Multiplication
--------------
* Complexity level: easy
* Lines of code to write: 2 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/numpy_arithmetic_matmul.py`

:English:
    #. Multiply ``a`` and ``b`` using scalar multiplication
    #. Multiply ``a`` and ``b`` using matrix multiplication
    #. Multiply ``b`` and ``a`` using scalar multiplication
    #. Multiply ``b`` and ``a`` using matrix multiplication
    #. Discuss results

:Polish:
    #. Przemnóż ``a`` i ``b`` używając mnożenia skalarnego
    #. Przemnóż ``a`` i ``b`` używając mnożenia macierzowego
    #. Przemnóż ``b`` i ``a`` używając mnożenia skalarnego
    #. Przemnóż ``b`` i ``a`` używając mnożenia macierzowego
    #. Omów wyniki

.. code-block:: python

        import numpy as np

        a = np.array([[1,0,1,0],
                      [0,1,1,0],
                      [3,2,1,0],
                      [4,1,2,0]])

        b = np.array([
                     [4,1],
                     [2,2],
                     [5,1],
                     [2,3]])
