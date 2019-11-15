.. _Control Flow Files:

******************
Control Flow Files
******************


Path
====

Absolute path
-------------
* ``FILE`` as constant (never hardcode paths)
* ``FILE`` as a raw string ``r'...'``

.. code-block:: python
    :caption: Windows paths

    FILE = 'C:\\Temp\\iris.csv'
    FILE = r'C:\Temp\iris.csv'

.. code-block:: python
    :caption: Linux, macOS, BSD

    FILE = '/tmp/iris.csv'
    FILE = r'/tmp/iris.csv'

Relative path
-------------
* ``FILE`` as constant (never hardcode paths)
* ``FILE`` as a raw string ``r'...'``

.. code-block:: python
    :caption: File in the same directory directory

    FILE = r'iris.csv'

.. code-block:: python
    :caption: File in parent directory

    FILE = r'../iris.csv'
    FILE = r'../data/iris.csv'

.. code-block:: python
    :caption: File in the same directory as script

    from os.path import dirname, join

    FILE = join(dirname(__file__), 'iris.csv')


Read from file
==============
* Works with both relative and absolute path
* Fails when directory with file cannot be accessed
* Fails when file cannot be accessed
* Uses context manager
* ``mode`` parameter to ``open()`` function is optional (defaults to ``mode='r'``)
* Reading access modes:

    * ``mode='r'`` - write in text mode (default)
    * ``mode='rt'`` - write in text mode
    * ``mode='rb'`` - write in binary mode

Reading file line by line
-------------------------
.. code-block:: python
    :caption: ``file`` can be iterated line by line

    with open(r'/tmp/iris.csv') as file:
        for line in file:
            print(line)

Reading whole file content
--------------------------
.. code-block:: python
    :caption: Read whole file as a text to ``content`` variable

    with open(r'/tmp/iris.csv') as file:
        content = file.read()

Reading file as ``list`` with lines
-----------------------------------
.. code-block:: python
    :caption: Convert file to list by line

    with open(r'/tmp/iris.csv') as file:
        lines = file.readlines()

Read selected lines from file
-----------------------------
.. code-block:: python
    :caption: Convert file to list by line, select 1-30 lines

    with open(r'/tmp/iris.csv') as file:
        lines = file.readlines()[1:30]

.. code-block:: python
    :caption: Convert file to list by line, select 1-30 lines

    with open(r'/tmp/iris.csv') as file:
        for line in file.readlines()[1:30]:
            print(line)


Writing
=======

Writing to file
---------------
* Works with both relative and absolute path
* Fails when directory with file cannot be accessed
* Creates file if not exists
* Truncate the file before writing
* ``mode`` parameter to ``open()`` function is required
* Writing modes:

    * ``mode='w'`` - write in text mode
    * ``mode='wt'`` - write in text mode
    * ``mode='wb'`` - write in binary mode

.. code-block:: python
    :caption: Writing to file

    with open(r'/tmp/iris.csv', mode='w') as file:
        file.write('hello')

Appending to file
-----------------
* Works with both relative and absolute path
* Fails when directory with file cannot be accessed
* Creates file if not exists
* Append to the end of file
* ``mode`` parameter to ``open()`` function is required
* Writing modes:

    * ``mode='a'`` - append in text mode
    * ``mode='at'`` - append in text mode
    * ``mode='ab'`` - append in binary mode

.. code-block:: python
    :caption: Appending to file

    with open(r'/tmp/iris.csv', mode='a') as file:
        file.write('hello')


Exception handling
==================
.. code-block:: python
    :caption: Exception handling while accessing files

    try:
        with open(r'/tmp/iris.csv') as file:
            for line in file:
                print(line)

    except FileNotFoundError:
        print('File does not exist')

    except PermissionError:
        print('Permission denied')


Good Engineering Practises
==========================
* ``FILE`` as a raw string ``r'...'`` constant
* ``encoding='utf-8'``
* Use context manager - ``with`` keyword


Assignments
===========

Content of a requested file
---------------------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/file_requested.py`

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

Parsing simple CSV file
-----------------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/file_parsing_csv.py`

:English:
    #. Download :download:`data/iris.csv` save as ``iris.csv``
    #. Define:

            * ``features`` - list of measurements (each row is a tuple)
            * ``labels`` - list of species names

    #. For each line in file:

        #. Remove whitespaces
        #. Split line by coma ``,``
        #. Append measurements to ``features``
        #. Append species name to ``labels``

    #. Print ``features`` and ``labels``

:Polish:
    #. Ściągnij :download:`data/iris.csv` i zapisz jako ``iris.csv``
    #. Zdefiniuj:

            - ``features`` - lista pomiarów (każdy wiersz to tuple)
            - ``labels`` - lista nazw gatunków

    #. Dla każdej linii:

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
* Filename: :download:`solution/file_parsing_simple.py`

:English:
    #. Copy input data from listing below and save to file ``hosts.txt``
    #. For each line in file:

        #. Remove leading and trailing whitespaces
        #. Split line by whitespace
        #. Separate IP address and hosts names
        #. Append IP address and hosts names to ``OUTPUT``

    #. Merge hostnames for the same IP

:Polish:
    #. Skopiuj dane wejściowe z listingu poniżej i zapisz do pliku ``hosts.txt``
    #. Dla każdej lini w piku:

        #. Usuń białe znaki na początku i końcu linii
        #. Podziel linię po białych znakach
        #. Odseparuj adres IP i nazwy hostów
        #. Dodaj adres IP i nazwy hostów do ``OUTPUT``

    #. Scal nazwy hostów dla tego samego IP

:Input:
    .. code-block:: text

        127.0.0.1       localhost
        127.0.0.1       astromatt
        10.13.37.1      nasa.gov esa.int roscosmos.ru
        255.255.255.255 broadcasthost
        ::1             localhost

:Output:
    .. code-block:: python

        OUTPUT: Dict[str, List[str]] = {
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

``/etc/hosts`` - parsing to ``List[dict]``
------------------------------------------
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/file_parsing_advanced.py`

:English:
    #. Copy input data from listing below and save to file ``hosts.txt``
    #. Copy also comments and empty lines
    #. For each line in file:

        #. Skup line if it's empty, is whitespace or starts with comment ``#``
        #. Remove leading and trailing whitespaces
        #. Split line by whitespace
        #. Separate IP address and hosts names
        #. Use one line ``if`` to check whether dot ``.`` is in the IP address
        #. If is present then protocol is IPv4 otherwise IPv6
        #. Append IP address and hosts names to ``OUTPUT``

    #. Merge hostnames for the same IP
    #. ``OUTPUT`` must be list of dicts (``List[dict]``)

:Polish:
    #. Skopiuj dane wejściowe z listingu poniżej i zapisz do pliku ``hosts.txt``
    #. Skopiuj również komentarz i pustą linię
    #. Dla każdej lini w piku:

        #. Pomiń linię jeżeli jest pusta, jest białym znakiem lub zaczyna się od komentarza ``#``
        #. Usuń białe znaki na początku i końcu linii
        #. Podziel linię po białych znakach
        #. Odseparuj adres IP i nazwy hostów
        #. Wykorzystaj jednolinikowego ``if`` do sprawdzenia czy jest kropka ``.`` w adresie IP
        #. Jeżeli jest obecna to protokół  jest IPv4, w przeciwnym przypadku IPv6
        #. Dodaj adres IP i nazwy hostów do ``OUTPUT``

    #. Scal nazwy hostów dla tego samego IP
    #. ``OUTPUT`` ma być listą dictów (``List[dict]``)

:Input:
    .. code-block:: text

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

:Output:
    .. code-block:: python

        OUTPUT: List[Dict[str, Union[str, Set[str]]] = [
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
    * ``str.isspace()``
    * ``value = True if ... else False``
