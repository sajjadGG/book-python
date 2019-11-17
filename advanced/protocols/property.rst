**********
Properties
**********


Accessing fields
================

Setter and Getter methods
-------------------------
* Java way
* don't do that in Python

.. code-block:: python
    :caption: Accessing class fields using setter and getter

    class Astronaut:
        name = ''

        def set_name(self, name):
            print('Log, that value is being changed')
            self.name = name

        def get_name(self):
            return self.name


    astro = Astronaut()
    astro.set_name('Jan Twardowski')

    print(astro.get_name())

Then your code starts to look like this:

    .. code-block:: python

        class MyClass:
            def __init__(self):
                self._x = None

            def get_x(self):
                return self._x

            def set_x(self, value):
                self._x = value

            def del_x(self):
                del self._x

Rationale for setter and getter methods
---------------------------------------
.. code-block:: python
    :caption: `HabitatOS <https://www.habitatos.space>`_ Z-Wave sensor admin
    :emphasize-lines: 9,14-20

    from django.contrib import admin
    from habitat._common.admin import HabitatAdmin
    from habitat.sensors.models import ZWaveSensor


    @admin.register(ZWaveSensor)
    class ZWaveSensorAdmin(HabitatAdmin):
        change_list_template = 'sensors/change_list_charts.html'
        list_display = ['mission_date', 'mission_time', 'type', 'device', 'value', 'unit']
        list_filter = ['created', 'type', 'unit', 'device']
        search_fields = ['^date', 'device']
        ordering = ['-datetime']

        def get_list_display(self, request):
            list_display = self.list_display

            if request.user.is_superuser:
                list_display = ['earth_datetime'] + list_display

            return list_display

Direct attribute access
-----------------------
* the Python way

.. code-block:: python
    :caption: Accessing class fields

    class Astronaut:
        def __init__(self, name=''):
            self.name = name


    astro = Astronaut()              # either put ``name`` as an argument for ``__init__()``
    astro.name = 'Jan Twardowski'     # or create dynamic field in runtime

    print(astro.name)


Properties
==========

Rationale
---------
* Disable attribute modification
* Logging value access
* Check boundary
* Raise exceptions (TypeError)
* Check argument type

Property class
--------------
.. code-block:: python

    property()
    # <property object at 0x10ff07940>

    property().getter
    # <built-in method getter of property object at 0x10ff07998>

    property().setter
    # <built-in method setter of property object at 0x10ff07940>

    property().deleter
    # <built-in method deleter of property object at 0x10ff07998>

Property decorator
------------------
* ``@decorator`` syntax is just syntactic sugar; the syntax:

    .. code-block:: python

        @property
        def x(self):
            return self._x

* really means the same thing as

    .. code-block:: python

        def x(self):
            return self._x

        x = property(x)

Creating properties with ``property`` class
-------------------------------------------
* Property's arguments are method pointers ``get_x``, ``set_x``, ``del_x`` and a docstring

.. code-block:: python
    :caption: Properties

    class MyClass:
        def __init__(self):
            self._protected = None

        def get_x(self):
            return self._protected

        def set_x(self, value):
            self._protected = value

        def del_x(self):
            del self._protected

        x = property(get_x, set_x, del_x, "I am the 'x' property.")

Creating properties with ``@property`` decorator
------------------------------------------------
.. code-block:: python
    :emphasize-lines: 5-11

    class MyClass:
        def __init__(self):
            self._protected = None

        @property
        def x(self):
            pass

        @x.getter
        def x(self):
            return self._protected

        @x.setter
        def x(self, value):
            self._protected = value

        @x.deleter
        def x(self):
            del self._protected

.. code-block:: python
    :caption: Properties as a decorators
    :emphasize-lines: 5-7

    class MyClass:
        def __init__(self):
            self._protected = None

        @property
        def x(self):
            return self._protected

        @x.setter
        def x(self, value):
            self._protected = value

        @x.deleter
        def x(self):
            del self._protected


Use Cases
=========

Getter
------
* ``@property`` - for defining getters

.. code-block:: python
    :caption: Using ``@property`` as a getter

    class Temperature:
        def __init__(self, initial_temperature):
            self._protected = initial_temperature

        @property
        def value(self):
            pass

        @value.getter
        def value(self):
            print('You are trying to access a value')
            return self._protected


    t = Temperature(100)

    print(t.value)
    # You are trying to access a value
    # 100

.. code-block:: python
    :caption: Using ``@property`` as a getter

    class Temperature:
        def __init__(self, initial_temperature):
            self._protected = initial_temperature

        @property
        def value(self):
            print('You are trying to access a value')
            return self._protected


    t = Temperature(100)

    print(t.value)
    # You are trying to access a value
    # 100

Setter
------
* ``@x.setter`` - defining setter for field ``x``
* Require field to be ``@property``

.. code-block:: python
    :caption: ``@x.setter``

    class Temperature:
        def __init__(self, initial_temperature):
            self._protected = initial_temperature

        @property
        def value(self):
            pass

        @value.getter
        def value(self):
            return self._protected

        @value.setter
        def value(self, new_value):
            if new_value < 0.0:
                raise ValueError('Kelvin Temperature cannot be below zero')
            else:
                self._protected = new_value


    t = Temperature(100)

    print(t.value)
    # 100

    t.value = -10
    # ValueError: Kelvin Temperature cannot be below zero


Deleter
-------
* ``@x.deleter`` - for defining deleter for field ``x``
* Require field to be ``@property``

.. code-block:: python
    :caption: ``@x.deleter``

    class Temperature:
        def __init__(self, initial_temperature):
            self._protected = initial_temperature

        @property
        def value(self):
            pass

        @value.getter
        def value(self):
            return self._protected

        @value.deleter
        def value(self):
            self._protected = 0.0


    t = Temperature(100)

    del t.value

    print(t.value)
    # 0


Assignments
===========

Immutable classes
-----------------
* Complexity level: medium
* Lines of code to write: 35 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/property_immutable.py`

:English:
    #. Create class ``Point`` with ``x``, ``y``, ``z`` attributes
    #. Add ``position`` property which returns tuple ``(x, y, z)``
    #. Deleting ``position`` sets all attributes to 0 (``x=0``, ``y=0``, ``z=0``)
    #. Prevent setting position

:Polish:
    #. Stwórz klasę ``Point`` z atrybutami ``x``, ``y``, ``z``
    #. Dodaj property ``position``, który zwraca tuple ``(x, y, z)``
    #. Usunięcie ``position`` ustawia wszystkie atrybuty na 0 (``x=0``, ``y=0``, ``z=0``)
    #. Zablokuj edycję atrybutów
