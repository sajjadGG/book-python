Loop While About
================


Rationale
---------
* Iterate over sequences (iterables)
* Repeat `if` until result is `False`


Syntax
------
* Continue execution when argument is ``True``
* Stops if argument is ``False``

Generic syntax:

.. code-block:: python

    while <condition>:
        <do something>

Example:

>>> # doctest: +SKIP
... while True:
...     pass


Getitem with Const
------------------
>>> data = ['a', 'b', 'c']
>>>
>>> print(data[0])
a
>>> print(data[1])
b
>>> print(data[2])
c
>>> print(data[3])
Traceback (most recent call last):
IndexError: list index out of range


Getitem with Variable
---------------------
>>> data = ['a', 'b', 'c']
>>>
>>> i = 0               # i = 0
>>> print(data[i])      # data[0]
a
>>>
>>> i += 1              # i = 1
>>> print(data[i])      # data[1]
b
>>>
>>> i += 1              # i = 2
>>> print(data[i])      # data[2]
c
>>>
>>> i += 1              # i = 3
>>> print(data[i])      # data[3]
Traceback (most recent call last):
IndexError: list index out of range


Getitem with Boundary Checking
------------------------------
>>> data = ['a', 'b', 'c']
>>> len(data)
3

>>> data = ['a', 'b', 'c']
>>> i = 0
>>>
>>> if i < len(data):
...     print(data[i])  # data[0]
...     i += 1          # i = 1
a
>>>
>>> if i < len(data):   # True
...     print(data[i])  # data[1]
...     i += 1          # i = 2
b
>>>
>>> if i < len(data):   # True
...     print(data[i])  # data[2]
...     i += 1          # i = 3
c
>>>
>>> if i < len(data):   # False
...     print(data[i])  # will not execute
...     i += 1          # will not execute


While Loop
----------
>>> data = ['a', 'b', 'c']
>>> i = 0
>>>
>>> while i < len(data):
...     print(data[i])
...     i += 1
a
b
c


Sequence Iteration
------------------
Better idea for this is to use ``for`` loop. ``for`` loop supports Iterators. ``len()`` must write all ``numbers`` to memory, to calculate its length:

>>> i = 0
>>> data = ['a', 'b', 'c']
>>>
>>> while i < 3:
...     print(i, data[i])
...     i += 1
0 a
1 b
2 c

>>> i = 0
>>> data = ['a', 'b', 'c']
>>> length = 3
>>>
>>> while i < length:
...     print(i, data[i])
...     i += 1
0 a
1 b
2 c

>>> i = 0
>>> data = ['a', 'b', 'c']
>>>
>>> while i < len(data):
...     print(i, data[i])
...     i += 1
0 a
1 b
2 c



Good Practices
--------------
* The longer the loop scope, the longer the variable name should be
* Avoid one letters if scope is longer than one line
* Use ``i`` for loop counter (it is traditional name in almost all languages)


Assignments
-----------
.. literalinclude:: assignments/loop_while_about_a.py
    :caption: :download:`Solution <assignments/loop_while_about_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_while_about_b.py
    :caption: :download:`Solution <assignments/loop_while_about_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_while_about_c.py
    :caption: :download:`Solution <assignments/loop_while_about_c.py>`
    :end-before: # Solution
