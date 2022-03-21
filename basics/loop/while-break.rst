Loop While Break
================

.. testsetup::

    # Simulate user input (for test automation)
    from unittest.mock import MagicMock
    input = MagicMock(side_effect=['1'])


Important
---------
* Force exit the loop


Syntax
------
>>> while True:
...     break


Example
-------
>>> i = 0
>>>
>>> while True:
...     print(i)
...     i += 1
...     if i == 3:
...         break
0
1
2


No Input
--------
* if user hit enter, without typing a number

>>> # doctest: +SKIP
... while True:
...     number = input('Type number: ')
...
...     if not number:
...         # if user hit enter
...         # without typing a number
...         break


Use Case - 0x01
---------------
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


Assignments
-----------
.. literalinclude:: assignments/loop_while_break_a.py
    :caption: :download:`Solution <assignments/loop_while_break_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_while_break_b.py
    :caption: :download:`Solution <assignments/loop_while_break_b.py>`
    :end-before: # Solution
