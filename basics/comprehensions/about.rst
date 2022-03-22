Comprehension About
===================
* Loop leaks out values

>>> result = []
>>>
>>> for x in range(0,5):
...     result.append(x)
>>>
>>> print(result)
[0, 1, 2, 3, 4]
>>>
>>> x
4

>>> result = [x for x in range(0,5)]
>>>
>>> print(result)
[0, 1, 2, 3, 4]
>>>
>>> x  # doctest: +SKIP
Traceback (most recent call last):
NameError: name 'x' is not defined


Syntax
------
Abstract Syntax:

>>> # doctest: +SKIP
... result = [<RETURN> for <VARIABLE> in <ITERABLE>]

Short syntax:

>>> [x for x in range(0,5)]
[0, 1, 2, 3, 4]

Long syntax:

>>> list(x for x in range(0,5))
[0, 1, 2, 3, 4]


Microbenchmark
--------------
>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = []
... for x in range(0,5):
...     result.append(x)
...
457 ns ± 69.4 ns per loop (mean ± std. dev. of 1000 runs, 1000 loops each)

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = [x for x in range(0,5)]
...
411 ns ± 76.6 ns per loop (mean ± std. dev. of 1000 runs, 1000 loops each)


Good Practices
--------------
* Use shorter variable names
* ``x`` is common name


Assignments
-----------
.. literalinclude:: assignments/comprehension_about_a.py
    :caption: :download:`Solution <assignments/comprehension_about_a.py>`
    :end-before: # Solution
