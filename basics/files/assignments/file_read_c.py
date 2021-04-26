"""
* Assignment: File Read CSV
* Required: yes
* Complexity: easy
* Lines of code: 15 lines
* Time: 8 min

English:
    1. Write `DATA` to file `FILE`
    2. Read `FILE`
    3. Separate header from data
    4. Write header (first line) to `header`
    5. Read file and for each line:
        a. Strip whitespaces
        b. Split line by coma `,`
        c. Convert measurements do `tuple[float]`
        d. Append measurements to `features`
        e. Append species name to `labels`
    6. Print `header`, `features` and `labels`
    7. Run doctests - all must succeed

Polish:
    1. Zapisz `DATA` do pliku `FILE`
    2. Wczytaj `FILE`
    3. Odseparuj nagłówek od danych
    4. Zapisz nagłówek (pierwsza linia) do `header`
    5. Zaczytaj plik i dla każdej linii:
        a. Usuń białe znaki z początku i końca linii
        b. Podziel linię po przecinku `,`
        c. Przekonwertuj pomiary do `tuple[float]`
        d. Dodaj pomiary do `features`
        e. Dodaj gatunek do `labels`
    6. Wyświetl `header`, `features` i `labels`
    7. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `tuple(float(x) for x in X)`

Tests:
    >>> header
    ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
    >>> features  # doctest: +NORMALIZE_WHITESPACE
    [(5.4, 3.9, 1.3, 0.4),
     (5.9, 3.0, 5.1, 1.8),
     (6.0, 3.4, 4.5, 1.6),
     (7.3, 2.9, 6.3, 1.8),
     (5.6, 2.5, 3.9, 1.1),
     (5.4, 3.9, 1.3, 0.4)]
    >>> labels
    ['setosa', 'virginica', 'versicolor', 'virginica', 'versicolor', 'setosa']
    >>> from os import remove; remove(FILE)
"""

FILE = '_temporary.csv'

DATA = """sepal_length,sepal_width,petal_length,petal_width,species
5.4,3.9,1.3,0.4,setosa
5.9,3.0,5.1,1.8,virginica
6.0,3.4,4.5,1.6,versicolor
7.3,2.9,6.3,1.8,virginica
5.6,2.5,3.9,1.1,versicolor
5.4,3.9,1.3,0.4,setosa
"""

header = []
features = []
labels = []

with open(FILE, mode='w') as file:
    file.write(DATA)


# Solution
with open(FILE) as file:
    header = file.readline().strip().split(',')

    for line in file:
        *X, y = line.strip().split(',')
        X = [float(x) for x in X]
        features.append(tuple(X))
        labels.append(y)