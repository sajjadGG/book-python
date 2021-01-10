Zip
===

Built-in
--------
* ``zip(*iterables)``

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
