***************
Function Return
***************


Syntax
======
.. code-block:: python
    :caption: Function definition with parameters

    def <name>(<parameters>):
        return <do something>

.. code-block:: python

    def add_numbers(a, b):
        return a + b

.. code-block:: python

    def mean(a, b):
        c = (a+b) / 2
        return c

Return Keyword
==============
.. highlights::
    * ``return`` keyword indicates outcome of the function
    * Code after ``return`` will not execute

.. code-block:: python

    def hello():
        return 'ehlo world'

    print(hello())
    # 'ehlo world'

.. code-block:: python

    def hello():
        return 'ehlo world'
        print('This will not be executed')

    print(hello())
    # 'ehlo world'


Returning Simple Types
======================
.. code-block:: python

    def my_function():
        return 42

.. code-block:: python

    def my_function():
        return 13.37

.. code-block:: python

    def my_function():
        return 'Mark Watney'

.. code-block:: python

    def my_function():
        return True


Return None
===========
* Python will ``return None`` if no explicit return is specified

.. code-block:: python

    def my_function():
        return None

.. code-block:: python

    def my_function():
        print('ehlo world')

.. code-block:: python

    def my_function():
        pass

.. code-block:: python

    def my_function():
        """My function"""


Return Sequences
================
.. code-block:: python

    def my_function():
        return list(42, 13.37, 'Mark Watney')

    def my_function():
        return [42, 13.37, 'Mark Watney']

.. code-block:: python

    def my_function():
        return tuple(42, 13.37, 'Mark Watney')

    def my_function():
        return (42, 13.37, 'Mark Watney')

    def my_function():
        return 42, 13.37, 'Mark Watney'

.. code-block:: python

    def my_function():
        return set({42, 13.37, 'Mark Watney'})

    def my_function():
        return {42, 13.37, 'Mark Watney'}

.. code-block:: python

    def my_function():
        return frozenset({42, 13.37, 'Mark Watney'})

Return Mapping
==============
.. code-block:: python

    def my_function():
        return dict(first_name='Mark', last_name='Watney')

    def my_function():
        return {'first_name': 'Mark', 'last_name': 'Watney'}


Returning nested types
======================
.. code-block:: python

    def my_function():
        return [
            ('Mark', 'Watney'),
            {'Jan Twardowski', 'Melissa Lewis'},
            {'astro': 'Иванович', 'agency': {'name': 'Roscosmos'}},
            {'astro': 'Jiménez', 'missions': ('Mercury', 'Gemini', 'Apollo')},
            {'astro': 'Vogel', 'missions': (set(), tuple(), list())},
        ]


Assignments
===========

Return Numbers
--------------
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/function_return_numbers.py`

:English:
    #. Define function ``add`` without parameters
    #. Function should return sum of ``42`` and ``13.37``
    #. Call function and intercept returned value
    #. Print value

:Polish:
    #. Zdefiniuj funkcję ``add`` bez parametrów
    #. Funkcja powinna zwracać sumę ``42`` and ``13.37``
    #. Wywołaj funkcję i przechwyć zwracaną wartość
    #. Wyświetl wartość

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
