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
>>> a
1
>>>
>>> b
2
>>>
>>> c
[3, 4]

Unpack values at the left side:

>>> *a, b, c = [1, 2, 3, 4]
>>>
>>>
>>> a
[1, 2]
>>>
>>> b
3
>>>
>>> c
4

Unpack values from both sides at once:

>>> a, *b, c = [1, 2, 3, 4]
>>>
>>>
>>> a
1
>>>
>>> b
[2, 3]
>>>
>>> c
4

Unpack from variable length:

>>> a, *b, c = [1, 2]
>>>
>>>
>>> a
1
>>> b
[]
>>> c
2

Cannot unpack from both sides at once:

>>> *a, b, *c = [1, 2, 3, 4]
Traceback (most recent call last):
SyntaxError: two starred expressions in assignment

Unpack requires values for required arguments:

>>> a, *b, c = [1]
Traceback (most recent call last):
ValueError: not enough values to unpack (expected at least 2, got 1)


Convention
----------
>>> first, *middle, last = [1, 2, 3, 4]
>>>
>>>
>>> first
1
>>>
>>> middle
[2, 3]
>>>
>>> last
4

>>> first, second, *others = [1, 2, 3, 4]
>>>
>>>
>>> first
1
>>>
>>> second
2
>>>
>>> others
[3, 4]


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
>>> mission
'ares3'
>>>
>>> crew
['watney', 'lewis', 'vogel', 'johanssen']


Use Case - 0x02
---------------
>>> first, second, *others = range(0,10)
>>>
>>> first
0
>>>
>>> second
1
>>>
>>> others
[2, 3, 4, 5, 6, 7, 8, 9]

>>> first, second, *_ = range(0,10)
>>>
>>> first
0
>>>
>>> second
1


Use Case - 0x03
---------------
* Python Version

>>> import sys
>>>
>>>
>>> major, minor, *_ = sys.version_info
>>> print(major, minor, sep='.')
3.9


Use Case - 0x04
---------------
* Iris 1D

>>> *features, label = (5.8, 2.7, 5.1, 1.9, 'virginica')
>>>
>>> features
[5.8, 2.7, 5.1, 1.9]
>>>
>>> label
'virginica'


Use Case - 0x05
---------------
>>> *features, label = (5.8, 2.7, 5.1, 1.9, 'virginica')
>>> avg = sum(features) / len(features)
>>>
>>> print(f'{avg=:.2f} {label=}')
avg=3.88, label=virginica


Use Case - 0x06
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
