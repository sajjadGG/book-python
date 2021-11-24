Mapping Generate
================


Recap
-----
Pair:

>>> data = ('commander', 'Melissa Lewis')

List of pairs:

>>> data = [
...     ('commander', 'Melissa Lewis'),
...     ('botanist', 'Mark Watney'),
...     ('pilot', 'Rick Martinez'),
... ]


List of Pairs
-------------
>>> data = [
...     ('commander', 'Melissa Lewis'),
...     ('botanist', 'Mark Watney'),
...     ('pilot', 'Rick Martinez')
... ]
>>>
>>> dict(data)  # doctest: +NORMALIZE_WHITESPACE
{'commander': 'Melissa Lewis',
  'botanist': 'Mark Watney',
  'pilot': 'Rick Martinez'}


Enumerate
---------
Function ``enumerate`` will create a list of pairs:

>>> crew = ['Melissa Lewis', 'Mark Watney', 'Rick Martinez']
>>>
>>> result = enumerate(crew)
>>>
>>>
>>> next(result)
(0, 'Melissa Lewis')
>>>
>>> next(result)
(1, 'Mark Watney')
>>>
>>> next(result)
(2, 'Rick Martinez')
>>>
>>> next(result)
Traceback (most recent call last):
StopIteration

Evaluate enumerate object to list instantly:

>>> crew = ['Melissa Lewis', 'Mark Watney', 'Rick Martinez']
>>>
>>> list(enumerate(crew))  # doctest: +NORMALIZE_WHITESPACE
[(0, 'Melissa Lewis'),
 (1, 'Mark Watney'),
 (2, 'Rick Martinez')]

Evaluate enumerate object to dict instantly:

>>> crew = ['Melissa Lewis', 'Mark Watney', 'Rick Martinez']
>>>
>>> dict(enumerate(crew))  # doctest: +NORMALIZE_WHITESPACE
{0: 'Melissa Lewis',
 1: 'Mark Watney',
 2: 'Rick Martinez'}


Zip
---
Function ``zip`` will create a list of pairs:

>>> roles = ['commander', 'botanist', 'pilot']
>>> crew = ['Melissa Lewis', 'Mark Watney', 'Rick Martinez']
>>>
>>> result = zip(roles, crew)
>>>
>>>
>>> next(result)
('commander', 'Melissa Lewis')
>>>
>>> next(result)
('botanist', 'Mark Watney')
>>>
>>> next(result)
('pilot', 'Rick Martinez')
>>>
>>> next(result)
Traceback (most recent call last):
StopIteration

>>> roles = ['commander', 'botanist', 'pilot']
>>> crew = ['Melissa Lewis', 'Mark Watney', 'Rick Martinez']
>>>
>>> list(zip(roles, crew))  # doctest: +NORMALIZE_WHITESPACE
[('commander', 'Melissa Lewis'),
 ('botanist', 'Mark Watney'),
 ('pilot', 'Rick Martinez')]

>>> roles = ['commander', 'botanist', 'pilot']
>>> crew = ['Melissa Lewis', 'Mark Watney', 'Rick Martinez']
>>>
>>> dict(zip(roles, crew))  # doctest: +NORMALIZE_WHITESPACE
{'commander': 'Melissa Lewis',
 'botanist': 'Mark Watney',
 'pilot': 'Rick Martinez'}

>>> roles = ['commander', 'botanist', 'pilot']
>>> firstnames = ['Melissa', 'Mark', 'Rick']
>>> lastnames = ['Lewis', 'Watney', 'Martinez']
>>>
>>> result = zip(roles, firstnames, lastnames)
>>>
>>>
>>> next(result)
('commander', 'Melissa', 'Lewis')
>>>
>>> role, fname, lname = next(result)
>>> role
'botanist'
>>> fname
'Mark'
>>> lname
'Watney'

>>> roles = ['commander', 'botanist', 'pilot']
>>> crew = [('Melissa', 'Lewis'), ('Mark', 'Watney'), ('Rick', 'Martinez')]
>>>
>>> result = zip(roles, crew)
>>>
>>>
>>> next(result)
('commander', ('Melissa', 'Lewis'))
>>>
>>> next(result)
('botanist', ('Mark', 'Watney'))
>>>
>>> next(result)
('pilot', ('Rick', 'Martinez'))
>>>
>>> next(result)
Traceback (most recent call last):
StopIteration

>>> roles = ['commander', 'botanist', 'pilot']
>>> crew = [('Melissa', 'Lewis'), ('Mark', 'Watney'), ('Rick', 'Martinez')]
>>>
>>> list(zip(roles, crew))  # doctest: +NORMALIZE_WHITESPACE
[('commander', ('Melissa', 'Lewis')),
 ('botanist', ('Mark', 'Watney')),
 ('pilot', ('Rick', 'Martinez'))]

>>> roles = ['commander', 'botanist', 'pilot']
>>> crew = [('Melissa', 'Lewis'), ('Mark', 'Watney'), ('Rick', 'Martinez')]
>>>
>>> dict(zip(roles, crew))  # doctest: +NORMALIZE_WHITESPACE
{'commander': ('Melissa', 'Lewis'),
 'botanist': ('Mark', 'Watney'),
 'pilot': ('Rick', 'Martinez')}


Use Case - 0x01
---------------
>>> months = ['January', 'February', 'March', 'April']
>>>
>>>
>>> dict(enumerate(months))
{0: 'January', 1: 'February', 2: 'March', 3: 'April'}
>>>
>>> dict(enumerate(months, start=1))
{1: 'January', 2: 'February', 3: 'March', 4: 'April'}


Assignments
-----------
.. literalinclude:: assignments/mapping_generate_a.py
    :caption: :download:`Solution <assignments/mapping_generate_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/mapping_generate_b.py
    :caption: :download:`Solution <assignments/mapping_generate_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/mapping_generate_c.py
    :caption: :download:`Solution <assignments/mapping_generate_c.py>`
    :end-before: # Solution
