Sequence Comparison
===================
* ``tuple`` - fast and memory efficient
* ``list`` - extensible and flexible
* ``set`` - very fast lookup


Tuple
-----
* Immutable - cannot add, modify or remove items
* Stores elements of any type
* Keeps order of inserting elements
* Possible to getitem and slice
* Elements can duplicate
* One contingent block of data in memory


List
----
* Mutable - can add, remove, and modify items
* Stores elements of any type
* Keeps order of inserting elements
* Possible to getitem and slice
* Elements can duplicate
* Implemented in memory as list of references to objects
* Objects are scattered in memory


Set
---
* Mutable - can add, remove, and modify items
* Stores only **hashable** elements (int, float, bool, None, str, tuple)
* Does not keep order of inserting elements
* It is not possible to getitem and slice
* Elements cannot duplicate
* Set is unordered data structure and do not record element position or insertion


Memory Footprint
----------------
>>> from sys import getsizeof
>>>
>>>
>>> getsizeof( (1,2,3) )
64
>>>
>>> getsizeof( [1,2,3] )
80
>>>
>>> getsizeof( {1,2,3} )
216


Memory
------
.. figure:: img/memory-compare.png

    Memory representation for ``list`` and ``tuple``


Performance
-----------
* ``O(n)`` - lookup (contains) in list and tuple
* ``O(1)`` - lookup (contains) in set
* [#pywikiTimeComplexity]_

>>> %%timeit -r 10_000 -n 10_000  # doctest: +SKIP
... 0 in (1, 2, 3)
...
48 ns ± 6.57 ns per loop (mean ± std. dev. of 10000 runs, 10,000 loops each)
>>>
>>> %%timeit -r 10_000 -n 10_000  # doctest: +SKIP
... 0 in [1, 2, 3]
...
49.1 ns ± 6.39 ns per loop (mean ± std. dev. of 10000 runs, 10,000 loops each)
>>>
>>> %%timeit -r 10_000 -n 10_000  # doctest: +SKIP
... 0 in {1, 2, 3}
...
27.2 ns ± 3.97 ns per loop (mean ± std. dev. of 10000 runs, 10,000 loops each)

>>> %%timeit -r 10_000 -n 10_000  # doctest: +SKIP
... 0 in (1, 2, 3, 4, 5, 6, 7, 8, 9)
...
99.2 ns ± 12.2 ns per loop (mean ± std. dev. of 10000 runs, 10,000 loops each)
>>>
>>> %%timeit -r 10_000 -n 10_000  # doctest: +SKIP
... 0 in [1, 2, 3, 4, 5, 6, 7, 8, 9]
...
98.5 ns ± 12.2 ns per loop (mean ± std. dev. of 10000 runs, 10,000 loops each)
>>>
>>> %%timeit -r 10_000 -n 10_000  # doctest: +SKIP
... 0 in {1, 2, 3, 4, 5, 6, 7, 8, 9}
...
27.8 ns ± 4.21 ns per loop (mean ± std. dev. of 10000 runs, 10,000 loops each)


References
----------
.. [#pywikiTimeComplexity] https://wiki.python.org/moin/TimeComplexity


.. todo:: Assignments
