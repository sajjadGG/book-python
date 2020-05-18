.. _Basic Files Read:

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


Read from file
==============
* Always remember to close file

.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    file = open(FILE)
    data = file.read()
    file.close()


Read using context manager
==========================
* Context managers use ``with ... as ...:`` syntax
* It closes file automatically upon block exit (dedent)
* More about context managers in :ref:`Context Managers`
* Using context manager is best practice

.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    with open(FILE) as file:
        data = file.read()


Read file at once
=================
* Note, that whole file must fit into memory

.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    with open(FILE) as file:
        data = file.read()


Read file as list of lines
==========================
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


Reading file as generator
=========================
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

Parsing simple CSV file
-----------------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min
* Solution: :download:`solution/file_read.py`

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
* Estimated time of completion: 15 min
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
