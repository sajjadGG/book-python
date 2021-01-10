Map
===

Built-in
--------
* ``map(callable, *iterables)``

>>> data = [1, 2, 3]
>>> result = map(float, data)
>>>
>>> next(result)
1.0
>>> next(result)
2.0
>>> next(result)
3.0
>>> next(result)
Traceback (most recent call last):
StopIteration

>>> data = [1, 2, 3]
>>> result = map(float, data)
>>>
>>> list(result)
[1.0, 2.0, 3.0]

>>> data = [1, 2, 3]
>>> result = map(float, data)
>>>
>>> tuple(map(float, data))
(1.0, 2.0, 3.0)

>>> data = [1, 2, 3]
>>> result = map(float, data)
>>>
>>> set(map(float, data))
{1.0, 2.0, 3.0}

>>> DATA = [1, 2, 3]
>>>
>>> result = (float(x) for x in DATA)
>>> list(result)
[1.0, 2.0, 3.0]

>>> DATA = [1.1, 2.2, 3.3]
>>> result = map(round, DATA)
>>> list(result)
[1, 2, 3]

>>> def square(x):
...     return x ** 2
...
>>> data = [1, 2, 3]
>>> result = map(square, data)
>>>
>>> list(result)
[1, 4, 9]


Use Cases
---------
>>> def increment(x):
...     return x + 1
>>>
>>>
>>> data = [1, 2, 3, 4]
>>> result = map(increment, data)
>>>
>>> list(result)
[2, 3, 4, 5]

>>> PL = {'ą': 'a', 'ć': 'c', 'ę': 'e',
...       'ł': 'l', 'ń': 'n', 'ó': 'o',
...       'ś': 's', 'ż': 'z', 'ź': 'z'}
>>>
>>> def translate(letter):
...     return PL.get(letter, letter)
>>>
>>>
>>> text = 'zażółć gęślą jaźń'
>>> result = map(translate, text)
>>> ''.join(result)
'zazolc gesla jazn'

>>> import sys
>>>
>>> # doctest: +SKIP
... print(sum(map(int, sys.stdin)))

.. code-block:: console

    $ cat ~/.profile |grep addnum
    alias addnum='python -c"import sys; print(sum(map(int, sys.stdin)))"'
