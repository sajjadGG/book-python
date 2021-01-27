Inheritance vs. Composition
===========================


Rationale
---------
* Composition over Inheritance

Please excuse me, for code style in this chapter.
Instead writing:

>>> class Car:
...     def engine_start(self):
...         pass
...
...     def engine_stop(self):
...         pass

I will write:

>>> class Car:
...     def engine_start(self): pass
...     def engine_stop(self): pass

This way the code is more dense and idea is much clearer to present.
There won't be any method implementations in examples.


Problem
-------
* Code duplication

>>> class Car:
...     def engine_start(self): pass
...     def engine_stop(self): pass
>>>
>>>
>>> class Truck:
...     def engine_start(self): pass
...     def engine_stop(self): pass


Inheritance
-----------
>>> class Vehicle:
...     def engine_start(self): pass
...     def engine_stop(self): pass
>>>
>>>
>>> class Car(Vehicle):
...     pass
>>>
>>> class Truck(Vehicle):
...     pass


Inheritance Problem
-------------------
* Motorcycle is a vehicle, but doesn't have windows.

>>> class Vehicle:
...     def engine_start(self): pass
...     def engine_stop(self): pass
...     def window_open(self): pass
...     def window_close(self): pass
>>>
>>>
>>> class Car(Vehicle):
...     pass
>>>
>>> class Truck(Vehicle):
...     pass
>>>
>>> class Motorcycle(Vehicle):
...     def window_open(self): raise NotImplementedError
...     def window_close(self): raise NotImplementedError


Multilevel Inheritance
----------------------
>>> class Vehicle:
...     def engine_start(): pass
...     def engine_stop(): pass
>>>
>>> class VehicleWithWindows(Vehicle):
...     def window_open(): pass
...     def window_close(): pass
>>>
>>>
>>> class Car(VehicleWithWindows):
...     pass
>>>
>>> class Truck(VehicleWithWindows):
...     pass
>>>
>>> class Motorcycle(Vehicle):
...     pass


Composition
-----------
>>> class Vehicle:
...     pass
>>>
>>> class Engine:
...     def engine_start(self): pass
...     def engine_stop(self): pass
>>>
>>> class Windows:
...     def window_open(self): pass
...     def window_close(self): pass
>>>
>>>
>>> class Car(Vehicle):
...     engine: Engine
...     window: Windows
>>>
>>> class Truck(Vehicle):
...     engine: Engine
...     window: Windows
>>>
>>> class Motorcycle(Vehicle):
...     engine: Engine


Aggregation
-----------
>>> class Vehicle:
...     pass
>>>
>>> class Part:
...     pass
>>>
>>> class Engine(Part):
...     def engine_start(self): pass
...     def engine_stop(self): pass
>>>
>>> class Windows(Part):
...     def window_open(self): pass
...     def window_close(self): pass
>>>
>>>
>>> class Car(Vehicle):
...     parts: list[Part]       # [Engine, Windows]
>>>
>>> class Truck(Vehicle):
...     parts: list[Part]       # [Engine, Windows]
>>>
>>> class Motorcycle(Vehicle):
...     parts: list[Part]       # [Engine]


Mixin Classes
-------------
* More information in `Method Resolution Order`

>>> class Vehicle:
...     pass
>>>
>>> class HasEngine:
...     def engine_start(self): pass
...     def engine_stop(self): pass
>>>
>>> class HasWindows:
...     def window_open(self): pass
...     def window_close(self): pass
>>>
>>>
>>> class Car(Vehicle, HasEngine, HasWindows):
...     pass
>>>
>>> class Truck(Vehicle, HasEngine, HasWindows):
...     pass
>>>
>>> class Motorcycle(Vehicle, HasEngine):
...     pass


Case Study
----------
Multi level inheritance is a bad pattern here

>>> class ToJSON:
...     def to_json(self):
...         import json
...         return json.dumps(self.__dict__)
>>>
>>> class ToPickle(ToJSON):
...     def to_pickle(self):
...         import pickle
...         return pickle.dumps(self)
>>>
>>>
>>> class Astronaut(ToPickle):
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
>>>
>>> print(astro.to_json())
{"firstname": "Mark", "lastname": "Watney"}
>>>
>>> print(astro.to_pickle())  # doctest: +SKIP
b'\x80\x04\x95I\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\tAstronaut' \
b'\x94\x93\x94)\x81\x94}\x94(\x8c\tfirstname\x94\x8c\x04Mark' \
b'\x94\x8c\x08lastname\x94\x8c\x06Watney\x94ub.'

Composition:

>>> class ToJSON:
...     def to_json(self):
...         import json
...         data = {k: v for k, v in vars(self).items() if not k.startswith('_')}
...         return json.dumps(data)
>>>
>>> class ToPickle:
...     def to_pickle(self):
...         import pickle
...         return pickle.dumps(self)
>>>
>>>
>>> class Astronaut:
...     firstname: str
...     lastname: str
...     __json_serializer: ToJSON
...     __pickle_serializer: ToPickle
...
...     def __init__(self, firstname, lastname, json_serializer=ToJSON, pickle_serializer=ToPickle):
...         self.firstname = firstname
...         self.lastname = lastname
...         self.__json_serializer = json_serializer
...         self.__pickle_serializer = pickle_serializer
...
...     def to_json(self):
...         return self.__json_serializer.to_json(self)
...
...     def to_pickle(self):
...         return self.__pickle_serializer.to_pickle(self)
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
>>>
>>> print(astro.to_json())
{"firstname": "Mark", "lastname": "Watney"}
>>>
>>> print(astro.to_pickle())  # doctest: +SKIP
b'\x80\x04\x95\xa3\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\tAstronaut\x94\x93\x94)\x81\x94}\x94(\x8c\tfirstname\x94\x8c\x04Mark\x94\x8c\x08lastname\x94\x8c\x06Watney\x94\x8c\x1b_Astronaut__json_serializer\x94h\x00\x8c\x06ToJSON\x94\x93\x94\x8c\x1d_Astronaut__pickle_serializer\x94h\x00\x8c\x08ToPickle\x94\x93\x94ub.'
>>>
>>>
>>> # It give me ability to write something better
>>> class MyBetterSerializer(ToJSON):
...     def to_json(self):
...         return ...
>>>
>>> astro = Astronaut('Mark', 'Watney', json_serializer=MyBetterSerializer)

Mixin classes - multiple inheritance:

>>> class ToJSON:
...     def to_json(self):
...         import json
...         return json.dumps(self.__dict__)
>>>
>>> class ToPickle:
...     def to_pickle(self):
...         import pickle
...         return pickle.dumps(self)
>>>
>>>
>>> class Astronaut(ToJSON, ToPickle):
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
>>>
>>>
>>> astro = Astronaut('Mark', 'Watney')
>>>
>>> print(astro.to_json())
{"firstname": "Mark", "lastname": "Watney"}
>>>
>>> print(astro.to_pickle())  # doctest: +SKIP
b'\x80\x04\x95I\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\tAstronaut' \
b'\x94\x93\x94)\x81\x94}\x94(\x8c\tfirstname\x94\x8c\x04Mark' \
b'\x94\x8c\x08lastname\x94\x8c\x06Watney\x94ub.'


Assignments
-----------
.. literalinclude:: assignments/oop_composition_a.py
    :caption: :download:`Solution <assignments/oop_composition_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_composition_b.py
    :caption: :download:`Solution <assignments/oop_composition_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_composition_c.py
    :caption: :download:`Solution <assignments/oop_composition_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/oop_composition_d.py
    :caption: :download:`Solution <assignments/oop_composition_d.py>`
    :end-before: # Solution
