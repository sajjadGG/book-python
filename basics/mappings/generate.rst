Mapping Generate
================


Pair
----
>>> pair = [
...     ('commander', 'Melissa Lewis')]
>>>
>>> dict(pair)
{'commander': 'Melissa Lewis'}


List of Pairs
-------------
>>> pairs = [
...     ('commander', 'Melissa Lewis'),
...     ('botanist', 'Mark Watney'),
...     ('chemist', 'Rick Martinez')]
>>>
>>> dict(pairs)  # doctest: +NORMALIZE_WHITESPACE
{'commander': 'Melissa Lewis',
  'botanist': 'Mark Watney',
  'chemist': 'Rick Martinez'}


Enumerate
---------
>>> crew = ['Melissa Lewis', 'Mark Watney', 'Rick Martinez']
>>> astronaut = enumerate(crew)
>>>
>>> next(astronaut)
(0, 'Melissa Lewis')
>>> next(astronaut)
(1, 'Mark Watney')
>>> next(astronaut)
(2, 'Rick Martinez')
>>> next(astronaut)
Traceback (most recent call last):
StopIteration

>>> crew = ['Melissa Lewis', 'Mark Watney', 'Rick Martinez']
>>>
>>> list(enumerate(crew))  # doctest: +NORMALIZE_WHITESPACE
[(0, 'Melissa Lewis'),
 (1, 'Mark Watney'),
 (2, 'Rick Martinez')]
>>> dict(enumerate(crew))  # doctest: +NORMALIZE_WHITESPACE
{0: 'Melissa Lewis',
 1: 'Mark Watney',
 2: 'Rick Martinez'}


Zip
---
* ``zip`` is a generator
* ``zip`` will create a list of pairs (like ``dict.items()``)

>>> roles = ['commander', 'botanist', 'chemist']
>>> crew = ['Melissa Lewis', 'Mark Watney', 'Rick Martinez']
>>>
>>> astronaut = zip(roles, crew)
>>> next(astronaut)
('commander', 'Melissa Lewis')
>>> next(astronaut)
('botanist', 'Mark Watney')
>>> next(astronaut)
('chemist', 'Rick Martinez')
>>> next(astronaut)
Traceback (most recent call last):
StopIteration

>>> roles = ['commander', 'botanist', 'chemist']
>>> crew = ['Melissa Lewis', 'Mark Watney', 'Rick Martinez']
>>>
>>> list(zip(roles, crew))  # doctest: +NORMALIZE_WHITESPACE
[('commander', 'Melissa Lewis'),
 ('botanist', 'Mark Watney'),
 ('chemist', 'Rick Martinez')]
>>>
>>> dict(zip(roles, crew))  # doctest: +NORMALIZE_WHITESPACE
{'commander': 'Melissa Lewis',
 'botanist': 'Mark Watney',
 'chemist': 'Rick Martinez'}

>>> roles = ['commander', 'botanist', 'chemist']
>>> firstnames = ['Melissa', 'Mark', 'Rick']
>>> lastnames = ['Lewis', 'Watney', 'Martinez']
>>>
>>> data = zip(roles, firstnames, lastnames)
>>> next(data)
('commander', 'Melissa', 'Lewis')
>>>
>>> role, fname, lname = next(data)
>>> role
'botanist'
>>> fname
'Mark'
>>> lname
'Watney'

>>> roles = ['commander', 'botanist', 'chemist']
>>> crew = [('Melissa', 'Lewis'), ('Mark', 'Watney'), ('Rick', 'Martinez')]
>>>
>>> astronauts = zip(roles, crew)
>>> next(astronauts)
('commander', ('Melissa', 'Lewis'))
>>> next(astronauts)
('botanist', ('Mark', 'Watney'))
>>> next(astronauts)
('chemist', ('Rick', 'Martinez'))
>>> next(astronauts)
Traceback (most recent call last):
StopIteration

>>> roles = ['commander', 'botanist', 'chemist']
>>> crew = [('Melissa', 'Lewis'), ('Mark', 'Watney'), ('Rick', 'Martinez')]
>>>
>>> list(zip(roles, crew))  # doctest: +NORMALIZE_WHITESPACE
[('commander', ('Melissa', 'Lewis')),
 ('botanist', ('Mark', 'Watney')),
 ('chemist', ('Rick', 'Martinez'))]
>>> dict(zip(roles, crew))  # doctest: +NORMALIZE_WHITESPACE
{'commander': ('Melissa', 'Lewis'),
 'botanist': ('Mark', 'Watney'),
 'chemist': ('Rick', 'Martinez')}


Use Case
--------
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
