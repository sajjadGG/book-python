****************
Setattr, Getattr
****************


Rationale
=========
* ``getattr(x, 'name')`` is equivalent to ``x.name``


Protocol
========
* ``__setattr__(object, attribute_name, value)``
* ``__getattribute__(object, attribute_name, default)``
* ``__getattr__(object, attribute_name, default)``
* ``__delattr__(object, attribute_name)``


``__setattr__()``
=================

Trigger
-------
* ``setattr(x, 'name', 'value')``

Implementation
--------------
.. code-block:: python
    :caption: Example ``__setattr__()``

    class Kelvin:
        def __init__(self, initial_temperature):
            self.temperature = initial_temperature

        def __setattr__(self, attribute_name, new_value):
            if attribute_name == 'value' and new_value < 0.0:
                raise ValueError('Temperature cannot be negative')
            else:
                object.__setattr__(self, attribute_name, new_value)


    temp = Kelvin(273)

    temp.value = 20
    print(temp.value)
    # 20

    temp.value = -10
    # ValueError: Temperature cannot be negative


``__getattr__()``
=================
* Called whenever you request an attribute that hasn't already been defined
* When ``__getattribute__()`` raised an ``AttributeError``

Rationale
---------
* Implementing a fallback for missing attributes


``__getattribute__()``
======================
* Called for every attribute access
* Before looking at the actual attributes on the object
* You can end up in infinite recursions very easily
* ``__getattribute__()`` is called before ``__getattr__()``
* if ``__getattribute__()`` raises ``AttributeError`` exception then the exception will be ignored and ``__getattr__()`` method will be invoked

Called by
---------
* ``getattr(x, 'name')``
* ``getattr(x, 'name', 'default value')``

Rationale
---------
* prevent access to attributes

Implementation
--------------
.. code-block:: python
    :caption: Example ``__getattribute__()``

    class Kelvin:
        def __init__(self, initial_temperature):
            self.temperature = initial_temperature

        def __getattribute__(self, attribute_name):
            if attribute_name == 'value':
                raise ValueError('Field is private, cannot display')
            else:
                return object.__getattribute__(self, attribute_name)


    temp = Kelvin(273)

    temp.value = 20
    print(temp.value)
    # ValueError: Field is private, cannot display


``__delattr__()``
=================
* ``del x.name``
* ``delattr(x, 'name')``

.. code-block:: python
    :caption: Example ``__delattr__()``

    class Kelvin:
        def __init__(self, initial_temperature):
            self.temperature = initial_temperature

        def __delattr__(self, attribute_name):
            if attribute_name == 'temperature':
                self.temperature = 0
            else:
                object.__delattr__(self, attribute_name)


    temp = Kelvin(273)

    del temp.temperature
    print(temp.temperature)
    # 0


``hasattr()``
=============
* Check if object has attribute
* no ``__hasattr__()``
* triggers ``__getattribute__()``


Assignments
===========

Immutable classes
-----------------
* Complexity level: medium
* Lines of code to write: 30 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/setattr_getattr_immutable.py`

:English:
    #. Create class ``Point`` with ``x``, ``y``, ``z`` attributes
    #. Prevent adding new attributes
    #. Prevent deleting attributes
    #. Prevent changing attributes
    #. Allow to set attributes only at the initialization

:Polish:
    #. Stwórz klasę ``Point`` z atrybutami ``x``, ``y``, ``z``
    #. Zablokuj możliwość dodawania nowych atrybutów
    #. Zablokuj możliwość usuwania atrybutów
    #. Zablokuj edycję atrybutów
    #. Pozwól na ustawianie atrybutów tylko przy inicjalizacji klasy
