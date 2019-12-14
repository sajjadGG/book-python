.. _Basic String Methods:

********************
Type ``str`` Methods
********************


String Immutability
===================
.. highlights::
    * ``str`` is immutable
    * ``str`` methods create a new modified ``str``

.. code-block:: python

    a = 'Python'
    a.replace('P', 'J')

    print(a)  # Python

.. code-block:: python

    a = 'Python'
    b = a.replace('P', 'J')

    print(a)  # Python
    print(b)  # Jython

.. code-block:: python

    a = 'Python'
    a = a.replace('P', 'J')

    print(a)  # Jython


String Arithmetic
=================
.. highlights::
    * Preferred string concatenation is using ``f-string`` formatting

.. code-block:: python

    first_name = 'Jan'
    last_name = 'Twardowski'

    name = first_name + ' ' + last_name
    # Jan Twardowski

.. code-block:: python

    'Ha' * 3            # HaHaHa
    '-' * 10            # ----------

.. code-block:: python
    :caption: How many string are there in a memory?

    first_name = 'Jan'
    last_name = 'Twardowski'
    age = 42

    # How many string are there in a memory?
    'Hello ' + first_name + ' ' + last_name + ' ' + str(age) + '!'

    # How many string are there in a memory?
    f'Hello {first_name} {last_name} {age}!'


String Methods
==============

Change Case
-----------
.. highlights::
    * Unify data format before analysis

.. code-block:: python

    name = 'jAn TwARDowSKi III'

    name.upper()       # 'JAN TWARDOWSKI III'
    name.lower()       # 'jan twardowski iii'
    name.title()       # 'Jan Twardowski Iii'
    name.capitalize()  # 'Jan twardowski iii'

.. code-block:: python

    name = 'Angus McGyver'

    name.upper()       # 'ANGUS MCGYVER'
    name.lower()       # 'angus mcgyver'
    name.title()       # 'Angus Mcgyver'
    name.capitalize()  # 'Angus mcgyver'

Replace
-------
.. code-block:: python

    name = 'Jan Twardowski Iii'

    name.replace('Iii', 'III')
    # 'Jan Twardowski III'

Strip Whitespace
----------------
.. code-block:: python

    name = '\tJan Twardowski    \n'

    name.strip()        # 'Jan Twardowski'
    name.rstrip()       # '\tJan Twardowski'
    name.lstrip()       # 'Jan Twardowski    \n'

Checking If Starts or Ends with Value
-------------------------------------
.. highlights::
    * Understand this as "starts with" and "ends with"

.. code-block:: python

    name = 'Jan Twardowski'

    name.startswith('Jan')  # True
    name.endswith(';')      # False

Splitting by Line
-----------------
.. code-block:: python

    DATA = """First Line
    Second Line
    Third Line
    """

    DATA.splitlines()
    # [
    #   'First Line',
    #   'Second Line',
    #   'Third Line'
    # ]

Splitting by Character or Whitespace
------------------------------------
.. code-block:: python

    setosa = '5.1,3.5,1.4,0.2,setosa'

    setosa.split(',')
    # ['5.1', '3.5', '1.4', '0.2', 'setosa']

.. code-block:: python

    text = 'We choose to go to the Moon'

    text.split(' ')
    # ['We', 'choose', 'to', 'go', 'to', 'the', 'Moon']

    text.split()
    # ['We', 'choose', 'to', 'go', 'to', 'the', 'Moon']

.. code-block:: python

    text = '10.13.37.1      nasa.gov esa.int roscosmos.ru'

    text.split(' ')
    # ['10.13.37.1', '', '', '', '', '', 'nasa.gov', 'esa.int', 'roscosmos.ru']

    text.split()
    # ['10.13.37.1', 'nasa.gov', 'esa.int', 'roscosmos.ru']

Joining with String
-------------------
.. code-block:: python

    text = ['We', 'choose', 'to', 'go', 'to', 'the', 'Moon']

    ' '.join(text)
    # 'We choose to go to the Moon'

.. code-block:: python

    setosa = [5.1, 3.5, 1.4, 0.2, 'setosa']

    ','.join(setosa)
    # '5.1,3.5,1.4,0.2,setosa'

Checking If Contains Only Whitespace
------------------------------------
.. code-block:: python

    ''.isspace()        # False
    ' '.isspace()       # True
    '\t'.isspace()      # True
    '\n'.isspace()      # True

Checking If Contains Only Alphabet Characters
---------------------------------------------
.. code-block:: python

    'hello'.isalpha()   # True
    'hello1'.isalpha()  # False

Finding Starting Position of a Sub-string
-----------------------------------------
.. code-block:: python

    text = 'We choose to go to the Moon'

    text.find('M')      # 23
    text.find('Moo')    # 23
    text.find('x')      # -1

Check If is a Part of Another String
------------------------------------
.. code-block:: python

    'Py' in 'Python'     # True
    'Monty' in 'Python'  # False

Counting Occurrences
--------------------
.. code-block:: python

    text = 'Moon'

    text.count('o')     # 2
    text.count('Moo')   # 1
    text.count('x')     # 0


Multiple Statements in One Line
===============================
.. code-block:: python

    a = 'Python'
    b = a.upper().replace('P', 'C').title()

    print(a)            # Python
    print(b)            # Cython

.. code-block:: python

    a = 'Python'

    b = a.upper().startswith('P').replace('P', 'C')
    # AttributeError: 'bool' object has no attribute 'replace'


Cleaning User Input
===================
.. highlights::
    * 80% of machine learning and data science is cleaning data

Is This the Same Address?
-------------------------
.. highlights::
    * This is a dump of distinct records of a single address
    * Which one of the below is a true address?

.. code-block:: text

    'ul. Jana III Sobieskiego'
    'ul Jana III Sobieskiego'
    'ul.Jana III Sobieskiego'
    'ulicaJana III Sobieskiego'
    'Ul. Jana III Sobieskiego'
    'UL. Jana III Sobieskiego'
    'ulica Jana III Sobieskiego'
    'Ulica. Jana III Sobieskiego'

    'os. Jana III Sobieskiego'

    'Jana 3 Sobieskiego'
    'Jana 3ego Sobieskiego'
    'Jana III Sobieskiego'
    'Jana Iii Sobieskiego'
    'Jana IIi Sobieskiego'
    'Jana lll Sobieskiego'  # three small letters 'L'

Spelling and Abbreviations
--------------------------
.. code-block:: text

    'ul'
    'ul.'
    'Ul.'
    'UL.'
    'ulica'
    'Ulica'

.. code-block:: text

    'os'
    'os.'
    'Os.'
    'osiedle'

    'oś'
    'oś.'
    'Oś.'
    'ośedle'

.. code-block:: text

    'pl'
    'pl.'
    'Pl.'
    'plac'

.. code-block:: text

    'al'
    'al.'
    'Al.'

    'aleja'
    'aleia'
    'alei'
    'aleii'
    'aleji'

House and Apartment Number
--------------------------
.. code-block:: text

    '1/2'
    '1 / 2'
    '1/ 2'
    '1 /2'
    '3/5/7'

.. code-block:: text

    '1 m. 2'
    '1 m 2'
    '1 apt 2'
    '1 apt. 2'

.. code-block:: text

    '180f/8f'
    '180f/8'
    '180/8f'

.. code-block:: text

    '13d bud. A'

Phone Numbers
-------------
.. code-block:: text

    +48 (12) 355 5678
    +48 123 555 678

.. code-block:: text

    123 555 678

    +48 12 355 5678
    +48 123-555-678
    +48 123 555 6789

    +1 (123) 555-6789
    +1 (123).555.6789

    +1 800-python
    +48123555678

    +48 123 555 678 wew. 1337
    +48 123555678,1
    +48 123555678,1,2,3


Assignments
===========

Example
-------
* Complexity level: easy
* Lines of code to write: 8 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/str_methods.py`

:English:
    #. For given text: ``UL. jana \tTWArdoWskIEGO 3``
    #. Use ``str`` methods to clean variable
    #. Expected value is ``Jana Twardowskiego III``

:Polish:
    #. Dla danego tekstu: ``UL. jana \tTWArdoWskIEGO 3``
    #. Wykorzystaj metody ``str`` do oczyszczenia
    #. Oczekiwana wartość ``Jana Twardowskiego III``

:Solution:
    .. literalinclude:: solution/str_methods.py
        :language: python

:The whys and wherefores:
    * Variable definition
    * Print formatting
    * Cleaning text input

String Cleaning
---------------
* Complexity level: easy
* Lines of code to write: 11 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/str_cleaning.py`

:English:
    #. For input data (see below)
    #. Expected value is ``Jana III Sobieskiego``
    #. Use only ``str`` methods to clean each variable
    #. Compare with output data (see below)
    #. Discuss how to create generic solution which fit all cases
    #. Implementation of such generic function will be in :ref:`Function Basics` chapter

:Polish:
    #. Dla danych wejściowych (patrz sekcja input)
    #. Oczekiwana wartość ``Jana III Sobieskiego``
    #. Wykorzystaj tylko metody ``str`` do oczyszczenia każdej zmiennej
    #. Porównaj wyniki z danymi wyjściowymi (patrz sekcja output)
    #. Przeprowadź dyskusję jak zrobić rozwiązanie generyczne pasujące do wszystkich przypadków
    #. Implementacja takiej generycznej funkcji będzie w rozdziale :ref:`Function Basics`

:Input:
    .. code-block:: python

        a = 'ul Jana III SobIESkiego'
        b = '\tul. Jana trzeciego Sobieskiego'
        c = 'ulicaJana III Sobieskiego'
        d = 'UL. JANA 3 \nSOBIESKIEGO'
        e = 'UL. jana III SOBiesKIEGO'
        f = 'ULICA JANA III SOBIESKIEGO  '
        g = 'ULICA. JANA III SOBIeskieGO'
        h = ' Jana 3 Sobieskiego  '
        i = 'Jana III Sobi\teskiego '

:Output:
    .. code-block:: python

        expected = 'Jana III Sobieskiego'

        print('a:', a == expected, a, sep='\t')
        print('b:', b == expected, b, sep='\t')
        print('c:', c == expected, c, sep='\t')
        print('d:', d == expected, d, sep='\t')
        print('e:', e == expected, e, sep='\t')
        print('f:', f == expected, f, sep='\t')
        print('g:', g == expected, g, sep='\t')
        print('h:', h == expected, h, sep='\t')
        print('i:', i == expected, i, sep='\t')

:The whys and wherefores:
    * Variable definition
    * Print formatting
    * Cleaning text input
