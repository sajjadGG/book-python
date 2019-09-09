*********
``float``
*********


Defining ``float``
==================
.. code-block:: python

    value = 10.5        # 10.5

Notation without leading or trailing zero
-----------------------------------------
* Used by ``numpy``

.. code-block:: python

    value = 10.         # 10.0
    value = .44         # 0.44

Engineering notation
--------------------
.. code-block:: python

    million = 1e6       # 1000000.0
    million = 1E6       # 1000000.0

.. code-block:: python

    million = +1E6      # 1000000.0
    million = -1E6      # -1000000.0

.. code-block:: python

    float(+1E6)         # 1000000.0
    float(-1E3)         # -1000.0

.. code-block:: python

    float(1e-4)         # 0.0001
    float(1E-3)         # 0.001

    float(1e-5)         # 1e-05
    float(1E-5)         # 1E-05

Maximal and minimal ``float`` values
------------------------------------
.. code-block:: python

    import sys

    sys.float_info.min  # 2.2250738585072014e-308
    sys.float_info.max  # 1.7976931348623157e+308

Infinity representation
-----------------------
.. code-block:: python

    1e308               # 1e+308
    1e309               # inf

.. code-block:: python

    float('-inf')       # -inf
    float('-Infinity')  # -inf

.. code-block:: python

    float('inf')        # inf
    float('Infinity')   # inf


Converting to ``float``
=======================
* Also known as "type casting"
* ``float()`` converts argument to ``float``

.. code-block:: python

    float(10.5)         # 10.5
    float(10)           # 10.0

.. code-block:: python

    float(1.23)         # 1.23
    float(-1.23)        # -1.23

.. code-block:: python

    float('+1.23')      # 1.23
    float('-1.23')      # -1.23

    float('1,23')       # ValueError: could not convert string to float: '1,23'
    float('-1,23')      # ValueError: could not convert string to float: '-1,23'


Numeric Functions
=================

Rounding numbers
----------------
.. code-block:: python

    pi = 3.14159265359

    round(pi)       # 3
    round(pi, 2)    # 3.14
    round(pi, 4)    # 3.1416

Absolute value
--------------
.. code-block:: python

    abs(1.5)        # 1.5
    abs(-1.5)       # 1.5

Number to the ``n-th`` power
----------------------------
.. code-block:: python

    pow(2, -1)      # 0.5
    pow(2.888, 3)   # 24.087491072

.. code-block:: python

    2 ** -1         # 0.5
    2.888 ** 3      # 24.087491072


Assignments
===========

Handling user input and type casting
------------------------------------
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/float_casting.py`

:User:
    #. User typed distance ``1337`` meters
    #. Print on the screen values in other units
    #. Use code output (see below) as a template
    #. Convert data to types shown in comments at the right side
    #. Instead ``...`` substitute calculated and converted values

:Polish:
    #. Użytkownik wprowadził odległość ``1337`` metrów
    #. Wyświetl wartość na ekranie w różnych jednostkach
    #. Użyj kodu wyjściowego (patrz poniżej) jako szablonu
    #. Przekonwertuj dane do typów podanych w komentarzu po prawej stronie
    #. Zamiast ``...`` podstaw wyliczone i przekonwertowane wartości

:Output:
    .. code-block:: python
        :caption: Output

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

SI Unit Conversion
------------------
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

:Polish:
    #. Ciśnienie operacyjne skafandra kosmicznego EMU: 4.3 PSI
    #. Ciśnienie operacyjne skafandra kosmicznego ORLAN: 400 hPa
    #. Oblicz ciśnienie operacyjne skafandra EMU w kPa
    #. Oblicz ciśnienie operacyjne skafandra Orlan w PSI
    #. Oblicz ciśnienie standardowej atmosfery na poziomie morza
    #. Oblicz ciśnienie parcjalne tlenu na poziomie morza
    #. Oa jakiej wysokości nad poziomem morza panuje ciśnienie równe ciśnieniu parcjalnemu tlenu?
    #. Wszystkie wyniki podaj w kPa oraz w PSI zaokrąglając do dwóch miejsc po przecinku

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Print formatting
    * Mathematical operations
    * Separation of business logic and view

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
