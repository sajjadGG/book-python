**********
Reflection
**********


Rationale
=========
* Act, when someone is trying to access an attribute


Syntax
======

Built-in Functions
------------------
* ``hasattr(obj, 'attribute_name') -> bool``
* ``setattr(obj, 'attribute_name', 'new value') -> None``
* ``getattr(obj, 'attribute_name', 'default value') -> Any``
* ``delattr(obj, 'attribute_name') -> None``

Protocol
--------
* ``__setattr__(self, attribute_name, value)``
* ``__getattribute__(self, attribute_name, default)``
* ``__getattr__(self, attribute_name, default)``
* ``__delattr__(self, attribute_name)``


``__setattr__()``
=================
* Called when trying to set attribute to a value
* ``setattr(x, 'name', 'value')`` is equivalent to ``x.name = 'value'``
* Call Stack:

    * ``astro.name = 'Mark Watney'``
    * => ``setattr(astro, 'name', 'Mark Watney')``
    * => ``obj.__setattr__('name', 'Mark Watney')``

.. code-block:: python

    class Astronaut:

        def __setattr__(self, attribute_name, new_value):
            if attribute_name.startswith('_'):
                raise PermissionError(f'Field "{attribute_name}" is protected, cannot "set" value.')
            else:
                return object.__setattr__(self, attribute_name, new_value)


    watney = Astronaut()

    watney.name = 'Mark Watney'
    print(watney.name)
    # Mark Watney

    watney._salary = 100
    # PermissionError: Field "_salary" is protected, cannot "set" value.

.. code-block:: python

    class Temperature:
        def __init__(self, initial_temperature):
            self.value = initial_temperature

        def __setattr__(self, attribute_name, new_value):
            if attribute_name == 'value' and new_value < 0.0:
                raise ValueError('Kelvin temperature cannot be negative')
            else:
                object.__setattr__(self, attribute_name, new_value)


    t = Temperature(100)

    t.value = 20
    print(t.value)
    # 20

    t.value = -10
    # ValueError: Kelvin temperature cannot be negative


``__delattr__()``
=================
* Called when trying to delete attribute
* ``delattr(x, 'name')`` is equivalent to ``del x.name``
* Call stack:

    * ``del astro.name``
    * => ``delattr(astro, 'name')``
    * => ``astro.__delattr__(name)``

.. code-block:: python

    class Astronaut:

        def __delattr__(self, attribute_name):
            if attribute_name.startswith('_'):
                raise PermissionError(f'Field "{attribute_name}" is protected, cannot "delete" value.')
            else:
                return object.__delattr__(self, attribute_name)


    watney = Astronaut()

    watney.name = 'Mark Watney'
    watney._salary = 100

    del watney.name
    del watney._salary
    # PermissionError: Field "_salary" is protected, cannot "delete" value.

.. code-block:: python

    class Temperature:
        def __init__(self, initial_temperature):
            self.value = initial_temperature

        def __delattr__(self, attribute_name):
            if attribute_name == 'value':
                self.value = 0.0
            else:
                object.__delattr__(self, attribute_name)


    t = Temperature(100)

    del t.value
    print(t.value)
    # 0.0


``__getattribute__()``
======================
* Called for every time, when you want to access any attribute
* ``getattr(x, 'name')`` is equivalent to ``x.name``
* Before even checking if this attribute exists
* if ``__getattribute__()`` raises ``AttributeError`` it calls ``__getattr__()``
* Call stack:

    * ``astro.name``
    * => ``getattr(astro, 'name')``
    * => ``astro.__getattribute__('name')``
    * if ``astro.__getattribute__(name)`` raise ``AttributeError``
    * => ``astro.__getattr__('name')``

.. code-block:: python
    :caption: Example ``__getattribute__()``

    class Astronaut:

        def __getattribute__(self, attribute_name):
            if attribute_name.startswith('_'):
                raise PermissionError(f'Field "{attribute_name}" is protected, cannot "get" value.')
            else:
                return object.__getattribute__(self, attribute_name)


    watney = Astronaut()

    watney.name = 'Mark Watney'
    print(watney.name)
    # Mark Watney

    print(watney._salary)
    # PermissionError: Field "_salary" is protected, cannot "get" value.

.. code-block:: python
    :caption: Example ``__getattribute__()``

    class Temperature:
        def __init__(self, initial_temperature):
            self.value = initial_temperature

        def __getattribute__(self, attribute_name):
            if attribute_name == 'value':
                raise PermissionError('Field is private')
            else:
                return object.__getattribute__(self, attribute_name)


    temp = Temperature(273)

    temp.value = 20
    print(temp.value)
    # PermissionError: Field is private


``__getattr__()``
=================
* Called whenever you request an attribute that hasn't already been defined
* if ``__getattribute__()`` raises ``AttributeError`` it calls ``__getattr__()``
* Implementing a fallback for missing attributes


``hasattr()``
=============
* Check if object has attribute
* There is no ``__hasattr__()`` method
* Calls ``__getattribute__()`` and checks if raises ``AttributeError``

.. code-block:: python

    class Temperature:
        def __init__(self, initial_temperature):
            self.value = initial_temperature


    t = Temperature(100)

    hasattr(t, 'kelvin')
    # False

    hasattr(t, 'initial_temperature')
    # False

    hasattr(t, 'value')
    # True


Example
=======
.. code-block:: python

    class Astronaut:

        def __getattribute__(self, attribute_name):
            if attribute_name.startswith('_'):
                raise PermissionError(f'Field "{attribute_name}" is protected, cannot "get" value.')
            else:
                return object.__getattribute__(self, attribute_name)

        def __setattr__(self, attribute_name, new_value):
            if attribute_name.startswith('_'):
                raise PermissionError(f'Field "{attribute_name}" is protected, cannot "set" value.')
            else:
                return object.__setattr__(self, attribute_name, new_value)


    watney = Astronaut()

    watney.name = 'Mark Watney'
    print(watney.name)
    # Mark Watney

    watney._salary = 100
    # PermissionError: Field "_salary" is protected, cannot "set" value.

    print(watney._salary)
    # PermissionError: Field "_salary" is protected, cannot "get" value.


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
