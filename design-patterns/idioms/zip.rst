Zip
===


Rationale
---------
* Combine two sequences
* Generator (lazy evaluated)
* Built-in


Syntax
------
* ``zip(*iterables)``
* required ``*iterables`` - 1 or many sequences or iterator object


Problem
-------
>>> firstnames = ['Mark', 'Melissa', 'Alex']
>>> lastnames = ['Watney', 'Lewis', 'Vogel']
>>>
>>> i = 0
>>> result = []
>>>
>>> while i < min(len(firstnames), len(lastnames)):
...     pair = (firstnames[i], lastnames[i])
...     result.append(pair)
...     i += 1
>>>
>>> result
[('Mark', 'Watney'), ('Melissa', 'Lewis'), ('Alex', 'Vogel')]

>>> firstnames = ['Mark', 'Melissa', 'Alex']
>>> lastnames = ['Watney', 'Lewis', 'Vogel']
>>>
>>> result = []
>>>
>>> for i in range(min(len(firstnames), len(lastnames))):
...     pair = (firstnames[i], lastnames[i])
...     result.append(pair)
>>>
>>> result
[('Mark', 'Watney'), ('Melissa', 'Lewis'), ('Alex', 'Vogel')]


Solution
--------
Lazy Evaluation:

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


Instant Evaluation:

>>> firstnames = ['Mark', 'Melissa', 'Alex']
>>> lastnames = ['Watney', 'Lewis', 'Vogel']
>>> result = zip(firstnames, lastnames)
>>>
>>> list(result)
[('Mark', 'Watney'), ('Melissa', 'Lewis'), ('Alex', 'Vogel')]


Generate Dict
-------------
>>> firstnames = ['Mark', 'Melissa', 'Alex']
>>> lastnames = ['Watney', 'Lewis', 'Vogel']
>>> result = zip(firstnames, lastnames)
>>>
>>> dict(result)
{'Mark': 'Watney', 'Melissa': 'Lewis', 'Alex': 'Vogel'}

>>> roles = ['botanist', 'commander', 'chemist']
>>> names = ['Mark Watney', 'Melissa Lewis', 'Alex Vogel']
>>>
>>> dict(zip(roles, names))  # doctest: +NORMALIZE_WHITESPACE
{'botanist': 'Mark Watney',
 'commander': 'Melissa Lewis',
 'chemist': 'Alex Vogel'}


Adjusts to the Shortest
-----------------------
* ``zip()`` adjusts to the shortest

>>> firstnames = ['Mark', 'Melissa']
>>> lastnames = ['Watney', 'Lewis', 'Vogel']
>>> result = zip(firstnames, lastnames)
>>>
>>> list(result)
[('Mark', 'Watney'), ('Melissa', 'Lewis')]

Adjust to the Longest
---------------------
* ``itertools.zip_longest(iter1 [,iter2 [...]], [fillvalue=None]) --> zip_longest object``

>>> from itertools import zip_longest
>>>
>>> firstnames = ['Mark', 'Melissa']
>>> lastnames = ['Watney', 'Lewis', 'Vogel']
>>>
>>> list(zip_longest(firstnames, lastnames))
[('Mark', 'Watney'), ('Melissa', 'Lewis'), (None, 'Vogel')]
>>> list(zip_longest(firstnames, lastnames, fillvalue=''))
[('Mark', 'Watney'), ('Melissa', 'Lewis'), ('', 'Vogel')]


Three-way merge
---------------
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


In For Loop
-----------
>>> roles = ['botanist', 'commander', 'chemist']
>>> names = ['Mark Watney', 'Melissa Lewis', 'Alex Vogel']
>>>
>>> for role, name in zip(roles, names):
...     print(f'{role} -> {name}')
botanist -> Mark Watney
commander -> Melissa Lewis
chemist -> Alex Vogel


Future
------
* ``zip(*iterables, strict=False)``
* Since Python 3.10: :pep:`618` -- Add Optional Length-Checking To zip [pep618]_
* Surce [py310doc]_

``zip()`` is often used in cases where the iterables are assumed to be of equal length.
In such cases, it’s recommended to use the ``strict=True`` option.
Its output is the same as regular ``zip()``

>>> list(zip(('a', 'b', 'c'), (1, 2, 3), strict=True))
[('a', 1), ('b', 2), ('c', 3)]

Unlike the default behavior, it checks that the lengths of iterables are identical, raising a ``ValueError`` if they aren’t:

>>> list(zip(['a', 'b', 'c'], [1, 2, 3, 4], strict=True))
Traceback (most recent call last):
ValueError: zip() argument 2 is longer than argument 1

Without the ``strict=True`` argument, any bug that results in iterables of different lengths will be silenced, possibly manifesting as a hard-to-find bug in another part of the program.


References
----------
.. [pep618] https://www.python.org/dev/peps/pep-0618/
.. [py310doc] https://docs.python.org/3.10/library/functions.html#zip
