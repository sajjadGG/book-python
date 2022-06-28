Generator Builtin
=================
* Generator-like objects
* Behaves similar, but is not generator
* ``range()``
* ``reversed()``
* ``enumerate()``
* ``zip()``
* ``map()``
* ``filter()``
* ``import itertools``


Range
-----
* Generate integers from ``start`` to ``stop`` incrementing by ``step``
* ``range([start], <stop>, [step])``
* optional ``start``, inclusive, default: ``0``
* required ``stop``, exclusive,
* optional ``step``, default: ``1``

>>> from inspect import isgeneratorfunction, isgenerator
>>>
>>>
>>> isgeneratorfunction(range)
False
>>>
>>> result = range(0,5)
>>> isgenerator(result)
False

>>> range(0,3)
range(0, 3)
>>> list(range(0,3))
[0, 1, 2]
>>> tuple(range(0,3))
(0, 1, 2)
>>> set(range(0,3))
{0, 1, 2}
>>> list(range(4,11,2))
[4, 6, 8, 10]


Reversed
--------
* Return a reverse iterator over the values of the given sequence
* ``reversed(sequence, /)``

>>> data = (1, 2, 3)
>>> list(reversed(data))
[3, 2, 1]


Enumerate
---------
* ``enumerate(iterable, start=0)``
* Return an enumerate object
* The enumerate object yields pairs containing a count (from start, which defaults to zero) and a value yielded by the iterable argument.

>>> from inspect import isgeneratorfunction, isgenerator
>>>
>>>
>>> isgeneratorfunction(enumerate)
False
>>> result = enumerate(['a', 'b', 'c'])
>>> isgenerator(result)
False

>>> months = ['January', 'February', 'March']
>>> result = enumerate(months)
>>>
>>> next(result)
(0, 'January')
>>> next(result)
(1, 'February')
>>> next(result)
(2, 'March')
>>> next(result)
Traceback (most recent call last):
StopIteration

>>> months = ['January', 'February', 'March']
>>> result = enumerate(months)
>>>
>>> list(result)
[(0, 'January'), (1, 'February'), (2, 'March')]

>>> months = ['January', 'February', 'March']
>>> result = enumerate(months)
>>>
>>> dict(result)
{0: 'January', 1: 'February', 2: 'March'}

>>> months = ['January', 'February', 'March']
>>> result = enumerate(months, start=1)
>>>
>>> dict(result)
{1: 'January', 2: 'February', 3: 'March'}

>>> months = ['January', 'February', 'March']
>>> result = {f'{i:02}':month for i,month in enumerate(months, start=1)}
>>>
>>> print(result)
{'01': 'January', '02': 'February', '03': 'March'}

>>> months = ['January', 'February', 'March']
>>>
>>> for i, month in enumerate(months, start=1):
...     print(f'{i} -> {month}')
1 -> January
2 -> February
3 -> March


Zip
---
* ``zip(*iterables, strict=False)``
* Iterate over several iterables in parallel, producing tuples with an item from each one.

The ``zip`` object yields n-length tuples, where n is the number of iterables
passed as positional arguments to ``zip()``. The i-th element in every tuple
comes from the i-th iterable argument to ``zip()``.  This continues until the
shortest argument is exhausted. [#pydoczip]_

If strict is true and one of the arguments is exhausted before the others,
raise a ``ValueError``.

>>> from inspect import isgeneratorfunction, isgenerator
>>>
>>>
>>> isgeneratorfunction(zip)
False
>>>
>>> result = zip(['a','b','c'], [1,2,3])
>>> isgenerator(result)
False

>>> firstnames = ['Mark', 'Melissa', 'Alex']
>>> lastnames = ['Watney', 'Lewis', 'Vogel']
>>> result = zip(firstnames, lastnames)
>>>
>>> next(result)
('Mark', 'Watney')
>>> next(result)
('Melissa', 'Lewis')
>>> next(result)
('Alex', 'Vogel')
>>> next(result)
Traceback (most recent call last):
StopIteration

>>> firstnames = ['Mark', 'Melissa', 'Alex']
>>> lastnames = ['Watney', 'Lewis', 'Vogel']
>>> result = zip(firstnames, lastnames)
>>>
>>> list(result)
[('Mark', 'Watney'), ('Melissa', 'Lewis'), ('Alex', 'Vogel')]

>>> firstnames = ['Mark', 'Melissa', 'Alex']
>>> lastnames = ['Watney', 'Lewis', 'Vogel']
>>> result = zip(firstnames, lastnames)
>>>
>>> dict(result)
{'Mark': 'Watney', 'Melissa': 'Lewis', 'Alex': 'Vogel'}

>>> roles = ['botanist', 'commander', 'chemist']
>>> names = ['Mark Watney', 'Melissa Lewis', 'Alex Vogel']

>>> dict(zip(roles, names))  # doctest: +NORMALIZE_WHITESPACE
{'botanist': 'Mark Watney',
 'commander': 'Melissa Lewis',
 'chemist': 'Alex Vogel'}

``zip()`` adjusts to the shortest:

>>> firstnames = ['Mark', 'Melissa']
>>> lastnames = ['Watney', 'Lewis', 'Vogel']
>>> result = zip(firstnames, lastnames)
>>>
>>> list(result)
[('Mark', 'Watney'), ('Melissa', 'Lewis')]

>>> roles = ['botanist', 'commander', 'chemist']
>>> firstnames = ['Mark', 'Melissa', 'Alex']
>>> lastnames = ['Watney', 'Lewis', 'Vogel']
>>> result = zip(roles, firstnames, lastnames)
>>>
>>> next(result)
('botanist', 'Mark', 'Watney')
>>> next(result)
('commander', 'Melissa', 'Lewis')
>>> next(result)
('chemist', 'Alex', 'Vogel')
>>> next(result)
Traceback (most recent call last):
StopIteration

>>> roles = ['botanist', 'commander', 'chemist']
>>> names = ['Mark Watney', 'Melissa Lewis', 'Alex Vogel']
>>>
>>> for role, name in zip(roles, names):
...     print(f'{role} -> {name}')
botanist -> Mark Watney
commander -> Melissa Lewis
chemist -> Alex Vogel


Map
---
* ``map(callable, *iterables)``

>>> from inspect import isgeneratorfunction, isgenerator
>>>
>>>
>>> isgeneratorfunction(map)
False
>>>
>>> result = map(float, [1,2,3])
>>> isgenerator(result)
False

>>> data = [1, 2, 3]
>>> result = map(float, data)
>>>
>>> next(result)
1.0
>>> next(result)
2.0
>>> next(result)
3.0
>>> next(result)
Traceback (most recent call last):
StopIteration

>>> data = [1, 2, 3]
>>> result = map(float, data)
>>>
>>> list(result)
[1.0, 2.0, 3.0]

>>> def square(x):
...     return x ** 2
...
>>> data = [1, 2, 3]
>>> result = map(square, data)
>>>
>>> list(result)
[1, 4, 9]



Filter
------
* ``filter(callable, *iterables)``

>>> from inspect import isgeneratorfunction, isgenerator
>>>
>>>
>>> def even(x):
...     return x % 2 == 0
>>>
>>>
>>> isgeneratorfunction(filter)
False
>>>
>>> result = filter(even, [1,2,3])
>>> isgenerator(result)
False

>>> def even(x):
...     return x % 2 == 0
>>>
>>>
>>> data = [1, 2, 3, 4, 5, 6]
>>> result = filter(even, data)
>>>
>>> next(result)
2
>>> next(result)
4
>>> next(result)
6
>>> next(result)
Traceback (most recent call last):
StopIteration

>>> def even(x):
...     return x % 2 == 0
>>>
>>>
>>> data = [1, 2, 3, 4, 5, 6]
>>> result = filter(even, data)
>>>
>>> list(result)
[2, 4, 6]


Performance:

>>> def even(x):
...     return x % 2 == 0
>>>
>>>
>>> data = [1, 2, 3, 4, 5, 6]

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = [x for x in data if even(x)]
1.11 µs ± 139 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = list(filter(even, data))
921 ns ± 112 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)



Performance
-----------
>>> def even(x):
...     return x % 2 == 0

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = [float(x) for x in data if even(x)]
1.9 µs ± 206 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = list(map(float, filter(parzysta, data)))
1.66 µs ± 175 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)


Use Case - 0x01
---------------
* Increment

>>> def increment(x):
...     return x + 1
>>>
>>>
>>> data = [1, 2, 3, 4]
>>> result = map(increment, data)
>>>
>>> list(result)
[2, 3, 4, 5]


Use Case - 0x02
---------------
* Translate

>>> PL = {'ą': 'a', 'ć': 'c', 'ę': 'e',
...       'ł': 'l', 'ń': 'n', 'ó': 'o',
...       'ś': 's', 'ż': 'z', 'ź': 'z'}
>>>
>>> def translate(letter):
...     return PL.get(letter, letter)
>>>
>>>
>>> text = 'zażółć gęślą jaźń'
>>> result = map(translate, text)
>>> ''.join(result)
'zazolc gesla jazn'


Use Case - 0x03
---------------
* Compare

>>> people = [
...     {'age': 21, 'name': 'Pan Twardowski'},
...     {'age': 25, 'name': 'Mark Watney'},
...     {'age': 18, 'name': 'Melissa Lewis'}]
>>>
>>>
>>> def adult(person):
...     return person['age'] >= 21
>>>
>>>
>>> result = filter(adult, people)
>>> list(result)  # doctest: +NORMALIZE_WHITESPACE
[{'age': 21, 'name': 'Pan Twardowski'},
 {'age': 25, 'name': 'Mark Watney'}]


Use Case - 0x04
---------------
* Bool

>>> people = [
...     {'is_astronaut': False, 'name': 'Pan Twardowski'},
...     {'is_astronaut': True, 'name': 'Mark Watney'},
...     {'is_astronaut': True, 'name': 'Melissa Lewis'}]
>>>
>>>
>>> def astronaut(person):
...     return person['is_astronaut']
>>>
>>>
>>> result = filter(astronaut, people)
>>> list(result)  # doctest: +NORMALIZE_WHITESPACE
[{'is_astronaut': True, 'name': 'Mark Watney'},
 {'is_astronaut': True, 'name': 'Melissa Lewis'}]


Use Case - 0x05
---------------
* Contains

>>> astronauts = ['Mark Watney', 'Melissa Lewis']
>>> people = ['Mark Watney', 'Melissa Lewis', 'Jimenez']
>>>
>>>
>>> def is_astronaut(person):
...     return person in astronauts
>>>
>>>
>>> result = filter(is_astronaut, people)
>>> list(result)
['Mark Watney', 'Melissa Lewis']


Use Case - 0x06
---------------
* Stdin

>>> import sys
>>>
>>> # doctest: +SKIP
... print(sum(map(int, sys.stdin)))

.. code-block:: console

    $ cat ~/.profile |grep addnum
    alias addnum='python -c"import sys; print(sum(map(int, sys.stdin)))"'


References
----------
.. [#pydoczip] Python Core Developers. Built-in Functions. Year: 2022. Retrieved: 2022-06-28. URL: https://docs.python.org/3/library/functions.html#zip


Assignments
-----------
.. literalinclude:: assignments/generator_builtin_a.py
    :caption: :download:`Solution <assignments/generator_builtin_a.py>`
    :end-before: # Solution
