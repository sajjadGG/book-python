************
Type ``int``
************


Type Definition
===============
.. highlights::
    * In Python 3 there is not maximal ``int`` value
    * Python 3 dynamically extends ``int``, when it's too big
    * You can use ``_`` for easier read especially with big numbers

.. code-block:: python

    value = 30              # 30
    value = -30             # -30

.. code-block:: python

    million = 1000000        # 1000000
    million = 1_000_000      # 1000000


Arithmetic Operators
====================
* ``+`` - Addition
* ``-`` - Subtraction
* ``*`` - Multiplication
* ``**`` - Power
* ``/`` - Division

.. code-block:: python

    10 + 2      # 12
    10 - 2      # 8
    10 * 2      # 20
    10 ** 2     # 100
    10 / 2      # 5


Assignments
===========

Example
-------
* Complexity level: medium
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/int_example.py`

:English:
    #. Calculate how many bits is one Megabyte
    #. How many times Megabyte is larger than Megabit?

:Polish:
    #. Oblicz ile bitów to jeden Megabajt
    #. Ile razy Megabajt jest większy od Megabita?

:Solution:
    .. literalinclude:: solution/int_example.py
        :language: python

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Mathematical operations

:Hint:
    * 1 Kb = 1024 b
    * 1 Mb = 1024 Kb
    * 1 B = 8 b
    * 1 KB = 1024 B
    * 1 MB = 1024 KB

Time
----
* Complexity level: easy
* Lines of code to write: 12 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/int_time.py`

:English:
    #. Calculate how many seconds is five minutes
    #. Calculate how many seconds is one hour
    #. Calculate how many seconds is work day (8 hours)
    #. Calculate how many seconds is work month (22 days per 8 hours)
    #. Calculate how many minutes is work week (40 hours)

:Polish:
    #. Oblicz ile sekund to pięć minut
    #. Oblicz ile sekund to jedna godzina
    #. Oblicz ile sekund to dzień pracy (8 godzin)
    #. Oblicz ile sekund to miesiąc pracy (22 dni po 8 godzin)
    #. Oblicz ile minut to tydzień pracy (40 godzin)

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Mathematical operations

:Hint:
    * 1 h = 60 min
    * 1 min = 60 s

Download time
-------------
* Complexity level: medium
* Lines of code to write: 10 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/int_download_time.py`

:English:
    #. Having internet connection with speed up to 100 Mb/s
    #. How long will take to download 100 MB?

:Polish:
    #. Mając łącze internetowe do 100 Mb/s
    #. Ile zajmie ściągnięcie pliku 100 MB?

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Mathematical operations

:Hint:
    * 1 Kb = 1024 b
    * 1 Mb = 1024 Kb
    * 1 B = 8 b
    * 1 KB = 1024 B
    * 1 MB = 1024 KB

Temperature
-----------
* Complexity level: medium
* Lines of code to write: 18 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/int_temperature.py`

:English:
    #. One Kelvin is equal to 1 Celsius degree (1K = 1°C)
    #. Zero Kelvin (absolute) is equal to -273.15 Celsius degrees
    #. For calculation use round number -273 (0K = -273°C)
    #. How many Kelvins and Celsius degrees has average temperatures at surface :cite:`MSL_REMS`:

        * Lunar day: 180 °C
        * Lunar night: 93 K
        * Mars average: −63 °C
        * Mars highest: 20 °C
        * Mars lowest: 120 K

:Polish:
    #. Jeden Kelwin to jeden stopień Celsiusza (1K = 1°C)
    #. Zero Kelwina (bezwzględne) to -273.15 stopni Celsiusza
    #. W zadaniu przyjmij równe -273°C (0K = -273°C)
    #. Ile Kelwinów, a ile stopni Celsiusza wynoszą średnie temperatury powierzchni :cite:`MSL_REMS`:

        * Księżyca w dzień: 180 °C
        * Księżyca w nocy: 93 K
        * Mars średnia: −63 °C
        * Mars najwyższa: 20 °C
        * Mars najniższa: 120 K

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Print formatting
    * Mathematical operations

