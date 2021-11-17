Block If
========

.. testsetup::

    # Simulate user input (for test automation)
    from unittest.mock import MagicMock
    input = MagicMock(side_effect=['Mark Watney'])


Syntax
------
>>> # doctest: +SKIP
... if <condition>:
...     <do something>


Oneline Block
-------------
>>> if True:
...     print('First line of the true statement')
First line of the true statement


Multiline Blocks
----------------
>>> if True:
...     print('First line of the true statement')
...     print('Second line of the true statement')
...     print('Third line of the true statement')
First line of the true statement
Second line of the true statement
Third line of the true statement


Nested Blocks
-------------
>>> if True:
...     print('First line of the true statement')
...     print('Second line of the true statement')
...
...     if True:
...         print('First line of inner true statement')
First line of the true statement
Second line of the true statement
First line of inner true statement


Value Check
-----------
>>> age = 30
>>>
>>> if age >= 18:
...     print('adult')
adult


Conditional Assignment
----------------------
>>> country = 'USA'
>>>
>>> if country == 'USA':
...     job = 'astronaut'
>>>
>>> print(job)
astronaut


Boundary Check
--------------
>>> age = 7
>>>
>>> if 0 <= age < 18:
...     print('Age is between 0 and 18')
Age is between 0 and 18

Checking if value is in range:

>>> a = 10
>>> b = 100
>>>
>>> if 0 <= a <= 50 < b:
...     print('Yes')
Yes


Checking If Empty
-----------------
>>> name = input('What is your name?: ')  # User input: Mark Watney
>>>
>>> if name:
...     print(f'My name is... {name}')
My name is... Mark Watney


Use Case - Even
---------------
>>> number = 4
>>>
>>> if number % 2 == 0:
...     print('even')
even


Assignments
-----------
.. literalinclude:: assignments/conditional_if_a.py
    :caption: :download:`Solution <assignments/conditional_if_a.py>`
    :end-before: # Solution
