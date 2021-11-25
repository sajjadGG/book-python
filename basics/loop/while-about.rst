Loop While About
================

.. testsetup::

    # Simulate user input (for test automation)
    from unittest.mock import MagicMock
    input = MagicMock(side_effect=['1'])


Rationale
---------
>>> data = ['a', 'b', 'c']
>>>
>>> data[0]
'a'
>>> data[1]
'b'
>>> data[2]
'c'

>>> data = ['a', 'b', 'c']
>>> i = 0
>>>
>>> if i < 3:
...     print(data[i])
...     i += 1
a
>>>
>>> if i < 3:
...     print(data[i])
...     i += 1
b
>>>
>>> if i < 3:
...     print(data[i])
...     i += 1
c

>>> data = ['a', 'b', 'c']
>>> i = 0
>>>
>>> while i < 3:
...     print(data[i])
...     i += 1
a
b
c


Syntax
------
* Continue execution when argument is ``True``
* Stops if argument is ``False``

``while`` loop generic syntax:

.. code-block:: python

    while <condition>:
        <do something>

>>> # doctest: +SKIP
... while True:
...     pass


Infinite Loop
-------------
Never ending loop.
Used in servers to wait forever for incoming connections.
Used in games for game logic.

>>> # doctest: +SKIP
... while True:
...     print('hello')


Until
-----
Has stop conditions

>>> i = 0
>>>
>>> while i < 3:
...     print(i)
...     i += 1
0
1
2


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
* Generic names:

    * ``i`` - for loop counter
    * ``abort`` - for abort flags
    * ``abort_flag`` - for abort flags


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
