FuncProg Namespace
==================
* Functions provide namespaces
* Only code inside that namespace can access it's locals


Variables Inside Function
-------------------------
* Variables inside function

>>> def run():
...     firstname = 'Mark'
...     lastname = 'Watney'

Before call:

>>> firstname
Traceback (most recent call last):
NameError: name 'firstname' is not defined
>>>
>>> lastname
Traceback (most recent call last):
NameError: name 'lastname' is not defined

After call:

>>> run()
>>>
>>> firstname
Traceback (most recent call last):
NameError: name 'firstname' is not defined
>>>
>>> lastname
Traceback (most recent call last):
NameError: name 'lastname' is not defined


Functions Inside Function
-------------------------
* Functions inside function

>>> def run():
...     def say_hello():
...         print('Hello')
...
...     def say_goodbye():
...         print('Goodbye')

>>> say_hello()
Traceback (most recent call last):
NameError: name 'say_hello' is not defined
>>>
>>> say_goodbye()
Traceback (most recent call last):
NameError: name 'say_goodbye' is not defined

>>> run()
>>>
>>> say_hello()
Traceback (most recent call last):
NameError: name 'say_hello' is not defined
>>>
>>> say_goodbye()
Traceback (most recent call last):
NameError: name 'say_goodbye' is not defined


Classes Inside Function
-----------------------
>>> def run():
...     class Astronaut:
...         pass
...
...     class Cosmonaut:
...         pass

>>> Astronaut()
Traceback (most recent call last):
NameError: name 'Astronaut' is not defined
>>>
>>> Cosmonaut()
Traceback (most recent call last):
NameError: name 'Cosmonaut' is not defined

>>> run()
>>>
>>> Astronaut()
Traceback (most recent call last):
NameError: name 'Astronaut' is not defined
>>>
>>> Cosmonaut()
Traceback (most recent call last):
NameError: name 'Cosmonaut' is not defined


Methods Inside Function
-----------------------
>>> def run():
...     class Astronaut:
...         def __init__(self, firstname, lastname):
...             self.firstname = firstname
...             self.lastname = lastname
...
...     class Cosmonaut:
...         def __init__(self, firstname, lastname):
...             self.firstname = firstname
...             self.lastname = lastname

>>> Astronaut('Mark', 'Watney')
Traceback (most recent call last):
NameError: name 'Astronaut' is not defined
>>>
>>> Cosmonaut('Pan', 'Twardowski')
Traceback (most recent call last):
NameError: name 'Cosmonaut' is not defined

>>> run()
>>>
>>> Astronaut('Mark', 'Watney')
Traceback (most recent call last):
NameError: name 'Astronaut' is not defined
>>>
>>> Cosmonaut('Pan', 'Twardowski')
Traceback (most recent call last):
NameError: name 'Cosmonaut' is not defined


Instances Inside Function
-------------------------
>>> def run():
...     class Astronaut:
...         def __init__(self, firstname, lastname):
...             self.firstname = firstname
...             self.lastname = lastname
...
...     class Cosmonaut:
...         def __init__(self, firstname, lastname):
...             self.firstname = firstname
...             self.lastname = lastname
...
...     mark = Astronaut('Mark', 'Watney')
...     pan = Cosmonaut('Pan', 'Twardowski')

>>> mark
Traceback (most recent call last):
NameError: name 'mark' is not defined
>>>
>>> pan
Traceback (most recent call last):
NameError: name 'pan' is not defined

>>> run()
>>>
>>> mark
Traceback (most recent call last):
NameError: name 'mark' is not defined
>>>
>>> pan
Traceback (most recent call last):
NameError: name 'pan' is not defined


All Together
------------
>>> def run():
...     firstname = 'Mark'
...     lastname = 'Watney'
...
...     def say_hello():
...         print('Hello')
...
...     def say_goodbye():
...         print('Goodbye')
...
...     class Astronaut:
...         def __init__(self, firstname, lastname):
...             self.firstname = firstname
...             self.lastname = lastname
...
...     class Cosmonaut:
...         def __init__(self, firstname, lastname):
...             self.firstname = firstname
...             self.lastname = lastname
...
...     mark = Astronaut('Mark', 'Watney')
...     pan = Cosmonaut('Pan', 'Twardowski')


Execute
-------
>>> def run():
...
...     def say_hello():
...         print('Hello')
...
...     def say_goodbye():
...         print('Goodbye')
...
...     say_hello()
...     say_goodbye()
>>>
>>>
>>> result = run()
Hello
Goodbye
>>>
>>> print(result)
None


Return Results
--------------
>>> def run():
...
...     def get_hello():
...         return 'Hello'
...
...     def get_goodbye():
...         return 'Goodbye'
...
...     return get_hello()
>>>
>>>
>>> run()
'Hello'

>>> def run():
...
...     def get_hello():
...         return 'Hello'
...
...     def get_goodbye():
...         return 'Goodbye'
...
...     return get_hello(), get_goodbye()
>>>
>>>
>>> run()
('Hello', 'Goodbye')


Return Function
---------------
>>> def run():
...     def say_hello():
...         print('Hello')
...
...     def say_goodbye():
...         print('Goodbye')
...
...     return say_hello
>>>
>>>
>>> hello = run()
>>> hello()
Hello

>>> def run():
...     def say_hello():
...         print('Hello')
...
...     def say_goodbye():
...         print('Goodbye')
...
...     return say_hello, say_goodbye
>>>
>>>
>>> hello, goodbye = run()
>>>
>>> hello()
Hello
>>>
>>> goodbye()
Goodbye

>>> def run():
...     class Astronaut:
...         def __init__(self, firstname, lastname):
...             self.firstname = firstname
...             self.lastname = lastname
...
...     return Astronaut('Mark', 'Watney')
>>>
>>>
>>> mark = run()
>>>
>>> vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney'}


Locals
------
>>> def run():
...     firstname = 'Mark'
...     lastname = 'Watney'
...
...     def say_hello():
...         print('Hello')
...
...     def say_goodbye():
...         print('Goodbye')
...
...     class Astronaut:
...         def __init__(self, firstname, lastname):
...             self.firstname = firstname
...             self.lastname = lastname
...
...     class Cosmonaut:
...         def __init__(self, firstname, lastname):
...             self.firstname = firstname
...             self.lastname = lastname
...
...     mark = Astronaut('Mark', 'Watney')
...     pan = Cosmonaut('Pan', 'Twardowski')
...
...     print(locals())

>>> run()   # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
{'firstname': 'Mark',
 'lastname': 'Watney',
 'say_hello': <function run.<locals>.say_hello at 0x...>,
 'say_goodbye': <function run.<locals>.say_goodbye at 0x...>,
 'Astronaut': <class '__main__.run.<locals>.Astronaut'>,
 'Cosmonaut': <class '__main__.run.<locals>.Cosmonaut'>,
 'mark': <__main__.run.<locals>.Astronaut object at 0x...>,
 'pan': <__main__.run.<locals>.Cosmonaut object at 0x...>}
