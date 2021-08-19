OOP Inheritance
===============


Inheritance Static Fields
-------------------------
On static fields:

>>> class Person:
...     firstname = 'Mark'
...     lastname = 'Watney'
...     job = 'unemployed'
>>>
>>>
>>> class Astronaut(Person):
...     job = 'astronaut'
>>>
>>>
>>> astro = Astronaut()
>>>
>>> astro.firstname
'Mark'
>>> astro.lastname
'Watney'
>>> astro.job
'astronaut'


Inheritance Dynamic Fields
--------------------------
>>> class Person:
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'
...         self.job = 'unemployed'
>>>
>>>
>>> class Astronaut(Person):
...     def __init__(self):
...         self.job = 'astronaut'
>>>
>>>
>>> astro = Astronaut()
>>> print(vars(astro))
{'job': 'astronaut'}


Super
-----
* Order is important

>>> class Person:
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'
...         self.job = 'unemployed'
>>>
>>>
>>> class Astronaut(Person):
...     def __init__(self):
...         self.job = 'astronaut'
...         super().__init__()
>>>
>>>
>>> astro = Astronaut()
>>> print(vars(astro))
{'job': 'unemployed', 'firstname': 'Mark', 'lastname': 'Watney'}

>>> class Person:
...     def __init__(self):
...         self.firstname = 'Mark'
...         self.lastname = 'Watney'
...         self.job = 'unemployed'
>>>
>>>
>>> class Astronaut(Person):
...     def __init__(self):
...         super().__init__()
...         self.job = 'astronaut'
>>>
>>>
>>> astro = Astronaut()
>>> print(vars(astro))
{'firstname': 'Mark', 'lastname': 'Watney', 'job': 'astronaut'}
