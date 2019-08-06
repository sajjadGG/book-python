*******
``int``
*******


Defining ``int``
================
* Python 3 dynamically extends ``int``, when it's too big
* In Python 3 there is not maximal ``int`` value
* You can use ``_`` for easier read especially with big numbers

.. code-block:: python

    value = 30              # 30
    value = -30             # -30

.. code-block:: python

    million = 1000000        # 1000000
    million = 1_000_000      # 1000000


Converting to ``int``
=====================
* Also known as "type casting"
* ``int()`` converts argument to ``int``

.. code-block:: python

    int(10)                 # 10

.. code-block:: python

    int(10.0)               # 10
    int(10.9)               # 10

.. code-block:: python

    int(1.23)               # 1
    int(-1.23)              # -1

.. code-block:: python

    int('10')               # 10
    int('10.5')             # ValueError: invalid literal for int() with base 10: ' 10.5'


Numerical Operators
===================

Addition
--------
.. csv-table:: Addition operators
    :header: "Operand", "Description"
    :widths: 15, 85

    "``+x``", "``x``"
    "``x + y``", "Sum ``x`` and ``y``"
    "``x += y``", "Incremental addition"

.. code-block:: python

    value = 10 + 2

    print(value)
    # 12

.. code-block:: python

    value = 10
    value += 2

    print(value)
    # 12

Subtraction
-----------
.. csv-table:: Subtraction operators
    :header: "Operand", "Description"
    :widths: 15, 85

    "``-x``", "``x`` negation"
    "``x - y``", "Subtract ``x`` and ``y``"
    "``x -= y``", "Incremental subtraction"

.. code-block:: python

    value = 10 - 2

    print(value)
    # 8

.. code-block:: python

    value = 10
    value -= 2

    print(value)
    # 8

Multiplication
--------------
.. csv-table:: Multiplication operators
    :header: "Operand", "Description"
    :widths: 15, 85

    "``x * y``", "Multiply ``x`` and ``y``"
    "``x *= y``", "Incremental multiplication"
    "``x ** y``", "``x`` to the power of ``y``"

.. code-block:: python

    value = 10 * 2

    print(value)
    # 20

.. code-block:: python

    value = 10
    value *= 2

    print(value)
    # 20

.. code-block:: python

    10 ** 2         # 100
    3 ** 4          # 81
    -1 ** 2         # 1

Division
--------
.. csv-table:: Division operators
    :header: "Operand", "Description"
    :widths: 15, 85

    "``x / y``", "Divide ``x`` and ``y``"
    "``x /= y``", "Incremental division"
    "``x // y``", "Quotient of division ``x`` by ``y``"
    "``x % y``", "Modulo. Reminder of division ``x`` by ``y``"

.. code-block:: python

    value = 10 / 2

    print(value)
    # 5

.. code-block:: python

    value = 10
    value /= 2

    print(value)
    # 5

.. code-block:: python

    10 // 2         # 5
    10 % 2          # 0

    10 // 3         # 3
    10 % 3          # 1


Numeric Functions
=================

Minimal value
-------------
.. code-block:: python

    min(3, 1, 5)    # 1

Maximal value
-------------
.. code-block:: python

    max(3, 1, 5)    # 5

Absolute value
--------------
.. code-block:: python

    abs(1)          # 1
    abs(-1)         # 1

Number to the ``n-th`` power
----------------------------
.. code-block:: python

    pow(10, 2)      # 100
    pow(3, 4)       # 81
    pow(-1, 2)      # 1


Assignments
===========

Bytes and Kilobytes
-------------------
* Filename: :download:`solution/int_bytes.py`
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min

#. Dane są jednostki informatyczne:

    #. 1 B = 8 b
    #. 1 KB = 1024 B
    #. 1 MB = 1024 KB

#. Ile bitów to jeden Megabajt?

Download speed
--------------
* Filename: :download:`solution/int_speed.py`
* Lines of code to write: 15 lines
* Estimated time of completion: 10 min

#. Dane są jednostki informatyczne:

    #. 1 B = 8 bit
    #. 1 KB = 1024 B
    #. 1 MB = 1024 KB

#. Mając łącze internetowe do 100 Mb/s
#. Ile zajmie ściągnięcie pliku 100 MB?

SI Unit Conversion
------------------
* Filename: :download:`solution/int_si_units.py`
* Lines of code to write: 15 lines
* Estimated time of completion: 10 min

#. Dane są jednostki w układzie SI:

    * 1000 g = 1 kg
    * 1 metric ton = 1000 kg
    * 1 h = 60 min
    * 1 min = 60 s
    * 1 ata = 1013 hPa (dokładnie 1013.25 hPa, ale przyjmij ``int``)

#. Przelicz:

    * 3 tony -> ile to gramów?
    * 1 godzina -> ile to sekund?
    * 4 ata -> ile to Pascali?

:The whys and wherefores:
    * Definiowanie zmiennych
    * Nazewnictwo zmiennych
    * Korzystanie z print formatting
    * Operacje matematyczne na zmiennych

Temperature
-----------
* Filename: :download:`solution/int_temperature.py`
* Lines of code to write: 18 lines
* Estimated time of completion: 15 min

#. Jeden Kelwin to jeden stopień Celsiusza (1K = 1°C)
#. Zero Kelwina (bezwzględne) to -273.15 stopni Celsiusza, w zadaniu przyjmij równe -273°C (0K = -273°C)
#. Ile Kelwinów, a ile stopni Celsiusza wynoszą średnie temperatury powierzchni :cite:`MSL_REMS`:

    * Księżyca w dzień: -180 °C
    * Księżyca w nocy: 93 K
    * Mars średnia: −63 °C
    * Mars najwyższa: 20 °C
    * Mars najniższa: 120 K

:The whys and wherefores:
    * Definiowanie zmiennych
    * Nazewnictwo zmiennych
    * Korzystanie z print formatting
    * Operacje matematyczne na zmiennych

