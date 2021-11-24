Sequence Unpack Assignment
==========================


Rationale
---------
* Scalar assignment
* Vector assignment


Syntax
------
Scalar assignment:

>>> a = 1

Vector assignment:

>>> a, b = 1, 2

Multi assignment:

>>> a = b = 1, 2


Scalar Assignment
-----------------
>>> a = 1
>>>
>>> print(a)
1



Vector Assignment
-----------------
>>> a, b = 1, 2
>>>
>>> print(a)
1
>>> print(b)
2

>>> a, b = 1, 2
>>> a, b, c = 1, 2, 3
>>> a, b, c, d = 1, 2, 3, 4
>>> a, b, c, d, e = 1, 2, 3, 4, 5


Right-Side Brackets
-------------------
Scalar assignments:

>>> a = 1, 2
>>> a = (1, 2)
>>> a = [1, 2]
>>> a = {1, 2}

Vector assignments:

>>> a, b = 1, 2
>>> a, b = (1, 2)
>>> a, b = [1, 2]
>>> a, b = {1, 2}

Rationale:

>>> a, b = 1, 2
>>> a, b = (1, 2)


Left-Side Brackets
------------------
>>> (a) = (1)
>>>
>>> print(a)
1

>>> (a, b) = 1, 2
>>> (a, b) = (1, 2)

>>> (a, b, c) = (1, 2, 3)
>>> (a, b, c) = (1, 2, 3)
>>> (a, b, c) = [1, 2, 3]

>>> [a, b, c] = [1, 2, 3]
>>> [a, b, c] = (1, 2, 3)


Errors
------
>>> a, b, c = 1, 2, 3, 4
Traceback (most recent call last):
ValueError: too many values to unpack (expected 3)

>>> a, b, c = 1, 2
Traceback (most recent call last):
ValueError: not enough values to unpack (expected 4, got 3)

>>> {a, b, c} = {1, 2, 3}
Traceback (most recent call last):
SyntaxError: can't assign to literal

>>> {a, b, c} = 1, 2, 3  # doctest: +SKIP
Traceback (most recent call last):
SyntaxError: cannot assign to set display here. Maybe you meant '==' instead of '='?


Unpacking
---------
>>> data = [1,2,3]
>>> a, b, c = data
>>>
>>>
>>> print(a)
1
>>>
>>> print(b)
2
>>>
>>> print(c)
3

>>> line = 'Mark,Watney,44'
>>> firstname, lastname, age = line.split(',')
>>>
>>>
>>> print(firstname)
'Mark'
>>>
>>> print(lastname)
'Watney'
>>>
>>> print(age)
'44'


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


Skipping Values
---------------
* ``_`` is regular variable name, not a special Python syntax
* ``_`` by convention is used for data we don't want to access in future

>>> _ = 'Mark Watney'
>>> print(_)
Mark Watney

>>> line = 'Mark,Watney,1'
>>> firstname, lastname, _ = line.split(',')
>>>
>>> print(firstname)
Mark
>>> print(lastname)
Watney

>>> line = 'Mark,Watney,1,2,3'
>>> firstname, lastname, _, _, _ = line.split(',')
>>>
>>> print(firstname)
Mark
>>> print(lastname)
Watney


Use Case - 0x01
---------------
* Skip

>>> a, b, _ = 1, 2, 3
>>> a, _, _ = 1, 2, 3
>>> a, _, c = 1, 2, 3
>>> _, b, _ = 1, 2, 3
>>> _, _, c = 1, 2, 3


Use Case - 0x02
---------------
* Passwd

>>> line = 'twardowski:x:1001:1001:Jan Twardowski:/home/twardowski:/bin/bash'
>>> line = line.split(':')
>>>
>>> username = line[0]
>>> fullname = line[4]
>>>
>>> print(username)
twardowski
>>> print(fullname)
Jan Twardowski

>>> line = 'twardowski:x:1001:1001:Jan Twardowski:/home/twardowski:/bin/bash'
>>> username, _, _, _, fullname, _, _ = line.split(':')
>>>
>>> print(username)
twardowski
>>> print(fullname)
Jan Twardowski


Use Case - 0x03
---------------
* Important

>>> _, important, _ = 1, 2, 3
>>>
>>> print(important)
2

>>> _, (important, _) = [1, (2, 3)]
>>>
>>> print(important)
2

>>> _, _, important = (True, [1, 2, 3, 4], 5)
>>> important
5

>>> _, _,  important = (True, [1, 2, 3, 4], (5, True))
>>> important
(5, True)
>>>
>>> _, _, (important, _) = (True, [1, 2, 3, 4], (5, True))
>>> important
5

Python understands this as:

>>> _ = (True, [1, 2, 3, 4], (5, True))
>>>
>>> a,b,c = (object, object, object)
>>> a,b,(c,d) = (object, object, (object,object))


Assignments
-----------
.. literalinclude:: assignments/sequence_unpack_a.py
    :caption: :download:`Solution <assignments/sequence_unpack_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/sequence_unpack_b.py
    :caption: :download:`Solution <assignments/sequence_unpack_b.py>`
    :end-before: # Solution
