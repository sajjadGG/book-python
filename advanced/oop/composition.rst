***************************
Inheritance vs. Composition
***************************


* Mixin Classes
* Composition over Inheritance


Problem with inheritance
========================
.. code-block:: python
    :caption: Inheritance pattern

    class Vehicle:
        def run(self):
            pass

        def drive(self):
            pass

        def window_open(self):
            pass

        def window_close(self):
            pass


    class Car(Vehicle):
        pass


    class Truck(Vehicle):
        pass


.. code-block:: python
    :caption: Problem with inheritance

    class Vehicle:
        def run(self):
            pass

        def drive(self):
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

.. code-block:: python

    class Vehicle:
        def run(self):
            pass

        def drive(self):
            pass


    class HasWindows:
        def window_open(self):
            pass

        def window_close(self):
            pass


    class Car(Vehicle, HasWindows):
        pass

    class Truck(Vehicle, HasWindows):
        pass

    class Motorbike(Vehicle):
        pass


Multi level inheritance problem
===============================
.. code-block:: python
    :caption: Multi level inheritance is a bad pattern here

    class JSONSerializable:
        def to_json(self):
            import json
            return json.dumps(self.__dict__)


    class PickleSerializable(JSONSerializable):
        def to_pickle(self):
            import pickle
            return pickle.dumps(self)


    class User(PickleSerializable):
        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name


    user = User(
        first_name='Jan',
        last_name='Twardowski',
        address='Copernicus Crater, Moon'
    )

    print(user.to_json())
    # {"first_name": "Jan", "last_name": "Twardowski", "address": "Copernicus Crater, Moon"}

    print(user.to_pickle())
    # b'\x80\x03c__main__\nUser\nq\x00)\x81q\x01}q\x02(X\n\x00\x00\x00first_nameq\x03X\x03\x00\x00\x00Janq\x04X\t\x00\x00\x00last_nameq\x05X\n\x00\x00\x00Twardowskiq\x06X\x07\x00\x00\x00addressq\x07X\x17\x00\x00\x00Copernicus Crater, Moonq\x08ub.'


Composition using Mixin classes
===============================
.. code-block:: python
    :caption: Mixin classes - multiple inheritance.

    class JSONSerializable:
        def to_json(self):
            import json
            return json.dumps(self.__dict__)


    class PickleSerializable:
        def to_pickle(self):
            import pickle
            return pickle.dumps(self)


    class User(JSONSerializable, PickleSerializable):
        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name


    user = User(
        first_name='Jan',
        last_name='Twardowski',
        address='Copernicus Crater, Moon'
    )

    print(user.to_json())
    # {"first_name": "Jan", "last_name": "Twardowski", "address": "Copernicus Crater, Moon"}

    print(user.to_pickle())
    # b'\x80\x03c__main__\nUser\nq\x00)\x81q\x01}q\x02(X\n\x00\x00\x00first_nameq\x03X\x03\x00\x00\x00Janq\x04X\t\x00\x00\x00last_nameq\x05X\n\x00\x00\x00Twardowskiq\x06X\x07\x00\x00\x00addressq\x07X\x17\x00\x00\x00Copernicus Crater, Moonq\x08ub.'


Assignments
===========

OOP Composition Mars
--------------------
* Complexity level: easy
* Lines of code to write: 8 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/oop_composition_mars.py`

:English:
    #. Create class ``Habitat``
    #. Create class ``Rocket``
    #. Create class ``Astronaut``
    #. Compose class ``MarsMission`` from ``Habitat``, ``Rocket``, ``Astronaut``

:Polish:
    #. Stwórz klasę ``Habitat``
    #. Stwórz klasę ``Rocket``
    #. Stwórz klasę ``Astronaut``
    #. Skomponuj klasę ``MarsMission`` z ``Habitat``, ``Rocket``, ``Astronaut``

OOP Composition Moveable
------------------------
* Complexity level: medium
* Lines of code to write: 20 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/oop_composition_moveable.py`

:English:
    #. Create immutable class ``Point``
    #. Create class ``Movable``
    #. Add methods ``get_position()``, ``set_position()``, ``print_position()``, ``change_position()`` to ``Movable``
    #. Each method creates new ``Point`` and stores it in ``Movable`` class

:Polish:
    #. Stwórz niemutowalną klasę ``Point``
    #. Stwórz klasę ``Movable``
    #. Dodaj metody ``get_position()``, ``set_position()``, ``print_position()``, ``change_position()`` do ``Movable``
    #. Każda metoda generuje nowy ``Point`` i zapamiętuje go w klasie ``Movable``
