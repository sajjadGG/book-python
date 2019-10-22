Arrays
======


Data Structures
---------------
* Skalar - jednowymiarowa
* Wektor - dwuwymiarowa
* Tensor - trójwymiarowa
* Tablica - czterowymiarowa
* Macierz - n-wymiarowa

Create array
------------
* From list:

    .. code-block:: python

        import numpy as np

        np.array([1, 2, 3])
        # [1, 2, 3]

        np.array([1, 4, 5, 8], float)
        # array([ 1., 4., 5., 8.])

        np.array([[1,2], [3,4]])
        # array([[1, 2],
        #        [3, 4]])

* Generate array:

    .. code-block:: python

        import numpy as np

        np.arange(3)
        # array([0, 1, 2])

        np.arange(3.0)
        # array([ 0.,  1.,  2.])

        np.arange(3, 7)
        # array([3, 4, 5, 6])

        np.arange(3, 7, step=2)
        # array([3, 5])

        np.arange(start=3, stop=7, step=2, dtype=float)
        # array([3., 5.])

Slice array
-----------
.. code-block:: python

    np.array([1, 4, 5, 8], float)
    # array([ 1., 4., 5., 8.])

    a[:2]
    # array([ 1., 4.])

    a[3]
    # 8.0

    a[0] = 5.
    # array([ 5., 4., 5., 8.])

.. code-block:: python

    a = np.array([[1, 2, 3], [4, 5, 6]], float)
    # array([[ 1., 2., 3.], [ 4., 5., 6.]])

    a[0,0]  # 1.0
    a[0,1]  # 2.0

.. code-block:: python

    a = np.array([[1, 2, 3], [4, 5, 6]], float)

    a[1,:]      # array([ 4., 5., 6.])
    a[:,2]      # array([ 3., 6.])
    a[-1:,-2:]  # array([[ 5., 6.]])

Array shape
-----------
.. code-block:: python

    a = np.array([[1, 2, 3], [4, 5, 6]], float)

    a.shape  # (2, 3)
    a.dtype  # dtype('float64')

.. code-block:: python

    a = np.array([[1, 2, 3], [4, 5, 6]], int)

    a.astype(float)
    a.dtype  # dtype('float64')

.. code-block:: python

    a = np.array([[1, 2, 3], [4, 5, 6]], float)

    len(a)  # 2

.. code-block:: python

    a = np.array([[1, 2, 3], [4, 5, 6]], float)

    2 in a
    # True

    0 in a
    # False

.. code-block:: python

    a = np.array(range(10), float)
    # array([ 0., 1., 2., 3., 4., 5., 6., 7., 8., 9.])

    a = a.reshape((5, 2))
    # array([[ 0., 1.],
    #        [ 2., 3.],
    #        [ 4., 5.],
    #        [ 6., 7.],
    #        [ 8., 9.]])

    a.shape
    # (5, 2)

.. code-block:: python

    a = np.array([1, 2, 3], float)

    b = a
    c = a.copy()

    a[0] = 0
    # array([0., 2., 3.])

    b
    # array([0., 2., 3.])

    c
    # array([1., 2., 3.])

.. code-block:: python

    a = np.array([1, 2, 3], float)

    a.tolist()
    # [1.0, 2.0, 3.0]

    list(a)
    # [1.0, 2.0, 3.0]

.. code-block:: python

    a = np.array([1, 2, 3], float)

    s = a.tostring()
    # '\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x08@'

    np.fromstring(s)
    # array([ 1., 2., 3.])

Array modification
------------------
.. code-block:: python

    a = np.array([1, 2, 3], float)
    # array([ 1., 2., 3.])

    a.fill(0)
    # array([ 0., 0., 0.])

.. code-block:: python

    a = np.array(range(6), float).reshape((2, 3))
    # array([[ 0., 1., 2.],
    #        [ 3., 4., 5.]])

    a.transpose()
    # array([[ 0., 3.],
    #        [ 1., 4.],
    #        [ 2., 5.]])

.. code-block:: python

    a = np.array([[1, 2, 3], [4, 5, 6]], float)
    # array([[ 1., 2., 3.],
    #        [ 4., 5., 6.]])

    a.flatten()
    # array([ 1., 2., 3., 4., 5., 6.])

.. code-block:: python

    a = np.array(range(6), float).reshape((2, 3, 1))
    # array([[[0.],
    #         [1.],
    #         [2.]],
    #
    #        [[3.],
    #         [4.],
    #         [5.]]])

Concatenation
-------------
.. code-block:: python

    a = np.array([1,2], float)
    b = np.array([3,4,5,6], float)
    c = np.array([7,8,9], float)

    np.concatenate((a, b, c))
    # array([1., 2., 3., 4., 5., 6., 7., 8., 9.])

.. code-block:: python

    a = np.array([[1, 2], [3, 4]], float)
    b = np.array([[5, 6], [7,8]], float)

    np.concatenate((a,b))
    # array([[ 1., 2.],
    #        [ 3., 4.],
    #        [ 5., 6.],
    #        [ 7., 8.]])

    np.concatenate((a,b), axis=0)
    # array([[ 1., 2.],
    #        [ 3., 4.],
    #        [ 5., 6.],
    #        [ 7., 8.]])

    np.concatenate((a,b), axis=1)
    # array([[ 1., 2., 5., 6.],
    #        [ 3., 4., 7., 8.]])

.. code-block:: python

    a = np.array([1, 2, 3], float)
    # array([1., 2., 3.])

    a[:,np.newaxis]
    # array([[ 1.],
    #        [ 2.],
    #        [ 3.]])

    a[:,np.newaxis].shape
    # (3,1)

    b[np.newaxis,:]
    # array([[ 1., 2., 3.]])

    b[np.newaxis,:].shape
    # (1,3)

.. code-block:: python

    n1 = np.array([1,2,3])
    n2 = np.array([[1,2],[3,4]])

    f'Wymiar: n1: {n1.ndim}, n2: {n2.ndim}'
    # Wymiar: n1: 1, n2: 2

    f'Kształt: n1: {n1.shape}, n2: {n2.shape}'
    # Kształt: n1: (3,), n2: (2, 2)

    f'Rozmiar: n1: {n1.size}, n2: {n2.size}'
    # Rozmiar: n1: 3, n2: 4

    f'Typ: n1: {n1.dtype}, n2: {n2.dtype}'
    # Typ: n1: int32, n2: int32

    f'Rozmiar elementu (w bajtach): n1: {n1.itemsize}, n2: {n2.itemsize}'
    # Rozmiar elementu (w bajtach): n1: 4, n2: 4

    f'Wskaźnik do danych: n1: {n1.data}, n2: {n2.data}'
    # Wskaźnik do danych: n1: <memory at 0x000001B93EC75348>, n2: <memory at 0x000001B93EC5BB40>


W przeciwieństwie do kolekcji, tablice mogą mieć tylko jeden typ elementu, choć może być złożony
https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html

.. code-block:: python

    for v in [1, 1., 1j]:
       a = np.array([v])
       print('Tablica: {}, typ: {}'.format(a, a.dtype))

    # Można też wymusić typ przy tworzeniu tablicy
    a = np.array([1], dtype=str)

    f'Tablica: {a}, typ: {a.dtype}'
    # Tablica: [1], typ: int32
    # Tablica: [1.], typ: float64
    # Tablica: [0.+1.j], typ: complex128
    # Tablica: ['1'], typ: <U1

.. code-block:: python

    np.arange(1,10)
    # [1 2 3 4 5 6 7 8 9]

    np.zeros((2,3))
    # [[0. 0. 0.]
    #  [0. 0. 0.]]

    np.ones((3,2))
    # [[1. 1.]
    #  [1. 1.]
    #  [1. 1.]]

    np.empty((2,7))  # Bez inicjalizacji
    # [[1.01855798e-312 1.18831764e-312 1.01855798e-312 9.54898106e-313
    #   1.06099790e-312 1.03977794e-312 1.23075756e-312]
    # [1.20953760e-312 1.06099790e-312 9.76118064e-313 1.01855798e-312
    #  1.01855798e-312 1.16709769e-312 4.44659081e-322]]

    np.random.rand(2,2)
    # [[0.6468727  0.76909227]
    #  [0.89730518 0.13993221]]

.. code-block:: python

    a = np.array([[1, 2, 3], [4, 5, 6]], float)

    np.zeros_like(a)
    # array([[ 0., 0., 0.],
    #        [ 0., 0., 0.]])

    np.ones_like(a)
    # array([[ 1., 1., 1.],
    #        [ 1., 1., 1.]])

    np.identity(4, dtype=float)
    # array([[ 1., 0., 0., 0.],
    #        [ 0., 1., 0., 0.],
    #        [ 0., 0., 1., 0.],
    #        [ 0., 0., 0., 1.]])

Array slicing
-------------
.. code-block:: python

    n1 = np.array([1,2,3])
    n2 = np.array([[1,2],[3,4]])

    n1[1], n2[1][1]
    # 2 4

    n2[1,1]
    # 4

    n2[1,:]
    # [3 4]

    n2[:,1]
    # [2 4]

    n2[1,:1]
    # [3]

.. code-block:: python

    a = np.random.randint(100,size=(2,3))
    # [[38  5 91]
    #  [26 33 65]]

    2*a
    # [[ 76  10 182]
    #  [ 52  66 130]]

    a**2
    # [[1444   25 8281]
    #  [ 676 1089 4225]]

    a*a
    # [[1444   25 8281]
    #  [ 676 1089 4225]]

Array math operations
---------------------
.. code-block:: python

    a = np.array([1,2,3], float)
    b = np.array([5,2,6], float)

    a + b
    # array([6., 4., 9.])

    a - b
    # array([-4., 0., -3.])

    a * b
    # array([5., 4., 18.])

    b / a
    # array([5., 1., 2.])

    a % b
    # array([1., 0., 3.])

    b**a
    # array([5., 4., 216.])

.. code-block:: python

    a = np.array([[1,2], [3,4]], float)
    b = np.array([[2,0], [1,3]], float)

    a * b
    # array([[2., 0.], [3., 12.]])

.. warning:: For two-dimensional arrays, multiplication ``*`` remains elementwise and does not correspond to matrix multiplication.

Array Multiplication
--------------------
.. code-block:: text

    a = np.array([[1, 0], [0, 1]])
    b = np.array([[4, 1], [2, 2]])

    a @ b
    # [[4, 1], [2, 2]]

.. code-block:: python

    a = np.array([1,2,3], float)
    b = np.array([4,5], float)

    a + b
    # ValueError: shape mismatch: objects cannot be broadcast to a single shape

.. code-block:: python

    a = np.array([[1, 2], [3, 4], [5, 6]], float)
    # array([[ 1., 2.],
    #  [ 3., 4.],
    #  [ 5., 6.]])

    b = np.array([-1, 3], float)
    # array([-1., 3.])

    a + b
    # array([[ 0., 5.],
    #  [ 2., 7.],
    #  [ 4., 9.]])

.. code-block:: python

    a = np.zeros((2,2), float)
    # array([[ 0., 0.],
    #        [ 0., 0.]])

    b = np.array([-1., 3.], float)
    # array([-1., 3.])

    a + b
    # array([[-1., 3.],
    #        [-1., 3.]])

    a + b[np.newaxis,:]
    # array([[-1., 3.],
    #        [-1., 3.]])

    a + b[:,np.newaxis]
    # array([[-1., -1.],
    #        [ 3., 3.]])

.. code-block:: python

    a = np.array([1.1, 1.5, 1.9], float)

    np.sqrt(a)
    # array([ 1., 2., 3.])

    np.floor(a)
    # array([ 1., 1., 1.])

    np.ceil(a)
    # array([ 2., 2., 2.])

    np.rint(a)
    # array([ 1., 2., 2.])

.. code-block:: python

    np.pi
    # 3.1415926535897931

    np.e
    # 2.7182818284590451

    np.nan
    # NaN

    np.inf
    # inf

Array iteration
---------------
.. code-block:: python

    >>> a = np.array([1, 4, 5], int)

    for x in a:
        print(x)

    # 1
    # 4
    # 5

.. code-block:: python

    a = np.array([[1, 2], [3, 4], [5, 6]], float)

    for x in a:
        print(x)

    # [ 1. 2.]
    # [ 3. 4.]
    # [ 5. 6.]

Array operations
----------------
.. code-block:: python

    a = np.array([2, 4, 3], float)

    a.sum()
    # 9.0

    a.prod()
    # 24.0

.. code-block:: python

    a = np.array([2, 1, 9], float)

    a.mean()
    # 4.0

    a.var()
    # 12.666666666666666

    a.std()
    # 3.5590260840104371

    a.min()
    # 1.0

    a.max()
    # 9.0

    a.argmin()  # index of an ``a.min()`` element in array
    # 1

    a.argmax()  # index of an ``a.max()`` element in array
    # 2

.. code-block:: python

    a = np.array([[0, 2], [3, -1], [3, 5]], float)

    a.mean(axis=0)
    # array([ 2., 2.])

    a.mean(axis=1)
    # array([ 1., 1., 4.])

    a.min(axis=1)
    # array([ 0., -1., 3.])

    a.max(axis=0)
    # array([ 3., 5.])

.. code-block:: python

    a = np.array([6, 2, 5, -1, 0], float)

    sorted(a)
    # [-1.0, 0.0, 2.0, 5.0, 6.0]

    a.sort()
    # array([-1., 0., 2., 5., 6.])

.. code-block:: python

    a = np.array([6, 2, 5, -1, 0], float)

    a.clip(0, 5)
    # array([ 5., 2., 5., 0., 0.])

.. code-block:: python

    a = np.array([1, 1, 4, 5, 5, 5, 7], float)

    np.unique(a)
    # array([ 1., 4., 5., 7.])

.. code-block:: python

    a = np.array([[1, 2], [3, 4]], float)

    a.diagonal()
    # array([ 1., 4.])

Array arithmetic
----------------
.. code-block:: python

    a = np.array([[1,2], [3,4]], float)
    b = np.array([[2,0], [1,3]], float)

    a * b
    # array([[2., 0.], [3., 12.]])

.. code-block:: python

    a = np.array([1,2,3], float)
    b = np.array([4,5], float)

    a + b
    # ValueError: shape mismatch: objects cannot be broadcast to a single shape

.. code-block:: python

    a = np.array([[1, 2], [3, 4], [5, 6]], float)
    b = np.array([-1, 3], float)

    a
    # array([[ 1., 2.],
    #        [ 3., 4.],
    #        [ 5., 6.]])

    b
    # array([-1., 3.])

    a + b
    # array([[ 0., 5.],
    #        [ 2., 7.],
    #        [ 4., 9.]])

.. code-block:: python

    a = np.zeros((2,2), float)
    # array([[ 0., 0.],
    #        [ 0., 0.]])

    b = np.array([-1., 3.], float)
    # array([-1., 3.])

    a + b
    # array([[-1., 3.],
    #        [-1., 3.]])

    a + b[np.newaxis,:]
    # array([[-1., 3.],
    #        [-1., 3.]])

    a + b[:,np.newaxis]
    # array([[-1., -1.],
    #        [ 3., 3.]])
