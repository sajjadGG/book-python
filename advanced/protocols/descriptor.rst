**********
Descriptor
**********


Protocol
========
* ``__get__(self, parent, parent_type=None) -> self``
* ``__set__(self, parent, new_value) -> None``
* ``__delete__(self, parent) -> None``


Rationale
=========
* Add managed attributes to objects
* Outsource functionality into specialized classes


Builtin Descriptors
===================
* ``@classmethod``
* ``@staticmethod``
* ``@property``
* functions in general


Examples
========

Outside class
-------------
.. code-block:: python

    class Kelvin:
        def __get__(self, parent, parent_type):
            return round(parent._current_value, 2)

        def __set__(self, parent, new_value):
            parent._current_value = new_value

        def __delete__(self, parent):
            parent._current_value = 0.0


    class Temperature:
        def __init__(self):
            self._current_value = 0.0
            self.kelvin = Kelvin()


    t = Temperature()

    t.kelvin = 10        # Will trigger ``Kelvin.__set__()``
    print(t.kelvin)      # Will trigger ``Kelvin.__get__()``
    del t.kelvin         # Will trigger ``Kelvin.__delete__()``

Inside class
------------
.. code-block:: python

    class Temperature:
        def __init__(self):
            self._current_value = 0.0
            self.kelvin = Temperature.Kelvin()

        class Kelvin:
            def __get__(self, parent, parent_type):
                return round(parent._current_value, 2)

            def __set__(self, parent, new_value):
                parent._current_value = new_value

            def __delete__(self, parent):
                parent._current_value = 0.0



    t = Temperature()

    t.kelvin = 10        # Will trigger ``Kelvin.__set__()``
    print(t.kelvin)      # Will trigger ``Kelvin.__get__()``
    del t.kelvin         # Will trigger ``Kelvin.__delete__()``


Case Study
==========

Temperature Conversion
----------------------
.. code-block:: python

    class Temperature:
        def __init__(self):
            self._current_value = 0.0
            self.kelvin = Temperature.Kelvin()
            self.celsius = Temperature.Celsius()
            self.fahrenheit = Temperature.Fahrenheit()

        class Kelvin:
            def __get__(self, parent, parent_type):
                return round(parent._current_value, 2)

            def __set__(self, parent, new_value):
                parent._current_value = new_value

            def __delete__(self, parent):
                parent._current_value = 0

        class Celsius:
            def __get__(self, parent, parent_type):
                temp = parent._current_value - 273.15
                return round(temp, 2)

            def __set__(self, parent, new_value):
                temp = new_value + 273.15
                parent._current_value = temp

            def __delete__(self, parent):
                self.__set__(parent, 0)

        class Fahrenheit:
            def __get__(self, parent, parent_type):
                temp = (parent._current_value - 273.15) * 9 / 5 + 32
                return round(temp, 2)

            def __set__(self, parent, fahrenheit):
                temp = (fahrenheit - 32) * 5 / 9 + 273.15
                parent._current_value = temp

            def __delete__(self, parent):
                self.__set__(parent, 0)


    t = Temperature()

    t.kelvin = 273.15
    print(f'K: {t.kelvin}')      # 273.15
    print(f'C: {t.celsius}')     # 0.0
    print(f'F: {t.fahrenheit}')  # 32.0

    print()

    t.fahrenheit = 100
    print(f'K: {t.kelvin}')      # 310.93
    print(f'C: {t.celsius}')     # 37.78
    print(f'F: {t.fahrenheit}')  # 100.0

    print()

    t.celsius = 100
    print(f'K: {t.kelvin}')      # 373.15
    print(f'C: {t.celsius}')     # 100.0
    print(f'F: {t.fahrenheit}')  # 212.0

    print()

    del t.celsius
    print(f'K: {t.kelvin}')      # 273.15
    print(f'C: {t.celsius}')     # 0.0
    print(f'F: {t.fahrenheit}')  # 32.0

    print()

    del t.fahrenheit
    print(f'K: {t.kelvin}')      # 255.37
    print(f'C: {t.celsius}')     # -17.78
    print(f'F: {t.fahrenheit}')  # 0


.. _Timezone Conversion:

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

        def __set__(self, parent, new_datetime):
            """
            First localize timezone naive datetime,
            this will add information about timezone,
            next convert to UTC (shift time by UTC offset).
            """
            local_time = self.timezone.localize(new_datetime)
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

Temperature
-----------
* Complexity level: easy
* Lines of code to write: 9 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/descriptor_temperature.py`

:English:
    #. Create class ``KelvinTemperature``
    #. Temperature must always be positive
    #. Use descriptors to check boundaries at each value modification

:Polish:
    #. Stwórz klasę ``KelvinTemperature``
    #. Temperatura musi być zawsze być dodatnia
    #. Użyj deskryptorów do sprawdzania wartości granicznych przy każdej modyfikacji

:Output:
    .. code-block:: python

        t = KelvinTemperature()

        t.value = 1
        print(t.value)
        # 1

        t.value = -1
        # ValueError: Negative temperature

:The whys and wherefores:
    * Using descriptors
    * Data validation

Geographic Coordinates
----------------------
* Complexity level: medium
* Lines of code to write: 25 lines
* Estimated time of completion: 15 min
* Solution: :download:`solution/descriptor_gps.py`

:English:
    #. From input data (see below) model the class ``GeographicCoordinate``
    #. Use descriptors to check value boundaries
    #. Deleting field should set it to ``None``
    #. Disable modification of ``elevation`` field
    #. Allow to set ``elevation`` field at the class initialization

:Polish:
    #. Na podstawie danych wejściowych (patrz sekcja input) zamodeluj klasę ``GeographicCoordinate``
    #. Użyj deskryptory do sprawdzania wartości brzegowych
    #. Kasowanie pola powinno ustawiać jego wartość na ``None``
    #. Zablokuj modyfikację pola ``elevation``
    #. Zezwól na ustawianie pola ``elevation`` podczas inicjalizacji

:Input Data:
    .. code-block:: text

        latitude - type: float, min: -90, max 90
        longitude - type: float, min: -180, max: 180
        elevation - type: float, min: -10994, max: 8848

:The whys and wherefores:
    * Using descriptors
    * Data validation
