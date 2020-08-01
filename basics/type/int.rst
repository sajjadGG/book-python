.. _Type Int:

********
Type Int
********


Type Definition
===============
.. highlights::
    * In Python 3 there is not maximal ``int`` value
    * Python 3 dynamically extends ``int``, when it's too big
    * You can use ``_`` for easier read especially with big numbers

.. code-block:: python
    :caption: ``int`` Type Definition

    data = 1337                 # 1337
    data = -1337                # -1337

.. code-block:: python

    million = 1000000           # 1000000
    million = 1_000_000         # 1000000


Type Casting
============
.. highlights::
    * ``int()`` - converts argument to ``int``
    * ``int()`` - does not round numbers

.. code-block:: python
    :caption: ``int()`` converts argument to ``int``

    int(13)                     # 13
    int(13.0)                   # 13
    int(13.3)                   # 13
    int(13.37)                  # 13

    int(-13.37)                 # -13

    int('1')                    # 1
    int('+1')                   # 1
    int('-1')                   # -1
    int('1_000_000')            # 1000000

    int('13.37')                # ValueError: invalid literal for int() with base 10: '13.37'
    int('13,37')                # ValueError: invalid literal for int() with base 10: '13,37'
    int('-13.37')               # ValueError: invalid literal for int() with base 10: '-13.37'
    int('-13,37')               # ValueError: invalid literal for int() with base 10: '-13,37'


Type Checking
=============
.. highlights::
    * ``type()`` - Returns type of an argument

.. code-block:: python

    type(1)                     # <class 'int'>
    type(-1)                    # <class 'int'>
    type(0)                     # <class 'int'>
    type(-0)                    # <class 'int'>


Assignments
===========

Type Int Time
-------------
* Complexity level: easy
* Lines of code to write: 12 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/type_int_time.py`

:English:
    #. Calculate how many seconds is one day
    #. Calculate how many minutes is one day
    #. Calculate how many seconds is work day (8 hours)
    #. Calculate how many hours is work month (22 work days)
    #. Calculate how many minutes is work week (5 work days)

:Polish:
    #. Oblicz ile sekund to jedna doba
    #. Oblicz ile minut to je jedna doba
    #. Oblicz ile sekund to dzień pracy (8 godzin)
    #. Oblicz ile godzin to miesiąc pracy (22 dni pracy)
    #. Oblicz ile minut to tydzień pracy (5 dni pracy)

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Mathematical operations

:Hint:
    * 1 h = 60 min
    * 1 min = 60 s

Type Int Bytes
--------------
* Complexity level: medium
* Lines of code to write: 9 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/type_int_bytes.py`

:English:
    #. File size is one megabyte
    #. Calculate size in bits
    #. Calculate size in megabits

:Polish:
    #. Wielkość pliku to jeden megabajt
    #. Oblicz wielkość w bitach
    #. Oblicz wielkość w megabitach

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

Type Int Bandwidth
------------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/type_int_bandwidth.py`

:English:
    #. Having internet connection with speed up to 100 Mb/s
    #. How long will take to download 100 MB?

:Polish:
    #. Mając łącze internetowe "do 100 Mb/s"
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

Type Int Temperature
--------------------
* Complexity level: medium
* Lines of code to write: 18 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/type_int_temperature.py`

:English:
    #. One Kelvin is equal to 1 Celsius degree (1K = 1°C)
    #. Zero Kelvin (absolute) is equal to -273.15 Celsius degrees
    #. For calculation use round number -273 (0K = -273°C)
    #. How many Kelvins and Celsius degrees has average temperatures at surface :cite:`MSL_REMS`:

        * Lunar day: 453 K
        * Lunar night: 93 K
        * Mars highest: 20 °C
        * Mars lowest: -153 °C
        * Mars average: −63 °C

:Polish:
    #. Jeden Kelwin to jeden stopień Celsiusza (1K = 1°C)
    #. Zero Kelwina (bezwzględne) to -273.15 stopni Celsiusza
    #. W zadaniu przyjmij równe -273°C (0K = -273°C)
    #. Ile Kelwinów, a ile stopni Celsiusza wynoszą średnie temperatury powierzchni :cite:`MSL_REMS`:

        * Księżyca w dzień: 453 K
        * Księżyca w nocy: 93 K
        * Mars najwyższa: 20 °C
        * Mars najniższa: -153 °C
        * Mars średnia: −63 °C

:The whys and wherefores:
    * Defining constants and variables
    * Naming convention
    * Print formatting
    * Mathematical operations

