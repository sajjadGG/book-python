Unpacking Parameter Syntax
==========================


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
...     print(a, b, c)
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

>>> help(sorted)
Help on built-in function sorted in module builtins:

sorted(iterable, /, *, key=None, reverse=False)
    Return a new list containing all items from the iterable in ascending order.

    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.


Use Case - Sum
--------------
* https://docs.python.org/3/library/functions.html#sum:

>>> help(sum)
Help on built-in function sum in module builtins:

sum(iterable, /, start=0)
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers

    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.


Use Case - Strip
----------------
* https://docs.python.org/3/library/stdtypes.html#str.strip

>>> help(str.strip)
Help on method_descriptor:

strip(self, chars=None, /)
    Return a copy of the string with leading and trailing whitespace removed.

    If chars is given and not None, remove characters in chars instead.


Use Case - Split
----------------
* https://docs.python.org/3/library/stdtypes.html#str.split

>>> help(str.split)
Help on method_descriptor:

split(self, /, sep=None, maxsplit=-1)
    Return a list of the words in the string, using sep as the delimiter string.

    sep
      The delimiter according which to split the string.
      None (the default value) means split according to any whitespace,
      and discard empty strings from the result.
    maxsplit
      Maximum number of splits to do.
      -1 (the default value) means no limit.


Assignments
-----------
.. literalinclude:: assignments/function_parameter_syntax_a.py
    :caption: :download:`Solution <assignments/function_parameter_syntax_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_parameter_syntax_b.py
    :caption: :download:`Solution <assignments/function_parameter_syntax_b.py>`
    :end-before: # Solution
