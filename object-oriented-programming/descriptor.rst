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

    class Kelvin:
        def __get__(self, parent, parent_type):
            return parent.value

        def __set__(self, parent, value):
            parent.value = value

        def __delete__(self, parent):
            parent.value = None


    class Temperature:
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

    from datetime import datetime
    from pytz import timezone, utc


    class TimeConverter:
        def __get__(self, parent, type):
            return parent.utc.astimezone(self.tz)

        def __set__(self, parent, value):
            parent.utc = self.tz.localize(value).astimezone(utc)

        def __delete__(self, parent):
            parent.utc = datetime(1, 1, 1)


    class EuropeWarsaw(TimeConverter):
        tz = timezone('Europe/Warsaw')


    class EuropeMoscow(TimeConverter):
        tz = timezone('Europe/Moscow')


    class Time:
        warsaw = EuropeWarsaw()
        moscow = EuropeMoscow()

        def __init__(self, dt=datetime.now(tz=utc)):
            self.utc = dt


    now = Time()

    print(now.warsaw)
    # 2019-03-28 13:07:14.486365+01:00

    now.warsaw = datetime(2019, 3, 28, 13, 00, 00)

    print(now.utc)
    # 2019-03-28 12:00:00+00:00

    print(now.moscow)
    # 2019-03-28 15:00:00+03:00



Assignments
===========

Longitude and Latitude
----------------------
* Filename: ``oop/descriptor_geographic.py``
* Lines of code to write: 25 lines
* Estimated time of completion: 15 min

#. Stwórz klasę ``GeographicCoordinate``
#. Klasa ma mieć pola:

    * ``latitude`` - min: -180.0; max: 180.0
    * ``longitude`` - min: -90.0; max 90.0
    * ``elevation`` - min: -10,994; max: 8,848 m

#. Wykorzystując deskryptory dodaj mechanizm sprawdzania wartości
#. Przy kasowaniu (``del``) wartości, nie usuwaj jej, a ustaw na ``None``
#. Zablokuj całkowicie modyfikację pola ``elevation``

:The whys and wherefores:
    * Wykorzystanie deskryptorów
    * Walidacja danych

Temperatura
-----------
* Filename: ``oop/descriptor_temperature.py``
* Lines of code to write: 25 lines
* Estimated time of completion: 15 min

#. Stwórz klasę ``KelvinTemperature``
#. Temperatura musi być dodatnia, sprawdzaj to przy zapisie do pola ``value``
#. Usunięcie temperatury nie usunie wartości, ale ustawi ją na ``None``

:The whys and wherefores:
    * Wykorzystanie deskryptorów
    * Walidacja danych
