***********************
Setter, Getter, Deleter
***********************


Accessing class fields using setter and getter
==============================================
.. code-block:: python
    :caption: Accessing class fields "Java way" -- don't do that in Python

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

Use case
--------
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


Accessing class fields using properties
=======================================
.. code-block:: python
    :caption: Accessing class fields - "the Python way"

    class Astronaut:
        def __init__(self, name=''):
            self.name = name

    astro = Astronaut()              # either put ``name`` as an argument for ``__init__()``
    astro.name = 'Jan Twardowski'     # or create dynamic field in runtime

    print(astro.name)


Dynamically creating fields
===========================
.. code-block:: python
    :caption: Funkcja inicjalizującą, która automatycznie dodaje pola do naszej klasy w zależności od tego co zostanie podane przy tworzeniu obiektu

    class Astronaut:
        def __init__(self, last_name, **kwargs):
            self.last_name = last_name

            for key, value in kwargs.items():
                setattr(self, key, value)


    jan = Astronaut(last_name='Twardowski', addresses=())
    ivan = Astronaut(first_name='Иван', last_name='Иванович', agency='Roscosmos')

    print(jan.last_name)   # Twardowski
    print(ivan.first_name)  # Иван

    print(jan.__dict__)    # {'last_name': 'Twardowski', 'addresses': ()}
    print(ivan.__dict__)    # {'last_name': 'Иванович', 'first_name': 'Иван', 'agency': 'Roscosmos'}


Getter
======
* ``@property`` - for defining getters
* Przykład użycia:

    * Blokowanie możliwości edycji pola klasy
    * Dodawanie logowania przy ustawianiu wartości

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
======
* ``@x.setter`` - for defining setter for field ``x``
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
=======
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


Accessors
=========

``__setattr__()``
-----------------
.. code-block:: python
    :caption: Example ``__setattr__()``

    class Kelvin:
        def __init__(self, initial_temperature):
            self.temperature = initial_temperature

        def __setattr__(self, name, new_value):
            if name == 'value' and new_value < 0.0:
                raise ValueError('Temperature cannot be negative')
            else:
                super().__setattr__(name, new_value)


    temp = Kelvin(273)

    temp.value = 20
    print(temp.value)
    # 20

    temp.value = -10
    # ValueError: Temperature cannot be negative

``__getattribute__()``
----------------------
.. code-block:: python
    :caption: Example ``__getattribute__()``

    class Kelvin:
        def __init__(self, temperature):
            self.temperature = temperature

        def __getattribute__(self, name):
            if name == 'value':
                raise ValueError('Field is private, cannot display')
            else:
                super().__getattribute__(name)


    temp = Kelvin(273)

    temp.value = 20
    print(temp.value)
    # ValueError: Field is private, cannot display

``__delattr__()``
-----------------
.. code-block:: python
    :caption: Example ``__delattr__()``

    class Point:
        x = 10
        y = -5
        z = 0

        def __delattr__(self, name):
            if name == 'z':
                raise ValueError('Cannot delete field')
            else:
                super().__delattr__(name)

    p = Point()

    del p.y

    delattr(p, 'z')
    # ValueError('Cannot delete field')
