.. _Files:

*****
Files
*****


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

    import os

    BASE_DIR = os.path.dirname(__file__)
    path = os.path.join(BASE_DIR, 'iris.csv')


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
* Complexity level: Easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/file_requested.py`

#. Za pomocą ``input()`` poproś użytkownika o podanie ścieżki do pliku
#. Wyświetl na ekranie zawartość pliku
#. Dopisz obsługę wyjątków dla braku uprawnień oraz tego że plik nie istnieje.

Parsing simple CSV file
-----------------------
* Complexity level: Easy
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/file_parsing_csv.py`
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

``/etc/hosts`` - parsing to ``dict``
------------------------------------
* Complexity level: Easy
* Lines of code to write: 10 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/file_parsing_simple.py`
* Input data: :numref:`listing-file-parsing-simple`

    .. literalinclude:: data/etc-hosts-simple.txt
        :name: listing-file-parsing-simple
        :language: text
        :caption: Zawartość pliku ``hosts.txt``

#. Utwórz plik tekstowy ``hosts.txt``
#. Do pliku skopiuj kod z listingu :numref:`listing-file-parsing-simple`
#. Sparsuj plik i dla każdej linii:

    #. Podziel linię po dowolnej ilości białych znaków (spacja, taby, itp)
    #. Wydziel ip i hosty
    #. Do struktury wynikowej dopisz ip, hostami
    #. Jeżeli IP jest już wpisane to scal listy hostname'ów dla wpisów o tym samym IP

#. Na końcu przedstaw dane w formacie ``Dict[str, List[str]]``:

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


``/etc/hosts`` - parsing to ``List[dict]``
------------------------------------------
* Complexity level: Medium
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/file_parsing_advanced.py`
* Input data: :numref:`listing-file-parsing-advanced`

    .. literalinclude:: data/etc-hosts.txt
        :name: listing-file-parsing-advanced
        :language: text
        :caption: Zawartość pliku ``hosts.txt``

#. Utwórz plik tekstowy ``hosts.txt``
#. Do pliku skopiuj kod z listingu :numref:`listing-file-parsing-advanced`
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
