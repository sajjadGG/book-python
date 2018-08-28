.. _Files:

*****
Files
*****


Czytanie
========
* Context manager ``with``

.. literalinclude:: src/file-read.py
    :language: python
    :caption: Reading from file


Zapis
=====
.. literalinclude:: src/file-write.py
    :language: python
    :caption: Writing to file


Tryby odczytu i zapisu
======================
.. csv-table::
    :header: "Character", "Meaning"
    :widths: 20, 80
    :file: data/open-modes.csv


Obsługa wyjątków
================
.. literalinclude:: src/file-exception.py
    :language: python
    :caption: Exception handling while accessing files


Assignments
===========

Zawartość zadanego pliku
------------------------
#. Napisz program, który wyświetli na ekranie zawartość pliku o nazwie podanej przez użytkownika.
#. Dopisz obsługę wyjątków dla braku uprawnień oraz tego że plik nie istnieje.

:About:
    * Filename: ``file_content.py``
    * Lines of code to write: 5 lines
    * Estimated time of completion: 5 min

Parsowanie ``/etc/hosts``
-------------------------
#. Do pliku ``hosts.txt`` w katalogu gdzie będzie Twój skrypt zapisz kod z szablonu: :numref:`listing-file-etc-hosts`
#. Ważne są komentarze, białe spacje i linie przerwy
#. Przedstaw go w formie listy dictów jak w przykładzie poniżej: :numref:`listing-file-hosts`
#. Zwróć uwagę na uprawnienia do odczytu pliku

:About:
    * Filename: ``file_hosts.py``
    * Lines of code to write: 10 lines
    * Estimated time of completion: 20 min

:The whys and wherefores:
    * czytanie i parsowanie pliku
    * nieregularne pliki konfiguracyjne (struktura może się zmieniać)
    * filtrowanie elementów
    * korzystanie z pętli i instrukcji warunkowych
    * parsowanie stringów
    * praca ze ścieżkami w systemie operacyjnym

:Hints:
    * ``str.isspace()``
    * inline ``if``

.. literalinclude:: src/etc-hosts.txt
    :name: listing-file-etc-hosts
    :language: text
    :caption: Przykładowa zawartość pliku ``hosts.txt``

.. literalinclude:: src/file-hosts.py
    :name: listing-file-hosts
    :language: python
    :caption: ``/etc/hosts`` example
