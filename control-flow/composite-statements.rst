********************
Composite statements
********************


Complex expressions
===================

``and``
-------
.. code-block:: python

    first_name = 'José'
    last_name = 'Jiménez'

    if first_name == 'José' and last_name == 'Jiménez':
        print('My name... José Jiménez')
    else:
        print('Your name is different')


``or``
------
.. code-block:: python

    first_name = 'José'
    last_name = 'Jiménez'

    if first_name == 'José' or first_name == 'Max':
        print('Your name is José or Max')
    else:
        print('Your name is different')


``and`` and ``or``
------------------
* Use parenthesis for explicit order

.. code-block:: python

    first_name = 'José'
    last_name = 'Jiménez'

    if (first_name == 'José' and last_name == 'Jiménez')
            or (first_name == 'Mark' and last_name == 'Watney'):
        print('Your name is José Jiménez or Mark Watney')
    else:
        print('Your name is different')


Good practice
=============

Complex conditions
------------------
.. code-block:: python

    for line in file:
        if line and not line.startswith('#') and not line.isspace():
            ...

Defining exit conditions first
------------------------------
.. code-block:: python

    for line in file:
        if line.startswith('#'):
            continue

        if line.isspace():
            continue

        ...


Control Statements
==================

``in`` with ``tuple``, ``dict``, ``list``, ``set``
--------------------------------------------------
* ``in`` checks whether value is in collection
* works with ``tuple``, ``dict``, ``list``, ``set``

.. code-block:: python

    usernames = {'José Jiménez', 'Jan Twardowski', 'Mark Watney'}

    if 'José Jiménez' in usernames:
        print(True)
    else:
        print(False)

``in`` with ``str``
-------------------
* ``in`` checks whether ``str`` is a part of another ``str``

.. code-block:: python

    text = 'My name... José Jiménez'

    if 'José' in text:
        print(True)
    else:
        print(False)

``not``
-------
* ``not`` negates (logically inverts) condition

.. code-block:: python

    name = None

    if not name:
        print('Name is not defined')

.. code-block:: python

    usernames = {'José', 'Max', 'Иван'}

    if 'José' not in usernames:
        print('Not found')

``is``
------
.. code-block:: python

    name = None

    if name is None:
        print('Name is not defined')

.. code-block:: python

    name = None

    if name is not None:
        print(name)


Assignments
===========

Classification of blood pressure in adults
------------------------------------------
* Complexity level: easy
* Lines of code to write: 25 lines
* Estimated time of completion: 25 min
* Filename: :download:`solution/ifelse_blood_pressure.py`

:English:
    #. Table contains classification of input data (see below)
    #. Blood Pressure classification according to American Heart Association
    #. User inputs blood pressure in ``XXX/YY`` format, where:

        - ``XXX: int`` systolic pressure
        - ``YY: int`` diastolic pressure

    #. Print on the screen status of given blood pressure
    #. If systolic and diastolic values are in different categories, assume worst case

:Polish:
    #. Tabela zawiera klasyfikację danych wejściowych (patrz poniżej)
    #. Klasyfikacja ciśnienia krwi wg. American Heart Association
    #. Użytkownik wprowadza ciśnienie krwi w formacie ``XXX/YY``, gdzie:

        - ``XXX: int`` to wartość ciśnienia skurczowego (ang. *systolic*)
        - ``YY: int`` to wartość ciśnienia rozkurczowego (ang. *diastolic*)

    #. Wyświetl na ekranie status wprowadzonego ciśnienia krwi
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
