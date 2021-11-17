Block Elif
==========

.. testsetup::

    def input(__prompt):
        """Stub user input, for testing purpose only"""
        return 'French'


Conditional Alternative
-----------------------
* Used to check for additional condition if first is not met
* In other languages is known as ``else if``

``elif`` generic syntax:

.. code-block:: python

    if <condition>:
        <do something>
    elif <condition>:
        <do something>
    else:
        <do something>

>>> language = input('What is your language?: ')  # User input 'Polish'
>>>
>>> if language == 'English':
...     print('Hello')
... elif language == 'Russian':
...     print('Здравствуйте')
... elif language == 'German':
...     print('Guten Tag')
... elif language == 'Polish':
...     print('Witaj')
... else:
...     print("I don't speak this language")
Witaj


Shorthand Expressions
---------------------
>>> number = 3
>>> is_even = (number % 2 == 0 )
>>>
>>> print(is_even)
False

>>> number = 3
>>> is_digit = (number in range(0,10))
>>>
>>> print(is_digit)
True


Conditional Expression
----------------------
>>> number = 3
>>>
>>> if number in range(0,10):
...     is_digit = True
... else:
...     is_digit = False
>>>
>>> print(is_digit)
True

>>> number = 3
>>> is_digit = True if number in range(0,10) else False
>>>
>>> print(is_digit)
True

>>> ip = '127.0.0.1'
>>> protocol = 'IPv4' if '.' in ip else 'IPv6'
>>>
>>> print(protocol)
IPv4

Normal ``if``:

>>> country = 'Russia'
>>>
>>> if country == 'USA':
...     job = 'astronaut'
... else:
...     job = 'cosmonaut'
>>>
>>> print(job)
cosmonaut

Inline ``if``:

>>> country = 'Russia'
>>> job = 'astronaut' if country == 'USA' else 'cosmonaut'
>>>
>>> print(job)
cosmonaut

Type Str Methods is Numeric:

>>> age = input('What is your age?: ')
>>> age = float(age) if age.isnumeric() else None
>>> print(age)
10.0


Assignments
-----------
.. literalinclude:: assignments/conditional_elif_a.py
    :caption: :download:`Solution <assignments/conditional_elif_a.py>`
    :end-before: # Solution
