Unpacking Assignment
====================


Rationale
---------
* Scalar assignment
* Vector assignment

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

>>> _, (interesting, _) = [1, (2, 3)]
>>>
>>> print(interesting)
2

>>> line = 'twardowski:x:1001:1001:Jan Twardowski:/home/twardowski:/bin/bash'
>>> username, _, _, _, fullname, _, _ = line.split(':')
>>>
>>> print(username)
twardowski
>>> print(fullname)
Jan Twardowski


Use Case
--------
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
.. literalinclude:: assignments/unpacking_assignment_a.py
    :caption: :download:`Solution <assignments/unpacking_assignment_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/unpacking_assignment_b.py
    :caption: :download:`Solution <assignments/unpacking_assignment_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/unpacking_assignment_c.py
    :caption: :download:`Solution <assignments/unpacking_assignment_c.py>`
    :end-before: # Solution
