.. _Types:

*****
Types
*****


Variables and constants
=======================

Variable declaration
--------------------
.. code-block:: python

    my_variable = 10
    my_variable = 'ehlo world'

Constant declaration
--------------------
.. code-block:: python

    MY_CONSTANT = 10
    MY_CONSTANT = 'ehlo world'

Variables vs. constants
-----------------------
* Jedyną różnicą jest konwencja nazewnicza
* Stałe zapisujemy dużymi literami
* Zmienne zapisujemy małymi literami

Types
-----
* Od Python 3.5 wprowadzono nową składnię
* Nowa składnia nie jest wymagana (ale jest dobrą praktyką)
* Nowa składnia uruchomiona w Python przed 3.5 rzuci SyntaxError
* Twórcy języka mówą, że typy nigdy nie będą wymagane
* Aby sprawdzić poprawność trzeba użyć bibliotek zewnętrznych tj: ``mypy`` lub ``pyre-check``
* Typy można znaleźć w wielu funkcjach w bibliotece standardowej
* Dobre IDE podpowiada typy i informuje o błędach

.. code-block:: python

    name: str = 'José Jiménez'
    age: int = 30

Type inference
--------------
* Static Typing (Java, C++, Swift)

.. code-block:: java

    String name = new String("José Jiménez")

* Dynamic Typing (Python, PHP, Ruby)

.. code-block:: python

    name = str('José Jiménez')

.. code-block:: python

    name: str = str('José Jiménez')  # Type annotations

    # Type annotations (type hinting not forcing)
    # this will work, but IDE should warn
    name: str = 10


Numerical types
===============

``int``
-------
* Python 3 dynamically extends ``int``, when it's too big
* In Python 3 there is not maximal ``int`` value
* Defining ``int``:

    .. code-block:: python

        value = 30
        value: int = 30

* For large numbers you can use ``_`` as thousands separator, or engineering notation:

    .. code-block:: python

        million = 1000000
        million = 1_000_000
        million = 1e6
        million = 1E6
        millionth = 1E-6

* ``int()`` converts argument to ``int``:

    .. code-block:: python

        int(10)                 # 10
        int(10.0)               # 10
        int(10.9)               # 10
        int(' 10')              # 10
        int(' 10.5')            # ValueError: invalid literal for int() with base 10: ' 10.5'

``float``
---------
* Defining ``float``:

    .. code-block:: python

        value = 10.5
        value: float = 10.5

* ``float()`` converts argument to ``float``:

    .. code-block:: python

        float(10)              # 10.0

        float('+1.23')         # 1.23
        float('-1.23')         # -1.23
        float('   -123.45\n')  # -123.45

        float('1e-003')        # 0.001
        float('+1E6')          # 1000000.0

        float('-inf')          # -inf
        float('-Infinity')     # -inf
        float('inf')           # inf
        float('Infinity')      # inf

``complex``
-----------
* Complex number with real and imaginary parts
* Engineering notation ``j`` not mathematical ``i``
* No space inside the expression
* Defining ``complex``:

    .. code-block:: python

        value = complex('1+2j')         # (1+2j)
        value = complex('1 + 2j')       # ValueError: complex() arg is a malformed string


Logical types
=============

``bool``
--------
* ``bool()`` converts argument to ``bool``
* First letter capitalized, other are lower cased
* Defining ``bool``:

    .. code-block:: python

        True
        False

``None``
--------
* Empty value (null)
* It is not ``False`` and ``0``
* Used for unknown (unset) values
* With ``if`` statements behaves like ``False`` and ``0``

.. code-block:: python

    name = None

    if name is None:
        print('What is your name?')

    if not wiek:
        print('What is your name?')


Character types
===============

``str``
-------
* ``str()`` converts argument to ``str``

.. code-block:: python

    name = 'José'       # 'José'
    name = "José"       # 'José'
    name: str = 'José'  # 'José'
    'José' * 3          # JoséJoséJosé

    str(1969)           # '1969'
    str(13.37)          # '13.37'

    name = """
        José Jiménez
        Max Peck
        Ivan Ivanovic
    """
    # '\n    José Jiménez\n    Max Peck\n    Ivan Ivanovic\n'


Single or double quote?
-----------------------
* ``"`` and ``'`` works the same
* Keep consistency in code
* Python console uses ``'``
* This is why I will use ``'`` in this book
* ``doctest`` uses single quotes and throws error on double quotes

.. code-block:: python

    my_str = 'it\'s José\'s book'
    my_str = "it's José's book"

.. code-block:: python

    my_str = '<a href="http://python.astrotech.io">Python and Machine Learning</a>'

Escape characters
-----------------
.. code-block:: text

    \n
    \r\n

.. figure:: img/type-machine.jpg
    :scale: 50%
    :align: center

    Why we have '\\r\\n' on Windows?

.. code-block:: text

    \x1F680     # after \x goes hexadecimal number
    \u0001F680  # after \u goes four hexadecimal numbers
    🚀
    \b1010      # after \b goes bytes
    \t
    \'

Characters before strings
-------------------------
* Format string: since Python 3.6

.. csv-table:: String modifiers
    :header-rows: 1
    :widths: 15, 30, 55
    :file: data/str-modifiers.csv

.. code-block:: python

    name = 'José Jiménez'

    f'My name {name}'
    u'zażółć gęślą jaźń'
    b'this is text'
    r'(?P<foo>)\n'
    r'C:\Users\Admin\file.txt'

.. code-block:: python

    print('C:\Users\Admin\file.txt')
    # ``\Users`` (``s`` is invalid hexadecimal for unicode)
    # SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape


``print()``
-----------
* Prints on the screen
* More in :numref:`Print Formatting`

.. code-block:: python

    print('My name José Jiménez')  # My name José Jiménez

    name = 'José Jiménez'
    print(f'My name {name}')       # My name José Jiménez

String immutability
-------------------
* ``str`` is immutable
* ``str`` methods create a new modified ``str``
* How many ``str`` are in the memory?

.. code-block:: python

    name = 'José'
    name += ' Jiménez'

    print(name)         # José Jiménez

String methods
--------------

``split()``
^^^^^^^^^^^
.. code-block:: python

    text = 'José Jiménez'
    text.split()        # ['José', 'Jiménez']

    text = 'Max,Peck'
    text.split(',')     # ['Max', 'Peck']

``strip()``, ``lstrip()``, ``rstrip()``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

    name = '    Max Peck    '

    name.strip()        # 'Max Peck'
    name.lstrip()       # 'Max Peck    '
    name.rstrip()       # '    Max Peck'

``startswith()``
^^^^^^^^^^^^^^^^
* starts_with

.. code-block:: python

    name = 'José Jiménez'

    if name.startswith('José'):
        print('My name José Jiménez')
    else:
        print('I have no name')

``join()``
^^^^^^^^^^
.. code-block:: python

    names = ['José', 'Max', 'Ivan', str(1961), '1969']

    ';'.join(names)
    # 'José;Max;Ivan;1961;1969'

``title()``, ``lower()``, ``upper()``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Unify data format before analysis
* Example:

    * 'Jana III Sobieskiego 1/2'
    * 'ul. Jana III Sobieskiego 1/2'
    * 'Ul. Jana III Sobieskiego 1/2'
    * 'UL. Jana III Sobieskiego 1/2'
    * 'os. Jana III Sobieskiego 1/2'
    * 'Jana 3 Sobieskiego 1/2'
    * 'Jana 3ego Sobieskiego 1/2'
    * 'Jana III Sobieskiego 1 m. 2'
    * 'Jana III Sobieskiego 1 apt 2'
    * 'Jana Iii Sobieskiego 1/2'
    * 'Jana IIi Sobieskiego 1/2'

.. code-block:: python

    name = 'joSé jiMénEz'

    name.title()    # 'José Jiménez'
    name.upper()    # 'JOSÉ JIMÉNEZ'
    name.lower()    # 'josé jiménez'

``replace()``
^^^^^^^^^^^^^
.. code-block:: python

    name = 'José Jiménez'
    name.replace('J', 'j')  # 'josé jiménez'

String splicing
---------------
.. code-block:: python

    text = 'Lorem ipsum'

    text[2]      # 'r'
    text[0:3]    # 'Lor'
    text[:3]     # 'Lor'
    text[1:4]    # 'ore'
    text[-3]     # 's'
    text[-3:]    # 'sum'
    text[-3:-1]  # 'su'
    text[:-2]    # 'Lorem ips'

    text[::2]    # 'Lrmism'
    text[::-1]   # 'muspi meroL'
    text[::-2]   # 'msimrL'

Handling user input
-------------------
* ``input()`` returns ``str``
* Space at the end of prompt

.. code-block:: python

    name = input('Type your name: ')


Assignments
===========

Basic usage of ``print()`` function
-----------------------------------
#. Stwórz skrypt o treści:

    .. code-block:: python

        import sys
        import os

        print(f'Python Executable: {sys.executable}')
        print(f'Python Version: {sys.version}')
        print(f'Virtualenv: {os.getenv("VIRTUAL_ENV")}')

#. Uruchom go w swoim IDE
#. Jaka wersja Python jest zainstalowana?
#. Gdzie Python jest zainstalowany?
#. Czy korzystasz z Virtualenv?

:Założenia:
    * Nazwa pliku: ``python_version.py``
    * Szacunkowa długość kodu: 5 linii
    * Maksymalny czas na zadanie: 5 min

:Co zadanie sprawdza?:
    * Czy Python działa
    * Jaka jest wersja Python
    * Czy korzystasz z Virtualenv
    * Korzystanie z print
    * Umiejętność uruchamiania skryptów
    * Szukanie rozwiązań zadań z książki

Handling user input and type casting
------------------------------------
#. Użytkownik wprowadza odległości w metrach
#. Użytkownik wprowadza tylko dane typu ``int`` lub ``float``
#. Do wyświetlania skorzystaj z kodu poniżej
#. Dane przy wyświetlaniu muszą być przekonwertowane do typów podanych w komentarzu
#. W miejsce ``...`` podstaw wyliczone i przekonwertowane zmienne

.. code-block:: python

    print(f'Meters: {...}')                    # int
    print(f'Kilometers: {...}')                # int
    print(f'Miles: {...}')                     # float
    print(f'Nautical Miles: {...}')            # float
    print(f'All: {...}, {...}, {...}, {...}')  # int, int, float, float

:Założenia:
    * Nazwa pliku: ``types_casting.py``
    * Szacunkowa długość kodu: 10 linii
    * Maksymalny czas na zadanie: 5 min

:Co zadanie sprawdza?:
    * Definiowanie zmiennych
    * Korzystanie z print formatting
    * Konwersja typów
    * Operacje matematyczne na zmiennych
    * Wczytywanie tekstu od użytkownika

:Podpowiedź:
    * 1000 m = 1 km
    * 1608 m = 1 mila
    * 1852 m = 1 mila morska

Variables and types
-------------------
#. Wczytaj od użytkownika imię
#. Użytkownik wprowadza tylko dane typu ``str``
#. Za pomocą f-string formatting wyświetl na ekranie:

    .. code-block:: text

        '''My name "José Jiménez".
	        I'm an """astronaut!"""'''

#. Gdzie wartość w podwójnym cudzysłowiu to ciąg od użytkownika (w przykładzie użytkownik wpisał ``José Jiménez``)
#. Zwróć uwagę na znaki apostrofów, cudzysłowów, tabulacji i nowych linii
#. W ciągu do wyświetlenia nie używaj spacji ani enterów - użyj ``\n`` i ``\t``
#. Tekst wyświetlony na ekranie ma mieć zamienione wszystkie spacje na ``_``
#. Nie korzystaj z dodawania stringów ``str + str``
#. Wynik ma wyglądać jak poniżej:

    .. code-block:: text

        '''My_name_"José_Jiménez".
        _I'm_an_"""astronaut!"""'''

:Założenia:
    * Nazwa pliku: ``types_input.py``
    * Szacunkowa długość kodu: 4 linie
    * Maksymalny czas na zadanie: 10 min

:Co zadanie sprawdza?:
    * Definiowanie zmiennych
    * Korzystanie z print formatting
    * Wczytywanie tekstu od użytkownika
