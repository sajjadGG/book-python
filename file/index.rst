.. _Files:

*****
Files
*****

Read, Write, Append
===================

Access modes
------------
.. csv-table::
    :header-rows: 1
    :widths: 20, 80
    :file: data/file-open-modes.csv

Reading file
------------
* ``FILENAME`` as a constant
* ``FILENAME`` as a raw string ``r'...'``
* ``encoding='utf-8'``

Read whole file as a text to ``content`` variable:

    .. literalinclude:: src/file-read-whole.py
        :language: python
        :caption: Read whole file as a text to ``content`` variable

Convert file to list by line:

    .. literalinclude:: src/file-readlines.py
        :language: python
        :caption: Convert file to list by line

Convert file to list by line, select 1-30 lines:

    .. literalinclude:: src/file-readlines-slice.py
        :language: python
        :caption: Convert file to list by line, select 1-30 lines

By default ``file`` can be iterated by line similar to ``file.readlines()``:

    .. literalinclude:: src/file-iterate-lines.py
        :language: python
        :caption: By default ``file`` can be iterated by line similar to ``file.readlines()``

Writing to file
---------------
* ``FILENAME`` as a constant
* ``FILENAME`` as a raw string ``r'...'``
* ``encoding='utf-8'``

.. literalinclude:: src/file-write.py
    :language: python
    :caption: Writing to file

Appending to file
-----------------
* ``FILENAME`` as a constant
* ``FILENAME`` as a raw string ``r'...'``
* ``encoding='utf-8'``

.. literalinclude:: src/file-append.py
    :language: python
    :caption: Appending to file


Exception handling
==================
.. literalinclude:: src/file-exception.py
    :language: python
    :caption: Exception handling while accessing files


Assignments
===========

Content of a requested file
---------------------------
#. Napisz program, który wyświetli na ekranie zawartość pliku o nazwie podanej przez użytkownika.
#. Dopisz obsługę wyjątków dla braku uprawnień oraz tego że plik nie istnieje.

:About:
    * Filename: ``file_content.py``
    * Lines of code to write: 5 lines
    * Estimated time of completion: 5 min

Parsing ``/etc/hosts``
----------------------
#. Do pliku ``hosts.txt`` w katalogu gdzie będzie Twój skrypt zapisz kod z szablonu: :numref:`listing-file-etc-hosts`
#. Ważne, żeby przepisać zawartość zawierającą komentarze, białe spacje i linie przerwy
#. Przeglądając plik linijka po linijce sparsuj go i przedstaw w formie listy dictów jak w przykładzie poniżej: :numref:`listing-file-hosts`
#. Zwróć uwagę na uprawnienia do odczytu pliku
#. Wykorzystaj inline if do sprawdzenia: jeżeli jest kropka w adresie IP to IPv4 w przeciwnym przypadku IPv6

:About:
    * Filename: ``file_hosts.py``
    * Lines of code to write: 10 lines
    * Estimated time of completion: 20 min

:Algorithm:
    #. Utwórz plik i skopiuj zawartość
    #. Otwórz plik
    #. Dla każdej linii:
    #. Jeżeli linia jest pusta, lub jest białym znakiem lub zaczyna się od komentarza, przeskocz do kolejnej linii
    #. Podziel linię po białych znakach
    #. Wydziel ip i hosty
    #. Jeżeli jest kropka w adresie IP to IPv4 w przeciwnym przypadku IPv6
    #. Do listy dopisz słownik z ip, hostami i protokołem
    #. Po zakończeniu parsowania wyświetl na ekranie

:The whys and wherefores:
    * czytanie i parsowanie pliku
    * nieregularne pliki konfiguracyjne (struktura może się zmieniać)
    * filtrowanie elementów
    * korzystanie z pętli i instrukcji warunkowych
    * parsowanie stringów
    * praca ze ścieżkami w systemie operacyjnym

:Hints:
    * ``str.isspace()``

.. literalinclude:: src/etc-hosts.txt
    :name: listing-file-etc-hosts
    :language: text
    :caption: Przykładowa zawartość pliku ``hosts.txt``

.. literalinclude:: src/file-hosts.py
    :name: listing-file-hosts
    :language: python
    :caption: ``/etc/hosts`` example
