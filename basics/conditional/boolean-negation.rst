Boolean Negation
================
* ``not`` logically inverts

>>> not True
False

>>> not False
True


SetUp
-----
Simulate user input (for test automation):

>>> from unittest.mock import MagicMock
>>> input = MagicMock(side_effect=['', 'Mark Watney'])


Checking If Empty
-----------------
>>> name = input('What is your name?: ')  #input: ''
>>>
>>> if name:
...     print('Not empty')
...
>>> if not name:
...     print('Empty')
Empty


>>> name = input('What is your name?: ')  #input: 'Mark Watney'
>>>
>>> if name is not None:
...     print(f'Hello {name}')
Hello Mark Watney


Control Flow
------------
* ``not`` negates (logically inverts) condition

>>> crew = {'mwatney', 'mlewis', 'rmartinez'}
>>>
>>> if 'ptwardowski' not in crew:
...     print('You are not assigned to the crew')
You are not assigned to the crew


.. todo:: Assignments
