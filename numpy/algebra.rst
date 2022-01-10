Linear Algebra
==============


Rationale
---------
>>> import numpy as np

Linear Algebra:

    * ``np.sign()``
    * ``np.abs()``
    * ``np.sqrt()``
    * ``np.power()``

Logarithms:

    * ``np.log()``
    * ``np.log10()``
    * ``np.exp()``


Vector and matrix mathematics
-----------------------------


Determinant of a square matrix
------------------------------
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6],
...               [7, 8, 9]])
>>>
>>> np.linalg.det(a)
0.0

>>> a = np.array([[4, 2, 0],
...               [9, 3, 7],
...               [1, 2, 1]])
>>>
>>> np.linalg.det(a)
-48.00000000000003


Inner product
-------------
* Compute inner product of two vectors
* ``np.inner()``
* Ordinary inner product of vectors for 1-D arrays
  (without complex conjugation)
* In higher dimensions a sum product over the last axes

Ordinary inner product for vectors:

>>> a = np.array([1, 2, 3])
>>> b = np.array([0, 1, 0])
>>>
>>> np.inner(a, b)
2

Multidimensional example:

>>> a = np.arange(24).reshape((2,3,4))
>>> b = np.arange(4)
>>>
>>> np.inner(a, b)
array([[ 14,  38,  62],
       [ 86, 110, 134]])


Outer product
-------------
* ``np.outer()``

Compute the outer product of two vectors

>>> a = np.array([1, 2, 3])
>>> b = np.array([4, 5, 6])
>>>
>>> np.outer(a, b)
array([[ 4,  5,  6],
       [ 8, 10, 12],
       [12, 15, 18]])

An example using a "vector" of letters:

>>> a = np.array(['a', 'b', 'c'])
>>>
>>> np.outer(a, [1, 2, 3])
Traceback (most recent call last):
numpy.core._exceptions._UFuncNoLoopError: ufunc 'multiply' did not contain a loop with signature matching types (dtype('<U1'), dtype('int64')) -> None

>>> a = np.array(['a', 'b', 'c'], dtype=object)
>>>
>>> np.outer(a, [1, 2, 3])
array([['a', 'aa', 'aaa'],
       ['b', 'bb', 'bbb'],
       ['c', 'cc', 'ccc']], dtype=object)


Cross product
-------------
* ``np.cross()``

The cross product of a and b in R^3 is a vector perpendicular to both a and b

Vector cross-product:

>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>>
>>> np.cross(a, b)
array([-3,  6, -3])

One vector with dimension 2:

>>> a = [1, 2]
>>> b = [4, 5, 6]
>>>
>>> np.cross(a, b)
array([12, -6, -3])


Eigenvalues and vectors of a square matrix
------------------------------------------
Each of a set of values of a parameter for which a differential equation has
a nonzero solution (an eigenfunction) under given conditions. Any number such
that a given matrix minus that number times the identity matrix has a zero
determinant.

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6],
...               [7, 8, 9]])
>>>
>>> vals, vecs = np.linalg.eig(a)
>>>
>>> vals
array([ 1.61168440e+01, -1.11684397e+00, -9.75918483e-16])
>>>
>>> vecs
array([[-0.23197069, -0.78583024,  0.40824829],
       [-0.52532209, -0.08675134, -0.81649658],
       [-0.8186735 ,  0.61232756,  0.40824829]])


Inverse of a square matrix
--------------------------
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6],
...               [7, 8, 9]])
>>>
>>> np.linalg.inv(a)
Traceback (most recent call last):
numpy.linalg.LinAlgError: Singular matrix

>>> a = np.array([[4, 2, 0],
...               [9, 3, 7],
...               [1, 2, 1]])
>>>
>>> b = np.linalg.inv(a)
>>> b
array([[ 0.22916667,  0.04166667, -0.29166667],
       [ 0.04166667, -0.08333333,  0.58333333],
       [-0.3125    ,  0.125     ,  0.125     ]])
>>>
>>> np.dot(a, b)
array([[1.00000000e+00, 5.55111512e-17, 0.00000000e+00],
       [0.00000000e+00, 1.00000000e+00, 2.22044605e-16],
       [0.00000000e+00, 1.38777878e-17, 1.00000000e+00]])


Singular value decomposition of a matrix
----------------------------------------
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6],
...               [7, 8, 9]])
>>>
>>> U, s, Vh = np.linalg.svd(a)
>>>
>>> U
array([[-0.21483724,  0.88723069,  0.40824829],
       [-0.52058739,  0.24964395, -0.81649658],
       [-0.82633754, -0.38794278,  0.40824829]])
>>>
>>> s
array([1.68481034e+01, 1.06836951e+00, 3.33475287e-16])
>>>
>>> Vh
array([[-0.47967118, -0.57236779, -0.66506441],
       [-0.77669099, -0.07568647,  0.62531805],
       [-0.40824829,  0.81649658, -0.40824829]])


Linear Algebra
--------------
.. csv-table:: Linear algebra basics
    :header: "Function", "Description"

    "norm", "Vector or matrix norm"
    "inv", "Inverse of a square matrix"
    "solve", "Solve a linear system of equations"
    "det", "Determinant of a square matrix"
    "slogdet", "Logarithm of the determinant of a square matrix"
    "lstsq", "Solve linear least-squares problem"
    "pinv", "Pseudo-inverse (Moore-Penrose) calculated using a singular value decomposition"
    "matrix_power", "Integer power of a square matrix"
    "matrix_rank", "Calculate matrix rank using an SVD-based method"

.. csv-table:: Eigenvalues and decompositions
    :header: "Function", "Description"

    "eig", "Eigenvalues and vectors of a square matrix"
    "eigh", "Eigenvalues and eigenvectors of a Hermitian matrix"
    "eigvals", "Eigenvalues of a square matrix"
    "eigvalsh", "Eigenvalues of a Hermitian matrix"
    "qr", "QR decomposition of a matrix"
    "svd", "Singular value decomposition of a matrix"
    "cholesky", "Cholesky decomposition of a matrix"

.. csv-table:: Tensor operations
    :header:  "Function", "Description"

    "tensorsolve", "Solve a linear tensor equation"
    "tensorinv", "Calculate an inverse of a tensor"

.. csv-table:: Exceptions
    :header: "Function", "Description"

    "LinAlgError", "Indicates a failed linear algebra operation"


Assignments
-----------
.. figure:: img/algebra-euclidean-distance.png

    Calculate Euclidean distance in Cartesian coordinate system

* :math:`distance(a, b) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}`
* :math:`distance(a, b) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + ... + (n_2 - n_1)^2}`

.. literalinclude:: assignments/numpy_algebra_euclidean_2d.py
    :caption: :download:`Solution <assignments/numpy_algebra_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/numpy_algebra_euclidean_ndim.py
    :caption: :download:`Solution <assignments/numpy_algebra_b.py>`
    :end-before: # Solution
