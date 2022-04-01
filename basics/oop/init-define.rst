OOP Init Define
===============
* It's a first method run after object is initiated
* All classes has default ``__init__()``

.. glossary::

    constructor
        Method called at object instantiation used to create object.
        Constructor is called on not fully initialized object and hence do
        not have access to object methods. Constructor should return
        ``None``.

    initializer
        Method called at object instantiation used to fill empty object with
        values. Initializer is called upon object initialization and hence
        can modify object and use its methods. Initializer should return
        ``None``.


Syntax
------
>>> class MyClass:
...     def __init__(self, required, optional=None):
...         pass
>>>
>>>
>>> myobj = MyClass('myvalue')


Initializer Method Without Arguments
------------------------------------
Initializer method without arguments:

>>> class Astronaut:
...     def __init__(self):
...         print('Hello')
>>>
>>>
>>> astro = Astronaut()
Hello


Initializer Method With Arguments
---------------------------------
>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         print(f'Hello {firstname} {lastname}')
>>>
>>>
>>> astro = Astronaut()
Traceback (most recent call last):
TypeError: Astronaut.__init__() missing 2 required positional arguments: 'firstname' and 'lastname'

>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         print(f'Hello {firstname} {lastname}')
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
Hello Mark Watney
>>>
>>> astro = Astronaut(firstname='Mark', lastname='Watney')
Hello Mark Watney

>>> class Astronaut:
...     def __init__(self, firstname, lastname='Unknown'):
...         print(f'Hello {firstname} {lastname}')
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
Hello Mark Watney
>>>
>>> astro = Astronaut('Mark')
Hello Mark Unknown


Assignments
-----------
.. literalinclude:: assignments/oop_init_define_a.py
    :caption: :download:`Solution <assignments/oop_init_define_a.py>`
    :end-before: # Solution
