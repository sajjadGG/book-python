.. _Function Basics:

***************
Function Basics
***************


Function definition
===================
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


Returning values
================
* ``return`` keyword indicates outcome of the function
* Code after ``return`` will not execute

.. code-block:: python

    def hello():
        return 'ehlo world'

    output = hello()

    print(output)
    # 'ehlo world'

.. code-block:: python

    def hello():
        return 'ehlo world'
        print('This will not be executed')

    output = hello()

    print(output)
    # 'ehlo world'

Returning simple types
----------------------
.. code-block:: python

    def function():
        return 42

.. code-block:: python

    def function():
        return 13.37

.. code-block:: python

    def function():
        return 'Mark Watney'

.. code-block:: python

    def function():
        return (42, 13.37, 'Mark Watney')

.. code-block:: python

    def function():
        return 42, 13.37, 'Mark Watney'

.. code-block:: python

    def function():
        return [42, 13.37, 'Mark Watney']

.. code-block:: python

    def function():
        return {42, 13.37, 'Mark Watney'}

.. code-block:: python

    def function():
        return {'first_name': 'Mark', 'last_name': 'Watney'}

.. code-block:: python

    def function():
        return True

.. code-block:: python

    def function():
        return None

.. code-block:: python

    def function():
        print('ehlo world')
        # Python will ``return None`` if no explicit return is specified

.. code-block:: python

    def function():
        pass
        # Python will ``return None`` if no explicit return is specified

.. code-block:: python

    def function():
        # Python will ``return None`` if no explicit return is specified

Returning nested types
----------------------
.. code-block:: python

    def function():
        return [
            ('Mark', 'Watney'),
            {'Jan Twardowski', 'Melissa Lewis'},
            {'astro': 'Иванович', 'agency': {'name': 'Roscosmos'}},
            {'astro': 'Jiménez', 'missions': ('Mercury', 'Gemini', 'Apollo')},
        ]

Function arguments
==================

Required arguments
------------------
.. code-block:: python

    def subtract(a, b):
        return a - b

Arguments with default value
----------------------------
* Arguments without default values are required
* Function will take default value if not overwritten by user
* Arguments with default values must be at the right side
* Arguments with default values can be omitted while executing

.. code-block:: python

    def subtract(a=1, b=2):
        return a - b

.. code-block:: python

    def subtract(a, b=2):
        return a - b

.. code-block:: python

    def subtract(a=1, b):
        return a - b

    # SyntaxError: non-default argument follows default argument

Positional arguments
--------------------
.. code-block:: python

    def subtract(a, b):
        return a - b

    subtract(2, 1)      # 1
    subtract(1, 2)      # -1

Keyword arguments
-----------------
* Arguments without default values are required
* Order of keyword arguments has no significance

.. code-block:: python

    def subtract(a, b):
        return a - b

    subtract(a=2, b=1)  # 1
    subtract(b=1, a=2)  # 1
    subtract(2, b=1)    # 1
    subtract(a=2, 1)    # SyntaxError: positional argument follows keyword argument

.. code-block:: python

    def hello(name='José Jiménez'):
         print(f'My name... {name}')


    hello('Mark Watney')          # My name... Mark Watney
    hello(name='Mark Watney')     # My name... Mark Watney
    hello()                       # My name... José Jiménez

.. code-block:: python

    def connect(username, password, host='127.0.0.1',
                port=80, ssl=True, keep_alive=1, persistent=False):
        print('Connecting...')


    connect('admin', 'admin', 'localhost', 80, False, 1, True)

    connect(host='localhost', username='admin', password='admin', ssl=True, keep_alive=1, persistent=True)

    connect(
        host='localhost',
        username='admin',
        password='admin',
        port=443,
        ssl=True,
        persistent=True,
    )

.. code-block:: python
    :emphasize-lines: 6,10

    def read_csv(filepath_or_buffer, sep=', ', delimiter=None, header='infer',
                 names=None, index_col=None, usecols=None, squeeze=False, prefix=None,
                 mangle_dupe_cols=True, dtype=None, engine=None, converters=None,
                 true_values=None, false_values=None, skipinitialspace=False,
                 skiprows=None, nrows=None, na_values=None, keep_default_na=True,
                 na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False,
                 infer_datetime_format=False, keep_date_col=False, date_parser=None,
                 dayfirst=False, iterator=False, chunksize=None, compression='infer',
                 thousands=None, decimal=b'.', lineterminator=None, quotechar='"',
                 quoting=0, escapechar=None, comment=None, encoding=None, dialect=None,
                 tupleize_cols=None, error_bad_lines=True, warn_bad_lines=True,
                 skipfooter=0, doublequote=True, delim_whitespace=False, low_memory=True,
                 memory_map=False, float_precision=None):
        """
        Definition of pandas.read_csv() function
        https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
        """


    my_file1 = read_csv('iris-clean.csv')

    my_file2 = read_csv('iris-clean.csv', encoding='utf-8')

    my_file3 = read_csv(
        filepath_or_buffer='iris-clean.csv',
        encoding='utf-8',
        verbose=True,
        usecols=['Sepal Length', 'Species']
    )


Naming convention
=================

Function name convention
------------------------
* It's not Java, do not use ``camelCase``

    .. code-block:: python

        def addNumbers(a, b):
            return a + b

* It's Python, use ``snake_case`` # Python - snake ;)

    .. code-block:: python

        def add_numbers(a, b):
            return a + b

Use better names, rather than comments
--------------------------------------
.. code-block:: python

    def cal_var(results):
        """Calculate variance"""
        return sum((Xi-m) ** 2 for Xi in results) / len(results)

.. code-block:: python

    def calculate_variance(results):
        return sum((Xi-m) ** 2 for Xi in results) / len(results)

Name collisions
---------------
* ``_`` at the end of name when name collision

    .. code-block:: python

        def print_(text):
            print(f'<strong>{text}</strong>')

System functions names
----------------------
* ``__`` at the beginning and end of name

    .. code-block:: python

        def __import__(module_name):
            ...


Variable scope
==============

Global scope
------------
* All variables in main program
* Variables are available inside all functions

.. code-block:: python

    print(globals())
    # {...}

Local scope
-----------
* Variables defined inside function
* Variables are not available from outside

.. code-block:: python

    print(locals())
    # {...}

.. code-block:: python

    def add_numbers(a, b=2):
        c = 3
        print(locals())

    add_numbers(1)
    # {'a': 1, 'b': 2, 'c': 3}


Assignments
===========

Cleaning text input
-------------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/functions_str_clean.py`

:English:
    #. For given input data (see below)
    #. Write function cleaning up data

:Polish:
    #. Dla danych wejściowych (patrz poniżej)
    #. Napisz funkcję czyszczącą dane

:Input:
    .. code-block:: python

        'ul.Mieszka II'
        'UL. Zygmunta III WaZY'
        '  bolesława chrobrego '
        'ul Jana III SobIESkiego'
        '\tul. Jana trzeciego Sobieskiego'
        'ulicaJana III Sobieskiego'
        'UL. JA\tNA 3 SOBIES  KIEGO'
        'ULICA JANA III SOBIESKIEGO  '
        'ULICA. JANA III SOBIeskieGO'
        ' Jana 3 Sobieskiego  '
        'Jana III Sobi\teskiego '

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
    #. Dla danych wejściowych (patrz poniżej)
    #. Zdefiniuj funkcję konwertującą ``int`` lub ``float`` na formę tekstową w mowie pilotów

:Input:
    .. csv-table:: Aviation Phonetic Numbers
        :header-rows: 1
        :file: data/aviation-numbers.csv

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
    #. Dla danych wejściowych (patrz poniżej)
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
        'minus thirty one three hundreds thirty seven thousands'
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
