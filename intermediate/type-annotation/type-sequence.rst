Type Annotation Sequences
=========================
* Before Python 3.9 you need ``from typing import List, Tuple, Set, Frozenset``
* Since Python 3.9: :pep:`585` -- Type Hinting Generics In Standard Collections

>>> DATA = [
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor')]
>>>
>>> x = DATA[0][-1]
>>> x  # doctest: +SKIP
>>> # IDE don't know what type is species
>>> # and cannot give hints for autocompletion

>>> DATA = [
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor')]
>>>
>>> x: str = DATA[0][-1]
>>> x  # doctest: +SKIP
>>> # IDE knows exactly what type is species
>>> # and what methods hint for autocompletion


Tuple
-----
Declaration:

>>> data: tuple
>>>
>>> data: tuple[int]
>>> data: tuple[float]
>>> data: tuple[bool]
>>> data: tuple[str]
>>>
>>> data: tuple[int, ...]
>>> data: tuple[float, ...]
>>> data: tuple[bool, ...]
>>> data: tuple[str, ...]

Empty:

>>> data: tuple = ()
>>> data: tuple = tuple()

Generic:

>>> data: tuple = (1, 2, 3)
>>> data: tuple = (1.1, 2.2, 3.3)
>>> data: tuple = ('a', 'b', 'c')

Strict:

>>> data: tuple[int, int, int] = (1, 2, 3)
>>> data: tuple[float, float, float] = (1.1, 2.2, 3.3)
>>> data: tuple[str, str, str] = ('a', 'b', 'c')
>>> data: tuple[str, int, float] = ('a', 2, 3.3)

Repeating:

>>> data: tuple[int, ...] = (1, 2, 3)
>>> data: tuple[float, ...] = (1.1, 2.2, 3.3)
>>> data: tuple[str, ...] = ('a', 'b', 'c')

Examples:

>>> data: tuple[str,str,int] = ('Mark', 'Watney', 40)
>>> data: tuple[float,float,float,float,str] = (5.1, 3.5, 1.4, 0.2, 'setosa')


List
----
Declaration:

>>> data: list
>>>
>>> data: list[int]
>>> data: list[float]
>>> data: list[bool]
>>> data: list[str]

Empty:

>>> data: list = []
>>> data: list = list()

Generic:

>>> data: list = [1, 2, 3]
>>> data: list = [1.1, 2.2, 3.3]
>>> data: list = ['a', 'b', 'c']

Strict and Repeating:

>>> data: list[int] = [1, 2, 3]
>>> data: list[float] = [1.1, 2.2, 3.3]
>>> data: list[str] = ['a', 'b', 'c']

Varying:

>>> data: list[int|float] = [1, 2, 3.3, 4.4]
>>> data: list[int|float|str] = [1, 2, 3.3, 4.0, 'a', 'b']


Set
---
Declaration:

>>> data: set
>>>
>>> data: set[int]
>>> data: set[float]
>>> data: set[bool]
>>> data: set[str]

Empty:

>>> data: set = set()

Generic:

>>> data: set = {1, 2, 3}
>>> data: set = {1.1, 2.2, 3.3}
>>> data: set = {'a', 'b', 'c'}

Strict and Repeating:

>>> data: set[int] = {1, 2, 3}
>>> data: set[float] = {1.1, 2.2, 3.3}
>>> data: set[str] = {'a', 'b', 'c'}

Varying:

>>> data: set[int|float] = {1, 2, 3.3, 4.4}
>>> data: set[int|float|str] = {1, 2, 3.3, 4.0, 'a', 'b'}


Frozenset
---------
Declaration:

>>> data: frozenset
>>>
>>> data: frozenset[int]
>>> data: frozenset[float]
>>> data: frozenset[bool]
>>> data: frozenset[str]

Empty:

>>> data: frozenset = frozenset()

Generic:

>>> data: frozenset = frozenset({1, 2, 3})
>>> data: frozenset = frozenset({1.1, 2.2, 3.3})
>>> data: frozenset = frozenset({'a', 'b', 'c'})

Strict and Repeating:

>>> data: frozenset[int] = frozenset({1, 2, 3})
>>> data: frozenset[float] = frozenset({1.1, 2.2, 3.3})
>>> data: frozenset[str] = frozenset({'a', 'b', 'c'})

Varying:

>>> data: frozenset[int|float] = frozenset({1, 2, 3.3, 4.4})
>>> data: frozenset[int|float|str] = frozenset({1, 2, 3.3, 4.0, 'a', 'b'})


List of Lists
-------------
Declaration:

>>> data: list
>>> data: list[list]
>>> data: list[list[int]]

Example:

>>> data: list = [
...     [1, 2, 3],
...     [4, 5, 6],
...     [7, 8, 9]]

>>> data: list[list] = [
...     [1, 2, 3],
...     [4, 5, 6],
...     [7, 8, 9]]

>>> data: list[list[int]] = [
...     [1, 2, 3],
...     [4, 5, 6],
...     [7, 8, 9]]


List of Tuples
--------------
Declaration:

>>> data: list
>>> data: list[tuple]
>>> data: list[tuple[float, float, float, float, str]]

Example:

>>> data: list = [
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...     (7.6, 3.0, 6.6, 2.1, 'virginica')]

>>> data: list[tuple] = [
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...     (7.6, 3.0, 6.6, 2.1, 'virginica')]

>>> data: list[tuple[float, float, float, float, str]] = [
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...     (7.6, 3.0, 6.6, 2.1, 'virginica')]


Aliases
-------
Declaration:

>>> row = tuple[int, int, int]
>>> data: list[row]

Example:

>>> Iris = tuple[float, float, float, float, str]
>>>
>>> data: list[Iris] = [
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...     (7.6, 3.0, 6.6, 2.1, 'virginica')]


Unions
------
Declaration:

>>> a = tuple[str, str, str]
>>> b = tuple[int, int, int]
>>> c = tuple[float, float, float]
>>>
>>> data: list[a | b | c]

>>> header = tuple[str, str, str]
>>> row = tuple[int, int, int]
>>>
>>> data: tuple[header,row,...]

Example:

>>> Header = tuple[str, str, str, str, str]
>>> Row = tuple[float, float, float, float, str]
>>>
>>> DATA: tuple[Header,Row,...] = (
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa'))


NamedTuple
----------
SetUp:

>>> from typing import NamedTuple

Problem:

>>> def hello_astronaut(astronaut):
...     result = f'Hello {astronaut[0]} {astronaut[1]}'
>>>
>>>
>>> mark = ('Mark', 'Watney', 40)
>>> hello_astronaut(mark)
>>>
>>> iris = ('Iris', 'Setosa')
>>> hello_astronaut(iris)

Solution 1 - tuple:

>>> def hello_astronaut(astronaut: tuple[str,str,int]):
...     result = f'Hello {astronaut[0]} {astronaut[1]}'
>>>
>>>
>>> mark = ('Mark', 'Watney', 40)
>>> hello_astronaut(mark) # ok
>>>
>>> iris = ('Iris', 'Setosa')
>>> hello_astronaut(iris)  # error (missing int)
>>>
>>> iris = ('Iris', 'Setosa', 1)
>>> hello_astronaut(iris)  # ok

Solution 2 - NamedTuple:

>>> class Astronaut(NamedTuple):
...     firstname: str
...     lastname: str
...     age: int
>>>
>>>
>>> def hello_astronaut(astronaut: Astronaut):
...     result = f'Hello {astronaut[0]} {astronaut[1]}'
>>>
>>>
>>> mark = Astronaut('Mark', 'Watney', 40)
>>> hello_astronaut(mark) # ok
>>>
>>> mark = Astronaut(firstname='Mark', lastname='Watney', age=40)
>>> hello_astronaut(mark) # ok
>>>
>>> iris = ('Iris', 'Setosa', 1)
>>> hello_astronaut(iris)  # ok

Using ``NamedTuple`` we can also make ``hello_astronaut()`` function
more readable by using attributes ``astronaut.firstname`` and
``astronaut.lastname`` instead of indexes, such as: ``astronaut[0]``
and ``astronaut[1]``.

>>> def hello_astronaut(astronaut: Astronaut):
...     result = f'Hello {astronaut.firstname} {astronaut.lastname}'

Note, that ``NamedTuple`` is still a tuple and you can compare both!

>>> class Astronaut(NamedTuple):
...     firstname: str
...     lastname: str

>>> a = ('Mark', 'Watney')
>>> b: Astronaut = ('Mark', 'Watney')
>>> c = Astronaut('Mark', 'Watney')
>>> d = Astronaut(firstname='Mark', lastname='Watney')

>>> isinstance(a, tuple)
True
>>>
>>> isinstance(b, tuple)
True
>>>
>>> isinstance(c, tuple)
True
>>>
>>> isinstance(d, tuple)
True

>>> type(a)
<class 'tuple'>
>>> type(b)
<class 'tuple'>
>>> type(c)
<class '__main__.Astronaut'>
>>> type(d)
<class '__main__.Astronaut'>

>>> Astronaut.mro()
[<class '__main__.Astronaut'>, <class 'tuple'>, <class 'object'>]

>>> a == b
True
>>> b == c
True
>>> c == d
True

>>> from sys import getsizeof
>>>
>>> getsizeof(a)
56
>>> getsizeof(b)
56
>>> getsizeof(c)
56
>>> getsizeof(d)
56


Use Case - 0x01
---------------
>>> GeographicCoordinate = tuple[float, float]
>>>
>>> locations: list[GeographicCoordinate] = [
...     (25.91375, -60.15503),
...     (-11.01983, -166.48477),
...     (-11.01983, -166.48477)]


Use Case - 0x02
---------------
>>> data: list[list|tuple|set] = [
...    [1, 2, 3],
...    (4, 5, 6),
...    {7, 8, 9}]

>>> data: list[list[int] | tuple[int, ...] | set[int]] = [
...    [1, 2, 3],
...    (4, 5, 6),
...    {7, 8, 9}]

>>> row = list[int] | tuple[int, ...] | set[int]
>>>
>>> data: list[row] = [
...    [1, 2, 3],
...    (4, 5, 6),
...    {7, 8, 9}]



Further Reading
---------------
* Example: https://github.com/pandas-dev/pandas/blob/8fd2d0c1eea04d56ec0a63fae084a66dd482003e/pandas/core/frame.py#L505
* More information in `Type Annotations`
* More information in `CI/CD Type Checking`

References
----------
.. [#pyDocTyping] https://docs.python.org/3/library/typing.html#module-contents
