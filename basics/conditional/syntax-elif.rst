.. testsetup::

    # Simulate user input (for test automation)
    from unittest.mock import MagicMock
    input = MagicMock(side_effect=['5', '5', '10', 'Polish'])


Block Elif
==========
* Used to check for additional condition if first is not met
* In other languages is known as ``else if``
* Conditional Alternative


Syntax
------
* Optional else

>>> # doctest: +SKIP
... if <condition>:
...     <do something>
... elif <condition>:
...     <do something>

>>> # doctest: +SKIP
... if <condition>:
...     <do something>
... elif <condition>:
...     <do something>
... else:
...     <do something>


Example
-------
>>> number = int(input('Type digit: '))  #input: '5'
>>>
>>>
>>> if 0 <= number < 3:
...     print('small')
... elif 3 <= number < 7:
...     print('medium')
... elif 7 <= number < 10:
...     print('large')
medium


Why not many ifs?
-----------------
* With many ifs, Python will evaluate all of them
* With elifs Python will stop, after first ``True`` evaluation

>>> number = int(input('Type digit: '))  #input: '5'
>>>
>>>
>>> if 0 <= number < 3:
...     print('small')
>>>
>>> if 3 <= number < 7:
...     print('medium')
medium
>>>
>>> if 7 <= number < 10:
...     print('large')


Else
----
>>> number = int(input('Type digit: '))  #input: '10'
>>>
>>>
>>> if 0 <= number < 3:
...     print('small')
... elif 3 <= number < 7:
...     print('medium')
... elif 7 <= number < 10:
...     print('large')
... else:
...     print('Not a digit')
Not a digit


Use Case - 0x01
---------------
>>> language = input('What is your language?: ')  # User input 'Polish'
>>>
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



.. todo:: Assignments
