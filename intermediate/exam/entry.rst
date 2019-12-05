****************
Pre-Intermediate
****************


Create
------
* Complexity level: easy
* Lines of code to write: 13 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/tuple_create.py`

:English:
    #. For given data input (see below)
    #. Create a ``tuple`` representing all Species
    #. Calculate mean for each numerical values column
    #. To convert table use multiline select with ``alt`` key in your IDE

:Polish:
    #. Dla danych wejściowych (patrz sekcja input)
    #. Stwórz ``tuple`` z nazwami gatunków
    #. Wylicz średnią arytmetyczną dla każdej z kolumn numerycznych
    #. Do przekonwertowania tabelki wykorzystaj zaznaczanie wielu linijek za pomocą klawisza ``alt`` w Twoim IDE

:Input:
    .. code-block:: text

        "Sepal length", "Sepal width", "Petal length", "Petal width", "Species"
        "5.8", "2.7", "5.1", "1.9", "virginica"
        "5.1", "3.5", "1.4", "0.2", "setosa"
        "5.7", "2.8", "4.1", "1.3", "versicolor"
        "6.3", "2.9", "5.6", "1.8", "virginica"
        "6.4", "3.2", "4.5", "1.5", "versicolor"
        "4.7", "3.2", "1.3", "0.2", "setosa"
        "7.0", "3.2", "4.7", "1.4", "versicolor"
        "7.6", "3.0", "6.6", "2.1", "virginica"
        "4.9", "3.0", "1.4", "0.2", "setosa"
        "4.9", "2.5", "4.5", "1.7", "virginica"
        "7.1", "3.0", "5.9", "2.1", "virginica"

:The whys and wherefores:
    * Defining ``tuple``
    * Learning IDE features

:Hints:
    * ``mean = sum(...) / len(...)``

Select
------
* Complexity level: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/nested_select.py`

:English:
    #. For given data input (see below)
    #. Write header (first line) to ``header`` variable
    #. Convert to ``list`` data from row 2, 6, 9 and add to ``output``
    #. Convert to ``tuple`` data from row 12, 15, 16 and add to ``output``
    #. Convert to ``dict`` data from row 18, 21 and add to ``output``:

        * key -> index number (18 or 21)
        * value -> species name

    #. Add empty ``set`` to ``output``
    #. Use only indexes
    #. Do not use ``for``, ``while`` or ``slice()``

:Polish:
    #. Dla danych wejściowych (patrz sekcja input)
    #. Zapisz nagłówek (pierwsza linia) do zmiennej ``header``
    #. Przekonwertuj do ``list`` dane z wierszy 2, 6, 9 i dodaj do ``output``
    #. Przekonwertuj do ``tuple`` dane z wierszy 12, 15, 16 i dodaj do ``output``
    #. Przekonwertuj do ``dict`` dane z wierszy 18, 21 i dodaj do ``output``:

        * klucz -> numer indeksu (18 or 21)
        * wartość -> nazwa gatunku

     #. Dodaj pusty ``set`` do ``output``
     #. Użyj tylko indeksów
     #. Nie używaj ``for``, ``while`` lub ``slice()``

:Input:
    .. code-block:: python

        INPUT = [
            ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
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
            (4.6, 3.1, 1.5, 0.2, 'setosa'),
        ]

:The whys and wherefores:
    * Using nested data structures
    * Using indexes
    * Type casting

Iris dataset
------------
* Complexity level: medium
* Lines of code to write: 20 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/slice_iris.py`

:English:
    #. For input data (see below)
    #. Use only ``slice``
    #. Extract list ``features`` with measurements (every row must be tuple)
    #. Extract species name (every fifth element) and write to ``labels`` list
    #. Write unique species names to ``species`` set

:Polish:
    #. Dla danych wejściowych (patrz sekcja input)
    #. Użyj tylko ``slice``
    #. Wyodrębnij listę ``features`` w pomiarami (każdy wiersz ma być krotką)
    #. Wyodrębnij nazwę gatunku (co piąty element) i zapisz do listy ``labels``
    #. Zapisz unikalne nazwy gatunków do zbioru ``species``

:Input:
    .. code-block:: python

        INPUT = (
            5.8, 2.7, 5.1, 1.9, 'virginica',
            5.1, 3.5, 1.4, 0.2, 'setosa',
            5.7, 2.8, 4.1, 1.3, 'versicolor',
            6.3, 2.9, 5.6, 1.8, 'virginica',
            6.4, 3.2, 4.5, 1.5, 'versicolor',
            4.7, 3.2, 1.3, 0.2, 'setosa',
        )

:Output:
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

:The whys and wherefores:
    * Defining and using ``list``, ``tuple``, ``set``
    * Slicing sequences

``List[tuple]`` to ``List[dict]``
---------------------------------
* Complexity level: easy
* Lines of code to write: 8 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/loop_dict_to_list.py`

:English:
    #. For input data (see below)
    #. Separate header and data
    #. Print ``List[dict]``

        - key - name from the header
        - value - measurement or species

:Polish:
    #. Dla danych wejściowych (patrz sekcja input)
    #. Odseparuj nagłówek i dane
    #. Wypisz ``List[dict]``

        - klucz: nazwa z nagłówka
        - wartość: wyniki pomiarów lub gatunek

:Input:
    .. code-block:: python

        INPUT = [
            ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
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
            (4.6, 3.1, 1.5, 0.2, 'setosa'),
        ]

:Output:
    .. code-block:: python

        OUTPUT: List[dict] = [
            {'Sepal length': 5.8, 'Sepal width': 2.7, 'Petal length': 5.1, 'Petal width': 1.9, 'Species': 'virginica'},
            {'Sepal length': 5.1, 'Sepal width': 3.5, 'Petal length': 1.4, 'Petal width': 0.2, 'Species': 'setosa'},
            {'Sepal length': 5.7, 'Sepal width': 2.8, 'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
            ...
        ]

:The whys and wherefores:
    * Working with nested data structures
    * Iterating over dict and lists

Get elements from nested data structure
---------------------------------------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/for_nested.py`

:English:
    #. For input data (see below)
    #. Separate header from data
    #. Iterate over data
    #. Print species names ending with "ca" or "sa"

:Polish:
    #. Dla danych wejściowych (patrz sekcja input)
    #. Oddziel nagłówek od danych
    #. Iteruj po danych
    #. Wypisz nazwy gatunków kończące się na "ca" lub "sa"

:Input:
    .. code-block:: python

        INPUT = [
            ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, {'virginica'}),
            (5.1, 3.5, 1.4, 0.2, {'setosa'}),
            (5.7, 2.8, 4.1, 1.3, {'versicolor'}),
            (6.3, 2.9, 5.6, 1.8, {'virginica'}),
            (6.4, 3.2, 4.5, 1.5, {'versicolor'}),
            (4.7, 3.2, 1.3, 0.2, {'setosa'}),
            (7.0, 3.2, 4.7, 1.4, {'versicolor'}),
            (7.6, 3.0, 6.6, 2.1, {'virginica'}),
            (4.6, 3.1, 1.5, 0.2, {'setosa'}),
        ]

:The whys and wherefores:
    * Accessing ``dict`` keys
    * Iterating over nested structure

String cleaning
---------------
* Complexity level: easy
* Lines of code to write: 11 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/str_cleaning.py`

:English:
    #. For input data (see below)
    #. Expected value is ``Jana III Sobieskiego``
    #. Use only ``str`` methods to clean each variable
    #. Compare with output data (see below)
    #. Discuss how to create generic solution which fit all cases
    #. Implementation of such generic function will be in :ref:`Function Basics` chapter

:Polish:
    #. Dla danych wejściowych (patrz sekcja input)
    #. Oczekiwana wartość ``Jana III Sobieskiego``
    #. Wykorzystaj tylko metody ``str`` do oczyszczenia każdej zmiennej
    #. Porównaj wyniki z danymi wyjściowymi (patrz sekcja output)
    #. Przeprowadź dyskusję jak zrobić rozwiązanie generyczne pasujące do wszystkich przypadków
    #. Implementacja takiej generycznej funkcji będzie w rozdziale :ref:`Function Basics`

:Input:
    .. code-block:: python

        a = 'ul Jana III SobIESkiego'
        b = '\tul. Jana trzeciego Sobieskiego'
        c = 'ulicaJana III Sobieskiego'
        d = 'UL. JANA 3 \nSOBIESKIEGO'
        e = 'UL. jana III SOBiesKIEGO'
        f = 'ULICA JANA III SOBIESKIEGO  '
        g = 'ULICA. JANA III SOBIeskieGO'
        h = ' Jana 3 Sobieskiego  '
        i = 'Jana III Sobi\teskiego '

:Output:
    .. code-block:: python

        expected = 'Jana III Sobieskiego'

        print(f'{a == expected}\t a: "{a}"')
        print(f'{b == expected}\t b: "{b}"')
        print(f'{c == expected}\t c: "{c}"')
        print(f'{d == expected}\t d: "{d}"')
        print(f'{e == expected}\t e: "{e}"')
        print(f'{f == expected}\t f: "{f}"')
        print(f'{g == expected}\t g: "{g}"')
        print(f'{h == expected}\t h: "{h}"')
        print(f'{i == expected}\t i: "{i}"')

:The whys and wherefores:
    * Variable definition
    * Print formatting
    * Cleaning text input

