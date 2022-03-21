Boolean Algebra
===============


Syntax
------
>>> True and True or False
True
>>>
>>> False and False or True
True

>>> (True and True) or False
True
>>>
>>> True and (True or False)
True

>>> True and False or False
False
>>>
>>> True and (False or False)
False


Example
-------
>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>>
>>> (firstname == 'Mark' and lastname == 'Watney') \
...     or (firstname == 'Melissa' and lastname == 'Lewis') \
...     or (firstname == 'Rick' and lastname == 'Martinez')
True

Because:

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>>
>>> firstname == 'Mark' and lastname == 'Watney'
True
>>>
>>> firstname == 'Melissa' and lastname == 'Lewis'
False
>>>
>>> firstname == 'Rick' and lastname == 'Martinez'
False

Rule:

>>> True or False or False
True


Control Flow
------------
* Use parenthesis for explicit order

>>> firstname = 'Pan'
>>> lastname = 'Twardowski'
>>>
>>> if (firstname == 'Mark' and lastname == 'Watney') \
...         or (firstname == 'Melissa' and lastname == 'Lewis') \
...         or (firstname == 'Rick' and lastname == 'Martinez'):
...
...     print('Hello astronaut')
... else:
...     print('Sorry, astronauts only')
Sorry, astronauts only


Good Practices
--------------
>>> # doctest: +SKIP
... for line in file:
...     if line and (not line.startswith('#') or not line.isspace()):
...         ...

>>> # doctest: +SKIP
... for line in file:
...     if len(line) == 0:
...         continue
...
...     if line.startswith('#'):
...         continue
...
...     if line.isspace():
...         continue


Assignments
-----------
.. literalinclude:: assignments/conditional_booleanalgebra_a.py
    :caption: :download:`Solution <assignments/conditional_booleanalgebra_a.py>`
    :end-before: # Solution
