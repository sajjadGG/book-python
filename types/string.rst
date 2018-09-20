.. _Character Types:

***************
Character Types
***************


``str``
=======
* ``"`` and ``'`` works the same
* Defining ``str``:

    .. code-block:: python

        name = 'José'       # 'José'
        name = "José"       # 'José'

        name: str = 'José'  # 'José'
        name: str = "José"  # 'José'

* ``str`` multiplication:

    .. code-block:: python

        'José' * 3          # JoséJoséJosé

* ``str()`` converts argument to ``str``":

    .. code-block:: python

        str(1969)           # '1969'
        str(13.37)          # '13.37'

* Multiline ``str``

    .. code-block:: python

        names = """
            José Jiménez
            Max Peck
            Иван Иванович
        """
        # '\n    José Jiménez\n    Max Peck\n    Иван Иванович\n'


Single or double quote?
=======================
* ``"`` and ``'`` works the same
* Choose one and keep consistency in code
* Python console uses ``'``, this is why I use ``'`` in this book
* ``doctest`` uses single quotes and throws error on double quotes
* Avoid single quotes, when ``str`` has a lot of contractions:

    .. code-block:: python

        my_str = 'it\'s José\'s book'
        my_str = "it's José's book"

* HTML uses double quotes, hence it's convenient to use single ones for ``str``:

    .. code-block:: python

        my_str = '<a href="http://python.astrotech.io">Python and Machine Learning</a>'

Escape characters
=================
.. code-block:: text

    \n
    \r\n

.. figure:: img/type-machine.jpg
    :scale: 25%
    :align: center

    Why we have '\\r\\n' on Windows?

.. code-block:: text

    \x1F680     # after \x goes hexadecimal number
    \U0001F680  # after \u goes four hexadecimal numbers
    🚀
    \b1010      # after \b goes bytes
    \t
    \'

Characters before strings
=========================
* Format string: since Python 3.6

.. csv-table:: String modifiers
    :header-rows: 1
    :widths: 15, 30, 55
    :file: data/str-modifiers.csv

.. code-block:: python

    name = 'José Jiménez'

    f'My name... {name}'
    u'zażółć gęślą jaźń'
    b'this is text'
    r'(?P<foo>)\n'
    r'C:\Users\Admin\file.txt'

.. code-block:: python

    print('C:\Users\Admin\file.txt')
    # ``\Users`` (``s`` is invalid hexadecimal for unicode)
    # SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape


``print()``
===========
* Prints on the screen
* More in :ref:`Print Formatting`

.. code-block:: python

    print('My name... José Jiménez')  # My name... José Jiménez

    name = 'José Jiménez'
    print(f'My name... {name}')       # My name... José Jiménez


String methods
==============

``title()``, ``lower()``, ``upper()``
-------------------------------------
* Unify data format before analysis
* Is this the same address?:

    .. code-block:: text

        'Jana III Sobieskiego 1/2'
        'ul Jana III Sobieskiego 1/2'
        'ul. Jana III Sobieskiego 1/2'
        'ul.Jana III Sobieskiego 1/2'
        'ulicaJana III Sobieskiego 1/2'
        'Ul. Jana III Sobieskiego 1/2'
        'UL. Jana III Sobieskiego 1/2'
        'ulica Jana III Sobieskiego 1/2'
        'Ulica. Jana III Sobieskiego 1/2'
        'os. Jana III Sobieskiego 1/2'
        'plac Jana III Sobieskiego 1/2'
        'pl Jana III Sobieskiego 1/2'
        'al Jana III Sobieskiego 1/2'
        'al. Jana III Sobieskiego 1/2'
        'aleja Jana III Sobieskiego 1/2'
        'alei Jana III Sobieskiego 1/2'
        'Jana 3 Sobieskiego 1/2'
        'Jana 3ego Sobieskiego 1/2'
        'Jana III Sobieskiego 1 m. 2'
        'Jana III Sobieskiego 1 apt 2'
        'Jana Iii Sobieskiego 1/2'
        'Jana IIi Sobieskiego 1/2'
        'Jana lll Sobieskiego 1/2'  # three small letters 'L'
        'Kozia wólka 5'
        ...

.. code-block:: python

    name = 'joSé jiMénEz III'

    name.title()    # 'José Jiménez Iii'
    name.upper()    # 'JOSÉ JIMÉNEZ III'
    name.lower()    # 'josé jiménez iii'

``replace()``
-------------
.. code-block:: python

    name = 'José Jiménez Iii'
    name.replace('Iii', 'III')  # 'José Jiménez III'

``strip()``, ``lstrip()``, ``rstrip()``
---------------------------------------
.. code-block:: python

    name = '    Max Peck    '

    name.strip()        # 'Max Peck'
    name.lstrip()       # 'Max Peck    '
    name.rstrip()       # '    Max Peck'

``startswith()``
----------------
* Understand this as ``starts_with``

.. code-block:: python

    name = 'José Jiménez'

    if name.startswith('José'):
        print('My name... José Jiménez')
    else:
        print('I have no name')

``split()``
-----------
.. code-block:: python

    text = 'José Jiménez'
    text.split()        # ['José', 'Jiménez']

    text = 'Max,Peck'
    text.split(',')     # ['Max', 'Peck']

``join()``
----------
.. code-block:: python

    names = ['José', 'Max', 'Иван', str(1961), '1969']

    ';'.join(names)
    # 'José;Max;Иван;1961;1969'


String immutability
===================
* ``str`` is immutable
* ``str`` methods create a new modified ``str``
* How many ``str`` are in the memory?
* f-string formatting are preferred over ``str`` addition

    .. code-block:: python

        first_name = 'José'
        last_name = 'Jiménez'

        print(first_name + ' ' + last_name)  # José Jiménez
        print(f'{first_name} {last_name}')   # José Jiménez


Handling user input
===================
* ``input()`` returns ``str``
* Space at the end of prompt

.. code-block:: python

    name = input('Type your name: ')


Assignments
===========

Variables and types
-------------------
#. Wczytaj od użytkownika imię
#. Użytkownik wprowadza tylko dane typu ``str``
#. Za pomocą f-string formatting wyświetl na ekranie:

    .. code-block:: text

        '''My name... "José Jiménez".
	    	I'm an """astronaut!"""'''

#. Druga linijka zaczyna się od tabulacji
#. Gdzie wartość w podwójnym cudzysłowiu to ciąg od użytkownika (w przykładzie użytkownik wpisał ``José Jiménez``)
#. Zwróć uwagę na znaki apostrofów, cudzysłowów, tabulacji i nowych linii
#. W ciągu do wyświetlenia nie używaj spacji ani enterów - użyj ``\n`` i ``\t``
#. Tekst wyświetlony na ekranie ma mieć zamienione wszystkie spacje na ``_``
#. Tekst wyświetlony na ekranie ma być w UPPERCASE
#. Nie korzystaj z dodawania stringów ``str + str``
#. Następnie znów wyświetl na ekranie wynik, tym razem z podmienionymi spacjami:

    .. code-block:: text

        '''MY_NAME_"JOSÉ_JIMÉNEZ".
        _I'M_AN_"""ASTRONAUT!"""'''

:About:
    * Filename: ``types_input.py``
    * Lines of code to write: 4 lines
    * Estimated time of completion: 10 min

:The whys and wherefores:
    * Definiowanie zmiennych
    * Korzystanie z print formatting
    * Wczytywanie tekstu od użytkownika
