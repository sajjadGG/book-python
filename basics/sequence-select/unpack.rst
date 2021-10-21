Unpacking Assignment
====================


Rationale
---------
* More information in `Unpacking Assignment`
* More information in `Unpacking Parameters`
* More information in `Unpacking Arguments`

>>> a = 1
>>> a, b = 1, 2
>>> a, b, c = 1, 2, 3

>>> a, b, c = (1, 2, 3)
>>> a, b, c = [1, 2, 3]
>>> a, b, c = {1, 2, 3}

>>> (a, b, c) = (1, 2, 3)
>>> (a, b, c) = [1, 2, 3]

>>> [a, b, c] = [1, 2, 3]
>>> [a, b, c] = (1, 2, 3)

.. figure:: img/function-unpacking,args,kwargs.png


Errors
------
>>> {a, b, c} = {1, 2, 3}
Traceback (most recent call last):
SyntaxError: can't assign to literal

>>> a, b, c = [1, 2, 3, 4]
Traceback (most recent call last):
ValueError: too many values to unpack (expected 3)

>>> a, b, c, d = [1, 2, 3]
Traceback (most recent call last):
ValueError: not enough values to unpack (expected 4, got 3)


Arbitrary Number of Arguments
-----------------------------
Unpacking values at the right side:

>>> a, b, *c = [1, 2, 3, 4]
>>>
>>> a
1
>>> b
2
>>> c
[3, 4]

Unpacking values at the left side:

>>> *a, b, c = [1, 2, 3, 4]
>>>
>>> a
[1, 2]
>>> b
3
>>> c
4

Unpacking values from both sides at once:

>>> a, *b, c = [1, 2, 3, 4]
>>>
>>> a
1
>>> b
[2, 3]
>>> c
4

Unpacking from variable length:

>>> a, *b, c = [1, 2]
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

Unpacking requires values for required arguments:

>>> a, *b, c = [1]
Traceback (most recent call last):
ValueError: not enough values to unpack (expected at least 2, got 1)


Nested
------
>>> a, (b, c) = [1, (2, 3)]
>>>
>>> a
1
>>> b
2
>>> c
3


Convention
----------
>>> first, *middle, last = [1, 2, 3, 4]
>>>
>>> first
1
>>> middle
[2, 3]
>>> last
4

>>> first, second, *others = [1, 2, 3, 4]
>>>
>>> first
1
>>> second
2
>>> others
[3, 4]


Skipping Values
---------------
* ``_`` is regular variable name, not a special Python syntax
* ``_`` by convention is used for data we don't want to access in future

>>> _ = 'Jan Twardowski'
>>> print(_)
Jan Twardowski

>>> line = 'Jan,Twardowski,1'
>>> firstname, lastname, _ = line.split(',')
>>>
>>> print(firstname)
Jan
>>> print(lastname)
Twardowski

>>> line = 'Jan,Twardowski,1,2,3,4,5'
>>> firstname, lastname, *_ = line.split(',')
>>>
>>> print(firstname)
Jan
>>> print(lastname)
Twardowski

>>> a, _, c = 1, 2, 3
>>>
>>> print(a)
1
>>> print(c)
3

>>> _, b, _ = 1, 2, 3
>>>
>>> print(b)
2

>>> line = '4.9,3.1,1.5,0.1,setosa'
>>> *_, label = line.split(',')
>>>
>>> print(label)
setosa

>>> line = 'twardowski:x:1001:1001:Jan Twardowski:/home/twardowski:/bin/bash'
>>> username, _, uid, *_ = line.split(':')
>>>
>>> print(username)
'twardowski'
>>> print(uid)
'1001'

>>> line = 'twardowski:x:1001:1001:Jan Twardowski:/home/twardowski:/bin/bash'
>>> username, _, _, _, fullname, *_ = line.split(':')
>>>
>>> print(username)
twardowski
>>> print(fullname)
Jan Twardowski

>>> line = 'twardowski:x:1001:1001:Jan Twardowski:/home/twardowski:/bin/bash'
>>> username, *_, home, _ = line.split(':')
>>>
>>> print(username)
twardowski
>>> print(home)
/home/twardowski

>>> _, (interesting, _) = [1, (2, 3)]
>>>
>>> print(interesting)
2


>>> a, b, (c, [d]) = [1, 2, (3, [4])]
>>> _, _, (_, [interesting]) = [1, 2, (3, [4])]


Use Cases
---------
>>> import sys
>>>
>>> sys.version_info
sys.version_info(major=3, minor=9, micro=7, releaselevel='final', serial=0)
>>>
>>> major, minor, *_ = sys.version_info
>>> print(major, minor, sep='.')
3.9

>>> *features, label = (5.8, 2.7, 5.1, 1.9, 'virginica')
>>>
>>> features
[5.8, 2.7, 5.1, 1.9]
>>> label
'virginica'

>>> *features, label = (5.8, 2.7, 5.1, 1.9, 'virginica')
>>> avg = sum(features) / len(features)
>>>
>>> print(label, avg)
virginica 3.875

>>> line = 'ares3,watney,lewis,vogel,johanssen'
>>> mission, *crew = line.split(',')
>>>
>>> mission
'ares3'
>>> crew
['watney', 'lewis', 'vogel', 'johanssen']

>>> first, second, *others = range(10)
>>>
>>> first
0
>>> second
1
>>> others
[2, 3, 4, 5, 6, 7, 8, 9]

>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>> for *features, label in DATA[1:]:
...     avg = sum(features) / len(features)
...     print(label, avg)
virginica 3.875
setosa 2.55
versicolor 3.475
virginica 4.1499999999999995
versicolor 3.9000000000000004
setosa 2.35


Assignments
-----------
.. literalinclude:: assignments/sequence_unpack_a.py
    :caption: :download:`Solution <assignments/sequence_unpack_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/sequence_unpack_b.py
    :caption: :download:`Solution <assignments/sequence_unpack_b.py>`
    :end-before: # Solution
