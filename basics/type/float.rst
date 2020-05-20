.. _Type Float:

**********
Type Float
**********


Type Definition
===============
* Notation without leading or trailing zero is used by ``numpy``

.. code-block:: python
    :caption: ``float`` Type Definition

    data = 13.37             # 13.37
    data = -13.37            # -13.37

.. code-block:: python
    :caption: Notation without leading or trailing zero

    data = 10.               # 10.0
    data = .44                # 0.44

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

    float(13)               # 13.0
    float(-13)              # -13.0
    float(13.37)            # 13.37
    float(-13.37)           # -13.37

    float('+13.37')         # 13.37
    float('-13.37')         # -13.37
    float('13,37')          # ValueError: could not convert string to float: '13,37'
    float('-13,37')         # ValueError: could not convert string to float: '-13,37'


Round Number
============
.. highlights::
    * ``round()`` - Rounds a number

.. code-block:: python
    :caption: ``round()`` - Rounds a number

    pi = 3.14159265359

    round(pi, 4)            # 3.1416
    round(pi, 2)            # 3.14
    round(pi)               # 3

    print(f'Pi number is {pi}')         # Pi number is 3.14159265359
    print(f'Pi number is {pi:f}')       # Pi number is 3.141593
    print(f'Pi number is {pi:.4f}')     # Pi number is 3.1416
    print(f'Pi number is {pi:.2f}')     # Pi number is 3.14


Built-in Functions
==================
* ``abs()`` - Absolute value
* ``pow()`` - Number to the ``n-th`` power
* Note, that arithmetic operator ``**`` also raises number to the power

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
    #. Use data from "Input" section (see below)
    #. Data uses imperial (US) system
    #. Convert to metric (SI) system
    #. Speed limit round to one decimal place

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Dane używają systemu imperialnego (US)
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
    #. Use code from "Input" section (see below)
    #. Convert units
    #. Instead ``...`` substitute calculated and converted values
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Przekonwertuj jednostki
    #. Zamiast ``...`` podstaw wyliczone i przekonwertowane wartości
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        m = 1337

        print(f'Meters: {...}')
        print(f'Kilometers: {...}')
        print(f'Miles: {...}')
        print(f'Nautical Miles: {...}')
        print(f'm: {...}, km: {...}, mi: {...}, nm: {...}')

:Output:
    .. code-block:: text

        Meters: 1337
        Kilometers: 1.337
        Miles: 0.83
        Nautical Miles: 0.72
        All: 1337, 1, 0.8, 0.7

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Print formatting
    * Mathematical operations
    * Separation of business logic and view

:Hints:
    * 1 km = 1000 m
    * 1 mile = 1609.344 m
    * 1 nautical mile = 1852 m

Float Calculation
-----------------
* Complexity level: medium
* Lines of code to write: 20 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/type_float_calculation.py`

:English:
    #. Operational pressure of EMU spacesuit: 4.3 PSI
    #. Operational pressure of ORLAN spacesuit: 400 hPa
    #. Calculate operational pressure in kPa for EMU
    #. Calculate operational pressure in PSI for Orlan
    #. Print all results in kPa and PSI rounding to two decimal places
    #. Compare result with "Output" section (see below)

:Polish:
    #. Ciśnienie operacyjne skafandra kosmicznego EMU: 4.3 PSI
    #. Ciśnienie operacyjne skafandra kosmicznego ORLAN: 400 hPa
    #. Oblicz ciśnienie operacyjne skafandra EMU w kPa
    #. Oblicz ciśnienie operacyjne skafandra Orlan w PSI
    #. Wypisz wszystkie wyniki w kPa oraz PSI zaokrąglając do dwóch miejsc po przecinku
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        EMU operating pressure: 29.65 kPa, 4.30 psi
        Orlan operating pressure: 40.00 kPa, 5.80 psi

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
    * 1 hPa = 100 Pa
    * 1 psi = 6894.757 Pa

Float Percent
-------------
* Complexity level: medium
* Lines of code to write: 9 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/type_float_percent.py`

:English:
    #. Calculate International Standard Atmosphere pressure at sea level
    #. Calculate partial pressure of Oxygen at sea level
    #. At what altitude above sea level, pressure is equal to partial pressure of Oxygen
    #. Print all results in kPa rounding to two decimal places
    #. Compare result with "Output" section (see below)

:Polish:
    #. Oblicz ciśnienie standardowej atmosfery na poziomie morza
    #. Oblicz ciśnienie parcjalne tlenu na poziomie morza
    #. Na jakiej wysokości nad poziomem morza panuje ciśnienie równe ciśnieniu parcjalnemu tlenu?
    #. Wypisz wszystkie wyniki w kPa zaokrąglając do dwóch miejsc po przecinku
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: text

        International Standard Atmosphere: 1013.25 hPa
        O2 partial pressure at sea level: 212.24 hPa
        Oxygen starvation altitude: 7088.63 m

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Print formatting
    * Mathematical operations
    * Separation of business logic and view

:Hint:
    * 1 hPa = 100 Pa
    * 1 ata = 1013.25 hPa (ISA - International Standard Atmosphere)
    * pressure gradient = -11.3 Pa / 1 m
    * Atmosphere gas composition:

        * Nitrogen 78.084%
        * Oxygen 20.946%
        * Argon 0.9340%
        * Carbon Dioxide 0.0407%
        * Others 0.001%
