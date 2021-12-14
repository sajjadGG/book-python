Unpack Assignment Star
======================


Rationale
---------
.. figure:: img/unpack-assignment,args,params.png


Arbitrary Number of Arguments
-----------------------------
Unpack values at the right side:

>>> a, b, *c = [1, 2, 3, 4]
>>>
>>>
>>> print(a)
1
>>>
>>> print(b)
2
>>>
>>> print(c)
[3, 4]

Unpack values at the left side:

>>> *a, b, c = [1, 2, 3, 4]
>>>
>>>
>>> print(a)
[1, 2]
>>>
>>> print(b)
3
>>>
>>> print(c)
4

Unpack values from both sides at once:

>>> a, *b, c = [1, 2, 3, 4]
>>>
>>>
>>> print(a)
1
>>>
>>> print(b)
[2, 3]
>>>
>>> print(c)
4

Unpack from variable length:

>>> a, *b, c = [1, 2]
>>>
>>>
>>> print(a)
1
>>> print(b)
[]
>>> print(c)
2

Cannot unpack from both sides at once:

>>> *a, b, *c = [1, 2, 3, 4]
Traceback (most recent call last):
SyntaxError: two starred expressions in assignment

Unpack requires values for required arguments:

>>> a, *b, c = [1]
Traceback (most recent call last):
ValueError: not enough values to unpack (expected at least 2, got 1)


Skipping Values
---------------
* ``_`` is regular variable name, not a special Python syntax
* ``_`` by convention is used for data we don't want to access in future

>>> _ = 'Jan Twardowski'
>>>
>>> print(_)
Jan Twardowski

>>> line = 'Jan,Twardowski,1,2,3,4,5'
>>> firstname, lastname, *_ = line.split(',')
>>>
>>>
>>> print(firstname)
Jan
>>>
>>> print(lastname)
Twardowski

>>> line = '4.9,3.1,1.5,0.1,setosa'
>>> *_, label = line.split(',')
>>>
>>> print(label)
setosa

>>> line = 'twardowski:x:1001:1001:Jan Twardowski:/home/twardowski:/bin/bash'
>>> username, *_, home, _ = line.split(':')
>>>
>>> print(username)
twardowski
>>>
>>> print(home)
/home/twardowski


Use Case - 0x01
---------------
>>> line = 'ares3,watney,lewis,vogel,johanssen'
>>> mission, *crew = line.split(',')
>>>
>>>
>>> print(mission)
ares3
>>>
>>> print(crew)
['watney', 'lewis', 'vogel', 'johanssen']


Use Case - 0x02
---------------
>>> first, *middle, last = [1, 2, 3, 4]
>>>
>>>
>>> print(first)
1
>>>
>>> print(middle)
[2, 3]
>>>
>>> print(last)
4

>>> first, second, *others = [1, 2, 3, 4]
>>>
>>>
>>> print(first)
1
>>>
>>> print(second)
2
>>>
>>> print(others)
[3, 4]


Use Case - 0x03
---------------
>>> first, second, *others = range(0,10)
>>>
>>>
>>> print(first)
0
>>>
>>> print(second)
1
>>>
>>> print(others)
[2, 3, 4, 5, 6, 7, 8, 9]

>>> first, second, *_ = range(0,10)
>>>
>>>
>>> print(first)
0
>>>
>>> print(second)
1


Use Case - 0x04
---------------
* Python Version

>>> import sys
>>>
>>>
>>> major, minor, *_ = sys.version_info
>>>
>>> print(major, minor, sep='.')
3.10


Use Case - 0x05
---------------
* Iris 1D

>>> *features, label = (5.8, 2.7, 5.1, 1.9, 'virginica')
>>>
>>>
>>> print(features)
[5.8, 2.7, 5.1, 1.9]
>>>
>>> print(label)
virginica


Use Case - 0x06
---------------
>>> *features, label = (5.8, 2.7, 5.1, 1.9, 'virginica')
>>> avg = sum(features) / len(features)
>>>
>>>
>>> print(f'{avg=:.2f}, {label=}')
avg=3.88, label='virginica'


Use Case - 0x07
---------------
* Iris 2D

>>> DATA = [
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
... ]
>>>
>>>
>>> for *features, label in DATA:
...     avg = sum(features) / len(features)
...     print(f'{avg=:.2f} {label=}')
avg=3.88 label='virginica'
avg=2.55 label='setosa'
avg=3.48 label='versicolor'


Assignments
-----------
.. literalinclude:: assignments/unpack_star_a.py
    :caption: :download:`Solution <assignments/unpack_star_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/unpack_star_b.py
    :caption: :download:`Solution <assignments/unpack_star_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/unpack_star_c.py
    :caption: :download:`Solution <assignments/unpack_star_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/unpack_star_d.py
    :caption: :download:`Solution <assignments/unpack_star_d.py>`
    :end-before: # Solution
