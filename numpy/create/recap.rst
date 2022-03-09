Array Create Recap
==================


SetUp
-----
>>> import numpy as np


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


Rationale
---------
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


.. todo:: Assignments
