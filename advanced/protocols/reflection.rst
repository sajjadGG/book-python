**********
Reflection
**********


Rationale
=========
* Act on accessing an attribute


Syntax
======
Built-in Functions:

    * ``setattr(obj, 'attribute_name', 'new value') -> None``
    * ``delattr(obj, 'attribute_name') -> None``
    * ``getattr(obj, 'attribute_name', 'default value') -> Any``
    * ``hasattr(obj, 'attribute_name') -> bool``

Protocol:

    * ``__setattr__(self, attribute_name, value)``
    * ``__delattr__(self, attribute_name)``
    * ``__getattr__(self, attribute_name, default)``
    * ``__getattribute__(self, attribute_name, default)``


Set Attribute
=============
* Called when trying to set attribute to a value
* ``setattr(astro, 'name', 'value')`` is equivalent to ``astro.name = 'value'``
* Call Stack:

    * ``astro.name = 'Mark Watney'``
    * => ``setattr(astro, 'name', 'Mark Watney')``
    * => ``astro.__setattr__('name', 'Mark Watney')``

.. code-block:: python

    class Astronaut:

        def __setattr__(self, name, value):
            if name.startswith('_'):
                raise PermissionError(f'Field "{name}" is protected, cannot "set" value.')
            else:
                return super().__setattr__(name, value)


    watney = Astronaut()

    watney.fullname = 'Mark Watney'
    print(watney.fullname)
    # Mark Watney

    watney._salary = 100
    # PermissionError: Field "_salary" is protected, cannot "set" value.


Delete Attribute
================
* Called when trying to delete attribute
* ``delattr(astro, 'name')`` is equivalent to ``del astro.name``
* Call stack:

    * ``del astro.name``
    * => ``delattr(astro, 'name')``
    * => ``astro.__delattr__(name)``

.. code-block:: python

    class Astronaut:

        def __delattr__(self, name):
            if name.startswith('_'):
                raise PermissionError(f'Field "{name}" is protected, cannot "delete" value.')
            else:
                return super().__delattr__(name)


    watney = Astronaut()

    watney.fullname = 'Mark Watney'
    watney._salary = 100

    del watney.fullname
    del watney._salary
    # PermissionError: Field "_salary" is protected, cannot "delete" value.


Get Attribute
=============
* Called for every time, when you want to access any attribute
* ``getattr(astro, 'name')`` is equivalent to ``astro.name``
* Before even checking if this attribute exists
* if ``__getattribute__()`` raises ``AttributeError`` it calls ``__getattr__()``
* Call stack:

    * ``astro.name``
    * => ``getattr(astro, 'name')``
    * => ``astro.__getattribute__('name')``
    * if ``astro.__getattribute__('name')`` raise ``AttributeError``
    * => ``astro.__getattr__('name')``

.. code-block:: python
    :caption: Example ``__getattribute__()``

    class Astronaut:

        def __getattribute__(self, name):
            if name.startswith('_'):
                raise PermissionError(f'Field "{name}" is protected, cannot "get" value.')
            else:
                return super().__getattribute__(name)


    watney = Astronaut()

    watney.fullname = 'Mark Watney'
    print(watney.fullname)
    # Mark Watney

    print(watney._salary)
    # PermissionError: Field "_salary" is protected, cannot "get" value.


Get Attribute if Does Not Exist
===============================
* Called whenever you request an attribute that hasn't already been defined
* if ``__getattribute__()`` raises ``AttributeError`` it calls ``__getattr__()``
* Implementing a fallback for missing attributes

.. code-block:: python
    :caption: Example ``__getattr__()``

    class Astronaut:
        def __init__(self):
            self.fullname = None

        def __getattr__(self, name):
            print('Getattr called')

            if name.startswith('_'):
                raise PermissionError(f'Field "{name}" is protected, cannot "get" value.')
            else:
                return super().__getattr__(name)


    watney = Astronaut()

    watney.fullname = 'Mark Watney'
    print(watney.fullname)
    # Mark Watney

    print(watney._salary)
    # Getattr called
    # PermissionError: Field "_salary" is protected, cannot "get" value.


Has Attribute
=============
* Check if object has attribute
* There is no ``__hasattr__()`` method
* Calls ``__getattribute__()`` and checks if raises ``AttributeError``

.. code-block:: python

    class Astronaut:
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname


    watney = Astronaut('Mark', 'Watney')

    print(hasattr(watney, 'firstname'))     # True
    print(hasattr(watney, 'lastname'))      # True
    print(hasattr(watney, 'fullname'))      # False

    watney.fullname = 'Mark Watney'

    print(hasattr(watney, 'fullname'))
    # True


Examples
========
.. code-block:: python

    class Astronaut:

        def __getattribute__(self, name):
            if name.startswith('_'):
                raise PermissionError(f'Field "{name}" is protected, cannot "get" value.')
            else:
                return super().__getattribute__(name)

        def __setattr__(self, name, value):
            if name.startswith('_'):
                raise PermissionError(f'Field "{name}" is protected, cannot "set" value.')
            else:
                return super().__setattr__(name, value)


    watney = Astronaut()

    watney.fullname = 'Mark Watney'
    print(watney.fullname)
    # Mark Watney

    watney._salary = 100
    # PermissionError: Field "_salary" is protected, cannot "set" value.

    print(watney._salary)
    # PermissionError: Field "_salary" is protected, cannot "get" value.

.. code-block:: python

    class Temperature:
        def __init__(self, kelvin):
            self.kelvin = kelvin

        def __setattr__(self, name, value):
            if value < 0.0:
                raise ValueError('Kelvin temperature cannot be negative')
            else:
                return super().__setattr__(name, value)


    t = Temperature(100)

    t.kelvin = 20
    print(t.kelvin)
    # 20

    t.kelvin = -10
    # ValueError: Kelvin temperature cannot be negative

.. code-block:: python

    class Temperature:
        def __init__(self, kelvin):
            self.kelvin = kelvin

        def __setattr__(self, name, value):
            super().__setattr__(name, value)

            if name == 'kelvin':
                super().__setattr__(name, value)
                self.celsius = 273.15 + self.kelvin
                self.fahrenheit = (self.kelvin-273.15) * 1.8 + 32


    t = Temperature(100)

    print(t.kelvin)
    # 100

    print(t.celsius)
    # 373.15

    print(t.fahrenheit)
    # -279.66999999999996


Assignments
===========

Protocol Reflection
-------------------
* Complexity level: medium
* Lines of code to write: 30 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/protocol_reflection.py`

:English:
    #. Create class ``Point`` with ``x``, ``y``, ``z`` attributes
    #. Prevent adding new attributes
    #. Prevent deleting attributes
    #. Prevent changing attributes
    #. Allow to set attributes only at the initialization

:Polish:
    #. Stwórz klasę ``Point`` z atrybutami ``x``, ``y``, ``z``
    #. Zablokuj możliwość dodawania nowych atrybutów
    #. Zablokuj możliwość usuwania atrybutów
    #. Zablokuj edycję atrybutów
    #. Pozwól na ustawianie atrybutów tylko przy inicjalizacji klasy

:Input:
    .. code-block:: python

        class Point:
            def __str__(self):
                return f'Point(x={self.x}, y={self.y}, z={self.z}')
