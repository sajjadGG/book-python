FuncProg Pure Functions
=======================


Rationale
---------
* Pure functions have no side effects (i.e. memory, state, I/O)

* Calling the pure function again with the same arguments returns the same
  result (this can enable caching optimizations such as memoization)

* If the result of a pure expression is not used,
  it can be removed without affecting other expressions

* If there is no data dependency between two pure expressions, their order
  can be reversed, or they can be performed in parallel and they cannot
  interfere with one another (the evaluation of any pure expression is
  thread-safe) [#WikipediaFunc]_


Pure Function
-------------
>>> def add(a, b):
...     return a + b
>>>
>>>
>>> add(1, 2)
3
>>> add(1, 2)
3
>>> add(1, 2)
3


Impure Function
---------------
>>> c = 3
>>>
>>>
>>> def add(a, b):
...     return a + b + c
>>>
>>>
>>> add(1, 2)
6
>>> add(1, 2)
6
>>> add(1, 2)
6
>>>
>>> c = 4
>>>
>>> add(1, 2)
7
>>> add(1, 2)
7
>>> add(1, 2)
7


Impure to Pure Function
-----------------------
>>> c = 3
>>>
>>>
>>> def add(a, b, c):
...     return a + b + c
>>>
>>>
>>> add(1, 2, c)
6
>>> add(1, 2, c)
6
>>> add(1, 2, c)
6
>>>
>>> c = 4
>>>
>>> add(1, 2, c)
7
>>> add(1, 2, c)
7
>>> add(1, 2, c)
7


Use Case 1
----------
Mathematical functions are pure in general

>>> def add(a, b):
...     return a + b

>>> def odd(x):
...     return x % 2

>>> def cube(x):
...     return x ** 3


Use Case 2
----------
Pure:

>>> DATA = [(5.8, 2.7, 5.1, 1.9, 'virginica'),
...         (5.1, 3.5, 1.4, 0.2, 'setosa'),
...         (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...         (6.3, 2.9, 5.6, 1.8, 'virginica'),
...         (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...         (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>>
>>> def function(data, species):
...     result = []
...     for *features, label in data:
...         if label == species:
...             result.append(features)
...     return result

Impure:

>>> DATA = [(5.8, 2.7, 5.1, 1.9, 'virginica'),
...         (5.1, 3.5, 1.4, 0.2, 'setosa'),
...         (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...         (6.3, 2.9, 5.6, 1.8, 'virginica'),
...         (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...         (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>>
>>> def function(species):
...     result = []
...     for *features, label in DATA:
...         if label == species:
...             result.append(features)
...     return result


References
----------
.. [#WikipediaFunc] Functional programming. Retrieved: 2020-10-09. URL: https://en.wikipedia.org/wiki/Functional_programming
