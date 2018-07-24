.. _Files:

*****
Files
*****

.. code-block:: python

    file = open(r'C:\Users\desktop.ini')

    content = file.read()   # reading file
    file.close()            # you have to close file manually

    print(content)

.. code-block:: python

    with open(r'C:\Users\desktop.ini') as file:
        content = file.read()

    # Python will close file automatically as soon as ``with`` block is over
    print(content)


Konstrukcja ``with``
====================
* Context manager


Czytanie
========
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

:Założenia:
    * Nazwa pliku: ``file_content.py``
    * Szacunkowa długość kodu: około 5 linii
    * Maksymalny czas na zadanie: 5 min

Parsowanie ``/etc/hosts``
-------------------------
#. Do pliku ``hosts.txt`` w katalogu gdzie będzie Twój skrypt zapisz kod z szablonu: :numref:`listing-file-etc-hosts`
#. Ważne są komentarze, białe spacje i linie przerwy
#. Przedstaw go w formie listy dictów jak w przykładzie poniżej: :numref:`listing-file-hosts`
#. Zwróć uwagę na uprawnienia do odczytu pliku

:Założenia:
    * Nazwa pliku: ``file_hosts.py``
    * Szacunkowa długość kodu: około 10 linii
    * Maksymalny czas na zadanie: 20 min

:Co zadanie sprawdza?:
    * czytanie i parsowanie pliku
    * nieregularne pliki konfiguracyjne (struktura może się zmieniać)
    * filtrowanie elementów
    * korzystanie z pętli i instrukcji warunkowych
    * parsowanie stringów
    * praca ze ścieżkami w systemie operacyjnym

:Podpowiedź:
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
