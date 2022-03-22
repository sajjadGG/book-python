Type Annotation Sequence
========================
* Before Python 3.9 you need ``from typing import List, Tuple, Set, Frozenset``
* Since Python 3.9: :pep:`585` -- Type Hinting Generics In Standard Collections

>>> DATA = [(5.8, 2.7, 5.1, 1.9, 'virginica'),
...         (5.1, 3.5, 1.4, 0.2, 'setosa'),
...         (5.7, 2.8, 4.1, 1.3, 'versicolor')]
>>>
>>> x = DATA[0][-1]
>>> x  # doctest: +SKIP
>>> # IDE don't know what type is species
>>> # and cannot give hints for autocompletion

>>> DATA = [(5.8, 2.7, 5.1, 1.9, 'virginica'),
...         (5.1, 3.5, 1.4, 0.2, 'setosa'),
...         (5.7, 2.8, 4.1, 1.3, 'versicolor')]
>>>
>>> x: str = DATA[0][-1]
>>> x  # doctest: +SKIP
>>> # IDE knows exactly what type is species
>>> # and what methods hint for autocompletion


Tuple
-----
Generic type annotation:

>>> data: tuple = ()
>>> data: tuple = tuple()
>>> data: tuple = 'a', 2, 3.3
>>> data: tuple = ('a', 2, 3.3)

Strict type annotation:

>>> data: tuple[int, int, int] = (1, 2, 3)
>>> data: tuple[str, str, str] = ('setosa', 'virginica', 'versicolor')
>>> data: tuple[str, int, float] = ('a', 2, 3.3)
>>> data: tuple[int, ...] = (1, 2, 3)
>>> data: tuple[str, ...] = ('setosa', 'virginica', 'versicolor')


List
----
Generic type annotation:

>>> data: list = list()
>>> data: list = []
>>> data: list = ['a', 1, 2.2]

Strict type annotation:

>>> data: list[int] = [1, 2, 3, 4]
>>> data: list[float] = [5.8, 2.7, 5.1, 1.9]
>>> data: list[str] = ['a', 'b', 'c', 'd']


Set
---
Generic type annotation:

>>> data: set = set()
>>> data: set = {'a', 1, 2.2}

Strict type annotation:

>>> data: set[int] = {1, 2, 3}
>>> data: set[float] = {0.0, 1.1, 2.2}
>>> data: set[str] = {'a', 'b', 'c'}


Frozenset
---------
Generic type annotation:

>>> data: frozenset = set()
>>> data: frozenset = {'a', 1, 2.2}

Strict type annotation:

>>> data: frozenset[int] = {1, 2, 3}
>>> data: frozenset[float] = {0.0, 1.1, 2.2}
>>> data: frozenset[str] = {'a', 'b', 'c'}


List of Tuples
--------------
Generic type annotation:

>>> data: list[tuple] = [
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...     (7.6, 3.0, 6.6, 2.1, 'virginica')]

Strict type annotation:

>>> data: list[tuple[float, float, float, float, str]] = [
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...     (7.6, 3.0, 6.6, 2.1, 'virginica')]


List of Lists
-------------
Generic type annotation:

>>> data: list[list] = [
...     [1, 2, 3],
...     [4, 5, 6],
...     [7, 8, 9]]

Strict type annotation:

>>> data: list[list[int]] = [
...     [1, 2, 3],
...     [4, 5, 6],
...     [7, 8, 9]]


Aliases
-------
Generic type annotation:

>>> GeographicCoordinate = tuple[float, float]
>>>
>>> locations: list[GeographicCoordinate] = [
...     (25.91375, -60.15503),
...     (-11.01983, -166.48477),
...     (-11.01983, -166.48477)]

>>> Iris = tuple[float, float, float, float, str]
>>>
>>> data: list[Iris] = [
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...     (7.6, 3.0, 6.6, 2.1, 'virginica')]


Unions
------
Generic type annotation:

>>> data: list[list|tuple|set] = [
...    [1, 2, 3],
...    (4, 5, 6),
...    {7, 8, 9}]

>>> data: list[list[int] | tuple[int, ...] | set[int]] = [
...    [1, 2, 3],
...    (4, 5, 6),
...    {7, 8, 9}]

>>> row = list[int] | tuple[int, ...] | set[int]
>>> data: list[row] = [
...    [1, 2, 3],
...    (4, 5, 6),
...    {7, 8, 9}]


NamedTuple
----------
>>> from typing import NamedTuple
>>> from sys import getsizeof
>>>
>>>
>>> class Astronaut(NamedTuple):
...     firstname: str
...     lastname: str
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney')
>>> mark
Astronaut(firstname='Mark', lastname='Watney')

>>> a = ('Mark', 'Watney')
>>> b = Astronaut('Mark', 'Watney')
>>>
>>> a == b
True
>>>
>>> getsizeof(a)
56
>>> getsizeof(b)
56


Further Reading
---------------
* Example: https://github.com/pandas-dev/pandas/blob/8fd2d0c1eea04d56ec0a63fae084a66dd482003e/pandas/core/frame.py#L505
* More information in `Type Annotations`
* More information in `CI/CD Type Checking`

References
----------
.. [#pyDocTyping] https://docs.python.org/3/library/typing.html#module-contents
