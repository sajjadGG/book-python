Sequence Tuple
==============


Rationale
---------
* Immutable - cannot add, modify or remove items


Definition
----------
Defining ``tuple()`` is more explicit, however empty tuple with ``()`` is used
more often and it's also faster:

>>> data = ()
>>> data = tuple()

Can store elements of any type:

>>> data = (1, 2, 3)
>>> data = (1.1, 2.2, 3.3)
>>> data = (True, False)
>>> data = ('a', 'b', 'c')
>>> data = ('a', 1, 2.2, True, None)


Type Casting
------------
Builtin function ``tuple()`` converts argument to ``tuple``

>>> data = 'abcd'
>>> tuple(data)
('a', 'b', 'c', 'd')

>>> data = ['a', 'b', 'c', 'd']
>>> tuple(data)
('a', 'b', 'c', 'd')

>>> data = ('a', 'b', 'c', 'd')
>>> tuple(data)
('a', 'b', 'c', 'd')

>>> tuple('a', 'b', 'c', 'd')
Traceback (most recent call last):
TypeError: tuple expected at most 1 argument, got 4


Optional Brackets
-----------------
Brackets are optional, but it's a good practice to always write them:

>>> data = (1, 2, 3)
>>> data = 1, 2, 3

Single element ``tuple`` require comma at the end (**important!**):

>>> data = (1,)
>>> type(data)
<class 'tuple'>

>>> data = (1)
>>> type(data)
<class 'int'>

Comma after last element of multi value tuple is optional:

>>> data = (1, 2)
>>> type(data)
<class 'tuple'>

>>> data = (1, 2,)
>>> type(data)
<class 'tuple'>


Tuple or Int, Float, Str
------------------------
>>> x = 1           # int
>>> x = 1.          # float
>>> x = 1,          # tuple

>>> x = (1)         # int
>>> x = (1.)        # float
>>> x = (1,)        # tuple

>>> x = 'one'       # str
>>> x = 'one',      # tuple
>>> x = 'one'.
Traceback (most recent call last):
SyntaxError: invalid syntax

>>> x = (12)        # int
>>> x = (1.2)       # float
>>> x = (1,2)       # tuple
>>> x = 1.,1.       # tuple
>>> x = 1.,.1       # tuple
>>> x = .1,1.       # tuple


Memory
------
.. figure:: img/memory-list.png

    Define list


Assignments
-----------
.. literalinclude:: assignments/sequence_tuple_a.py
    :caption: :download:`Solution <assignments/sequence_tuple_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/sequence_tuple_b.py
    :caption: :download:`Solution <assignments/sequence_tuple_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/sequence_tuple_c.py
    :caption: :download:`Solution <assignments/sequence_tuple_c.py>`
    :end-before: # Solution
