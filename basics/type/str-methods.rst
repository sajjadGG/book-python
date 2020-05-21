.. _Type Str Methods:

****************
Type Str Methods
****************


Rationale
=========
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


Change Case
===========
.. highlights::
    * Unify data format before analysis

.. code-block:: python

    name = 'jAn TwARDowSKi III'

    name.upper()       # 'JAN TWARDOWSKI III'
    name.lower()       # 'jan twardowski iii'
    name.title()       # 'Jan Twardowski Iii'
    name.capitalize()  # 'Jan twardowski iii'

.. code-block:: python

    name = 'Angus MacGyver'

    name.upper()       # 'ANGUS MACGYVER'
    name.lower()       # 'angus macgyver'
    name.title()       # 'Angus Macgyver'
    name.capitalize()  # 'Angus macgyver'


Replace
=======
.. code-block:: python

    name = 'Jan Twardowski Iii'

    name.replace('Iii', 'III')
    # 'Jan Twardowski III'


Strip Whitespace
================
.. code-block:: python

    name = '\tJan Twardowski    \n'

    name.strip()        # 'Jan Twardowski'
    name.rstrip()       # '\tJan Twardowski'
    name.lstrip()       # 'Jan Twardowski    \n'


Starts or Ends With
===================
.. highlights::
    * Understand this as "starts with" and "ends with"

.. code-block:: python

    name = 'Jan Twardowski'

    name.startswith('Jan')  # True
    name.endswith(';')      # False


Split by Line
=============
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


Split by Character
==================
.. highlights::
    * No argument - any number of whitespaces

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


Join
====
.. code-block:: python

    text = ['We', 'choose', 'to', 'go', 'to', 'the', 'Moon']

    ' '.join(text)
    # 'We choose to go to the Moon'

.. code-block:: python

    setosa = [5.1, 3.5, 1.4, 0.2, 'setosa']

    ','.join(setosa)
    # '5.1,3.5,1.4,0.2,setosa'


Is Whitespace
=============
.. code-block:: python

    ''.isspace()        # False
    ' '.isspace()       # True
    '\t'.isspace()      # True
    '\n'.isspace()      # True

.. figure:: img/iss.jpg
    :width: 50%
    :align: center

    ISS - International Space Station.
    Credits: NASA/Crew of STS-132 (img: s132e012208).


Is Alphabet Characters
======================
.. code-block:: python

    'hello'.isalpha()   # True
    'hello1'.isalpha()  # False


Find Sub-String Position
========================
.. code-block:: python

    text = 'We choose to go to the Moon'

    text.find('M')      # 23
    text.find('Moo')    # 23
    text.find('x')      # -1


Contains
========
.. code-block:: python

    'Py' in 'Python'     # True
    'Monty' in 'Python'  # False


Count Occurrences
=================
.. code-block:: python

    text = 'Moon'

    text.count('o')     # 2
    text.count('Moo')   # 1
    text.count('x')     # 0


Remove Prefix or Suffix
=======================
.. versionadded:: Python 3.9
    :pep:`616` New ``str.removeprefix()`` and ``str.removesuffix()`` string methods


Methods Chaining
================
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

Addresses
---------
.. highlights::
    * Is This the Same Address?
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

Streets
-------
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
* Solution: :download:`solution/type_str_methods.py`

:English:
    #. For given text: ``UL. jana \tTWArdoWskIEGO 3``
    #. Use ``str`` methods to clean variable
    #. Expected value is ``Jana Twardowskiego III``

:Polish:
    #. Dla danego tekstu: ``UL. jana \tTWArdoWskIEGO 3``
    #. Wykorzystaj metody ``str`` do oczyszczenia
    #. Oczekiwana wartość ``Jana Twardowskiego III``

:Solution:
    .. literalinclude:: solution/type_str_methods.py
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
* Solution: :download:`solution/type_str_cleaning.py`

:English:
    #. Use data from "Input" section (see below)
    #. Expected value is ``Jana III Sobieskiego``
    #. Use only ``str`` methods to clean each variable
    #. Discuss how to create generic solution which fit all cases
    #. Implementation of such generic function will be in :ref:`Cleaning text input` chapter
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Oczekiwana wartość ``Jana III Sobieskiego``
    #. Wykorzystaj tylko metody ``str`` do oczyszczenia każdej zmiennej
    #. Przeprowadź dyskusję jak zrobić rozwiązanie generyczne pasujące do wszystkich przypadków
    #. Implementacja takiej generycznej funkcji będzie w rozdziale :ref:`Cleaning text input`
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

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

        a = a.replace('ul', '').title().replace('Iii', 'III').strip()
        b = b
        c = c
        d = d
        e = e
        f = f
        g = g
        h = h
        i = i

        expected = 'Jana III Sobieskiego'

        print(f'{a == expected}\ta = "{a}"')
        print(f'{b == expected}\tb = "{b}"')
        print(f'{c == expected}\tc = "{c}"')
        print(f'{d == expected}\td = "{d}"')
        print(f'{e == expected}\te = "{e}"')
        print(f'{f == expected}\tf = "{f}"')
        print(f'{g == expected}\tg = "{g}"')
        print(f'{h == expected}\th = "{h}"')
        print(f'{i == expected}\ti = "{i}"')

:Output:
    .. code-block:: text

        True	a = "Jana III Sobieskiego"
        True	b = "Jana III Sobieskiego"
        True	c = "Jana III Sobieskiego"
        True	d = "Jana III Sobieskiego"
        True	e = "Jana III Sobieskiego"
        True	f = "Jana III Sobieskiego"
        True	g = "Jana III Sobieskiego"
        True	h = "Jana III Sobieskiego"
        True	i = "Jana III Sobieskiego"

:The whys and wherefores:
    * Variable definition
    * Print formatting
    * Cleaning text input
