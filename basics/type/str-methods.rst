.. _Basic String Methods:

********************
Type ``str`` Methods
********************


String immutability
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


``str`` methods
===============

Changing Character Case
-----------------------
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

Replacing parts of the ``str``
------------------------------
.. code-block:: python

    name = 'Jan Twardowski Iii'

    name.replace('Iii', 'III')
    # 'Jan Twardowski III'

Cleaning ``str`` from whitespaces
---------------------------------
.. code-block:: python

    name = '\tJan Twardowski    \n'

    name.strip()        # 'Jan Twardowski'
    name.rstrip()       # '\tJan Twardowski'
    name.lstrip()       # 'Jan Twardowski    \n'

Checking if ``str`` starts or ends with value
---------------------------------------------
.. highlights::
    * Understand this as "starts with" and "ends with"

.. code-block:: python

    name = 'Jan Twardowski'

    name.startswith('Jan')  # True
    name.endswith(';')      # False

Splitting by character or whitespace
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

Splitting by line
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

Joining ``str``
---------------
.. code-block:: python

    text = ['We', 'choose', 'to', 'go', 'to', 'the', 'Moon']

    ' '.join(text)
    # 'We choose to go to the Moon'

.. code-block:: python

    setosa = [5.1, 3.5, 1.4, 0.2, 'setosa']

    ','.join(setosa)
    # '5.1,3.5,1.4,0.2,setosa'

Checking if ``str`` contains only whitespace
--------------------------------------------
.. code-block:: python

    ''.isspace()        # False
    ' '.isspace()       # True
    '\t'.isspace()      # True
    '\n'.isspace()      # True

Checking if ``str`` contains only alphabet characters
-----------------------------------------------------
.. code-block:: python

    'hello'.isalpha()   # True
    'hello1'.isalpha()  # False

Finding starting position of a sub-string
-----------------------------------------
.. code-block:: python

    text = 'We choose to go to the Moon'

    text.find('M')      # 23
    text.find('Moo')    # 23
    text.find('x')      # -1

Check if ``str`` is a part of another ``str``
---------------------------------------------
.. code-block:: python

    'Py' in 'Python'     # True
    'Monty' in 'Python'  # False

Counting occurrences
--------------------
.. code-block:: python

    text = 'Moon'

    text.count('o')     # 2
    text.count('Moo')   # 1
    text.count('x')     # 0


Multiple statements in one line
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


Cleaning ``str`` from user input
================================
.. highlights::
    * 80% of machine learning and data science is cleaning data

Is this the same address?
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

Different way of spelling and abbreviating
------------------------------------------
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

House number and apartment
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

Phone numbers
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

String cleaning
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
    #. Dla danych wejściowych (patrz poniżej)
    #. Oczekiwana wartość ``Jana III Sobieskiego``
    #. Wykorzystaj tylko metody ``str`` do oczyszczenia każdej zmiennej
    #. Porównaj wyniki z danymi wyjściowymi (patrz poniżej)
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

        print(f'{a == expected}\t a: "{a}"')
        print(f'{b == expected}\t b: "{b}"')
        print(f'{c == expected}\t c: "{c}"')
        print(f'{d == expected}\t d: "{d}"')
        print(f'{e == expected}\t e: "{e}"')
        print(f'{f == expected}\t f: "{f}"')
        print(f'{g == expected}\t g: "{g}"')
        print(f'{h == expected}\t h: "{h}"')
        print(f'{i == expected}\t i: "{i}"')

:The whys and wherefores:
    * Variable definition
    * Print formatting
    * Cleaning text input
