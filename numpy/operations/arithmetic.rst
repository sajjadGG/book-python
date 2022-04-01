Array Arithmetic
================


.. glossary::

    Scalar
        Single Value

    Vectorized Operations
        Single statement without a loop that explains a looping concept.
        Applies operation to each element.

        >>> import numpy as np
        >>> a = np.array([1, 2, 3])
        >>>
        >>> a + 1
        array([2, 3, 4])


SetUp
-----
>>> import numpy as np


Addition
--------
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> a + 2
array([[3, 4, 5],
       [6, 7, 8]])


Subtraction
-----------
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> a - 2
array([[-1,  0,  1],
       [ 2,  3,  4]])


Division
--------
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])

True division:

>>> a / 2
array([[0.5, 1. , 1.5],
       [2. , 2.5, 3. ]])

Floor division:

>>> a // 2
array([[0, 1, 1],
       [2, 2, 3]])

Modulo:

>>> a % 2
array([[1, 0, 1],
       [0, 1, 0]])


Multiplication
--------------
* Scalar multiplication

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> a * 2
array([[ 2,  4,  6],
       [ 8, 10, 12]])


Power
-----
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> a ** 2
array([[ 1,  4,  9],
       [16, 25, 36]])
>>>
>>> np.power(a, 2)
array([[ 1,  4,  9],
       [16, 25, 36]])

Performance:

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... a ** 2
522 ns ± 78.6 ns per loop (mean ± std. dev. of 1000 runs, 1000 loops each)

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... np.power(a, 2)
684 ns ± 83.4 ns per loop (mean ± std. dev. of 1000 runs, 1000 loops each)


Roots
-----
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> a ** (1/2)
array([[1.        , 1.41421356, 1.73205081],
       [2.        , 2.23606798, 2.44948974]])
>>>
>>> np.sqrt(a)
array([[1.        , 1.41421356, 1.73205081],
       [2.        , 2.23606798, 2.44948974]])

Performance:

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... a ** (1/2)
1.79 µs ± 217 ns per loop (mean ± std. dev. of 1000 runs, 1000 loops each)

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... np.sqrt(a)
855 ns ± 89.3 ns per loop (mean ± std. dev. of 1000 runs, 1000 loops each)


.. todo:: Assignments
