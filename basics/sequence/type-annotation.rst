Sequence Type Annotation
========================


Rationale
---------
* Before Python 3.9 you need ``from typing import List, Set, Tuple, Dict``
* Since Python 3.9 - :pep:`585` -- Type Hinting Generics In Standard Collections

>>> DATA = [(5.8, 2.7, 5.1, 1.9, 'virginica'),
...        (5.1, 3.5, 1.4, 0.2, 'setosa'),
...        (5.7, 2.8, 4.1, 1.3, 'versicolor')]
...
>>> x = DATA[0][-1]
... # IDE don't know what type is species
... # and cannot give hints for autocompletion

>>> DATA = [(5.8, 2.7, 5.1, 1.9, 'virginica'),
...        (5.1, 3.5, 1.4, 0.2, 'setosa'),
...        (5.7, 2.8, 4.1, 1.3, 'versicolor')]
...
>>> x: str = DATA[0][-1]
... # IDE knows exactly what type is species
... # and what methods hint for autocompletion


Tuple
-----
Generic type annotation:

>>> data: tuple = ()
>>> data: tuple = tuple()
>>> data: tuple = 'a', 2, 3.3
>>> data: tuple = ('a', 2, 3.3)

Strict type annotation, since Python 3.9:

>>> data: tuple[int, int, int] = (1, 2, 3)
>>> data: tuple[str, str, str] = ('setosa', 'virginica', 'versicolor')
>>> data: tuple[str, int, float] = ('a', 2, 3.3)
>>> data: tuple[int, ...] = (1, 2, 3)
>>> data: tuple[str, ...] = ('setosa', 'virginica', 'versicolor')

Strict type annotation, before Python 3.9:

>>> from typing import Tuple
>>>
>>> data: Tuple[int, int, int] = (1, 2, 3)
>>> data: Tuple[str, str, str] = ('setosa', 'virginica', 'versicolor')
>>> data: Tuple[str, int, float] = ('a', 2, 3.3)
>>> data: Tuple[int, ...] = (1, 2, 3)
>>> data: Tuple[str, ...] = ('setosa', 'virginica', 'versicolor')


List
----
Generic type annotation:

>>> data: list = list()
>>> data: list = []
>>> data: list = ['a', 1, 2.2]

Strict type annotation, since Python 3.9:

>>> data: list[int] = [1, 2, 3, 4]
>>> data: list[float] = [5.8, 2.7, 5.1, 1.9]
>>> data: list[str] = ['a', 'b', 'c', 'd']

Strict type annotation, before Python 3.9:

>>> from typing import List
>>>
>>> data: List[int] = [1, 2, 3, 4]
>>> data: List[float] = [5.8, 2.7, 5.1, 1.9]
>>> data: List[str] = ['a', 'b', 'c', 'd']


Set
---
Generic type annotation:

>>> data: set = set()
>>> data: set = {'a', 1, 2.2}

Strict type annotation, since Python 3.9:

>>> data: set[int] = {1, 2, 3}
>>> data: set[float] = {0.0, 1.1, 2.2}
>>> data: set[str] = {'a', 'b', 'c'}

Strict type annotation, before Python 3.9:

>>> from typing import Set
>>>
>>> data: Set[int] = {1, 2, 3}
>>> data: Set[float] = {0.0, 1.1, 2.2}
>>> data: Set[str] = {'a', 'b', 'c'}


Frozenset
---------
Generic type annotation:

>>> data: frozenset = set()
>>> data: frozenset = {'a', 1, 2.2}

Strict type annotation, since Python 3.9:

>>> data: frozenset[int] = {1, 2, 3}
>>> data: frozenset[float] = {0.0, 1.1, 2.2}
>>> data: frozenset[str] = {'a', 'b', 'c'}

Strict type annotation, before Python 3.9:

>>> from typing import FrozenSet
>>>
>>> data: FrozenSet[int] = {1, 2, 3}
>>> data: FrozenSet[float] = {0.0, 1.1, 2.2}
>>> data: FrozenSet[str] = {'a', 'b', 'c'}


List of Tuples
--------------
Generic type annotation:

>>> data: list[tuple] = [
...    (4.7, 3.2, 1.3, 0.2, 'setosa'),
...    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...    (7.6, 3.0, 6.6, 2.1, 'virginica')]

Strict type annotation, since Python 3.9:

>>> data: list[tuple[float, float, float, float, str]] = [
...    (4.7, 3.2, 1.3, 0.2, 'setosa'),
...    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...    (7.6, 3.0, 6.6, 2.1, 'virginica')]

Generic type annotation, before Python 3.9:

>>> from typing import List
>>>
>>> data: List[tuple] = [
...    (4.7, 3.2, 1.3, 0.2, 'setosa'),
...    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...    (7.6, 3.0, 6.6, 2.1, 'virginica')]


Strict type annotation, before Python 3.9:

>>> from typing import List, Tuple
>>>
>>> data: List[Tuple[float, float, float, float, str]] = [
...    (4.7, 3.2, 1.3, 0.2, 'setosa'),
...    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...    (7.6, 3.0, 6.6, 2.1, 'virginica')]


List of Lists
-------------
Generic type annotation:

>>> data: list[list] = [
...    [1, 2, 3],
...    [4, 5, 6],
...    [7, 8, 9]]

>>> data: list[list[int]] = [
...    [1, 2, 3],
...    [4, 5, 6],
...    [7, 8, 9]]


Generic type annotation, before Python 3.9:

>>> from typing import List
>>>
>>> data: List[list] = [
...    [1, 2, 3],
...    [4, 5, 6],
...    [7, 8, 9]]

Strict type annotation, since Python 3.9:

>>> from typing import List
>>>
>>> data: List[List[int]] = [
...    [1, 2, 3],
...    [4, 5, 6],
...    [7, 8, 9]]


Aliases
-------
Generic type annotation:

>>> Point = tuple[int, int]
>>> locations: list[Point] = [
...    (0, 1),
...    (5, -3),
...    (-10, 20)]

>>> GeographicCoordinate = tuple[float, float]
>>> locations: list[GeographicCoordinate] = [
...    (25.91375, -60.15503),
...    (-11.01983, -166.48477),
...    (-11.01983, -166.48477)]

>>> Iris = tuple[float, float, float, float, str]
>>> data: list[Iris] = [
...    (4.7, 3.2, 1.3, 0.2, 'setosa'),
...    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...    (7.6, 3.0, 6.6, 2.1, 'virginica')]

Strict type annotation, before Python 3.9:

>>> GeographicCoordinate = Tuple[float, float]
>>> locations: List[GeographicCoordinate] = [
...    (25.91375, -60.15503),
...    (-11.01983, -166.48477),
...    (-11.01983, -166.48477)]

>>> Iris = Tuple[float, float, float, float, str]
>>> data: List[Iris] = [
...    (4.7, 3.2, 1.3, 0.2, 'setosa'),
...    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...    (7.6, 3.0, 6.6, 2.1, 'virginica')]


Unions
------
Generic type annotation:

>>> from typing import Union
>>>
>>> data: list[Union[list, tuple, set]] = [
...    [1, 2, 3],
...    (4, 5, 6),
...    {7, 8, 9}]

>>> from typing import Union
>>>
>>> data: list[Union[list[int], tuple[int, ...], set[int]]] = [
...    [1, 2, 3],
...    (4, 5, 6),
...    {7, 8, 9}]

>>> from typing import Union
>>>
>>> row = Union[list[int], tuple[int, ...], set[int]]
>>> data: list[row] = [
...    [1, 2, 3],
...    (4, 5, 6),
...    {7, 8, 9}]

Strict type annotation, before Python 3.9:

>>> from typing import Union, List
>>>
>>> data: List[Union[list, tuple, set]] = [
...    [1, 2, 3],
...    (4, 5, 6),
...    {7, 8, 9}]


>>> from typing import Union, List, Tuple, Set
>>>
>>> data: List[Union[List[int], Tuple[int, int, int], Set[int]]] = [
...    [1, 2, 3],
...    (4, 5, 6),
...    {7, 8, 9}]

>>> from typing import Union, List, Tuple, Set
>>>
>>> Row = Union[List[int],
...            Tuple[int, int, int],
...            Set[int]]
...
>>> data: List[Row] = [
...    [1, 2, 3],
...    (4, 5, 6),
...    {7, 8, 9}]


Further Reading
---------------
* Example: https://github.com/pandas-dev/pandas/blob/8fd2d0c1eea04d56ec0a63fae084a66dd482003e/pandas/core/frame.py#L505
* More information in `Type Annotations`
* More information in `CI/CD Type Checking`
