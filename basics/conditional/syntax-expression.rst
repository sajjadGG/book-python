Boolean Expression
==================

.. testsetup::

    # Simulate user input (for test automation)
    from unittest.mock import MagicMock
    input = MagicMock(side_effect=['10'])


Rationale
---------
* Conditional Expression
* Shorthand Expressions


Recap
-----
>>> number = 3
>>>
>>> if number in range(0,10):
...     is_digit = True
... else:
...     is_digit = False
>>>
>>> print(is_digit)
True


Conditional Expression
----------------------
>>> number = 3
>>> is_digit = True if number in range(0,10) else False
>>>
>>> print(is_digit)
True


Shorthand Expressions
---------------------
>>> number = 3
>>> is_digit = (number in range(0,10))
>>>
>>> print(is_digit)
True


Use Case - 0x01
---------------
* Is adult

>>> adult = 'Yes' if age >= 18 else 'No'
>>>
>>> print(adult)
Yes


Use Case - 0x02
---------------
* Is numeric

>>> age = input('What is your age?: ')   # Use input: '10'
>>> age = float(age) if age.isnumeric() else None
>>>
>>> print(age)
10.0


Use Case - 0x03
---------------
* Even/odd

>>> number = 3
>>> is_even = (number % 2 == 0 )
>>>
>>> print(is_even)
False


Use Case - 0x04
---------------
* Astronaut/Cosmonaut

>>> country = 'Russia'
>>> job = 'astronaut' if country == 'USA' else 'cosmonaut'
>>>
>>> print(job)
cosmonaut


Use Case - 0x05
---------------
* IPv4/IPv6

>>> ip = '127.0.0.1'
>>> protocol = 'IPv4' if '.' in ip else 'IPv6'
>>>
>>> print(protocol)
IPv4

>>> ip = 'fe80::aede:48ff:fe01:1133'
>>> protocol = 'IPv4' if '.' in ip else 'IPv6'
>>>
>>> print(protocol)
IPv6



Assignments
-----------
.. literalinclude:: assignments/conditional_expression_a.py
    :caption: :download:`Solution <assignments/conditional_expression_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/conditional_expression_b.py
    :caption: :download:`Solution <assignments/conditional_expression_b.py>`
    :end-before: # Solution
