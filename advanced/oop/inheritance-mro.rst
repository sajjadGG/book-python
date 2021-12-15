OOP Inheritance MRO
===================


Rationale
---------
* MRO - Method Resolution Order
* Inheritance Diamond


Problem
-------
>>> class Person:
...     def __init__(self):
...         print('Person init')
>>>
>>>
>>> class Astronaut(Person):
...     def __init__(self):
...         print('Astronaut init')
>>>
>>>
>>> class Cosmonaut(Person):
...     def __init__(self):
...         print('Cosmonaut init')
>>>
>>>
>>> class Crew(Astronaut, Cosmonaut):
...     def __init__(self):
...         print('Crew init')
>>>
>>>
>>> crew = Crew()
Crew init


Small Diamond
-------------
.. figure:: img/oop-mro-diamond-small-empty.png

>>> class Person:
...     def __init__(self):
...         print('Person init')
>>>
>>>
>>> class Astronaut(Person):
...     def __init__(self):
...         print('Astronaut init')
>>>
>>>
>>> class Cosmonaut(Person):
...     def __init__(self):
...         print('Cosmonaut init')
>>>
>>>
>>> class Crew(Astronaut, Cosmonaut):
...     pass
>>>
>>>
>>> crew = Crew()
Astronaut init

>>> class Person:
...     def __init__(self):
...         print('Person init')
>>>
>>>
>>> class Astronaut(Person):
...     def __init__(self):
...         print('Astronaut init')
>>>
>>>
>>> class Cosmonaut(Person):
...     def __init__(self):
...         print('Cosmonaut init')
>>>
>>>
>>> class Crew(Astronaut, Cosmonaut):
...     def __init__(self):
...         super().__init__()
>>>
>>>
>>> crew = Crew()
Astronaut init

.. figure:: img/oop-mro-diamond-small-path.png

>>> Crew.mro()  # doctest: +NORMALIZE_WHITESPACE
[<class 'Crew'>,
 <class 'Astronaut'>,
 <class 'Cosmonaut'>,
 <class 'Person'>,
 <class 'object'>]

>>> Crew.__mro__  # doctest: +NORMALIZE_WHITESPACE
(<class 'Crew'>,
 <class 'Astronaut'>,
 <class 'Cosmonaut'>,
 <class 'Person'>,
 <class 'object'>)


Large Diamond
-------------
.. figure:: img/oop-mro-diamond-large-empty.png

>>> class Person:
...     def __init__(self):
...         print('Person init')
>>>
>>>
>>> class Astronaut(Person):
...     def __init__(self):
...         print('Astronaut init')
>>>
>>> class VeteranAstronaut(Astronaut):
...     def __init__(self):
...         print('VeteranAstronaut init')
>>>
>>>
>>> class Cosmonaut(Person):
...     def __init__(self):
...         print('Cosmonaut init')
>>>
>>> class VeteranCosmonaut(Cosmonaut):
...     def __init__(self):
...         print('VeteranCosmonaut init')
>>>
>>>
>>> class Crew(VeteranAstronaut, VeteranCosmonaut):
...     def __init__(self):
...         super().__init__()
>>>
>>>
>>> crew = Crew()
VeteranAstronaut init

>>> class Person:
...     def __init__(self):
...         print('Person init')
>>>
>>>
>>> class Astronaut(Person):
...     def __init__(self):
...         print('Astronaut init')
>>>
>>> class VeteranAstronaut(Astronaut):
...     def __init__(self):
...         super().__init__()
...         print('VeteranAstronaut init')
>>>
>>>
>>> class Cosmonaut(Person):
...     def __init__(self):
...         print('Cosmonaut init')
>>>
>>> class VeteranCosmonaut(Cosmonaut):
...     def __init__(self):
...         super().__init__()
...         print('VeteranCosmonaut init')
>>>
>>>
>>> class Crew(VeteranAstronaut, VeteranCosmonaut):
...     pass
>>>
>>>
>>> crew = Crew()
Astronaut init
VeteranAstronaut init


Problematic super()
-------------------
>>> class Person:
...     def __init__(self):
...         print('Person init')
>>>
>>>
>>> class Astronaut(Person):
...     def __init__(self):
...         super().__init__()
...         print('Astronaut init')
>>>
>>> class VeteranAstronaut(Astronaut):
...     def __init__(self):
...         super().__init__()
...         print('VeteranAstronaut init')
>>>
>>>
>>> class Cosmonaut(Person):
...     def __init__(self):
...         super().__init__()
...         print('Cosmonaut init')
>>>
>>> class VeteranCosmonaut(Cosmonaut):
...     def __init__(self):
...         super().__init__()
...         print('VeteranCosmonaut init')
>>>
>>>
>>> class Crew(VeteranAstronaut, VeteranCosmonaut):
...     pass
>>>
>>>
>>> crew = Crew()
Person init
Cosmonaut init
VeteranCosmonaut init
Astronaut init
VeteranAstronaut init

>>> class Person:
...     def __init__(self):
...         print('Person init')
>>>
>>>
>>> class Astronaut(Person):
...     def __init__(self):
...         print('Astronaut init')
...         super().__init__()
>>>
>>> class VeteranAstronaut(Astronaut):
...     def __init__(self):
...         print('VeteranAstronaut init')
...         super().__init__()
>>>
>>>
>>> class Cosmonaut(Person):
...     def __init__(self):
...         print('Cosmonaut init')
...         super().__init__()
>>>
>>> class VeteranCosmonaut(Cosmonaut):
...     def __init__(self):
...         print('VeteranCosmonaut init')
...         super().__init__()
>>>
>>>
>>> class Crew(VeteranAstronaut, VeteranCosmonaut):
...     pass
>>>
>>>
>>> crew = Crew()
VeteranAstronaut init
Astronaut init
VeteranCosmonaut init
Cosmonaut init
Person init


Why?!
-----
* Raymond Hettinger - Super considered super! - PyCon 2015 [#Hettinger2015]_

.. figure:: img/oop-mro-diamond-large-path.png

>>> Crew.mro()  # doctest: +NORMALIZE_WHITESPACE
[<class 'Crew'>,
 <class 'VeteranAstronaut'>,
 <class 'Astronaut'>,
 <class 'VeteranCosmonaut'>,
 <class 'Cosmonaut'>,
 <class 'Person'>,
 <class 'object'>]


Compare
-------
.. figure:: img/oop-mro-diamond-both-path.png


References
----------
.. [#Hettinger2015] https://www.youtube.com/watch?v=EiOglTERPEo


Assignments
-----------
.. todo:: Create assignments
