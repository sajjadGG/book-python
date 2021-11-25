Loop While Else
===============


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


Assignments
-----------
.. literalinclude:: assignments/loop_while_else_a.py
    :caption: :download:`Solution <assignments/loop_while_else_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_while_else_b.py
    :caption: :download:`Solution <assignments/loop_while_else_b.py>`
    :end-before: # Solution
