.. _Operacje na plikach:

*******************
Operacje na plikach
*******************

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

    "``'r'``", "open for reading (default)"
    "``'w'``", "open for writing, truncating the file first"
    "``'a'``", "open for writing, appending to the end of the file if it exists"
    "``'b'``", "binary mode"
    "``'+'``", "open a disk file for updating (reading and writing)"


Obsługa wyjątków
================
.. literalinclude:: src/file-write.py
    :language: python
    :caption: Exception handling while accessing files


Zadania kontrolne
=================

Zawartość zadanego pliku
------------------------
#. Napisz program, który wyświetli na ekranie zawartość pliku o nazwie podanej przez użytkownika.
#. Dopisz obsługę wyjątków dla braku uprawnień oraz tego że plik nie istnieje.


Parsowanie ``/etc/passwd``
--------------------------
#. Sparsuj plik ``/etc/passwd`` i przedstaw go w formacie listy dictów:

    - User name
    - Encrypted password
    - User ID number (UID)
    - User's group ID number (GID)
    - Full name of the user (GECOS)
    - User home directory
    - Login shell

#. Zwróć username, uid oraz grupy użytkowników, których UID jest mniejszy niż 50.
#. Gdyby w Twoim systemie nie było pliku, skorzystaj z szablonu poniżej:

    .. literalinclude:: src/file-passwd.txt
        :language: text
        :caption: ``/etc/passwd`` example

:Co zadanie sprawdza?:
    * czytanie i parsowanie pliku
    * nieregularne pliki konfiguracyjne (struktura może się zmieniać)
    * filtrowanie elementów
    * korzystanie z pętli i instrukcji warunkowych
    * parsowanie stringów
    * praca ze ścieżkami w systemie operacyjnym


Parsowanie ``/etc/hosts``
-------------------------
#. Z twojego systemu operacyjnego wyciągnij plik ``/etc/hosts`` i przedstaw go w formie listy dictów jak w przykładzie poniżej:

    .. literalinclude:: src/file-hosts.py
        :language: python
        :caption: ``/etc/hosts`` example

#. Zwróć uwagę na uprawnienia do odczytu pliku
#. System Windows również posiada ten plik (``C:/Windows/System32/drivers/etc/hosts``)
#. Gdyby w Twoim systemie nie było pliku, skorzystaj z szablonu poniżej:

    .. literalinclude:: src/file-hosts.txt
        :language: text
        :caption: ``/etc/hosts`` example

:Co zadanie sprawdza?:
    * czytanie i parsowanie pliku
    * nieregularne pliki konfiguracyjne (struktura może się zmieniać)
    * filtrowanie elementów
    * korzystanie z pętli i instrukcji warunkowych
    * parsowanie stringów
    * praca ze ścieżkami w systemie operacyjnym
