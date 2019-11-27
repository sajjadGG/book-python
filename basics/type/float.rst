**************
Type ``float``
**************


Defining ``float``
==================
.. code-block:: python

    value = 13.37           # 13.37
    value = -13.37          # -13.37

.. code-block:: python
    :caption: Type annotation

    value: float = 13.37    # 13.37

Notation without leading or trailing zero
-----------------------------------------
.. highlights::
    * Used by ``numpy``

.. code-block:: python

    value = 10.             # 10.0
    value = .44             # 0.44

Engineering notation
--------------------
.. code-block:: python

    million = 1e6           # 1000000.0
    million = 1E6           # 1000000.0

.. code-block:: python

    +1e6                    # 1000000.0
    -1e6                    # -1000000.0

.. code-block:: python

    1e-3                    # 0.001
    1e-4                    # 0.0001
    1e-5                    # 1e-05
    1e-6                    # 1e-06

.. code-block:: python

    1.337 * 1e3             # 1337.0
    1.337 * 1e-3            # 0.001337


Converting to ``float``
=======================
.. highlights::
    * Also known as "type casting"
    * ``float()`` converts argument to ``float``

.. code-block:: python

    float(10)               # 10.0
    float(-10)              # -10.0

    float(10.5)             # 10.5
    float(-10.5)            # -10.5

.. code-block:: python

    float(13.37)            # 13.37
    float(-13.37)           # -13.37

.. code-block:: python

    float('+13.37')         # 13.37
    float('-13.37')         # -13.37

    float('13,37')          # ValueError: could not convert string to float: '13,37'
    float('-13,37')         # ValueError: could not convert string to float: '-13,37'


Numeric Functions
=================

Rounding numbers
----------------
.. code-block:: python

    pi = 3.14159265359

    round(pi)               # 3
    round(pi, 2)            # 3.14
    round(pi, 4)            # 3.1416

    print(f'{pi:.2f}')      # 3.14
    print(f'{pi:.4f}')      # 3.1416

Absolute value
--------------
.. code-block:: python

    abs(13.37)              # 13.37
    abs(-13.37)             # 13.37

Number to the ``n-th`` power
----------------------------
.. code-block:: python

    pow(2, -1)              # 0.5
    pow(1.337, 3)           # 2.389979753

    pow(4, 0.5)             # 2.0
    pow(2, 0.5)             # 1.4142135623730951

.. code-block:: python

    2 ** -1                 # 0.5
    1.337 ** 3              # 2.389979753

    4 ** 0.5                # 2.0
    2 ** 0.5                # 1.4142135623730951

Assignments
===========

Example
-------
* Complexity level: easy
* Lines of code to write: 13 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/float_si_units.py`

:English:
    * Input data (see below)
    * Use Imperial (US) measurements system
    * Convert to metric (SI) system

:Polish:
    * Dane wejściowe (por. sekcja input)
    * Używają system Imperialny (US)
    * Przelicz je na system metryczny (układ SI)

:Input:
    * Plane altitude: 10.000 ft
    * Bottle volume: 20 Fl Oz
    * Speed limit: 75 mph

:Solution:
    .. literalinclude:: solution/float_si_units.py
        :language: python

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Mathematical operations

Handling user input and type casting
------------------------------------
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/float_casting.py`

:English:
    #. User typed distance ``1337`` meters
    #. Print values in other units
    #. Use code output (see below) as a template
    #. Convert data to types shown in comments at the right side
    #. Instead ``...`` substitute calculated and converted values

:Polish:
    #. Użytkownik wprowadził odległość ``1337`` metrów
    #. Wypisz wartość w różnych jednostkach
    #. Użyj kodu wyjściowego (por. sekcja input) jako szablonu
    #. Przekonwertuj dane do typów podanych w komentarzu po prawej stronie
    #. Zamiast ``...`` podstaw wyliczone i przekonwertowane wartości

:Output:
    .. code-block:: python

        print(f'Meters: {...}')                              # int
        print(f'Kilometers: {...}')                          # int
        print(f'Miles: {...}')                               # float
        print(f'Nautical Miles: {...}')                      # float
        print(f'm: {...}, km: {...}, mi: {...}, nm: {...}')  # int, int, float, float

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

Spacesuit Pressures
-------------------
* Complexity level: medium
* Lines of code to write: 20 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/float_pressure.py`

:English:
    #. Operational pressure of EMU spacesuit: 4.3 PSI
    #. Operational pressure of ORLAN spacesuit: 400 hPa
    #. Calculate operational pressure in kPa for EMU
    #. Calculate operational pressure in PSI for Orlan
    #. Calculate International Standard Atmosphere pressure at sea level
    #. Calculate partial pressure of Oxygen at sea level
    #. At what altitude above sea level, pressure is equal to partial pressure of Oxygen
    #. All results print in kPa and PSI rounding to two decimal places

:Polish:
    #. Ciśnienie operacyjne skafandra kosmicznego EMU: 4.3 PSI
    #. Ciśnienie operacyjne skafandra kosmicznego ORLAN: 400 hPa
    #. Oblicz ciśnienie operacyjne skafandra EMU w kPa
    #. Oblicz ciśnienie operacyjne skafandra Orlan w PSI
    #. Oblicz ciśnienie standardowej atmosfery na poziomie morza
    #. Oblicz ciśnienie parcjalne tlenu na poziomie morza
    #. Na jakiej wysokości nad poziomem morza panuje ciśnienie równe ciśnieniu parcjalnemu tlenu?
    #. Wszystkie wyniki podaj w kPa oraz w PSI zaokrąglając do dwóch miejsc po przecinku

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Print formatting
    * Mathematical operations
    * Separation of business logic and view

.. figure:: img/spacesuits.png
    :scale: 25%
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
