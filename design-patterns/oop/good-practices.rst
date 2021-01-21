Good Engineering Practises
==========================


Objects and instances
---------------------
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
----------------
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

        def switch_on(self):
            self.status = 'on'

        def switch_off(self):
            self.status = 'off'


    light = Light()
    light.switch_on()
    light.switch_off()

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
--------------------------
* Java way: setters, getters, deleters
* Python way: :ref:`properties <Protocol Property>`, :ref:`reflection <Protocol Reflection>` or :ref:`descriptors <Protocol Descriptor>`
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


Collections Abstract Base Classes
---------------------------------
* Source: https://docs.python.org/dev/library/collections.abc.html#collections-abstract-base-classes

========================== ====================== ======================= ====================================================
ABC                        Inherits from          Abstract Methods        Mixin Methods
========================== ====================== ======================= ====================================================
:class:`Container`                                ``__contains__``
:class:`Hashable`                                 ``__hash__``
:class:`Iterable`                                 ``__iter__``
:class:`Iterator`          :class:`Iterable`      ``__next__``            ``__iter__``
:class:`Reversible`        :class:`Iterable`      ``__reversed__``
:class:`Generator`         :class:`Iterator`      ``send``, ``throw``     ``close``, ``__iter__``, ``__next__``
:class:`Sized`                                    ``__len__``
:class:`Callable`                                 ``__call__``
:class:`Collection`        :class:`Sized`,        ``__contains__``,
                           :class:`Iterable`,     ``__iter__``,
                           :class:`Container`     ``__len__``

:class:`Sequence`          :class:`Reversible`,   ``__getitem__``,        ``__contains__``, ``__iter__``, ``__reversed__``,
                           :class:`Collection`    ``__len__``             ``index``, and ``count``

:class:`MutableSequence`   :class:`Sequence`      ``__getitem__``,        Inherited :class:`Sequence` methods and
                                                  ``__setitem__``,        ``append``, ``reverse``, ``extend``, ``pop``,
                                                  ``__delitem__``,        ``remove``, and ``__iadd__``
                                                  ``__len__``,
                                                  ``insert``

:class:`ByteString`        :class:`Sequence`      ``__getitem__``,        Inherited :class:`Sequence` methods
                                                  ``__len__``

:class:`Set`               :class:`Collection`    ``__contains__``,       ``__le__``, ``__lt__``, ``__eq__``, ``__ne__``,
                                                  ``__iter__``,           ``__gt__``, ``__ge__``, ``__and__``, ``__or__``,
                                                  ``__len__``             ``__sub__``, ``__xor__``, and ``isdisjoint``

:class:`MutableSet`        :class:`Set`           ``__contains__``,       Inherited :class:`Set` methods and
                                                  ``__iter__``,           ``clear``, ``pop``, ``remove``, ``__ior__``,
                                                  ``__len__``,            ``__iand__``, ``__ixor__``, and ``__isub__``
                                                  ``add``,
                                                  ``discard``

:class:`Mapping`           :class:`Collection`    ``__getitem__``,        ``__contains__``, ``keys``, ``items``, ``values``,
                                                  ``__iter__``,           ``get``, ``__eq__``, and ``__ne__``
                                                  ``__len__``

:class:`MutableMapping`    :class:`Mapping`       ``__getitem__``,        Inherited :class:`Mapping` methods and
                                                  ``__setitem__``,        ``pop``, ``popitem``, ``clear``, ``update``,
                                                  ``__delitem__``,        and ``setdefault``
                                                  ``__iter__``,
                                                  ``__len__``


:class:`MappingView`       :class:`Sized`                                 ``__len__``
:class:`ItemsView`         :class:`MappingView`,                          ``__contains__``,
                           :class:`Set`                                   ``__iter__``
:class:`KeysView`          :class:`MappingView`,                          ``__contains__``,
                           :class:`Set`                                   ``__iter__``
:class:`ValuesView`        :class:`MappingView`,                          ``__contains__``, ``__iter__``
                           :class:`Collection`
:class:`Awaitable`                                ``__await__``
:class:`Coroutine`         :class:`Awaitable`     ``send``, ``throw``     ``close``
:class:`AsyncIterable`                            ``__aiter__``
:class:`AsyncIterator`     :class:`AsyncIterable` ``__anext__``           ``__aiter__``
:class:`AsyncGenerator`    :class:`AsyncIterator` ``asend``, ``athrow``   ``aclose``, ``__aiter__``, ``__anext__``
========================== ====================== ======================= ====================================================

.. todo:: Make this table more readable


Assignments
-----------
.. todo:: Create assignments
