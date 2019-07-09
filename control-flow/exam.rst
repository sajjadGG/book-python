**********************
Exam from basic topics
**********************


Relational Files Database
=========================
* Filename: :download:`solution/exam.py`
* Lines of code to write: 60 lines
* Estimated time of completion: 60 min
* Input data: :numref:`code-file-etc-passwd`, :numref:`code-file-etc-shadow`, :numref:`code-file-etc-group`

#. Poniższe listingi prezentują zawartość plików:

    - ``/etc/passwd`` - :numref:`code-file-etc-passwd`
    - ``/etc/shadow`` - :numref:`code-file-etc-shadow`
    - ``/etc/group`` - :numref:`code-file-etc-group`

#. Skopuj ich zawartość każdego z tych plików na dysk do plików ``.txt``
#. Uwaga: komentarze i puste mają również być skopiowane!
#. Sparsuj plik i przedstaw go w formacie ``List[dict]``
#. Zwróć listę użytkowników, których ``UID`` jest większy niż 1000
#. W ramach ``dict`` połącz dane, tak aby uzyskać wynik:

    .. code-block:: python

        [
            {
                'username': 'twardowski',
                'uid': 1001,
                'gid': 1001,
                'home': '/home/twardowski',
                'shell': '/bin/bash',
                'algorithm': 'SHA-512',
                'password': 'tgfvvFWJJ5...k4kijuhE50',
                'salt': 'P9zn0KwR',
                'groups': ['staff', 'sysadmin'],
                'last_changed': datetime.date(2015, 7, 16),
                'locked': False,
            },
            ...
        ]

:The whys and wherefores:
    * czytanie i parsowanie pliku
    * łączenie danych z różnych plików w jeden format wynikowy
    * nieregularne pliki konfiguracyjne (struktura może się zmieniać)
    * filtrowanie elementów
    * korzystanie z pętli i instrukcji warunkowych
    * parsowanie stringów
    * praca ze ścieżkami w systemie operacyjnym
    * różna reprezentacja danych (podmienianie wartości)

.. literalinclude:: data/etc-passwd.txt
    :name: code-file-etc-passwd
    :language: text
    :caption: Przykładowa zawartość pliku ``/etc/passwd``

.. literalinclude:: data/etc-shadow.txt
    :name: code-file-etc-shadow
    :language: text
    :caption: Przykładowa zawartość pliku ``/etc/shadow``

.. literalinclude:: data/etc-group.txt
    :name: code-file-etc-group
    :language: text
    :caption: Przykładowa zawartość pliku ``/etc/group``
