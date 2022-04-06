Loop While Else
===============
* Not only ``if`` statement has ``else`` clause
* Conditionals: ``if ... elif ... else``
* Exceptions: ``try ... except ... else``
* While loop: ``while ... else``
* For loop: ``for ... else``


Example
-------
* 3, 2, 1, 0, Launching rocket to outer space
* 3, 2, Fuel leak detected. Abort, Abort, Abort!
* Note, this will print the value first, decrement and then check for leak

>>> i = 3
>>>
>>> while i >= 0:
...     print(i)
...     i -= 1
...
...     if i == None:  # no problems detected
...         print('Fuel leak detected. Abort, Abort, Abort!')
...         break
3
2
1
0
>>>
>>> print('Launching rocket to outer space')
Launching rocket to outer space

* Can we launch a rocket?

>>> i = 3
>>>
>>> while i >= 0:
...     print(i)
...     i -= 1
...
...     if i == 1:  # problem detected in the last second
...         print('Fuel leak detected. Abort, Abort, Abort!')
...         break
3
2
Fuel leak detected. Abort, Abort, Abort!
>>>
>>> print('Launching rocket to outer space')
Launching rocket to outer space

* This time we aborted and still launched - this is not good
* How to detect if the countdown was successful?


Flag
----
In order to answer those questions we need to introduce a variable to hold
the status if the countdown was aborted or successful. Let's name it
``abort``. If the flag is set to ``True``, then there was an abort procedure
called during the countdown and we cannot launch a rocket to outer space.

>>> abort = False
>>> i = 3
>>>
>>> while i >= 0:
...     print(i)
...     i -= 1
...
...     if i == 1:  # problem detected in the last second
...         print('Fuel leak detected. Abort, Abort, Abort!')
...         abort = True
...         break
3
2
Fuel leak detected. Abort, Abort, Abort!
>>>
>>> if not abort:
...     print('Launching rocket to outer space')

But the problem here is that the follow-up code is split from the ``while``
loop. This can cause problems if the codebase will grow.


Else
----
The ``else`` clause to ``while`` loop will be executed if a loop does not
exit with ``break`` statement. In the other words: if there was no problem
detected during the countdown, launch the rocket to outer space.

>>> i = 3
>>>
>>> while i >= 0:
...     print(i)
...     i -= 1
...
...     if i == 1:  # problem detected in the last second
...         print('Fuel leak detected. Abort, Abort, Abort!')
...         break
... else:
...     print('Launching rocket to outer space')
3
2
Fuel leak detected. Abort, Abort, Abort!

>>> i = 3
>>>
>>> while i >= 0:
...     print(i)
...     i -= 1
...
...     if i == None:  # no problems detected
...         print('Fuel leak detected. Abort, Abort, Abort!')
...         break
... else:
...     print('Launching rocket to outer space')
3
2
1
0
Launching rocket to outer space


Assignments
-----------
.. literalinclude:: assignments/loop_while_else_a.py
    :caption: :download:`Solution <assignments/loop_while_else_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/loop_while_else_b.py
    :caption: :download:`Solution <assignments/loop_while_else_b.py>`
    :end-before: # Solution
