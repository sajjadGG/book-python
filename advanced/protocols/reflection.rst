**********
Reflection
**********



Built-in Functions
==================
* ``setattr(obj, 'attribute_name', 'new value') -> None``
* ``getattr(obj, 'attribute_name', 'default value') -> Any``
* ``hasattr(obj, 'attribute_name') -> bool``
* ``delattr(obj, 'attribute_name') -> None``
* ``getattr(x, 'name')`` is equivalent to ``x.name``


Protocol
========
* ``__setattr__(self, attribute_name, value)``
* ``__getattribute__(self, attribute_name, default)``
* ``__getattr__(self, attribute_name, default)``
* ``__delattr__(self, attribute_name)``


``__setattr__()``
=================
* ``setattr(x, 'name', 'value')``

.. code-block:: python
    :caption: Example ``__setattr__()``

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
* ``del x.name``
* ``delattr(x, 'name')``

.. code-block:: python
    :caption: Example ``__delattr__()``

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
* Before even checking if this attribute exists
* ``__getattribute__()`` is called before ``__getattr__()``
* if ``__getattribute__()`` raises ``AttributeError`` exception, then the exception will be ignored and ``__getattr__()`` method will be invoked

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
* ``getattr(x, 'name')`` is equivalent to ``x.name``
* When ``__getattribute__()`` raised an ``AttributeError``
* Implementing a fallback for missing attributes


``hasattr()``
=============
* Check if object has attribute
* There is no ``__hasattr__()`` method
* Triggers ``__getattribute__()``


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
