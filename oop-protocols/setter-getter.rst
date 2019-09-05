***********************
Setter, Getter, Deleter
***********************


Rationale
=========
* Disable attribute modification
* Logging value access
* Check boundary
* Raise exceptions (TypeError)
* Check argument type


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
    :caption: Use case uzasadnionego użycia gettera w kodzie
    :emphasize-lines: 9,14-20

    from django.contrib import admin
    from habitat._common.admin import HabitatAdmin
    from habitat.sensors.models import ZWaveSensor


    @admin.register(ZWaveSensor)
    class ZWaveSensorAdmin(HabitatAdmin):
        change_list_template = 'sensors/change_list_charts.html'
        list_display = ['mission_date', 'mission_date', 'type', 'device', 'value', 'unit']
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
        def foo(self):
            return self._foo

* really means the same thing as

    .. code-block:: python

        def foo(self):
            return self._foo

        foo = property(foo)

Creating properties
-------------------
* Property's arguments are method pointers ``get_x``, ``set_x``, ``del_x`` and a docstring
* Code using properties

    .. code-block:: python
        :caption: Properties

        class MyClass:
            def __init__(self):
                self._x = None

            def get_x(self):
                return self._x

            def set_x(self, value):
                self._x = value

            def del_x(self):
                del self._x

            x = property(get_x, set_x, del_x, "I am the 'x' property.")

* Equivalent code using decorators

    .. code-block:: python
        :caption: Properties as a decorators

        class MyClass:
            def __init__(self):
                self._x = None

            @property
            def x(self):
                return self._x

            @x.setter
            def x(self, value):
                self._x = value

            @x.deleter
            def x(self):
                del self._x

Use Cases
=========

Getter
------
* ``@property`` - for defining getters

.. code-block:: python
    :caption: Using ``@property`` as a getter

    class Temperature:
        def __init__(self, kelvin: float = 0.0):
            self.kelvin = kelvin

        @property
        def celsius(self):
            temp = self.kelvin - 273.15
            return round(temp, 2)


    temp = Temperature(kelvin=309.75)

    print(temp.celsius)
    # 36.6


Setter
------
* ``@x.setter`` - defining setter for field ``x``
* Require field to be ``@property``

.. code-block:: python
    :caption: ``@x.setter``

    class Temperature:
        def __init__(self, kelvin: float = 0.0):
            self.kelvin = kelvin

        @property
        def celsius(self):
            temp = self.kelvin - 273.15
            return round(temp, 2)

        @celsius.setter
        def celsius(self, value):
            if value < -273.15:
                raise ValueError('Temperature below -273.15 is not possible')
            else:
                self.kelvin = value + 273.15

    temp = Temperature()

    print(temp.kelvin)
    # 0.0

    temp.celsius = 36.60
    print(temp.kelvin)
    # 309.75

    temp.celsius = -1000
    # ValueError: Temperature below -273.15 is not possible

Deleter
-------
* ``@x.deleter`` - for defining deleter for field ``x``
* Require field to be ``@property``

.. code-block:: python
    :caption: ``@x.deleter``

    class Temperature:
        def __init__(self, kelvin: float = 0.0):
            self.kelvin = kelvin

        @property
        def celsius(self):
            temp = self.kelvin - 273.15
            return round(temp, 2)

        @celsius.deleter
        def celsius(self):
            self.kelvin = 0.0

    temp = Temperature(kelvin=100)

    print(temp.celsius)
    # -173.15

    del temp.celsius

    print(temp.celsius)
    # -273.15
