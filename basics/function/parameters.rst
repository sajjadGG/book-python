*******************
Function Parameters
*******************


Arguments vs Parameters
=======================
* argument is the value/variable/reference being passed to the function
* parameter is the receiving variable used within the function/block


Syntax
======
.. code-block:: python
    :caption: Function definition with parameters

    def my_function(<parameters>):
        <do something>

.. code-block:: python

    def add(a, b):
        print(a + b)


Required Parameters
===================
.. highlights::
    * Parameters without default values are required
    *

.. code-block:: python

    def add(a, b):
        print(a + b)


    add()
    # TypeError: add() missing 2 required positional arguments: 'a' and 'b'

    add(1)
    # TypeError: add() missing 1 required positional argument: 'b'

    add(1, 2)
    # 3

    add(1, 2, 3)
    # TypeError: add() takes 2 positional arguments but 3 were given


Optional Parameters
===================
.. highlights::
    * Optional parameters has default value
    * Function will use default value if not overwritten by user
    * Parameters with default values can be omitted while executing

.. code-block:: python

    def add(a=10, b=20):
        print(a + b)


    add()
    # 30

    add(1)
    # 21

    add(10, 20)
    # 30

    add(10, 20, 30)
    # TypeError: add() takes from 0 to 2 positional arguments but 3 were given


Required and Optional Parameters
================================
.. highlights::
    * Required parameters must be at the left side
    * Optional parameters must be at the right side
    * There cannot be required parameter after optional

.. code-block:: python

    def add(a, b=20):
        print(a + b)


    add()
    # TypeError: add() missing 1 required positional argument: 'a'

    add(1)
    # 21

    add(1, 2)
    # 3

    add(1, 2, 3)
    # TypeError: add() takes from 1 to 2 positional arguments but 3 were given

.. code-block:: python

    def add(a=1, b):
        print(a + b)

    # SyntaxError: non-default argument follows default argument

.. code-block:: python

    def add(a, b=1, c):
        print(a + b + c)

    # SyntaxError: non-default argument follows default argument


Examples
========

Example 1
---------
.. code-block:: python

    def add(a, b):
        print(a + b)


    add(1, 2)
    # 3

    add(1.5, 2.5)
    # 4.0

    add('a', 'b')
    # 'ab'

Example 2
---------
.. code-block:: python

    def echo(text):
        print(text)


    echo('hello')
    # hello

Example 3
---------
.. code-block:: python

    def connect(username, password, host='127.0.0.1', port=22,
                ssl=True, keep_alive=1, persistent=False):

        print('Connecting...')

Example 4
---------
* Definition of pandas.read_csv() function.
* Source:  https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html

.. code-block:: python

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

        print('Reading CSV...')


Assignments
===========

Function Parameters Example
---------------------------
* Complexity level: easy
* Lines of code to write: 2 lines
* Estimated time of completion: 1 min
* Solution: :download:`solution/function_parameters_example.py`

:English:
    #. Define function ``add``
    #. Function parameter is sequence of integers
    #. Print sum of all sequence values

:Polish:
    #. Zdefiniuj funkcję ``add``
    #. Parametrem do funkcji ma być sekwencja liczb całkowitych
    #. Wypisz sumę wszystkich wartości sekwencji

:Solution:
    .. literalinclude:: solution/function_params_example.py
        :language: python

Function Parameters Echo
------------------------
* Complexity level: easy
* Lines of code to write: 2 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/function_parameters_echo.py`

:English:
    #. Define function ``echo`` with two parameters
    #. Parameter ``a`` is required
    #. Parameter ``b`` is required
    #. Wypisz ``a`` i ``b``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Zdefiniuj funkcję ``echo`` z dwoma parametrami
    #. Parametr ``a`` jest wymagany
    #. Parametr ``b`` jest wymagany
    #. Wypisz ``a`` i ``b``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: python

        echo(1, 2)
        # a=1 b=2

        echo(3, 4)
        # a=3 b=4

Function Parameters Default
---------------------------
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/function_parameters_default.py`

:English:
    #. Define function ``default`` with two parameters
    #. Parameter ``a`` is required
    #. Parameter ``b`` is optional and has default value ``None``
    #. If only one argument was passed, consider second equal to the first one
    #. Wypisz ``a`` i ``b``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Zdefiniuj funkcję ``default`` z dwoma parametrami
    #. Parametr ``a`` jest wymagany
    #. Parametr ``b`` jest opcjonalny i ma domyślną wartość ``None``
    #. Funkcja zwraca wynik pierwszego argumentu do potęgi drugiego
    #. Jeżeli tylko jeden argument był podany, przyjmij drugi równy pierwszemu
    #. Wypisz ``a`` i ``b``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: python

        default(1)
        # a=1 b=1

        default(2, 3)
        # a=2 b=3

Aviation numbers
----------------
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min
* Solution: :download:`solution/function_args_aviation_numbers.py`

:English:
    #. Use data from "Input" section (see below)
    #. Given is pilot's alphabet for numbers
    #. Convert ``CONVERSION: Dict[int, str]`` to ``ALPHABET: Dict[str, str]`` (keys as ``str``)
    #. For input data (see input section below)
    #. Define function converting ``int`` or ``float`` to text form in Pilot's Speak
    #. You can modify ``ALPHABET``
    #. You cannot change ``CONVERSION``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Dany jest alfabet pilotów dla numerów
    #. Przekonwertuj ``CONVERSION: Dict[int, str]`` na ``ALPHABET: Dict[str, str]`` (klucze jako ``str``)
    #. Dla danych wejściowych (patrz sekcja input poniżej)
    #. Zdefiniuj funkcję konwertującą ``int`` lub ``float`` na formę tekstową w mowie pilotów
    #. Możesz modyfikować ``ALPHABET``
    #. Nie możesz zmieniać ``CONVERSION``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        CONVERSION = {
            0: 'zero',
            1: 'one',
            2: 'two',
            3: 'tree',
            4: 'fower',
            5: 'fife',
            6: 'six',
            7: 'seven',
            8: 'ait',
            9: 'niner',
        }

    .. code-block:: python

        >>> pilot_say(1969)
        'one niner six niner'

        >>> pilot_say(31337)
        'tree one tree tree seven'

        >>> pilot_say(13.37)
        'one tree and tree seven'

        >>> pilot_say(31.337)
        'tree one and tree tree seven'

        >>> pilot_say(-1969)
        'minus one niner six niner'

        >>> pilot_say(-31.337)
        'minus tree one and tree tree seven'

        >>> pilot_say(-49.35)
        'minus fower niner and tree fife'

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

.. _Cleaning text input:

Cleaning text input
-------------------
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min
* Solution: :download:`solution/function_args_str_clean.py`

:English:
    #. Use data from "Input" section (see below)
    #. Write function cleaning up data
    #. Function takes one argument of type ``str``
    #. Function returns cleaned text
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Napisz funkcję czyszczącą dane
    #. Funkcja przyjmuje jeden argument typu ``str``
    #. Funkcja zwraca oczyszczony tekst
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        >>> clean('ul.Mieszka II')
        'Mieszka II'

        >>> clean('UL. Zygmunta III WaZY')
        'Zygmunta III Wazy'

        >>> clean('  bolesława chrobrego ')
        'Bolesława Chrobrego'

        >>> clean('ul Jana III SobIESkiego')
        'Jana III Sobieskiego'

        >>> clean('\tul. Jana trzeciego Sobieskiego')
        'Jana III Sobieskiego'

        >>> clean('ulicaJana III Sobieskiego')
        'Jana III Sobieskiego'

        >>> clean('UL. JA    NA 3 SOBIES  KIEGO')
        'Jana III Sobieskiego'

        >>> clean('ULICA JANA III SOBIESKIEGO  ')
        'Jana III Sobieskiego'

        >>> clean('ULICA. JANA III SOBIeskieGO')
        'Jana III Sobieskiego'

        >>> clean(' Jana 3 Sobieskiego  ')
        'Jana III Sobieskiego'

        >>> clean('Jana III Sobi  eskiego ')
        'Jana III Sobieskiego'

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

Number to human readable
------------------------
* Complexity level: hard
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min
* Solution: :download:`solution/function_args_numstr_human.py`

:English:
    #. Use data from "Input" section (see below)
    #. Define function converting ``int`` or ``float`` to text form
    #. Text form must be in proper grammar form
    #. Max 6 digits before decimal separator (point ``.``)
    #. Max 5 digits after decimal separator (point ``.``)
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zdefiniuj funkcję konwertującą ``int`` lub ``float`` na formę tekstową
    #. Forma tekstowa musi być poprawna gramatycznie
    #. Max 6 cyfr przed separatorem dziesiętnym (point ``.``)
    #. Max 5 cyfr po separatorze dziesiętnym (point ``.``)
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

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
