Loop While Patterns
===================


Important
---------
* Until
* Infinite Loop
* Exit Flag


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


Infinite Loop
-------------
Never ending loop.
Used in servers to wait forever for incoming connections.
Used in games for game logic.

>>> # doctest: +SKIP
... while True:
...     print('hello')


Exit Flag
---------
>>> abort = False
>>> i = 3
>>>
>>> while not abort:
...     print(i)
...     i -= 1
...
...     if i == 1:  # problem detected in the last second
...         print('Fuel leak detected. Abort, Abort, Abort!')
...         abort = True
3
2
Fuel leak detected. Abort, Abort, Abort!

In real life the exit flag pattern is useful if you have for example
multi-threaded application. You can kill all the threads if any thread
changes the flag. Multi-threaded apps will share this value and kill the
loop as soon as the condition will be evaluated.
