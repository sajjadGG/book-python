Function Generators
===================


Range
-----
* It is not a generator
* optional ``start``, inclusive, default: ``0``
* required ``stop``, exclusive,
* optional ``step``, default: ``1``

``range()`` syntax:

.. code-block:: python

    range([start], <stop>, [step])

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


Enumerate
---------
* ``enumerate(*iterables)``

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
* ``zip(*iterables)``

>>> firstnames = ['Mark', 'Melissa', 'Rick']
>>> lastnames = ['Watney', 'Lewis', 'Martinez']
>>>
>>> result = zip(firstnames, lastnames)
>>>
>>>
>>> next(result)
('Mark', 'Watney')
>>>
>>> next(result)
('Melissa', 'Lewis')
>>>
>>> next(result)
('Rick', 'Martinez')
>>>
>>> next(result)
Traceback (most recent call last):
StopIteration

>>> firstnames = ['Mark', 'Melissa', 'Rick']
>>> lastnames = ['Watney', 'Lewis', 'Martinez']
>>>
>>> result = zip(firstnames, lastnames)
>>>
>>> list(result)
[('Mark', 'Watney'), ('Melissa', 'Lewis'), ('Rick', 'Martinez')]

>>> firstnames = ['Mark', 'Melissa', 'Rick']
>>> lastnames = ['Watney', 'Lewis', 'Martinez']
>>>
>>> result = zip(firstnames, lastnames)
>>>
>>> dict(result)
{'Mark': 'Watney', 'Melissa': 'Lewis', 'Rick': 'Martinez'}

>>> roles = ['botanist', 'commander', 'pilot']
>>> names = ['Mark Watney', 'Melissa Lewis', 'Rick Martinez']
>>>
>>> dict(zip(roles, names))  # doctest: +NORMALIZE_WHITESPACE
{'botanist': 'Mark Watney',
 'commander': 'Melissa Lewis',
 'pilot': 'Rick Martinez'}

``zip()`` adjusts to the shortest:

>>> firstnames = ['Mark', 'Melissa']
>>> lastnames = ['Watney', 'Lewis', 'Martinez']
>>>
>>> result = zip(firstnames, lastnames)
>>>
>>> list(result)
[('Mark', 'Watney'), ('Melissa', 'Lewis')]

>>> roles = ['botanist', 'commander', 'pilot']
>>> firstnames = ['Mark', 'Melissa', 'Rick']
>>> lastnames = ['Watney', 'Lewis', 'Martinez']
>>>
>>> result = zip(roles, firstnames, lastnames)
>>>
>>>
>>> next(result)
('botanist', 'Mark', 'Watney')
>>>
>>> next(result)
('commander', 'Melissa', 'Lewis')
>>>
>>> next(result)
('pilot', 'Rick', 'Martinez')
>>>
>>> next(result)
Traceback (most recent call last):
StopIteration

>>> roles = ['botanist', 'commander', 'pilot']
>>> names = ['Mark Watney', 'Melissa Lewis', 'Rick Martinez']
>>>
>>>
>>> for role, name in zip(roles, names):
...     print(f'{role} -> {name}')
botanist -> Mark Watney
commander -> Melissa Lewis
pilot -> Rick Martinez


Map
---
* Apply function to all elements of data
* ``map(callable, *iterables)``

>>> data = [1, 2, 3]
>>> result = map(float, data)
>>>
>>>
>>> next(result)
1.0
>>>
>>> next(result)
2.0
>>>
>>> next(result)
3.0
>>> next(result)
Traceback (most recent call last):
StopIteration


Filter
------
* ``filter(callable, *iterables)``

>>> def even(x):
...     return x % 2 == 0
>>>
>>>
>>> data = [0, 1, 2, 3, 4]
>>> result = filter(even, data)
>>>
>>>
>>> next(result)
0
>>>
>>> next(result)
2
>>>
>>> next(result)
4
>>> next(result)
Traceback (most recent call last):
StopIteration


Generator Chain
---------------
* Function composition

>>> def even(x):
...     return x % 2 == 0
>>>
>>>
>>> data = (x for x in range(0,5))
>>> data = map(float, data)
>>> data = filter(even, data)
>>>
>>>
>>> next(data)
0.0
>>>
>>> next(data)
2.0
>>>
>>> next(data)
4.0
>>> next(data)
Traceback (most recent call last):
StopIteration


Itertools
---------
* Learn more at https://docs.python.org/3/library/itertools.html
* More information in `Itertools`
* ``itertools.count(start=0, step=1)``
* ``itertools.cycle(iterable)``
* ``itertools.repeat(object[, times])``
* ``itertools.accumulate(iterable[, func, *, initial=None])``
* ``itertools.chain(*iterables)``
* ``itertools.compress(data, selectors)``
* ``itertools.islice(iterable, start, stop[, step])``
* ``itertools.starmap(function, iterable)``
* ``itertools.product(*iterables, repeat=1)``
* ``itertools.permutations(iterable, r=None)``
* ``itertools.combinations(iterable, r)``
* ``itertools.combinations_with_replacement(iterable, r)``
* ``itertools.groupby(iterable, key=None)``


Use Case - 0x01
---------------
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
>>> def square(x):
...     return x ** 2
>>>
>>>
>>> data = [1, 2, 3]
>>> result = map(square, data)
>>>
>>> list(result)
[1, 4, 9]


Use Case - 0x03
---------------
>>> PL = {'ą': 'a', 'ć': 'c', 'ę': 'e',
...       'ł': 'l', 'ń': 'n', 'ó': 'o',
...       'ś': 's', 'ż': 'z', 'ź': 'z'}
>>>
>>>
>>> def translate(letter):
...     return PL.get(letter, letter)
>>>
>>>
>>> text = 'zażółć gęślą jaźń'
>>> result = map(translate, text)
>>>
>>> ''.join(result)
'zazolc gesla jazn'


Use Case - 0x04
---------------
>>> people = [
...     {'age': 21, 'name': 'Mark Watney'},
...     {'age': 25, 'name': 'Melissa Lewis'},
...     {'age': 18, 'name': 'Rick Martinez'}]
>>>
>>>
>>> def adult(person):
...     return person['age'] >= 21
>>>
>>>
>>> result = filter(adult, people)
>>>
>>> list(result)  # doctest: +NORMALIZE_WHITESPACE
[{'age': 21, 'name': 'Mark Watney'},
 {'age': 25, 'name': 'Melissa Lewis'}]


Use Case - 0x05
---------------
>>> people = [
...     {'is_astronaut': False, 'name': 'Mark Watney'},
...     {'is_astronaut': True, 'name': 'Melissa Lewis'},
...     {'is_astronaut': True, 'name': 'Rick Martinez'}]
>>>
>>>
>>> def astronaut(person):
...     return person['is_astronaut']
>>>
>>>
>>> result = filter(astronaut, people)
>>>
>>> list(result)  # doctest: +NORMALIZE_WHITESPACE
[{'is_astronaut': True, 'name': 'Melissa Lewis'},
 {'is_astronaut': True, 'name': 'Rick Martinez'}]


Use Case - 0x06
---------------
Sum stdin (standard input):

>>> import sys
>>>
>>> # doctest: +SKIP
... print(sum(map(int, sys.stdin)))

.. code-block:: console

    $ cat ~/.profile |grep addnum
    alias addnum='python -c"import sys; print(sum(map(int, sys.stdin)))"'


Assignments
-----------
.. literalinclude:: assignments/function_generators_a.py
    :caption: :download:`Solution <assignments/function_generators_a.py>`
    :end-before: # Solution
