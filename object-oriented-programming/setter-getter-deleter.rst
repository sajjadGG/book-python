***********************
Setter, Getter, Deleter
***********************


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
    print(temp.value)  # 20

    temp.value = -10
    print(temp.value)  # ValueError: Temperature cannot be negative

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
    print(temp.value)  # ValueError: Field is private, cannot display

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
