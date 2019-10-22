Matrix
======
Numpy ma również typ macierzy matrix. Jest on bardzo podobny do tablicy ale podstawowe operacje wykonywane są w sposób macierzowy a nie tablicowy.

.. code-block:: python

    a = np.matrix([[1,2], [3,4]])
    b = np.matrix([[5,6], [7,8]])

    a * b
    # [[19 22]
    #  [43 50]]

    a ** 2
    # [[ 7 10]
    #  [15 22]]

    a * 2
    # [[2 4]
    #  [6 8]]

.. code-block:: python

    d = np.diag([3,4])
    # [[3 0]
    #  [0 4]]

    d * m
    # [[ 3  6]
    #  [12 16]]

Niemniej, tablice można używać podobnie, ale do mnożenia trzeba wykorzystywać funkcje dot:

.. code-block:: python

    a = np.array([[1,2], [3,4]])
    b = np.array([[5,6], [7,8]])

    a * b
    # [[ 5 12]
    #  [21 32]]

    a.dot(b)
    # [[19 22]
    #  [43 50]]

    a ** 2
    #  [[ 1  4]
    #   [ 9 16]]

    a * 2
    # [[2 4]
    #  [6 8]]

Dodatkowo, operacje algebry liniowej można wykonywać zarówno na tablicach jak i macierzach, np:

.. code-block:: python

    print('det(m) = {}'.format(np.linalg.det(m)))
    print('det(a) = {}'.format(np.linalg.det(a)))


Assignments
===========

Matrix multiplication
---------------------
* Complexity level: easy
* Lines of code to write: 2 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/numpy_matmul.py`

#. Używając ``numpy`` oraz operatora ``@`` oraz ``*``
#. Czym się różnią?

.. code-block:: python

    def matrix_multiplication(A, B):
        """
        >>> import numpy as np

        >>> A = np.array([[1, 0], [0, 1]])
        >>> B = [[4, 1], [2, 2]]
        >>> matrix_multiplication(A, B)
        [[4, 1], [2, 2]]

        >>> A = [[1,0,1,0], [0,1,1,0], [3,2,1,0], [4,1,2,0]]
        >>> B = np.matrix([[4,1], [2,2], [5,1], [2,3]])
        >>> matrix_multiplication(A, B)
        [[9, 2], [7, 3], [21, 8], [28, 8]]
        """
        pass
