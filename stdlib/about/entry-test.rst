****************
Pre-Intermediate
****************


Entry Test Select
=================
* Assignment: Entry Test Select
* Filename: entry_test_select.py
* Complexity: easy
* Lines of code: 6 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Write header (first line) to ``header`` variable
    3. Convert to ``list`` data from row 2, 6, 9 and add to ``result``
    4. Convert to ``tuple`` data from row 12, 15, 16 and add to ``result``
    5. Convert to ``dict`` data from row 18, 21 and add to ``result``:

        a. key -> index number (18 or 21)
        b. value -> species name

    6. Add empty ``set`` to ``result``
    7. Use only indexes
    8. Do not use ``for``, ``while`` or ``slice()``

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zapisz nagłówek (pierwsza linia) do zmiennej ``header``
    3. Przekonwertuj do ``list`` dane z wierszy 2, 6, 9 i dodaj do ``result``
    4. Przekonwertuj do ``tuple`` dane z wierszy 12, 15, 16 i dodaj do ``result``
    5. Przekonwertuj do ``dict`` dane z wierszy 18, 21 i dodaj do ``result``:

        a. klucz -> numer indeksu (18 or 21)
        b. wartość -> nazwa gatunku

    6. Dodaj pusty ``set`` do ``result``
    7. Użyj tylko indeksów
    8. Nie używaj ``for``, ``while`` lub ``slice()``

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


Entry Test Slice
================
* Assignment: Entry Test Slice
* Filename: entry_test_slice.py
* Complexity: easy
* Lines of code: 20 lines
* Time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Use only ``slice``
    3. Extract list ``features`` with measurements (every row must be tuple)
    4. Extract species name (every fifth element) and write to ``labels`` list
    5. Write unique species names to ``species`` set
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Użyj tylko ``slice``
    3. Wyodrębnij listę ``features`` w pomiarami (każdy wiersz ma być krotką)
    4. Wyodrębnij nazwę gatunku (co piąty element) i zapisz do listy ``labels``
    5. Zapisz unikalne nazwy gatunków do zbioru ``species``
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Given:
    .. code-block:: python

        DATA = (
            5.8, 2.7, 5.1, 1.9, 'virginica',
            5.1, 3.5, 1.4, 0.2, 'setosa',
            5.7, 2.8, 4.1, 1.3, 'versicolor',
            6.3, 2.9, 5.6, 1.8, 'virginica',
            6.4, 3.2, 4.5, 1.5, 'versicolor',
            4.7, 3.2, 1.3, 0.2, 'setosa',
        )

Tests:
    .. code-block:: python

        features = [
            (5.8, 2.7, 5.1, 1.9),
            (5.1, 3.5, 1.4, 0.2),
            (5.7, 2.8, 4.1, 1.3),
            (6.3, 2.9, 5.6, 1.8),
            (6.4, 3.2, 4.5, 1.5),
            (4.7, 3.2, 1.3, 0.2),
        ]

        labels = [
            'virginica',
            'setosa',
            'versicolor',
            'virginica',
            'versicolor',
            'setosa',
        ]

        species = {
            'versicolor',
            'setosa',
            'virginica',
        }


Entry Test Listdict
===================
* Assignment: Entry Test Listdict
* Filename: entry_test_listdict.py
* Complexity: easy
* Lines of code: 8 lines
* Time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Separate header and data
    3. Print ``result: list[dict]``

        a. key - name from the header
        b. value - measurement or species

    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Odseparuj nagłówek i dane
    3. Wypisz ``result: list[dict]``

        a. klucz: nazwa z nagłówka
        b. wartość: wyniki pomiarów lub gatunek

    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

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
    >>> result
    [{'Sepal length': 5.8, 'Sepal width': 2.7, 'Petal length': 5.1, 'Petal width': 1.9, 'Species': 'virginica'},
     {'Sepal length': 5.1, 'Sepal width': 3.5, 'Petal length': 1.4, 'Petal width': 0.2, 'Species': 'setosa'},
     {'Sepal length': 5.7, 'Sepal width': 2.8, 'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
     ...]


Entry Test Nested
=================
* Assignment: Entry Test Nested
* Filename: entry_test_nested.py
* Complexity: easy
* Lines of code: 3 lines
* Time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Separate header from data
    3. Iterate over data
    4. Print species names ending with "ca" or "osa"

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Oddziel nagłówek od danych
    3. Iteruj po danych
    4. Wypisz nazwy gatunków kończące się na "ca" lub "osa"

Given:
    .. code-block:: python

        DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
                (5.8, 2.7, 5.1, 1.9, {'virginica'}),
                (5.1, 3.5, 1.4, 0.2, {'setosa'}),
                (5.7, 2.8, 4.1, 1.3, {'versicolor'}),
                (6.3, 2.9, 5.6, 1.8, {'virginica'}),
                (6.4, 3.2, 4.5, 1.5, {'versicolor'}),
                (4.7, 3.2, 1.3, 0.2, {'setosa'}),
                (7.0, 3.2, 4.7, 1.4, {'versicolor'}),
                (7.6, 3.0, 6.6, 2.1, {'virginica'}),
                (4.6, 3.1, 1.5, 0.2, {'setosa'})]
