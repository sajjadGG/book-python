.. _Basic Files:

*****
Files
*****


Path
====

Absolute path
-------------
.. highlights::
    * paths on Linux, macOS, BSD and other POSIX compliant OSes uses ``/``
    * paths on Windows uses ``\``

.. code-block:: python
    :caption: Windows and POSIX absolute paths

    FILE = 'C:\\Temp\\iris.csv'
    FILE = r'C:\Temp\iris.csv'

    FILE = '/tmp/iris.csv'
    FILE = r'/tmp/iris.csv'

Relative path
-------------
.. highlights::
    * ``.`` - Current directory
    * ``..`` - Parent directory

.. code-block:: python
    :caption: File in the same directory

    FILE = r'iris.csv'
    FILE = r'./iris.csv'

    FILE = r'tmp/iris.csv'
    FILE = r'./tmp/iris.csv'

    FILE = r'../iris.csv'
    FILE = r'../tmp/iris.csv'

    FILE = r'../../iris.csv'
    FILE = r'../../tmp/iris.csv'

Make absolute from relative path
--------------------------------
.. code-block:: python
    :caption: Make absolute from relative path

    from os.path import dirname, join

    __file__
    # /home/python/my_script.py

    dirname(__file__)
    # /home/python/

    join(dirname(__file__), 'iris.csv')
    # /home/python/iris.csv


Read from file
==============
.. highlights::
    * Works with both relative and absolute path
    * Fails when directory with file cannot be accessed
    * Fails when file cannot be accessed
    * Uses context manager
    * ``mode`` parameter to ``open()`` function is optional (defaults to ``mode='r'``)
    * Reading access modes:

        * ``mode='rt'`` - read in text mode (default)
        * ``mode='rb'`` - read in binary mode
        * ``mode='r'`` - read in text mode

.. code-block:: python
    :caption: Reading file line by line

    FILE = r'/tmp/iris.csv'

    with open(FILE) as file:
        for line in file:
            print(line)

.. code-block:: python
    :caption: Read whole file as a text to ``content`` variable

    FILE = r'/tmp/iris.csv'

    with open(FILE) as file:
        content = file.read()

.. code-block:: python
    :caption: Reading file as ``list`` with lines

    FILE = r'/tmp/iris.csv'

    with open(FILE) as file:
        lines = file.readlines()

.. code-block:: python
    :caption: Read selected (1-30) lines from file

    FILE = r'/tmp/iris.csv'

    with open(FILE) as file:
        lines = file.readlines()[1:30]

.. code-block:: python
    :caption: Read selected (1-30) lines from file

    FILE = r'/tmp/iris.csv'

    with open(FILE) as file:
        for line in file.readlines()[1:30]:
            print(line)

.. code-block:: python
    :caption: Read whole file and split by lines, separate header from content

    FILE = r'/tmp/iris.csv'

    with open(FILE) as file:
        header, *content = file.readlines()

        for line in content:
            print(line)

.. code-block:: python
    :caption: Read header, and use generator to iterate over other lines

    FILE = r'/tmp/iris.csv'

    with open(FILE) as file:
        header = file.readline()

        for line in file:
            print(line)


Writing to file
===============
.. highlights::
    * Works with both relative and absolute path
    * Fails when directory with file cannot be accessed
    * Creates file if not exists
    * Truncate the file before writing
    * ``mode`` parameter to ``open()`` function is required
    * Writing modes:

        * ``mode='wt'`` - write in text mode
        * ``mode='wb'`` - write in binary mode
        * ``mode='w'`` - write in text mode

.. code-block:: python
    :caption: Writing to file

    FILE = r'/tmp/iris.csv'

    with open(FILE, mode='w') as file:
        file.write('hello')


Appending to file
=================
.. highlights::
    * Works with both relative and absolute path
    * Fails when directory with file cannot be accessed
    * Creates file if not exists
    * Append to the end of file
    * ``mode`` parameter to ``open()`` function is required
    * Writing modes:

        * ``mode='at'`` - append in text mode
        * ``mode='ab'`` - append in binary mode
        * ``mode='a'`` - append in text mode

.. code-block:: python
    :caption: Appending to file

    FILE = r'/tmp/iris.csv'

    with open(FILE, mode='a') as file:
        file.write('hello')


Encoding
========
* ``utf-8`` - international standard (should be always used!)
* ``iso-8859-1`` - ISO standard for Western Europe and USA
* ``iso-8859-2`` - ISO standard for Central Europe (including Poland)
* ``cp1250`` or ``windows-1250`` - Polish encoding on Windows
* ``cp1251`` or ``windows-1251`` - Russian encoding on Windows
* ``cp1252`` or ``windows-1252`` - Western European encoding on Windows
* ``ASCII`` - ASCII characters only

.. code-block:: python

    FILE = r'/tmp/example.txt'

    with open(FILE, mode='w', encoding='utf-8') as file:
        file.write('Иван Иванович')

    with open(FILE, encoding='utf-8') as file:
        print(file.read())
    # Иван Иванович

.. code-block:: python

    FILE = r'/tmp/example.txt'

    with open(FILE, mode='w', encoding='cp1250') as file:
        file.write('Иван Иванович')
    # Traceback (most recent call last):
    #   ...
    # UnicodeEncodeError: 'charmap' codec can't encode characters in
    # position 0-3: character maps to <undefined>

.. code-block:: python

    FILE = r'/tmp/example.txt'

    with open(FILE, mode='w', encoding='utf-8') as file:
        file.write('Иван Иванович')

    with open(FILE, encoding='cp1250') as file:
        print(file.read())
    # Traceback (most recent call last):
    #   ...
    # UnicodeDecodeError: 'charmap' codec can't decode byte 0x98 in position 1: character maps to <undefined>


Exception handling
==================
.. code-block:: python
    :caption: Exception handling while accessing files

    FILE = r'/tmp/example.txt'

    try:
        with open(FILE) as file:
            print(file.read())

    except FileNotFoundError:
        print('File does not exist')

    except PermissionError:
        print('Permission denied')


Good Engineering Practises
==========================
.. highlights::
    * Never hardcode paths, always use ``FILE`` or similar
    * ``FILE`` should be constant
    * ``FILE`` as a raw string ``r'...'``
    * ``encoding='utf-8'``
    * Use context manager - ``with`` keyword


Assignments
===========

Example
-------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/file_example.py`

:English:
    #. Using ``input()`` ask user for a file path
    #. Print file content
    #. Handle exception for not existing file
    #. Handle exception for not having sufficient permissions

:Polish:
    #. Używając ``input()`` zapytaj użytkownika o ścieżkę do pliku
    #. Wypisz zawartość pliku
    #. Obsłuż wyjątek dla nieistniejącego pliku
    #. Obsłuż wyjątek dla braku wystarczających uprawnień

:Solution:
    .. literalinclude:: solution/file_example.py
        :language: python

Save to CSV file
----------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/file_write.py`

:English:
    #. Use data from "Input" section (see below)
    #. Separate header from data
    #. Write data to file: ``iris.csv``
    #. First line in file must be a header
    #. Use coma (``,``) as a separator
    #. Use ``utf-8`` encoding and ``\n`` for line terminator

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Odseparuj nagłówek do danych
    #. Zapisz dane do pliku: ``iris.csv``
    #. Pierwsza linią w pliku musi być nagłówkiem
    #. Użyj przecinka (``,``) jako separatora
    #. Użyj kodowania ``utf-8`` i ``\n`` jako koniec linii

:Input:
    .. code-block:: python

        DATA = [
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
            (4.9, 2.5, 4.5, 1.7, 'virginica'),
            (7.1, 3.0, 5.9, 2.1, 'virginica'),
            (4.6, 3.4, 1.4, 0.3, 'setosa'),
            (5.4, 3.9, 1.7, 0.4, 'setosa'),
            (5.7, 2.8, 4.5, 1.3, 'versicolor'),
            (5.0, 3.6, 1.4, 0.3, 'setosa'),
            (5.5, 2.3, 4.0, 1.3, 'versicolor'),
            (6.5, 3.0, 5.8, 2.2, 'virginica'),
            (6.5, 2.8, 4.6, 1.5, 'versicolor'),
            (6.3, 3.3, 6.0, 2.5, 'virginica'),
            (6.9, 3.1, 4.9, 1.5, 'versicolor'),
            (4.6, 3.1, 1.5, 0.2, 'setosa'),
        ]

Parsing simple CSV file
-----------------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min
* Solution: :download:`solution/file_parsing_csv.py`

:English:
    #. Download :download:`data/iris.csv` save as ``iris.csv``
    #. Define:

            * ``features: List[tuple]`` - list of measurements (each row is a tuple)
            * ``labels: List[str]`` - list of species names

    #. Read file and for each line:

        #. Remove whitespaces
        #. Split line by coma ``,``
        #. Append measurements to ``features``
        #. Append species name to ``labels``

    #. Print ``features`` and ``labels``

:Polish:
    #. Ściągnij :download:`data/iris.csv` i zapisz jako ``iris.csv``
    #. Zdefiniuj:

            * ``features: List[tuple]`` - lista pomiarów (każdy wiersz to tuple)
            * ``labels: List[str]`` - lista nazw gatunków

    #. Zaczytaj plik i dla każdej linii:

        #. Usuń białe znaki
        #. Podziel linię po przecinku ``,``
        #. Dodaj pomiary do ``features``
        #. Dodaj gatunek do ``labels``

    #. Wyświetl ``features`` i ``labels``

:The whys and wherefores:
    * Reading file
    * Iterating over lines in file
    * String methods
    * Working with nested sequences

``/etc/hosts`` - parsing to ``dict``
------------------------------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/file_parsing_simple.py`

:English:
    #. Use data from "Input" section (see below)
    #. Using ``file.write()`` save input data from listing below to file ``hosts-simple.txt``
    #. Read file and for each line:

        #. Skip line if contains only whitespaces (``str.isspace()``)
        #. Remove leading and trailing whitespaces
        #. Split line by whitespace
        #. Separate IP address and hosts names
        #. Append IP address and hosts names to ``result``

    #. Merge hostnames for the same IP
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Używając ``file.write()`` zapisz dane wejściowe z listingu poniżej do pliku ``hosts-simple.txt``
    #. Zaczytaj plik i dla każdej lini:

        #. Pomiń linię, jeżeli zawiera tylko białe znaki (``str.isspace()``)
        #. Usuń białe znaki na początku i końcu linii
        #. Podziel linię po białych znakach
        #. Odseparuj adres IP i nazwy hostów
        #. Dodaj adres IP i nazwy hostów do ``result``

    #. Scal nazwy hostów dla tego samego IP
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        DATA = """
        127.0.0.1       localhost
        127.0.0.1       astromatt
        10.13.37.1      nasa.gov esa.int roscosmos.ru
        255.255.255.255 broadcasthost
        ::1 `            localhost
        """

:Output:
    .. code-block:: python

        result: Dict[str, List[str]] = {
            '127.0.0.1': ['localhost', 'astromatt'],
            '10.13.37.1': ['nasa.gov', 'esa.int', 'roscosmos.ru'],
            '255.255.255.255': ['broadcasthost'],
            '::1': ['localhost'],
        }

:The whys and wherefores:
    * Reading file
    * Iterating over lines in file
    * String methods
    * Working with nested sequences

:Hint:
    * ``str.isspace()``
    * ``str.split()``

``/etc/hosts`` - parsing to ``List[dict]``
------------------------------------------
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min
* Solution: :download:`solution/file_parsing_advanced.py`

:English:
    #. Use data from "Input" section (see below)
    #. Using ``file.write()`` save input data from listing below to file ``hosts-advanced.txt``
    #. Read file and for each line:

        #. Skip line if it's empty, is whitespace or starts with comment ``#``
        #. Remove leading and trailing whitespaces
        #. Split line by whitespace
        #. Separate IP address and hosts names
        #. Use one line ``if`` to check whether dot ``.`` is in the IP address
        #. If is present then protocol is IPv4 otherwise IPv6
        #. Append IP address and hosts names to ``result``

    #. Merge hostnames for the same IP
    #. ``result`` must be list of dicts (``List[dict]``)
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Używając ``file.write()`` zapisz dane wejściowe z listingu poniżej do pliku ``hosts-advanced.txt``
    #. Przeczytaj plik i dla każdej lini:

        #. Pomiń linię jeżeli jest pusta, jest białym znakiem lub zaczyna się od komentarza ``#``
        #. Usuń białe znaki na początku i końcu linii
        #. Podziel linię po białych znakach
        #. Odseparuj adres IP i nazwy hostów
        #. Wykorzystaj jednolinikowego ``if`` do sprawdzenia czy jest kropka ``.`` w adresie IP
        #. Jeżeli jest obecna to protokół  jest IPv4, w przeciwnym przypadku IPv6
        #. Dodaj adres IP i nazwy hostów do ``result``

    #. Scal nazwy hostów dla tego samego IP
    #. ``result`` ma być listą dictów (``List[dict]``)
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        DATA = """
        ##
        # ``/etc/hosts`` structure:
        #   - IPv4 or IPv6
        #   - Hostnames
         ##

        127.0.0.1       localhost
        127.0.0.1       astromatt
        10.13.37.1      nasa.gov esa.int roscosmos.ru
        255.255.255.255 broadcasthost
        ::1             localhost
        """

:Output:
    .. code-block:: python

        result: List[Dict[str, Union[str, Set[str]]] = [
            {'ip': '127.0.0.1', 'protocol': 'ipv4', 'hostnames': {'localhost', 'astromatt'}},
            {'ip': '10.13.37.1', 'protocol': 'ipv4', 'hostnames': {'nasa.gov', 'esa.int', 'roscosmos.ru'}},
            {'ip': '255.255.255.255', 'protocol': 'ipv4', 'hostnames': {'broadcasthost'}},
            {'ip': '::1', 'protocol': 'ipv6', 'hostnames': {'localhost'}}
        ]

:The whys and wherefores:
    * czytanie i parsowanie pliku
    * nieregularne pliki konfiguracyjne (struktura może się zmieniać)
    * filtrowanie elementów
    * korzystanie z pętli i instrukcji warunkowych
    * parsowanie stringów
    * praca ze ścieżkami w systemie operacyjnym

:Hints:
    * ``str.split()``
    * ``str.isspace()``
    * ``value = True if ... else False``
