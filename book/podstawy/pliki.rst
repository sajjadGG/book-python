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
.. literalinclude:: src/file-exception.py
    :language: python
    :caption: Exception handling while accessing files


Zadania kontrolne
=================

Zawartość zadanego pliku
------------------------
#. Napisz program, który wyświetli na ekranie zawartość pliku o nazwie podanej przez użytkownika.
#. Dopisz obsługę wyjątków dla braku uprawnień oraz tego że plik nie istnieje.

Parsowanie ``/etc/hosts``
-------------------------
#. Do pliku ``hosts`` w katalogu gdzie będzie Twój skrypt zapisz poniższy szablon:
#. Ważne są komentarze, białe spacje i linie przerwy
#. Przedstaw go w formie listy dictów jak w przykładzie poniżej:

    .. literalinclude:: src/file-hosts.py
        :language: python
        :caption: ``/etc/hosts`` example

#. Zwróć uwagę na uprawnienia do odczytu pliku

:Co zadanie sprawdza?:
    * czytanie i parsowanie pliku
    * nieregularne pliki konfiguracyjne (struktura może się zmieniać)
    * filtrowanie elementów
    * korzystanie z pętli i instrukcji warunkowych
    * parsowanie stringów
    * praca ze ścieżkami w systemie operacyjnym

.. literalinclude:: src/file-etc-hosts.txt
    :name: code-file-etc-hosts
    :language: text
    :caption: Przykładowa zawartość pliku ``/etc/hosts``

Parsowanie ``/etc/passwd``
--------------------------
#. Poniższe listingi prezentują przykładową zawartość plików:

    - ``/etc/passwd`` - :numref:`code-file-etc-passwd`
    - ``/etc/shadow`` - :numref:`code-file-etc-shadow`
    - ``/etc/group`` - :numref:`code-file-etc-group`

#. Skopuj ich zawartość do plików (shadow, passwd, group) na dysku w katalogu gdzie masz kod programu (uwaga: komentarze i puste mają również być skopiowane)
#. Sparsuj plik i przedstaw go w formacie listy dictów
#. W ramach dicta połącz dane, tak aby uzyskać wynik:

    .. code-block:: python

        users = [{
            'login': 'jimenez',
            'uid': 1001,
            'gid': 1001,
            'home': '/home/jimenez',
            'shell': '/bin/bash',
            'algorithm': 'SHA-512',
            'password': 'P9zn0KwR...k4kijuhE50',
            'groups': ['staff', 'sysadmin'],
            'lastchanged': datetime.date(2015, 7, 16),
            'locked': False,
        }, ...]

#. Zwróć listę użytkowników, których UID jest większy niż 1000 (są to konta niesystemowe - użytkowników).

:Co zadanie sprawdza?:
    * czytanie i parsowanie pliku
    * łączenie danych z różnych plików w jeden format wynikowy
    * nieregularne pliki konfiguracyjne (struktura może się zmieniać)
    * filtrowanie elementów
    * korzystanie z pętli i instrukcji warunkowych
    * parsowanie stringów
    * praca ze ścieżkami w systemie operacyjnym
    * różna reprezentacja danych (podmienianie wartości)

.. literalinclude:: src/file-etc-passwd.txt
    :name: code-file-etc-passwd
    :language: text
    :caption: Przykładowa zawartość pliku ``/etc/passwd``

.. literalinclude:: src/file-etc-shadow.txt
    :name: code-file-etc-shadow
    :language: text
    :caption: Przykładowa zawartość pliku ``/etc/shadow``

.. literalinclude:: src/file-etc-group.txt
    :name: code-file-etc-group
    :language: text
    :caption: Przykładowa zawartość pliku ``/etc/group``
