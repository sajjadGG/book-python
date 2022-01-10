Array Create
============


Rationale
---------


SetUp
-----
>>> import numpy as np


Declare
-------
1-dimensional Array:

>>> np.array([1, 2, 3])
array([1, 2, 3])
>>>
>>> np.array([1.0, 2.0, 3.0])
array([1., 2., 3.])
>>>
>>> np.array([1.1, 2.2, 3.3])
array([1.1, 2.2, 3.3])
>>>
>>> np.array([1, 2, 3], float)
array([1., 2., 3.])
>>>
>>> np.array([1, 2, 3], dtype=float)
array([1., 2., 3.])

2-dimensional Array:

>>> np.array([[1, 2, 3],
...           [4, 5, 6],
...           [7, 8, 9]])
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])

3-dimensional Array:

>>> np.array([[[1, 2, 3],
...            [4, 5, 6],
...            [7, 8, 9]],
...
...           [[1, 2, 3],
...            [4, 5, 6],
...            [7, 8, 9]]])
...
array([[[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]],
<BLANKLINE>
       [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]])

.. figure:: img/numpy-create-cake.png

    Multi layer cake as an analog for n-dim array [#CAKE]_


Array range
-----------
Array from Python ``range()``:

>>> np.array(range(5))
array([0, 1, 2, 3, 4])
>>>
>>> np.array(range(5), float)
array([0., 1., 2., 3., 4.])
>>>
>>> np.array(range(5, 10))
array([5, 6, 7, 8, 9])
>>>
>>> np.array(range(5, 10), float)
array([5., 6., 7., 8., 9.])
>>>
>>> np.array(range(5, 10, 2))
array([5, 7, 9])
>>>
>>> np.array(range(5, 10, 2), float)
array([5., 7., 9.])

Array from Python comprehension:

>>> np.array([x for x in range(5)])
array([0, 1, 2, 3, 4])
>>>
>>> np.array([x for x in range(5)], float)
array([0., 1., 2., 3., 4.])
>>>
>>> np.array([x for x in range(5, 10)])
array([5, 6, 7, 8, 9])
>>>
>>> np.array([x for x in range(5, 10)], float)
array([5., 6., 7., 8., 9.])
>>>
>>> np.array([x for x in range(5, 10, 2)])
array([5, 7, 9])
>>>
>>> np.array([x for x in range(5, 10, 2)], float)
array([5., 7., 9.])

Array from ``np.arange()``:

>>> np.arange(5)
array([0, 1, 2, 3, 4])
>>>
>>> np.arange(5, dtype=float)
array([0., 1., 2., 3., 4.])
>>>
>>> np.arange(5.0)
array([0., 1., 2., 3., 4.])
>>>
>>> np.arange(5, 10)
array([5, 6, 7, 8, 9])
>>>
>>> np.arange(5, 10, step=2)
array([5, 7, 9])
>>>
>>> np.arange(start=5, stop=10, step=2)
array([5, 7, 9])
>>>
>>> np.arange(start=5, stop=10, step=2, dtype=float)
array([5., 7., 9.])
>>>
>>> np.arange(0.0, 1.0, 0.1)
array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
>>>
>>> np.arange(0.0, 1.0, 0.2)
array([0. , 0.2, 0.4, 0.6, 0.8])
>>>
>>> np.arange(0.0, 1.0, 0.3)
array([0. , 0.3, 0.6, 0.9])


Linspace
--------
>>> # doctest: +SKIP
... def linspace(self,
...              start=...,
...              stop=...,
...              num=50,
...              endpoint=True,
...              retstep=False,
...              dtype=None
...              axis=0
... ) -> np.ndarray: ...

Return evenly spaced numbers over a specified interval.

>>> np.linspace(2.0, 3.0, num=5)
array([2.  , 2.25, 2.5 , 2.75, 3.  ])
>>>
>>> np.linspace(2.0, 3.0, num=5, endpoint=False)
array([2. , 2.2, 2.4, 2.6, 2.8])

>>> data, step = np.linspace(2.0, 3.0, num=5, retstep=True)
>>>
>>> data
array([2.  , 2.25, 2.5 , 2.75, 3.  ])
>>>
>>> step
0.25


Zeros
-----
>>> np.zeros((2, 3))
array([[0., 0., 0.],
       [0., 0., 0.]])
>>>
>>> np.zeros(shape=(2, 3))
array([[0., 0., 0.],
       [0., 0., 0.]])

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> np.zeros_like(a)
array([[0, 0, 0],
       [0, 0, 0]])

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]], float)
>>>
>>> np.zeros_like(a)
array([[0., 0., 0.],
       [0., 0., 0.]])


Ones
----
>>> np.ones((3, 2))
array([[1., 1.],
       [1., 1.],
       [1., 1.]])
>>>
>>> np.ones(shape=(3, 2))
array([[1., 1.],
       [1., 1.],
       [1., 1.]])

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> np.ones_like(a)
array([[1, 1, 1],
       [1, 1, 1]])

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]], float)
>>>
>>> np.ones_like(a)
array([[1., 1., 1.],
       [1., 1., 1.]])


Empty
-----
* Garbage from memory
* Will reuse previous if given shape was already created

>>> np.empty((3,4))  # doctest: +SKIP
array([[ 2.31584178e+077,  1.29073692e-231,  2.96439388e-323, 0.00000000e+000],
      [-2.32034891e+077,  2.68678047e+154,  2.18018101e-314, 2.18022275e-314],
      [ 0.00000000e+000,  2.18023445e-314,  1.38338381e-322, 9.03690495e-309]])

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> np.empty((2,3))
array([[1., 2., 3.],
       [4., 5., 6.]])

>>> a = np.array([[1, 2, 3],
...               [4, 5, 6]])
>>>
>>> np.empty_like(a)
array([[1, 2, 3],
       [4, 5, 6]])


Full
----
>>> np.full((2, 2), np.inf)
array([[inf, inf],
       [inf, inf]])
>>>
>>> np.full((2, 2), 10)
array([[10, 10],
       [10, 10]])


Identity
--------
>>> np.identity(2)
array([[1., 0.],
       [0., 1.]])
>>>
>>> np.identity(3)
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
>>>
>>> np.identity(4, int)
array([[1, 0, 0, 0],
       [0, 1, 0, 0],
       [0, 0, 1, 0],
       [0, 0, 0, 1]])


Stringify
---------
>>> a = np.array([[1, 2, 3],
...               [4, 5, 6],
...               [7, 8, 9]])
>>>
>>> str(a)
'[[1 2 3]\n [4 5 6]\n [7 8 9]]'
>>>
>>> print(a)
[[1 2 3]
 [4 5 6]
 [7 8 9]]
>>>
>>> repr(a)
'array([[1, 2, 3],\n       [4, 5, 6],\n       [7, 8, 9]])'
>>>
>>> a
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>>
>>> print(repr(a))
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])


Recap
-----
>>> a = np.array([1, 2, 3])
>>> b = np.array(range(0, 10))
>>> c = np.arange(0, 10, 2)
>>> d = np.linspace(0, 10, 100)
>>> e = np.zeros(shape=(2,3))
>>> f = np.zeros_like(a)
>>> g = np.ones(shape=(2,3))
>>> h = np.ones_like(a)
>>> i = np.empty(shape=(2,3))
>>> j = np.empty_like(a)
>>> k = np.full(shape=(2, 2), fill_value=np.nan)
>>> l = np.full_like(a, np.nan)
>>> m = np.identity(4)


Performance
-----------
>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = np.arange(0, 100, step=2, dtype=float)
651 ns ± 86.5 ns per loop (mean ± std. dev. of 1000 runs, 1000 loops each)

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = np.array(range(0, 100, 2), dtype=float)
4.38 µs ± 341 ns per loop (mean ± std. dev. of 1000 runs, 1000 loops each)

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = np.array([x for x in range(0, 100) if x % 2 == 0], dtype=float)
8.25 µs ± 534 ns per loop (mean ± std. dev. of 1000 runs, 1000 loops each)

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = np.array([float(x) for x in range(0, 100) if x % 2 == 0])
10.8 µs ± 718 ns per loop (mean ± std. dev. of 1000 runs, 1000 loops each)

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = np.array([float(x) for x in range(0, 100, 2)])
6.81 µs ± 443 ns per loop (mean ± std. dev. of 1000 runs, 1000 loops each)

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = np.array([x for x in range(0, 100, 2)], dtype=float)
4.38 µs ± 349 ns per loop (mean ± std. dev. of 1000 runs, 1000 loops each)


References
----------
.. [#CAKE] https://i.ytimg.com/vi/iCOhz07Ng6g/maxresdefault.jpg


Assignments
-----------
.. literalinclude:: assignments/numpy_create_a.py
    :caption: :download:`Solution <assignments/numpy_create_a.py>`
    :end-before: # Solution
