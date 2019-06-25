.. _Files:

*****
Files
*****


Path
====

Absolute path
-------------
* Windows:

    .. code-block:: python

        FILE = r'C:\Temp\iris.csv'

* Linux, macOS, BSD

    .. code-block:: python

        FILE = r'/tmp/iris.csv'

Relative path
-------------
* File in the same directory directory

    .. code-block:: python

        FILE = r'iris.csv'

* File in parent directory

    .. code-block:: python

        FILE = r'../data/iris.csv'


Access modes
============
.. csv-table::
    :widths: 20, 80
    :header: "Character", "Meaning"

    "``'r'``", "open for reading (default)"
    "``'w'``", "open for writing, truncating the file first"
    "``'a'``", "open for writing, appending to the end of the file if it exists"
    "``'rb'``", "read binary mode"
    "``'wb'``", "write binary mode"
    "``'ab'``", "append binary mode"


Read from file
==============
* Works with both relative and absolute path
* Uses context manager

Reading file line by line
-------------------------
* Fails when directory with file cannot be accessed
* Fails when file cannot be accessed

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
* Fails when directory with file cannot be accessed
* Creates file if not exists
* Overwrite old content

.. code-block:: python
    :caption: Writing to file

    with open(r'/tmp/iris.csv', mode='w') as file:
        file.write('hello')

Appending to file
-----------------
* Fails when directory with file cannot be accessed
* Creates file if not exists
* Append to the end of file

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
* Use context manager


Assignments
===========

Content of a requested file
---------------------------
* Filename: ``file_content.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min

#. Napisz program, który wyświetli na ekranie zawartość pliku o nazwie podanej przez użytkownika.
#. Dopisz obsługę wyjątków dla braku uprawnień oraz tego że plik nie istnieje.

:Hints:
    * ``input()``

Parsing simple CSV file
-----------------------
* Filename: ``file_iris.py``
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min
* Input data: http://raw.githubusercontent.com/AstroMatt/book-python/master/control-flow/data/iris.csv

#. Skopiuj plik do siebie na dysk i nazwij go ``iris.csv``
#. Dla każdej linii:

    #. Oczyść linię z białych znaków
    #. Podziel linię po przecinku
    #. Zapisz rekordy do:

        - ``X: List[Tuple[float]]`` - features
        - ``y: List[str]`` - labels

:The whys and wherefores:
    * czytanie i parsowanie pliku
    * nieregularne pliki konfiguracyjne (struktura może się zmieniać)
    * filtrowanie elementów
    * korzystanie z pętli i instrukcji warunkowych
    * parsowanie stringów
    * praca ze ścieżkami w systemie operacyjnym


Parsing ``/etc/hosts`` - simple
-------------------------------
* Filename: ``file_hosts_simple.py``
* Lines of code to write: 10 lines
* Estimated time of completion: 10 min
* Input data: :numref:`listing-etc-hosts-simple`

    .. literalinclude:: data/etc-hosts-simple.txt
        :name: listing-etc-hosts-simple
        :language: text
        :caption: Zawartość pliku ``hosts.txt``

#. Utwórz plik tekstowy ``hosts.txt``
#. Do pliku skopiuj kod z listingu :numref:`listing-etc-hosts`
#. Sparsuj plik i dla każdej linii:

    #. Podziel linię po dowolnej ilości białych znaków (spacja, taby, itp)
    #. Wydziel ip i hosty
    #. Do struktury wynikowej dopisz ip, hostami
    #. Jeżeli IP jest już wpisane to scal listy hostname'ów dla wpisów o tym samym IP

#. Na końcu przedstaw dane w formacie:

    * Wersja prosta ``Dict[str, List[str]]``:

        .. code-block:: python

            {
                '127.0.0.1': ['localhost', 'astromatt'],
                '10.13.37.1': ['nasa.gov', 'esa.int', 'roscosmos.ru'],
                '255.255.255.255': ['broadcasthost'],
                '::1': ['localhost'],
            }

:The whys and wherefores:
    * czytanie i parsowanie pliku
    * nieregularne pliki konfiguracyjne (struktura może się zmieniać)
    * filtrowanie elementów
    * korzystanie z pętli i instrukcji warunkowych
    * parsowanie stringów
    * praca ze ścieżkami w systemie operacyjnym


Parsing ``/etc/hosts``
----------------------
* Filename: ``file_hosts.py``
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min
* Input data: :numref:`listing-etc-hosts`

    .. literalinclude:: data/etc-hosts.txt
        :name: listing-etc-hosts
        :language: text
        :caption: Zawartość pliku ``hosts.txt``

#. Utwórz plik tekstowy ``hosts.txt``
#. Do pliku skopiuj kod z listingu :numref:`listing-etc-hosts`
#. Ważne, żeby przepisać zawartość zawierającą komentarze, białe spacje i linie przerwy
#. Sparsuj plik i dla każdej linii:

    #. Pomiń linię jeżeli jest pusta, jest białym znakiem lub zaczyna się od komentarza
    #. Podziel linię po dowolnej ilości białych znaków (spacja, taby, itp)
    #. Wydziel ip i hosty
    #. Wykorzystaj jednolinikowego ``if`` do sprawdzenia czy jest kropka w adresie IP (to IPv4) w przeciwnym przypadku IPv6
    #. Do listy wynikowej dopisz słownik z ip, hostami i protokołem
    #. Jeżeli IP jest już wpisane do naszej listy wynikowej to scal listy hostname'ów dla wpisów o tym samym IP

#. Na końcu przedstaw dane w formacie ``List[Dict[str, Union[str, Set[str]]]``:

    .. code-block:: python
        :caption: ``/etc/hosts`` example

        [
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
