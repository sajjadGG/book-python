Unpack Parameter Syntax
=======================


Recap
-----
>>> def echo(a, b, c=3):
...      print(f'{a=} {b=} {c=}')
>>>
>>>
>>> echo(1, 2)
a=1 b=2 c=3
>>>
>>> echo(1, b=2)
a=1 b=2 c=3
>>>
>>> echo(1, c=3)
Traceback (most recent call last):
TypeError: echo() missing 1 required positional argument: 'b'
>>>
>>> echo(1, 2, 3)
a=1 b=2 c=3
>>>
>>> echo(1, 2, c=3)
a=1 b=2 c=3
>>>
>>> echo(1, b=2, c=3)
a=1 b=2 c=3
>>>
>>> echo(a=1, b=2, c=3)
a=1 b=2 c=3



Keyword-only Parameters
-----------------------
* All parameters after ``*`` must be keyword-only

>>> def echo(a, *, b, c=3):
...     print(f'{a=} {b=} {c=}')
>>>
>>>
>>> echo(1, 2)
Traceback (most recent call last):
TypeError: echo() takes 1 positional argument but 2 were given
>>>
>>> echo(1, b=2)
a=1 b=2 c=3
>>>
>>> echo(1, c=3)
Traceback (most recent call last):
TypeError: echo() missing 1 required keyword-only argument: 'b'
>>>
>>> echo(1, 2, 3)
Traceback (most recent call last):
TypeError: echo() takes 1 positional argument but 3 were given
>>>
>>> echo(1, 2, c=3)
Traceback (most recent call last):
TypeError: echo() takes 1 positional argument but 2 positional arguments (and 1 keyword-only argument) were given
>>>
>>> echo(1, b=2, c=3)
a=1 b=2 c=3
>>>
>>> echo(a=1, b=2, c=3)
a=1 b=2 c=3


Positional-only Parameters
--------------------------
* Since Python 3.8: :pep:`570` -- Python Positional-Only Parameters
* All parameters before ``/`` must be positional-only

>>> def echo(a, /, b, c=3):
...     print(f'{a=} {b=} {c=}')
>>>
>>>
>>> echo(1, 2)
a=1 b=2 c=3
>>>
>>> echo(1, b=2)
a=1 b=2 c=3
>>>
>>> echo(1, c=3)
Traceback (most recent call last):
TypeError: echo() missing 1 required positional argument: 'b'
>>>
>>> echo(1, 2, 3)
a=1 b=2 c=3
>>>
>>> echo(1, 2, c=3)
a=1 b=2 c=3
>>>
>>> echo(1, b=2, c=3)
a=1 b=2 c=3
>>>
>>> echo(a=1, b=2, c=3)
Traceback (most recent call last):
TypeError: echo() got some positional-only arguments passed as keyword arguments: 'a'


Positional and Keyword Parameters
---------------------------------
>>> def echo(a, /, b, *, c=3):
...     print(f'{a=} {b=} {c=}')
>>>
>>>
>>> echo(1, 2)
a=1 b=2 c=3
>>>
>>> echo(1, b=2)
a=1 b=2 c=3
>>>
>>> echo(1, c=3)
Traceback (most recent call last):
TypeError: echo() missing 1 required positional argument: 'b'
>>>
>>> echo(1, 2, 3)
Traceback (most recent call last):
TypeError: echo() takes 2 positional arguments but 3 were given
>>>
>>> echo(1, 2, c=3)
a=1 b=2 c=3
>>>
>>> echo(1, b=2, c=3)
a=1 b=2 c=3
>>>
>>> echo(a=1, b=2, c=3)
Traceback (most recent call last):
TypeError: echo() got some positional-only arguments passed as keyword arguments: 'a'


Use Case - Add
--------------
* https://docs.python.org/3/library/operator.html#operator.add

>>> def add(a, b, /):
...     return a + b


Use Case - Divmod
-----------------
>>> def divmod(a, b, /):
...     return a//b, a%b


Use Case - Sorted
-----------------
* https://docs.python.org/3/library/functions.html#sorted:
* `sorted(iterable, /, *, key=None, reverse=False)`

>>> from inspect import signature
>>>
>>>
>>> signature(sorted)
<Signature (iterable, /, *, key=None, reverse=False)>


Use Case - Sum
--------------
* https://docs.python.org/3/library/functions.html#sum:
* `sum(iterable, /, start=0)`

>>> from inspect import signature
>>>
>>>
>>> signature(sum)
<Signature (iterable, /, start=0)>


Use Case - Strip
----------------
* https://docs.python.org/3/library/stdtypes.html#str.strip
* `str.strip(self, chars=None, /)`

>>> from inspect import signature
>>>
>>>
>>> signature(str.strip)
<Signature (self, chars=None, /)>


Use Case - Split
----------------
* https://docs.python.org/3/library/stdtypes.html#str.split
* `str.split(self, /, sep=None, maxsplit=-1)`

>>> from inspect import signature
>>>
>>>
>>> signature(str.split)
<Signature (self, /, sep=None, maxsplit=-1)>


Assignments
-----------
.. literalinclude:: assignments/function_parameter_syntax_a.py
    :caption: :download:`Solution <assignments/function_parameter_syntax_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_parameter_syntax_b.py
    :caption: :download:`Solution <assignments/function_parameter_syntax_b.py>`
    :end-before: # Solution
