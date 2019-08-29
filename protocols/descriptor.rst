**********
Descriptor
**********


The Descriptor Protocol
=======================
* They provide the developer with the ability to add managed attributes to objects
* ``__get__(self, obj, type=None) -> self``
* ``__set__(self, obj, value) -> None``
* ``__delete__(self, obj) -> None``


Builtin Descriptor Object Examples
==================================
* classmethod
* staticmethod
* property
* functions in general


Example
=======
.. code-block:: python

    class Temperature:
        class Kelvin:
            def __get__(self, parent, parent_type):
                return parent.value

            def __set__(self, parent, value):
                parent.value = value

            def __delete__(self, parent):
                parent.value = None

        kelvin = Kelvin()


    temp = Temperature()

    temp.kelvin = 10        # Will trigger ``Kelvin.__set__()``
    print(temp.kelvin)      # Will trigger ``Kelvin.__get__()``
    del temp.kelvin         # Will trigger ``Kelvin.__delete__()``

Case Study
==========

Temperature Conversion
----------------------
.. code-block:: python

    class Temperature:
        class Kelvin:
            def __get__(self, parent, parent_type):
                return round(parent._value, 2)

            def __set__(self, parent, value):
                parent._value = round(value, 2)

            def __delete__(self, parent):
                parent._value = 0

        class Celsius:
            def __get__(self, parent, parent_type):
                temp = parent._value - 273.15
                return round(temp, 2)

            def __set__(self, parent, value):
                temp = value + 273.15
                parent._value = round(temp, 2)

            def __delete__(self, parent):
                parent._value = 0

        class Fahrenheit:
            def __get__(self, parent, parent_type):
                temp = (parent._value-273.15) * 9/5 + 32
                return round(temp, 2)

            def __set__(self, parent, fahrenheit):
                temp = (fahrenheit-32) * 5/9 + 273.15
                parent._value = round(temp, 2)

            def __delete__(self, parent):
                parent._value = 0

        kelvin = Kelvin()
        celsius = Celsius()
        fahrenheit = Fahrenheit()


    temp = Temperature()

    temp.kelvin = 273.15
    print(f'K: {temp.kelvin}')  # 273.15
    print(f'C: {temp.celsius}')  # 0.0
    print(f'F: {temp.fahrenheit}')  # 32.0

    print()

    temp.fahrenheit = 100
    print(f'K: {temp.kelvin}')  # 310.93
    print(f'C: {temp.celsius}')  # 37.78
    print(f'F: {temp.fahrenheit}')  # 100.0

    print()

    temp.celsius = 100
    print(f'K: {temp.kelvin}')  # 373.15
    print(f'C: {temp.celsius}')  # 100.0
    print(f'F: {temp.fahrenheit}')  # 212.0

    print()

    del temp.celsius
    print(f'K: {temp.kelvin}')  # 0
    print(f'C: {temp.celsius}')  # -273.15
    print(f'F: {temp.fahrenheit}')  # -459.67

Timezone Conversion
-------------------
.. code-block:: python

    from dataclasses import dataclass
    from datetime import datetime
    from pytz import timezone


    class Timezone:
        def __init__(self, name):
            self.timezone = timezone(name)

        def __get__(self, parent, *args, **kwargs):
            """
            Converts absolute time to desired timezone.
            """
            return parent.utc.astimezone(self.timezone)

        def __set__(self, parent, value):
            """
            First localize timezone naive datetime,
            this will add information about timezone,
            next convert to UTC (shift time by UTC offset).
            """
            local_time = self.timezone.localize(value)
            parent.utc = local_time.astimezone(timezone('UTC'))

        def __delete__(self, parent):
            """
            Set to the not existent date
            """
            parent.utc = datetime(1, 1, 1)


    @dataclass
    class Time:
        utc = datetime.now(tz=timezone('UTC'))
        warsaw = Timezone('Europe/Warsaw')
        moscow = Timezone('Europe/Moscow')
        est = Timezone('America/New_York')
        pdt = Timezone('America/Los_Angeles')


    t = Time()

    t.warsaw = datetime(1969, 7, 21, 3, 56, 15)
    print(t.utc)      # 1969-07-21 02:56:15+00:00
    print(t.moscow)   # 1969-07-21 05:56:15+03:00
    print(t.est)      # 1969-07-20 22:56:15-04:00
    print(t.pdt)      # 1969-07-20 19:56:15-07:00


Assignments
===========

Longitude and Latitude
----------------------
* Complexity level: medium
* Lines of code to write: 25 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/descriptor_geographic.py`

#. Stwórz klasę ``GeographicCoordinate``
#. Klasa ma mieć pola:

    * ``latitude`` - min: -90.0; max 90.0
    * ``longitude`` - min: -180.0; max: 180.0
    * ``elevation`` - min: -10,994; max: 8,848 m

#. Wykorzystując deskryptory dodaj mechanizm sprawdzania wartości
#. Przy kasowaniu (``del``) wartości, nie usuwaj jej, a ustaw na ``None``
#. Zablokuj całkowicie modyfikację pola ``elevation``
#. Co zrobić, aby można było inicjalnie ustawić pole ``elevation``, ale później już jego modyfikacja jest zablokowana?

:The whys and wherefores:
    * Wykorzystanie deskryptorów
    * Walidacja danych

Temperature
-----------
* Complexity level: medium
* Lines of code to write: 25 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/descriptor_temperature.py`

#. Stwórz klasę ``KelvinTemperature``
#. Temperatura musi być dodatnia, sprawdzaj to przy zapisie do pola ``value``
#. Usunięcie temperatury nie usunie wartości, ale ustawi ją na ``None``

:The whys and wherefores:
    * Wykorzystanie deskryptorów
    * Walidacja danych
