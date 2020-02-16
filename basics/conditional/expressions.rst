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

    first_name = 'José'
    last_name = 'Jiménez'

    if first_name == 'José' and last_name == 'Jiménez':
        print('My name... José Jiménez')
    else:
        print("I don't know this catchphrase")

    # My name... José Jiménez

``or``
------
.. code-block:: python

    name = 'Jan'

    if name == 'Jan' or name == 'Melissa':
        print('Hello astronaut')
    else:
        print('Sorry, astronauts only')

    # Hello astronaut

``and`` and ``or``
------------------
.. highlights::
    * Use parenthesis for explicit order

.. code-block:: python

    first_name = 'José'
    last_name = 'Jiménez'

    if (first_name == 'Jan' and last_name == 'Twardowski')
            or (first_name == 'Mark' and last_name == 'Watney'):
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

``in`` with ``tuple``, ``dict``, ``list``, ``set``
--------------------------------------------------
.. highlights::
    * ``in`` checks whether value is in collection
    * works with ``tuple``, ``dict``, ``list``, ``set``
    * Checking if something in ``set`` - O(1) :ref:`Performance Optimization Contains`
    * Checking if something in ``list`` - O(n) :ref:`Performance Optimization Contains`

.. code-block:: python

    crew = {'Jan Twardowski', 'Mark Watney', 'Melissa Lewis'}

    if 'José Jiménez' in crew:
        print('Yes')
    else:
        print('No')

    # No

``in`` with ``str``
-------------------
.. highlights::
    * ``in`` checks whether ``str`` is a part of another ``str``

.. code-block:: python

    text = 'Monty Python'

    if 'Python' in text:
        print('Yes')
    else:
        print('No')

    # Yes

``not``
-------
.. highlights::
    * ``not`` negates (logically inverts) condition

.. code-block:: python

    crew = {'José', 'Max', 'Иван'}

    if 'Jan' not in crew:
        print('You are not assigned to the crew')

    # You are not assigned to the crew

.. code-block:: python

    name = None

    if not name:
        print('Name is empty')

``is``
------
.. code-block:: python

    name = None

    if name is None:
        print('Name is empty')

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
    #. User inputs blood pressure in ``XXX/YY`` or ``XXX/YYY`` format, where:

        - ``XXX: int`` systolic pressure
        - ``YY: int`` or ``YYY: int`` diastolic pressure

    #. Print status of given blood pressure
    #. If systolic and diastolic values are in different categories, assume worst case

:Polish:
    #. Tabela zawiera klasyfikację danych wejściowych (patrz sekcja input)
    #. Klasyfikacja ciśnienia krwi wg. American Heart Association
    #. Użytkownik wprowadza ciśnienie krwi w formacie ``XXX/YY`` lub ``XXX/YYY``, gdzie:

        - ``XXX: int`` to wartość ciśnienia skurczowego (ang. *systolic*)
        - ``YY: int`` lub ``YYY: int`` to wartość ciśnienia rozkurczowego (ang. *diastolic*)

    #. Wypisz status wprowadzonego ciśnienia krwi
    #. Gdy wartości ciśnienia skurczowego i rozkurczowego należą do różnych kategorii, przyjmij gorszy przypadek

.. csv-table:: Classification of blood pressure in adults :cite:`Whelton2018`
    :header-rows: 1

    "Blood Pressure Category", "Systolic [mm Hg]", "Operator", "Diastolic [mm Hg]"
    "Normal", "Less than 120", "and", "Less than 80"
    "Elevated", "120-129", "and", "Less than 80"
    "Hypertension stage 1", "130-139", "or", "80-89"
    "Hypertension stage 2", "140 or higher", "or", "90 or higher"
    "Hypertensive Crisis", "Higher than 180", "and/or", "Higher than 120"

:The whys and wherefores:
    * Reading user input
    * Type casting
    * Conditional statements
    * Composite conditional statements
    * Checking for corner cases
    * Defining constants and variables
