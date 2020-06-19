.. _Files Read:

*********
File Read
*********


Rationale
=========
.. highlights::
    * Works with both relative and absolute path
    * Fails when directory with file cannot be accessed
    * Fails when file cannot be accessed
    * Uses context manager
    * ``mode`` parameter to ``open()`` function is optional (defaults to ``mode='rt'``)


Read From File
==============
.. highlights::
    * Always remember to close file

.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    file = open(FILE)
    data = file.read()
    file.close()


Read Using Context Manager
==========================
.. highlights::
    * Context managers use ``with ... as ...:`` syntax
    * It closes file automatically upon block exit (dedent)
    * Using context manager is best practice
    * More information in :ref:`Context Managers`

.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    with open(FILE) as file:
        data = file.read()


Read File at Once
=================
.. highlights::
    * Note, that whole file must fit into memory

.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    with open(FILE) as file:
        data = file.read()


Read File as List of Lines
==========================
.. highlights::
    * Note, that whole file must fit into memory

.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    with open(FILE) as file:
        data = file.readlines()

.. code-block:: python
    :caption: Read selected (1-30) lines from file

    FILE = r'/tmp/myfile.txt'

    with open(FILE) as file:
        lines = file.readlines()[1:30]

.. code-block:: python
    :caption: Read selected (1-30) lines from file

    FILE = r'/tmp/myfile.txt'

    with open(FILE) as file:
        for line in file.readlines()[1:30]:
            print(line)

.. code-block:: python
    :caption: Read whole file and split by lines, separate header from content

    FILE = r'/tmp/myfile.txt'

    with open(FILE) as file:
        header, *content = file.readlines()

        for line in content:
            print(line)


Reading File as Generator
=========================
.. highlights::
    * Use generator to iterate over other lines
    * In those examples, ``file`` is a generator

.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    with open(FILE) as file:
        for line in file:
            print(line)

.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    with open(FILE) as file:
        header = file.readline()

        for line in file:
            print(line)


Assignments
===========

File Read CSV
-------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/file_read_csv.py`

:English:
    #. Download :download:`data/iris.csv` save as ``iris.csv``
    #. Separate header from data
    #. Write header (first line) to ``header: list``
    #. Define:

            * ``features: List[tuple]`` - list of measurements (each row is a tuple)
            * ``labels: List[str]`` - list of species names

    #. Read file and for each line:

        #. Remove whitespaces
        #. Split line by coma ``,``
        #. Append measurements to ``features``
        #. Append species name to ``labels``

    #. Print ``header``, ``features`` and ``labels``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Ściągnij :download:`data/iris.csv` i zapisz jako ``iris.csv``
    #. Odseparuj nagłówek od danych
    #. Zapisz nagłówek (pierwsza linia) do ``header: list``
    #. Zdefiniuj:

            * ``features: List[tuple]`` - lista pomiarów (każdy wiersz to tuple)
            * ``labels: List[str]`` - lista nazw gatunków

    #. Zaczytaj plik i dla każdej linii:

        #. Usuń białe znaki
        #. Podziel linię po przecinku ``,``
        #. Dodaj pomiary do ``features``
        #. Dodaj gatunek do ``labels``

    #. Wyświetl ``header``, ``features`` i ``labels``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: python

        header: List[str]
        # ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

        features: List[tuple]
        # [(5.4, 3.9, 1.3, 0.4), (5.9, 3.0, 5.1, 1.8), (6.0, 3.4, 4.5, 1.6),
        #  (7.3, 2.9, 6.3, 1.8), (5.6, 2.5, 3.9, 1.1), (5.4, 3.9, 1.3, 0.4),
        #  (5.5, 2.6, 4.4, 1.2), (5.7, 2.9, 4.2, 1.3), (4.9, 3.1, 1.5, 0.1), ...]

        labels: list
        # ['setosa', 'virginica', 'versicolor', 'virginica', 'versicolor',
        #  'setosa', 'versicolor', 'versicolor', 'setosa', 'virginica',
        #  'virginica', 'setosa', 'setosa', ...]


:The whys and wherefores:
    * Reading file
    * Iterating over lines in file
    * String methods
    * Working with nested sequences

File Read Parsing Dict
----------------------
* Complexity level: medium
* Lines of code to write: 10 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/file_read_parsing_dict.py`

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
        ::1             localhost
        """

:Output:
    .. code-block:: python

        result: dict
        # {'127.0.0.1': ['localhost', 'astromatt'],
        #  '10.13.37.1': ['nasa.gov', 'esa.int', 'roscosmos.ru'],
        #  '255.255.255.255': ['broadcasthost'],
        #  '::1': ['localhost']}

:The whys and wherefores:
    * Reading file
    * Iterating over lines in file
    * String methods
    * Working with nested sequences

:Hint:
    * ``str.isspace()``
    * ``str.split()``

File Read Parsing List of Dicts
-------------------------------
* Complexity level: hard
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min
* Solution: :download:`solution/file_read_parsing_listdict.py`

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

        result: List[dict]
        # [{'ip': '127.0.0.1', 'protocol': 'ipv4', 'hostnames': {'localhost', 'astromatt'}},
        #  {'ip': '10.13.37.1', 'protocol': 'ipv4', 'hostnames': {'nasa.gov', 'esa.int', 'roscosmos.ru'}},
        #  {'ip': '255.255.255.255', 'protocol': 'ipv4', 'hostnames': {'broadcasthost'}},
        #  {'ip': '::1', 'protocol': 'ipv6', 'hostnames': {'localhost'}}]

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
