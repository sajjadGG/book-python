**************
Type ``float``
**************


Type Definition
===============
* Notation without leading or trailing zero is used by ``numpy``

.. code-block:: python
    :caption: ``float`` Type Definition

    value = 13.37           # 13.37
    value = -13.37          # -13.37

.. code-block:: python
    :caption: Notation without leading or trailing zero

    value = 10.             # 10.0
    value = .44             # 0.44

.. code-block:: python
    :caption: Engineering notation

    million = 1e6           # 1000000.0
    million = 1E6           # 1000000.0

    +1e6                    # 1000000.0
    -1e6                    # -1000000.0

    1e-3                    # 0.001
    1e-4                    # 0.0001
    1e-5                    # 1e-05
    1e-6                    # 1e-06

    1.337 * 1e3             # 1337.0
    1.337 * 1e-3            # 0.001337


Type Casting
============
* ``float()`` converts argument to ``float``

.. code-block:: python
    :caption: ``float()`` converts argument to ``float``

    float(13)                   # 13.0
    float(-13)                  # -13.0
    float(13.37)                # 13.37
    float(-13.37)               # -13.37

    float('+13.37')             # 13.37
    float('-13.37')             # -13.37
    float('13,37')              # ValueError: could not convert string to float: '13,37'
    float('-13,37')             # ValueError: could not convert string to float: '-13,37'


Rounding Numbers
================
.. highlights::
    * ``round()`` - Rounds a number

.. code-block:: python
    :caption: ``round()`` - Rounds a number

    round(3.1415926)        # 3
    round(3.1415926, 2)     # 3.14
    round(3.1415926, 4)     # 3.1416

.. code-block:: python
    :caption: ``round()`` - Rounds a number

    pi = 3.14159265359

    round(pi)               # 3
    round(pi, 2)            # 3.14
    round(pi, 4)            # 3.1416

    print(f'{pi:.2f}')      # 3.14
    print(f'{pi:.4f}')      # 3.1416


Numeric Functions
=================
* ``abs()`` - Absolute value
* ``pow()`` - Number to the ``n-th`` power

.. code-block:: python
    :caption: ``pow()`` - Number to the ``n-th`` power

    pow(10, 2)          # 100
    pow(2, -1)          # 0.5

    pow(1.337, 3)       # 2.389979753
    pow(4, 0.5)         # 2.0
    pow(2, 0.5)         # 1.4142135623730951

.. code-block:: python
    :caption: ``abs()`` - Absolute value

    abs(1)                      # 1
    abs(13.37)                  # 13.37

    abs(-1)                     # 1
    abs(-13.37)                 # 13.37


Assignments
===========

Float Example
-------------
* Complexity level: easy
* Lines of code to write: 13 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/type_float_example.py`

:English:
    #. Input data (see below)
    #. Use Imperial (US) measurements system
    #. Convert to metric (SI) system
    #. Speed limit round to one decimal place

:Polish:
    #. Dane wejściowe (patrz sekcja input)
    #. Używają system Imperialny (US)
    #. Przelicz je na system metryczny (układ SI)
    #. Ograniczenie prędkości zaokrąglij do jednego miejsca po przecinku

:Input:
    * Plane altitude: 10.000 ft
    * Bottle volume: 20 Fl Oz
    * Speed limit: 75 mph

:Solution:
    .. literalinclude:: solution/type_float_example.py
        :language: python

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Mathematical operations

Float Casting
-------------
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/type_float_casting.py`

:English:
    #. Declare variable for storing value of 1337 meters
    #. Print values in other units
    #. Use code output (see below) as a template
    #. Convert data to types shown in comments at the right side
    #. Instead ``...`` substitute calculated and converted values

:Polish:
    #. Zdefiniuj zmienną dla przechowywania wartości 1337 metrów
    #. Wypisz wartość w różnych jednostkach
    #. Użyj kodu wyjściowego (patrz sekcja input) jako szablonu
    #. Przekonwertuj dane do typów podanych w komentarzu po prawej stronie
    #. Zamiast ``...`` podstaw wyliczone i przekonwertowane wartości

:Non-functional requirements:
    * Do not use ``input()``

:Input:
    .. code-block:: python

        print(f'Meters: {...}')                              # int
        print(f'Kilometers: {...}')                          # float
        print(f'Miles: {...}')                               # float (two decimal places)
        print(f'Nautical Miles: {...}')                      # float (two decimal places)
        print(f'm: {...}, km: {...}, mi: {...}, nm: {...}')  # int, int, float (one decimal place), float (one decimal place)

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Print formatting
    * Mathematical operations
    * Separation of business logic and view

:Hints:
    * 1000 m = 1 km
    * 1608 m = 1 mile
    * 1852 m = 1 nautical mile

Float Calculation
-----------------
* Complexity level: medium
* Lines of code to write: 20 lines
* Estimated time of completion: 20 min
* Solution: :download:`solution/type_float_calculation.py`

:English:
    #. Operational pressure of EMU spacesuit: 4.3 PSI
    #. Operational pressure of ORLAN spacesuit: 400 hPa
    #. Calculate operational pressure in kPa for EMU
    #. Calculate operational pressure in PSI for Orlan
    #. Calculate International Standard Atmosphere pressure at sea level
    #. Calculate partial pressure of Oxygen at sea level
    #. At what altitude above sea level, pressure is equal to partial pressure of Oxygen
    #. Print all results in kPa and PSI rounding to two decimal places

:Polish:
    #. Ciśnienie operacyjne skafandra kosmicznego EMU: 4.3 PSI
    #. Ciśnienie operacyjne skafandra kosmicznego ORLAN: 400 hPa
    #. Oblicz ciśnienie operacyjne skafandra EMU w kPa
    #. Oblicz ciśnienie operacyjne skafandra Orlan w PSI
    #. Oblicz ciśnienie standardowej atmosfery na poziomie morza
    #. Oblicz ciśnienie parcjalne tlenu na poziomie morza
    #. Na jakiej wysokości nad poziomem morza panuje ciśnienie równe ciśnieniu parcjalnemu tlenu?
    #. Wypisz wszystkie wyniki w kPa oraz PSI zaokrąglając do dwóch miejsc po przecinku

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Print formatting
    * Mathematical operations
    * Separation of business logic and view

.. figure:: img/spacesuits.png
    :width: 75%
    :align: center

    EMU and Orlan

:Hint:
    * 1 ata = 1013.25 hPa (ISA - International Standard Atmosphere)
    * 1 psi = 6894.757 Pa
    * pressure gradient = -11.3 Pa / 1 meter
    * Atmosphere gas composition:

        * Nitrogen 78.084%
        * Oxygen 20.946%
        * Argon 0.9340%
        * Carbon Dioxide 0.0407%
        * Others 0.001%
