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
...     def engine_start(self): pass
...     def engine_stop(self): pass
>>>
>>> class VehicleWithWindows(Vehicle):
...     def window_open(self): pass
...     def window_close(self): pass
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
...     parts: list[Part] = [Engine, Windows]
>>>
>>> class Truck(Vehicle):
...     parts: list[Part] = [Engine, Windows]
>>>
>>> class Motorcycle(Vehicle):
...     parts: list[Part] = [Engine]


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
Problem:

>>> class Astronaut:
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname
...
...     def to_pickle(self):
...         import pickle
...         return pickle.dumps(self)
...
...     def to_json(self):
...         import json
...         return json.dumps(self.__dict__)

This class contains methods, which could be also used by other classes,
this will lower the amount of code to maintain. So we refactor and
`Extract superclass`.

>>> class Serialize:
...     def to_pickle(self):
...         import pickle
...         return pickle.dumps(self)
...
...     def to_json(self):
...         import json
...         return json.dumps(self.__dict__)
>>>
>>>
>>> class Astronaut(Serialize):
...     def __init__(self, firstname, lastname):
...         self.firstname = firstname
...         self.lastname = lastname

It's better. Now we can reuse ``Serialize`` class. However... Is that true,
that each class can be serialized to JSON and Pickle at the same time?

We can improve code by splitting those capabilities into separate classes.
In this case, the `Multi level inheritance` is a bad pattern here:

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

It will work as intended for the end-user, but the code structure is disturbed.
Not all classes which are serialized to Pickle, are also serialized to JSON. In
out case it's a must. This kind of `Multi-level inheritance` could be found in
languages which does not support `Multiple inheritance`. Java is such language.
In that case, developers are not using inheritance, and they even go to the
extreme, by considering inheritance a bad practice. They use composition:

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

This work as intended, and nothing changed for the end-user. This maybe a good
pattern for Java, but for Python ecosystem is over-engineered (to complex for
that particular usecase).

That was a must, because Java don't have `Multiple inheritance` and
`Simple inheritance` or `Multilevel inheritance` was a bad idea.  In Python
there is `Multiple inheritance` capability which enables to create a small
and specialized classes and mix them together in order to create objects. Those
are called `Mixin classes` and they use `multiple inheritance` mechanism:

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
