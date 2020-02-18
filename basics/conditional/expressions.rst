.. _Conditional Expressions:

***********************
Conditional Expressions
***********************


Complex expressions
===================

``and``
-------
.. code-block:: python
    :caption: Inside joke (see :ref:`José Jiménez`)

    firstname = 'Mark'
    lastname = 'Watney'

    if firstname == 'Mark' and lastname == 'Watney':
        print('Hello Space Pirate')
    else:
        print('Sorry, astronauts only')
    # Hello Space Pirate

``or``
------
.. code-block:: python

    name = 'Watney'

    if name == 'Watney' or name == 'Twardowski':
        print('Hello astronaut')
    else:
        print('Sorry, astronauts only')
    # Hello astronaut

``and`` and ``or``
------------------
.. highlights::
    * Use parenthesis for explicit order

.. code-block:: python

    firstname = 'José'
    lastname = 'Jiménez'

    if (firstname == 'Mark' and lastname == 'Watney') \
            or (firstname == 'Jan' and lastname == 'Twardowski') \
            or (firstname == 'Melissa' and lastname == 'Lewis'):
        print('Hello astronaut')
    else:
        print('Sorry, astronauts only')

    # Sorry, astronauts only

Good practice
=============

Complex conditions
------------------
.. code-block:: python

    for line in file:
        if line and not line.startswith('#') or not line.isspace():
            ...

Defining exit conditions first
------------------------------
.. code-block:: python

    for line in file:
        line = line.strip()

        if line.startswith('#'):
            continue

        if line.isspace():
            continue

        ...


Control Statements
==================

``in``
------
.. highlights::
    * ``in`` checks whether value is in sequence
    * works with ``tuple``, ``dict``, ``list``, ``set``, ``str``
    * Checking if something in ``set`` - O(1) :ref:`Performance Optimization Contains`
    * Checking if something in ``list`` - O(n) :ref:`Performance Optimization Contains`

.. code-block:: python

    text = 'Monty Python'

    if 'Python' in text:
        print('Yes')
    else:
        print('No')
    # Yes

.. code-block:: python

    crew = ['Watney', 'Twardowski', 'Lewis']

    if 'Jiménez' in crew:
        print('Yes')
    else:
        print('No')
    # No

.. code-block:: python

    crew = {'Watney', 'Twardowski', 'Lewis'}

    if 'Jiménez' in crew:
        print('Yes')
    else:
        print('No')
    # No

``is``
------
.. code-block:: python

    name = None

    if name is None:
        print('Name is empty')

``not``
-------
.. highlights::
    * ``not`` negates (logically inverts) condition

.. code-block:: python

    crew = None

    if not name:
        print('Name is empty')

.. code-block:: python

    crew = {'Watney', 'Twardowski', 'Lewis'}

    if 'Ivanovich' not in crew:
        print('You are not assigned to the crew')
    # You are not assigned to the crew

.. code-block:: python

    name = None

    if name is not None:
        print(name)


Assignments
===========

Classification of blood pressure in adults
------------------------------------------
* Complexity level: medium
* Lines of code to write: 25 lines
* Estimated time of completion: 25 min
* Solution: :download:`solution/ifelse_blood_pressure.py`

:English:
    #. Table contains classification of input data (see below)
    #. Blood Pressure classification according to American Heart Association
    #. User inputs blood pressure in ``XXX/YY`` or ``XXX/YYY`` format
    #. User will not input invalid data
    #. Data format:

        - ``XXX: int`` systolic pressure
        - ``YY: int`` or ``YYY: int`` diastolic pressure

    #. Print status of given blood pressure
    #. If systolic and diastolic values are in different categories, assume worst case

:Polish:
    #. Tabela zawiera klasyfikację danych wejściowych (patrz sekcja input)
    #. Klasyfikacja ciśnienia krwi wg. American Heart Association
    #. Użytkownik wprowadza ciśnienie krwi w formacie ``XXX/YY`` lub ``XXX/YYY``
    #. Użtkownik nie będzie wprowadzał danych niepoprawnych
    #. Format danych:

        - ``XXX: int`` to wartość ciśnienia skurczowego (ang. *systolic*)
        - ``YY: int`` lub ``YYY: int`` to wartość ciśnienia rozkurczowego (ang. *diastolic*)

    #. Wypisz status wprowadzonego ciśnienia krwi
    #. Gdy wartości ciśnienia skurczowego i rozkurczowego należą do różnych kategorii, przyjmij gorszy przypadek
    #. (z gwiazdką)

.. csv-table:: Classification of blood pressure in adults :cite:`Whelton2018`
    :header-rows: 1

    "Blood Pressure Category", "Systolic [mm Hg]", "Operator", "Diastolic [mm Hg]"
    "Normal", "Less than 120", "and", "Less than 80"
    "Elevated", "120-129", "and", "Less than 80"
    "Hypertension stage 1", "130-139", "or", "80-89"
    "Hypertension stage 2", "140 or higher", "or", "90 or higher"
    "Hypertensive Crisis", "Higher than 180", "and/or", "Higher than 120"

:Input:
    .. code-block:: text

        '119/79': 'Normal',
        '120/80': 'Hypertension stage 1',
        '121/79': 'Elevated',
        '120/81': 'Hypertension stage 1',
        '130/80': 'Hypertension stage 1',
        '130/89': 'Hypertension stage 1',
        '140/85': 'Hypertension stage 2',
        '140/89': 'Hypertension stage 2',
        '141/90': 'Hypertension stage 2',
        '141/91': 'Hypertension stage 2',
        '180/120': ('Hypertension stage 2', 'Hypertensive Crisis')

:The whys and wherefores:
    * Reading user input
    * Type casting
    * Conditional statements
    * Composite conditional statements
    * Checking for corner cases
    * Defining constants and variables
