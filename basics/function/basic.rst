.. _Function Basics:

***************
Function Basics
***************


Function definition
===================
.. highlights::
    * Reuse code
    * Improves code readability
    * Clean-up code
    * Allows for easier refactoring

.. code-block:: python

    def hello():
        print('My name... José Jiménez')

    hello()     # My name... José Jiménez
    hello()     # My name... José Jiménez
    hello()     # My name... José Jiménez


Naming convention
=================
.. highlights::
    * Do not use ``camelCase`` names
    * ``CamelCase`` is reserved for class names
    * Use ``snake_case`` names # Python - snake ;)
    * Add underscore (``_``) at the end of name when name collide
    * System functions names starts and ends with 'dunder' - double underscore: ``__``

.. code-block:: python
    :caption: Do not use ``camelCase``, CamelCase is reserved for class names. Use ``snake_case``

    def addNumbers(a, b):
        return a + b

    def add_numbers(a, b):
        return a + b

.. code-block:: python
    :caption: Use better names, rather than comments

    def cal_var(results):
        """Calculate variance"""
        return sum((Xi-m) ** 2 for Xi in results) / len(results)

    def calculate_variance(results):
        return sum((Xi-m) ** 2 for Xi in results) / len(results)

.. code-block:: python
    :caption: Add underscore (``_``) at the end of name when name collide

    def print_(text):
        print(f'<strong>{text}</strong>')

.. code-block:: python
    :caption: System functions names starts and ends with 'dunder' - double underscore: ``__``

    def __import__(module_name):
        ...



Assignments
===========

Example
-------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/functions_example.py`

:English:
    #. For given input data (see below)
    #. Define ``wanted: Set[str]`` with 'setosa' and 'versicolor'
    #. Iterate over data and split row into ``features`` and ``label`` (last)
    #. Define function which sums ``features``, only when ``label`` is in ``wanted``
    #. When ``label`` is not in ``wanted`` return ``0`` (zero)
    #. Print sum

:Polish:
    #. Dla danych wejściowych (patrz sekcja input)
    #. Zdefiniuj ``wanted: Set[str]`` z 'setosa' oraz 'versicolor'
    #. Iterując po danych rozdziel wiersz na ``features`` i ``label`` (ostatni)
    #. Zdefiniuj funkcję sumującą ``features``, tylko gdy ``label`` jest w ``wanted``
    #. Gdy ``label`` nie występuje w ``wanted`` zwróć ``0`` (zero)
    #. Wypisz sumę

:Input:
    .. code-block:: python

        INPUT = [
            ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 2.9, 5.6, 1.8, 'virginica'),
            (6.4, 3.2, 4.5, 1.5, 'versicolor'),
            (4.7, 3.2, 1.3, 0.2, 'setosa'),
            (7.0, 3.2, 4.7, 1.4, 'versicolor'),
            (7.6, 3.0, 6.6, 2.1, 'virginica'),
            (4.9, 3.0, 1.4, 0.2, 'setosa'),
        ]

:Output:
    .. code-block:: python

        OUTPUT: float
        # 74.9

:Solution:
    .. literalinclude:: solution/functions_example.py
        :language: python

Cleaning text input
-------------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/functions_str_clean.py`

:English:
    #. For given input data (see below)
    #. Write function cleaning up data
    #. Function takes one argument of type ``str``
    #. Function returns cleaned text

:Polish:
    #. Dla danych wejściowych (patrz sekcja input)
    #. Napisz funkcję czyszczącą dane
    #. Funkcja przyjmuje jeden argument typu ``str``
    #. Funkcja zwraca oczyszczony tekst

:Input:
    .. code-block:: python

        INPUT = [
            'ul.Mieszka II',
            'UL. Zygmunta III WaZY',
            '  bolesława chrobrego ',
            'ul Jana III SobIESkiego',
            '\tul. Jana trzeciego Sobieskiego',
            'ulicaJana III Sobieskiego',
            'UL. JA    NA 3 SOBIES  KIEGO',
            'ULICA JANA III SOBIESKIEGO  ',
            'ULICA. JANA III SOBIeskieGO',
            ' Jana 3 Sobieskiego  ',
            'Jana III Sobi  eskiego ',
        ]

:Output:
    .. code-block:: python

        'Mieszka II'
        'Zygmunta III Wazy'
        'Bolesława Chrobrego'
        'Jana III Sobieskiego'
        'Jana III Sobieskiego'
        'Jana III Sobieskiego'
        'Jana III Sobieskiego'
        'Jana III Sobieskiego'
        'Jana III Sobieskiego'
        'Jana III Sobieskiego'
        'Jana III Sobieskiego'

:The whys and wherefores:
    * Defining and calling functions
    * Passing function arguments
    * Cleaning data from user input

.. todo:: Translate input data to English

Aviation numbers
----------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/functions_aviation_numbers.py`

:English:
    #. For input data (see below)
    #. Define function converting ``int`` or ``float`` to text form in Pilot's Speak

:Polish:
    #. Dla danych wejściowych (patrz sekcja input)
    #. Zdefiniuj funkcję konwertującą ``int`` lub ``float`` na formę tekstową w mowie pilotów

:Input:
    .. code-block:: text

        0, "zero"
        1, "one"
        2, "two"
        3, "tree"
        4, "fower"
        5, "fife"
        6, "six"
        7, "seven"
        8, "ait"
        9, "niner"

    .. code-block:: python

        1969
        31337
        13.37
        31.337
        -1969
        -31.337
        -49.35

:Output:
    .. code-block:: python

        'one niner six niner'
        'tree one tree tree seven'
        'one tree and tree seven'
        'tree one and tree tree seven'
        'minus one niner six niner'
        'minus tree one and tree tree seven'
        'minus fower niner and tree fife'

:The whys and wherefores:
    * Defining and calling functions
    * Passing function arguments
    * Cleaning data from user input
    * ``dict`` lookups

Number to human readable
------------------------
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/functions_numstr_human.py`

:English:
    #. For input data (see below)
    #. Define function converting ``int`` or ``float`` to text form
    #. Text form must be in proper grammar form
    #. Max 6 digits before decimal separator (point ``.``)
    #. Max 5 digits after decimal separator (point ``.``)

:Polish:
    #. Dla danych wejściowych (patrz sekcja input)
    #. Zdefiniuj funkcję konwertującą ``int`` lub ``float`` na formę tekstową
    #. Forma tekstowa musi być poprawna gramatycznie
    #. Max 6 cyfr przed separatorem dziesiętnym (point ``.``)
    #. Max 5 cyfr po separatorze dziesiętnym (point ``.``)

:Input:
    .. code-block:: python

        1969
        31337
        13.37
        31.337
        -1969
        -31.337
        -49.35

:Output:
    .. code-block:: python

        'one thousand nine hundred sixty nine'
        'thirty one thousand three hundred thirty seven'
        'thirteen and thirty seven hundredths'
        'thirty one three hundreds thirty seven thousands'
        'minus one thousand nine hundred sixty nine'
        'minus thirty one and three hundreds thirty seven thousands'
        'minus forty nine and thirty five hundreds'

:The whys and wherefores:
    * Defining and calling functions
    * Passing function arguments
    * Cleaning data from user input
    * ``dict`` lookups

Roman numbers
-------------
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/functions_roman.py`

:English:
    #. Define function converting roman numerals to integer
    #. Define function converting integer to roman numerals

:Polish:
    #. Zdefiniuj funkcję przeliczającą liczbę rzymską na całkowitą
    #. Zdefiniuj funkcję przeliczającą liczbę całkowitą na rzymską

:The whys and wherefores:
    * Defining and calling functions
    * Checking for corner cases
    * Passing function arguments
    * Cleaning data from user input
    * ``dict`` lookups
