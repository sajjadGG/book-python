OOP Inheritance MRO
===================


Important
---------
* MRO - Method Resolution Order
* Inheritance Diamond


Problem
-------
>>> class Person:
...     def __init__(self):
...         print('Person')
>>>
>>>
>>> class Astronaut(Person):
...     def __init__(self):
...         print('Astronaut')
>>>
>>>
>>> class Cosmonaut(Person):
...     def __init__(self):
...         print('Cosmonaut')
>>>
>>>
>>> class Crew(Astronaut, Cosmonaut):
...     def __init__(self):
...         print('Crew')
>>>
>>>
>>> crew = Crew()
Crew


Small Diamond
-------------
.. figure:: img/oop-mro-diamond-small-empty.png

>>> class Person:
...     def __init__(self):
...         print('Person')
>>>
>>>
>>> class Astronaut(Person):
...     def __init__(self):
...         print('Astronaut')
>>>
>>>
>>> class Cosmonaut(Person):
...     def __init__(self):
...         print('Cosmonaut')
>>>
>>>
>>> class Crew(Astronaut, Cosmonaut):
...     pass
>>>
>>>
>>> crew = Crew()
Astronaut

>>> class Person:
...     def __init__(self):
...         print('Person')
>>>
>>>
>>> class Astronaut(Person):
...     def __init__(self):
...         print('Astronaut')
>>>
>>>
>>> class Cosmonaut(Person):
...     def __init__(self):
...         print('Cosmonaut')
>>>
>>>
>>> class Crew(Astronaut, Cosmonaut):
...     def __init__(self):
...         super().__init__()
>>>
>>>
>>> crew = Crew()
Astronaut

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
...         print('Person')
>>>
>>>
>>> class Astronaut(Person):
...     def __init__(self):
...         print('Astronaut')
>>>
>>> class VeteranAstronaut(Astronaut):
...     def __init__(self):
...         print('VeteranAstronaut')
>>>
>>>
>>> class Cosmonaut(Person):
...     def __init__(self):
...         print('Cosmonaut')
>>>
>>> class VeteranCosmonaut(Cosmonaut):
...     def __init__(self):
...         print('VeteranCosmonaut')
>>>
>>>
>>> class Crew(VeteranAstronaut, VeteranCosmonaut):
...     def __init__(self):
...         super().__init__()
>>>
>>>
>>> crew = Crew()
VeteranAstronaut

>>> class Person:
...     def __init__(self):
...         print('Person')
>>>
>>>
>>> class Astronaut(Person):
...     def __init__(self):
...         print('Astronaut')
>>>
>>> class VeteranAstronaut(Astronaut):
...     def __init__(self):
...         super().__init__()
...         print('VeteranAstronaut')
>>>
>>>
>>> class Cosmonaut(Person):
...     def __init__(self):
...         print('Cosmonaut')
>>>
>>> class VeteranCosmonaut(Cosmonaut):
...     def __init__(self):
...         super().__init__()
...         print('VeteranCosmonaut')
>>>
>>>
>>> class Crew(VeteranAstronaut, VeteranCosmonaut):
...     pass
>>>
>>>
>>> crew = Crew()
Astronaut
VeteranAstronaut


Problematic super()
-------------------
>>> class Person:
...     def __init__(self):
...         print('Person')
>>>
>>>
>>> class Astronaut(Person):
...     def __init__(self):
...         print('Astronaut')
...         super().__init__()
>>>
>>> class VeteranAstronaut(Astronaut):
...     def __init__(self):
...         print('VeteranAstronaut')
...         super().__init__()
>>>
>>>
>>> class Cosmonaut(Person):
...     def __init__(self):
...         print('Cosmonaut')
...         super().__init__()
>>>
>>> class VeteranCosmonaut(Cosmonaut):
...     def __init__(self):
...         print('VeteranCosmonaut')
...         super().__init__()
>>>
>>>
>>> class Crew(VeteranAstronaut, VeteranCosmonaut):
...     pass
>>>
>>>
>>> crew = Crew()
VeteranAstronaut
Astronaut
VeteranCosmonaut
Cosmonaut
Person


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


.. todo:: Assignments
