Loop While
==========

.. testsetup::

    # Mock input() built-in function
    from unittest.mock import MagicMock
    input = MagicMock(return_value='1')


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


Convention
----------
* The longer the loop scope, the longer the variable name should be
* Avoid one letters if scope is longer than one line
* Generic names:

    * ``i`` - for loop counter
    * ``abort`` - for abort flags
    * ``abort_flag`` - for abort flags


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


Iterating Over Sequence
-----------------------
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


Exit flag
---------
Exit flag pattern is useful if you have for example multi-threaded application:

>>> abort = False
>>> i = 10
>>>
>>> while not abort:
...     print(i)
...     i -= 1
...
...     if i == 6:
...         print('Fuel leak detected. Abort, Abort, Abort!')
...         abort = True
10
9
8
7
Fuel leak detected. Abort, Abort, Abort!


Force Exit the Loop
-------------------
Force exit the loop using ``break`` keyword:

>>> i = 10
>>>
>>> while True:
...     print(i)
...     i -= 1
...
...     if i == 6:
...         print('Fuel leak detected. Abort, Abort, Abort!')
...         break
10
9
8
7
Fuel leak detected. Abort, Abort, Abort!

Exiting the loop using ``break`` keyword:

>>> # doctest: +SKIP
... while True:
...     number = input('Type number: ')
...
...     if not number:
...         # if user hit enter
...         # without typing a number
...         break


Force Skip Iteration
--------------------
* if ``continue`` is encountered, it will jump to next loop iteration

>>> TEXT = ['# "Moon Speech" by John F. Kennedy, Rice Stadium, Houston, TX, 1962-09-12',
...         '# Source: http://er.jsc.nasa.gov/seh/ricetalk.htm',
...         'We choose to go to the Moon.',
...         'We choose to go to the Moon in this decade and do the other things.',
...         'Not because they are easy, but because they are hard.',
...         'Because that goal will serve to organize and measure the best of our energies a skills.',
...         'Because that challenge is one that we are willing to accept.',
...         'One we are unwilling to postpone.',
...         'And one we intend to win']
>>>
>>> i = 0
>>>
>>> while i < len(TEXT):
...     line = TEXT[i]
...     i += 1
...
...     if line.startswith('#'):
...         continue
...
...     print(line)
We choose to go to the Moon.
We choose to go to the Moon in this decade and do the other things.
Not because they are easy, but because they are hard.
Because that goal will serve to organize and measure the best of our energies a skills.
Because that challenge is one that we are willing to accept.
One we are unwilling to postpone.
And one we intend to win

Force skip iteration using ``continue`` keyword:

>>> i = 0
>>>
>>> while i < 10:
...     print(i, end=', ')
...     i += 1
...
...     if i % 3:
...         continue
...
...     print(end='\n')  # doctest: +NORMALIZE_WHITESPACE
0, 1, 2,
3, 4, 5,
6, 7, 8,
9,


Assignments
-----------
.. literalinclude:: assignments/loop_while_a.py
    :caption: :download:`Solution <assignments/loop_while_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_while_b.py
    :caption: :download:`Solution <assignments/loop_while_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_while_c.py
    :caption: :download:`Solution <assignments/loop_while_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_while_d.py
    :caption: :download:`Solution <assignments/loop_while_d.py>`
    :end-before: # Solution
