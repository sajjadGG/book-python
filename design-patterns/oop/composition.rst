Inheritance vs. Composition
===========================


Rationale
---------
* Composition over Inheritance


Code Duplication
----------------
.. code-block:: python

    class Car:
        def engine_start(self):
            pass

        def engine_stop(self):
            pass


    class Truck:
        def engine_start(self):
            pass

        def engine_stop(self):
            pass


Inheritance
-----------
.. code-block:: python

    class Vehicle:
        def engine_start(self):
            pass

        def engine_stop(self):
            pass


    class Car(Vehicle):
        pass


    class Truck(Vehicle):
        pass


Inheritance Problem
-------------------
.. code-block:: python

    class Vehicle:
        def engine_start(self):
            pass

        def engine_stop(self):
            pass

        def window_open(self):
            pass

        def window_close(self):
            pass


    class Car(Vehicle):
        pass


    class Truck(Vehicle):
        pass


    class Motorbike(Vehicle):
        """Motorbike is a vehicle, but doesn't have windows."""

        def window_open(self):
            raise NotImplementedError

        def window_close(self):
            raise NotImplementedError


Multilevel Inheritance
----------------------
.. code-block:: python

    class A:
        pass

    class B(A):
        pass

    class C(B):
        pass


Composition
-----------
.. code-block:: python

    class Vehicle:
        pass

    class HasEngine:
        def engine_start(self):
            pass

        def engine_stop(self):
            pass

    class HasWindows:
        def window_open(self):
            pass

        def window_close(self):
            pass


    class Car(Vehicle):
        engine: HasEngine
        window: HasWindows

    class Truck(Vehicle):
        engine: HasEngine
        window: HasWindows

    class Motorbike(Vehicle):
        engine: HasEngine
        window: None


Mixin Classes
-------------
.. code-block:: python

    class Vehicle:
        pass

    class HasEngine:
        def engine_start(self):
            pass

        def engine_stop(self):
            pass

    class HasWindows:
        def window_open(self):
            pass

        def window_close(self):
            pass


    class Car(Vehicle, HasEngine, HasWindows):
        pass

    class Truck(Vehicle, HasEngine, HasWindows):
        pass

    class Motorbike(Vehicle, HasEngine):
        pass


Case Study
----------
Multi level inheritance is a bad pattern here
.. code-block:: python

    class ToJSON:
        def to_json(self):
            import json
            return json.dumps(self.__dict__)

    class ToPickle(ToJSON):
        def to_pickle(self):
            import pickle
            return pickle.dumps(self)


    class Astronaut(ToPickle):
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname


    astro = Astronaut('Mark', 'Watney')

    print(astro.to_json())
    # {"firstname": "Mark", "lastname": "Watney"}

    print(astro.to_pickle())
    # b'\x80\x04\x95I\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\tAstronaut' \
    # b'\x94\x93\x94)\x81\x94}\x94(\x8c\tfirstname\x94\x8c\x04Mark' \
    # b'\x94\x8c\x08lastname\x94\x8c\x06Watney\x94ub.'

Composition:

.. code-block:: python

    class ToJSON:
        def to_json(self):
            import json
            data = {k: v for k, v in vars(self).items() if not k.startswith('_')}
            return json.dumps(data)

    class ToPickle:
        def to_pickle(self):
            import pickle
            return pickle.dumps(self)


    class Astronaut:
        firstname: str
        lastname: str
        __json_serializer: ToJSON
        __pickle_serializer: ToPickle

        def __init__(self, firstname, lastname, json_serializer=ToJSON, pickle_serializer=ToPickle):
            self.firstname = firstname
            self.lastname = lastname
            self.__json_serializer = json_serializer
            self.__pickle_serializer = pickle_serializer

        def to_json(self):
            return self.__json_serializer.to_json(self)

        def to_pickle(self):
            return self.__pickle_serializer.to_pickle(self)


    astro = Astronaut('Mark', 'Watney')

    print(astro.to_json())
    # {"firstname": "Mark", "lastname": "Watney"}

    print(astro.to_pickle())
    # b'\x80\x04\x95\xa3\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\tAstronaut\x94\x93\x94)\x81\x94}\x94(\x8c\tfirstname\x94\x8c\x04Mark\x94\x8c\x08lastname\x94\x8c\x06Watney\x94\x8c\x1b_Astronaut__json_serializer\x94h\x00\x8c\x06ToJSON\x94\x93\x94\x8c\x1d_Astronaut__pickle_serializer\x94h\x00\x8c\x08ToPickle\x94\x93\x94ub.'


    # It give me ability to write something better
    class MyBetterSerializer(ToJSON):
        def to_json(self):
            return ...

    astro = Astronaut('Mark', 'Watney', json_serializer=MyBetterSerializer)

Mixin classes - multiple inheritance:

.. code-block:: python

    class ToJSON:
        def to_json(self):
            import json
            return json.dumps(self.__dict__)

    class ToPickle:
        def to_pickle(self):
            import pickle
            return pickle.dumps(self)


    class Astronaut(ToJSON, ToPickle):
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname


    astro = Astronaut('Mark', 'Watney')

    print(astro.to_json())
    # {"firstname": "Mark", "lastname": "Watney"}

    print(astro.to_pickle())
    # b'\x80\x04\x95I\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\tAstronaut' \
    # b'\x94\x93\x94)\x81\x94}\x94(\x8c\tfirstname\x94\x8c\x04Mark' \
    # b'\x94\x8c\x08lastname\x94\x8c\x06Watney\x94ub.'


Assignments
-----------
.. literalinclude:: ../_assignments/oop_composition_a.py
    :caption: :download:`Solution <../_assignments/oop_composition_a.py>`
    :end-before: # Solution

.. literalinclude:: ../_assignments/oop_composition_b.py
    :caption: :download:`Solution <../_assignments/oop_composition_b.py>`
    :end-before: # Solution
