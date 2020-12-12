.. _Stdlib Exit Test:

****************
Stdlib Exit Test
****************


Exit Test Encoder
=================
* Assignment: Exit Test Encoder
* Filename: exit_test_encoder.py
* Complexity: medium
* Lines of code: 13 lines
* Time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Define:

        a. ``features: list[tuple]`` - measurements
        b. ``labels: list[int]`` - species
        c. ``label_encoder: dict[int, str]`` - species name encoder

    3. Separate header from data
    4. To encode and decode ``labels`` (species) we need ``label_encoder: dict[int, str]``:

        a. key - id (incremented integer value)
        b. value - species name

    5. ``label_encoder`` must be generated from ``DATA``
    6. For each row add appropriate data to ``features``, ``labels`` and ``label_encoder``
    7. Print ``features``, ``labels`` and ``label_encoder``
    8. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj:

        a. ``features: list[tuple]`` - pomiary
        b. ``labels: list[int]`` - gatunki
        c. ``label_encoder: dict[int, str]`` - słownik podmiany nazw gatunków

    3. Odseparuj nagłówek od danych
    4. Aby móc zakodować i odkodować ``labels`` (gatunki) potrzebny jest ``label_encoder: dict[int, str]``:

        a. key - identyfikator (kolejna liczba rzeczywista)
        b. value - nazwa gatunku

    5. ``label_encoder`` musi być wygenerowany z ``DATA``
    6. Dla każdego wiersza dodawaj odpowiednie dane do ``feature``, ``labels`` i ``label_encoder``
    7. Wypisz ``feature``, ``labels`` i ``label_encoder``
    8. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. code-block:: python

        DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
                (5.8, 2.7, 5.1, 1.9, 'virginica'),
                (5.1, 3.5, 1.4, 0.2, 'setosa'),
                (5.7, 2.8, 4.1, 1.3, 'versicolor'),
                (6.3, 2.9, 5.6, 1.8, 'virginica'),
                (6.4, 3.2, 4.5, 1.5, 'versicolor'),
                (4.7, 3.2, 1.3, 0.2, 'setosa'),
                (7.0, 3.2, 4.7, 1.4, 'versicolor'),
                (7.6, 3.0, 6.6, 2.1, 'virginica'),
                (4.9, 3.0, 1.4, 0.2, 'setosa'),
                (4.9, 2.5, 4.5, 1.7, 'virginica'),
                (7.1, 3.0, 5.9, 2.1, 'virginica'),
                (4.6, 3.4, 1.4, 0.3, 'setosa'),
                (5.4, 3.9, 1.7, 0.4, 'setosa'),
                (5.7, 2.8, 4.5, 1.3, 'versicolor'),
                (5.0, 3.6, 1.4, 0.3, 'setosa'),
                (5.5, 2.3, 4.0, 1.3, 'versicolor'),
                (6.5, 3.0, 5.8, 2.2, 'virginica'),
                (6.5, 2.8, 4.6, 1.5, 'versicolor'),
                (6.3, 3.3, 6.0, 2.5, 'virginica'),
                (6.9, 3.1, 4.9, 1.5, 'versicolor'),
                (4.6, 3.1, 1.5, 0.2, 'setosa')]

Tests:
    >>> features  # doctest: +NORMALIZE_WHITESPACE
    [(5.8, 2.7, 5.1, 1.9),
     (5.1, 3.5, 1.4, 0.2),
     (5.7, 2.8, 4.1, 1.3),
     (6.3, 2.9, 5.6, 1.8),
     (6.4, 3.2, 4.5, 1.5),
     (4.7, 3.2, 1.3, 0.2), ...]

    >>> labels
    [0, 1, 2, 1, 2, 0, ...]

    >>> label_encoder  # doctest: +NORMALIZE_WHITESPACE
    {0: 'virginica',
     1: 'setosa',
     2: 'versicolor'}


Exit Test Passwd
================
* Assignment: Exit Test Passwd
* Filename: exit_test_passwd.py
* Complexity: medium
* Lines of code: 100 lines
* Time: 21 min

English:
    1. Use data from "Given" section (see below)
    2. Save listings content to files:

        a. ``etc_passwd.txt``
        b. ``etc_shadow.txt``
        c. ``etc_group.txt``

    3. Copy also comments and empty lines
    4. Parse files and convert it to ``result: list[dict]``
    5. Return list of users with ``UID`` greater than 1000
    6. User dict should contains data collected from all files
    7. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zapisz treści listingów do plików:

        a. ``etc_passwd.txt``
        b. ``etc_shadow.txt``
        c. ``etc_group.txt``

    3. Skopiuj również komentarze i puste linie
    4. Sparsuj plik i przedstaw go w formacie ``result: list[dict]``
    5. Zwróć listę użytkowników, których ``UID`` jest większy niż 1000
    6. Dict użytkownika powinien zawierać dane z wszystkich plików
    7. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. literalinclude:: data/etc-passwd.txt
        :name: code-exam-etc-passwd
        :language: text
        :caption: Przykładowa zawartość pliku ``/etc/passwd``

    .. literalinclude:: data/etc-shadow.txt
        :name: code-exam-etc-shadow
        :language: text
        :caption: Przykładowa zawartość pliku ``/etc/shadow``

    .. literalinclude:: data/etc-group.txt
        :name: code-exam-etc-group
        :language: text
        :caption: Przykładowa zawartość pliku ``/etc/group``

Tests:
    .. code-block:: text

        >>> result  # doctest: +NORMALIZE_WHITESPACE
        [{'username': 'twardowski',
          'uid': 1001,
          'gid': 1001,
          'home': '/home/twardowski',
          'shell': '/bin/bash',
          'algorithm': 'SHA-512',
          'password': 'tgfvvFWJJ5...k4kijuhE50',
          'salt': 'P9zn0KwR',
          'groups': {'astronauts', 'sysadmin'},
          'last_changed': datetime.date(2015, 7, 16),
          'locked': False},
        ...]
