Boolean Conjunction
===================


.. code-block:: text

    1 & 1 -> 1
    1 & 0 -> 0
    0 & 1 -> 0
    0 & 0 -> 0


Syntax
------
>>> True and True
True

>>> True and False
False

>>> False and True
False

>>> False and False
False


Example 1
---------
>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>> firstname == 'Mark' and lastname == 'Watney'
True

Because:

>>> firstname == 'Mark'
True
>>> lastname == 'Watney'
True

Rule:

>>> True and True
True


Example 2
---------
>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>> firstname == 'Mark' and lastname == 'Twardowski'
False

Because:

>>> firstname == 'Mark'
True
>>> lastname == 'Twardowski'
False

Rule:

>>> True and False
False


Control Flow
------------
>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>> if firstname == 'Mark' and lastname == 'Watney':
...     print('Hello Space Pirate')
... else:
...     print('Sorry, astronauts only')
Hello Space Pirate


.. todo:: Assignments
