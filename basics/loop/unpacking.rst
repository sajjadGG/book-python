Loop Unpacking Assignment
-------------------------


Recap
-----
>>> a, b = 1, 2
>>> a, b = (1, 2)
>>> k, v = (1, 2)
>>> key, value = (1, 2)
>>> role, name = ('commander', 'Melissa Lewis')


List of Pairs
-------------
>>> DATA = [('commander', 'Melissa Lewis'),
...         ('botanist', 'Mark Watney'),
...         ('chemist', 'Alex Vogel')]
>>>
>>> for role, name in DATA:
...     print(f'{role} -> {name}')
commander -> Melissa Lewis
botanist -> Mark Watney
chemist -> Alex Vogel


List of Tuples
--------------
>>> DATA = [(5.1, 3.5, 1.4, 0.2, 'setosa'),
...         (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...         (6.3, 2.9, 5.6, 1.8, 'virginica')]
>>>
>>> for sepal_length, sepal_width, petal_length, petal_width, species in DATA:
...     print(f'{species} -> {sepal_length}')
setosa -> 5.1
versicolor -> 5.7
virginica -> 6.3

>>> DATA = [(5.1, 3.5, 1.4, 0.2, 'setosa'),
...         (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...         (6.3, 2.9, 5.6, 1.8, 'virginica')]
>>>
>>> for sl, sw, pl, pw, s in DATA:
...     print(f'{s} -> {sl}')
setosa -> 5.1
versicolor -> 5.7
virginica -> 6.3


Unpacking Assignment
--------------------
>>> *features, label = (5.8, 2.7, 5.1, 1.9, 'virginica')
>>>
>>> features
[5.8, 2.7, 5.1, 1.9]
>>> label
'virginica'

>>> DATA = [(5.8, 2.7, 5.1, 1.9, 'virginica'),
...         (5.1, 3.5, 1.4, 0.2, 'setosa'),
...         (5.7, 2.8, 4.1, 1.3, 'versicolor')]
>>>
>>> for *features, label in DATA:
...     avg = sum(features) / len(features)
...     print(f'{label} -> {avg}')
virginica -> 3.875
setosa -> 2.55
versicolor -> 3.475

>>> DATA = [(5.8, 2.7, 5.1, 1.9, 'virginica'),
...         (5.1, 3.5, 1.4, 0.2, 'setosa'),
...         (5.7, 2.8, 4.1, 1.3, 'versicolor')]
>>>
>>> for *X,y in DATA:
...     avg = sum(X) / len(X)
...     print(f'{y} -> {avg}')
virginica -> 3.875
setosa -> 2.55
versicolor -> 3.475


Unused Values
-------------
>>> DATA = [(5.1, 3.5, 1.4, 0.2, 'setosa'),
...         (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...         (6.3, 2.9, 5.6, 1.8, 'virginica')]
>>>
>>> for sepal_length, _, _, _, species in DATA:
...     print(f'{species} -> {sepal_length}')
setosa -> 5.1
versicolor -> 5.7
virginica -> 6.3

>>> DATA = [(5.8, 2.7, 5.1, 1.9, 'virginica'),
...         (5.1, 3.5, 1.4, 0.2, 'setosa'),
...         (5.7, 2.8, 4.1, 1.3, 'versicolor')]
>>>
>>> for sepal_length, *_, species in DATA:
...     print(f'{species} -> {sepal_length}')
virginica -> 5.8
setosa -> 5.1
versicolor -> 5.7


Mixed
-----
>>> DATA = [(1, 2),
...         ('name', 'Jan Twardowski'),
...         ('species', ['setosa', 'versicolor', 'virginica']),
...         ((1, 2), ['Johnson Space Center', 'Kennedy Space Center']),
...         (['NASA', 'ESA', 'Roscosmos'], 1)]
>>>
>>> for first, second in DATA:
...     print(f'{first} -> {second}')
1 -> 2
name -> Jan Twardowski
species -> ['setosa', 'versicolor', 'virginica']
(1, 2) -> ['Johnson Space Center', 'Kennedy Space Center']
['NASA', 'ESA', 'Roscosmos'] -> 1


Enumerate
---------
* Pythonic way
* Preferred over ``i=0`` and ``i+=1`` for every iteration
* ``enumerate()`` will return ``counter`` and ``value`` for every iteration

>>> DATA = ['a', 'b', 'c']
>>> result = enumerate(DATA)
>>>
>>> next(result)
(0, 'a')
>>> next(result)
(1, 'b')
>>> next(result)
(2, 'c')
>>> next(result)
Traceback (most recent call last):
StopIteration

``enumerate()`` will return ``counter`` and ``value`` for every iteration:

>>> DATA = ['a', 'b', 'c']
>>>
>>> for i, letter in enumerate(DATA):
...     print(f'{i} -> {letter}')
0 -> a
1 -> b
2 -> c

``enumerate()`` can start with custom number:

>>> DATA = ['a', 'b', 'c']
>>>
>>> for i, letter in enumerate(DATA, start=5):
...     print(f'{i} -> {letter}')
5 -> a
6 -> b
7 -> c

>>> DATA = [(5.1, 3.5, 1.4, 0.2, 'setosa'),
...         (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...         (6.3, 2.9, 5.6, 1.8, 'virginica')]
>>>
>>> for i, row in enumerate(DATA):
...     print(f'{i} -> {row}')
0 -> (5.1, 3.5, 1.4, 0.2, 'setosa')
1 -> (5.7, 2.8, 4.1, 1.3, 'versicolor')
2 -> (6.3, 2.9, 5.6, 1.8, 'virginica')


Zip
---
>>> roles = ['commander', 'botanist', 'chemist']
>>> crew = ['Melissa Lewis', 'Mark Watney', 'Alex Vogel']
>>> result = zip(roles, crew)
>>>
>>> next(result)
('commander', 'Melissa Lewis')
>>> next(result)
('botanist', 'Mark Watney')
>>> next(result)
('chemist', 'Alex Vogel')
>>> next(result)
Traceback (most recent call last):
StopIteration

>>> roles = ['commander', 'botanist', 'chemist']
>>> crew = ['Melissa Lewis', 'Mark Watney', 'Alex Vogel']
>>>
>>> for role, name in zip(roles, crew):
...     print(f'{role} -> {name}')
commander -> Melissa Lewis
botanist -> Mark Watney
chemist -> Alex Vogel


Assignments
-----------
.. literalinclude:: assignments/loop_unpacking_a.py
    :caption: :download:`Solution <assignments/loop_unpacking_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_unpacking_b.py
    :caption: :download:`Solution <assignments/loop_unpacking_b.py>`
    :end-before: # Solution
