****************
setattr, getattr
****************


Rationale
=========
* ``getattr(x, 'name')`` is equivalent to ``x.name``


Protocol
========
* ``__setattr__(object, attribute, value)``
* ``__getattribute__(object, attribute, default)``
* ``__delattr__(object, attribute)``


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

        def __setattr__(self, name, new_value):
            if name == 'value' and new_value < 0.0:
                raise ValueError('Temperature cannot be negative')
            object.__setattr__(name, new_value)


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
        def __init__(self, temperature):
            self.temperature = temperature

        def __getattribute__(self, name):
            if name == 'value':
                raise ValueError('Field is private, cannot display')
            object.__getattribute__(name)


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

    class Point:
        x = 10
        y = -5
        z = 0

        def __delattr__(self, name):
            if name == 'z':
                raise ValueError('Cannot delete field')
            object.__delattr__(name)

    p = Point()

    del p.y

    delattr(p, 'z')
    # ValueError('Cannot delete field')

``hasattr()``
-------------
* Check if object has attribute
* no ``__hasattr__()``
* triggers ``__getattribute__()``
