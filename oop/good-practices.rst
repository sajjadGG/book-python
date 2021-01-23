Good Engineering Practises
**************************


Objects and instances
=====================
.. code-block:: python

    text = str('Jan,Twardowski')
    text.split(',')
    # ['Jan', 'Twardowski']

    text = str('Jan,Twardowski')
    str.split(text, ',')
    # ['Jan', 'Twardowski']

.. code-block:: python

    'Jan,Twardowski'.split(',')
    # ['Jan', 'Twardowski']

    str.split('Jan,Twardowski', ',')
    # ['Jan', 'Twardowski']


Tell - don't ask
================
* Tell-Don't-Ask is a principle that helps people remember that object-orientation is about bundling data with the functions that operate on that data.
* It reminds us that rather than asking an object for data and acting on that data, we should instead tell an object what to do.
* This encourages to move behavior into an object to go with the data.

Bad:

.. code-block:: python

    class Light:
        status = 'off'


    light = Light()
    light.status = 'on'
    light.status = 'off'

Good:

.. code-block:: python

    class Light:
        status = 'off'

        def turn_on(self):
            self.status = 'on'

        def turn_off(self):
            self.status = 'off'


    light = Light()
    light.turn_on()
    light.turn_off()

Bad:

.. code-block:: python

    class Hero:
        health: int = 10


    hero = Hero()

    while hero.health > 0:
        ...

Good:

.. code-block:: python

    class Hero:
        health: int = 10

        def is_alive(self):
            return self.health > 0


    hero = Hero()

    while hero.is_alive():
        ...


Setters, Getters, Deleters
==========================
* Java way: setters, getters, deleters
* Python way: properties, reflection, descriptors
* More information in `Protocol Property`
* More information in `Protocol Reflection`
* More information in `Protocol Descriptor`
* In Python you prefer direct attribute access

Accessing class fields using setter and getter:

.. code-block:: python

    class Astronaut:
        _name: str

        def set_name(self, name):
            self._name = name

        def get_name(self):
            return self._name


    astro = Astronaut()
    astro.set_name('Mark Watney')
    print(astro.get_name())
    # Mark Watney

Problem with setters and getters:

.. code-block:: python

    class Point:
        _x: int
        _y: int

        def get_x(self):
            return self._x

        def set_x(self, value):
            self._x = value

        def del_x(self):
            del self._x

        def get_y(self):
            return self._y

        def set_y(self, value):
            self._x = value

        def del_y(self):
            del self._y

Rationale for Setters and Getters:

.. code-block:: python

    class Temperature:
        kelvin: int

        def set_kelvin(self, kelvin):
            if kelvin < 0:
                raise ValueError('Kelvin cannot be negative')
            else:
                self._kelvin = kelvin


    t = Temperature()
    t.set_kelvin(-1)
    # Traceback (most recent call last):
    # ValueError: Kelvin cannot be negative

Rationale for Setters and Getters:

.. code-block:: python

    class Astronaut:
        _name: str

        def set_name(self, name):
            self._name = name.title()

        def get_name(self):
            return self._name


    astro = Astronaut()
    astro.set_name('JaN TwARdoWskI')
    print(astro.get_name())
    # Jan Twardowski

Rationale for Setters and Getters `HabitatOS <https://www.habitatos.space>`_ Z-Wave sensor admin:

.. code-block:: python

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


GRASP
=====
**General responsibility assignment software patterns (or principles)**, abbreviated GRASP, consist of guidelines for assigning responsibility to classes and objects in object-oriented design.

The different patterns and principles used in GRASP are controller, creator, indirection, information expert, high cohesion, low coupling, polymorphism, protected variations, and pure fabrication. All these patterns answer some software problem, and these problems are common to almost every software development project. These techniques have not been invented to create new ways of working, but to better document and standardize old, tried-and-tested programming principles in object-oriented design.


Assignments
===========
.. todo:: Create assignments
