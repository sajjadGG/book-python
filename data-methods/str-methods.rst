***************
``str`` Methods
***************


String immutability
===================
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


String Arithmetic
=================
* Preferred string concatenation is using ``f-string`` formatting

.. code-block:: python

    first_name = 'Jan'
    last_name = 'Twardowski'

    name = first_name + ' ' + last_name
    # Jan Twardowski

.. code-block:: python

    'José' * 3          # JoséJoséJosé
    '-' * 10            # ----------


``str`` methods
===============

Changing Character Case
-----------------------
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
* Understand this as "starts with" and "ends with"

.. code-block:: python

    name = 'Jan Twardowski'

    name.startswith('Jan')  # True
    name.endswith(';')      # False

Splitting by whitespace
-----------------------
.. code-block:: python

    setosa = '5.1,3.5,1.4,0.2,setosa'

    setosa.split(',')
    # ['5.1', '3.5', '1.4', '0.2', 'setosa']

.. code-block:: python

    text = 'We choose to go to the Moon'

    text.split()
    # ['We', 'choose', 'to', 'go', 'to', 'the', 'Moon']

    text.split(' ')
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
    text.find('x')      # -1

Check if ``str`` is a part of another ``str``
---------------------------------------------
.. code-block:: python

    'th' in 'Python'     # True
    'hello' in 'Python'  # False

Counting occurrences
--------------------
.. code-block:: python

    text = 'Moon'

    text.count('o')     # 2
    text.count('Moo')   # 1


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
* 80% of machine learning and data science is cleaning data

Is this the same address?
-------------------------
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

    123 555 678

    +48 (12) 355 5678
    +48 12 355 5678
    +48 123 555 678

    +48 123-555-678
    +48123555678
    +48 123 555 6789

    +1 (123) 555-6789
    +1 (123).555.6789

    +1 800-python

    +48 123 555 678 wew. 1337


Assignments
===========

String cleaning
---------------
* Filename: ``data-methods/str_cleaning.py``
* Lines of code to write: 11 lines
* Estimated time of completion: 15 min

.. code-block:: python

    expected = 'Jana III Sobieskiego'

    a = '  Jana III Sobieskiego '
    b = 'ul Jana III SobIESkiego'
    c = '\tul. Jana trzeciego Sobieskiego'
    d = 'ulicaJana III Sobieskiego'
    e = 'UL. JA\tNA 3 SOBIES\tKIEGO'
    f = 'UL. jana III SOBiesKIEGO'
    g = 'ULICA JANA III SOBIESKIEGO  '
    h = 'ULICA. JANA III SOBIeskieGO'
    i = ' Jana 3 Sobieskiego  '
    j = 'Jana III Sobi\teskiego '
    k = 'ul.Jana III Sob\n\nieskiego\n'

    print(f'{a == expected}\t a: "{a}"')
    print(f'{b == expected}\t b: "{b}"')
    print(f'{c == expected}\t c: "{c}"')
    print(f'{d == expected}\t d: "{d}"')
    print(f'{e == expected}\t e: "{e}"')
    print(f'{f == expected}\t f: "{f}"')
    print(f'{g == expected}\t g: "{g}"')
    print(f'{h == expected}\t h: "{h}"')
    print(f'{i == expected}\t i: "{i}"')
    print(f'{j == expected}\t j: "{j}"')
    print(f'{k == expected}\t k: "{k}"')

#. Wykorzystując metody ``str``
#. Dane przeczyść, tak aby zmienne miały wartość ``Jana III Sobieskiego``
#. Nie wykorzystuj mechanizmu ``slice``
#. Przeprowadź dyskusję jak zrobić rozwiązanie generyczne pasujące do wszystkich? (Implementacja rozwiązania będzie w rozdziale :ref:`Function Basics`)

:The whys and wherefores:
    * Definiowanie zmiennych
    * Korzystanie z print formatting
    * Wczytywanie tekstu od użytkownika
