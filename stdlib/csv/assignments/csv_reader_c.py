"""
* Assignment: CSV Reader Enumerate
* Complexity: medium
* Lines of code: 8 lines
* Time: 8 min

English:
    1. Using `csv.reader()` read data from file
    2. Define `result: list[tuple]` with converted data
    3. Use Unix `\n` line terminator
    4. Run doctests - all must succeed

Polish:
    1. Za pomocą `csv.reader()` wczytaj dane z pliku
    2. Zdefiniuj `result: list[tuple]` z przekonwerowanymi danymi
    3. Użyj zakończenia linii Unix `\n`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * For Python before 3.8: `dict(OrderedDict)`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [('5.8', '2.7', '5.1', '1.9', 'virginica'),
     ('5.1', '3.5', '1.4', '0.2', 'setosa'),
     ('5.7', '2.8', '4.1', '1.3', 'versicolor')]

    >>> remove(FILE)
"""

import csv


FILE = r'_temporary.csv'

DATA = """3,4,setosa,virginica,versicolor
5.8,2.7,5.1,1.9,1
5.1,3.5,1.4,0.2,0
5.7,2.8,4.1,1.3,2"""

with open(FILE, mode='w') as file:
    file.write(DATA)

# list[tuple]: data from file (note the list[tuple] format!)
result = []

# Solution
with open(FILE, mode='r') as file:
    species = file.readline().strip().split(',')[2:]
    species = dict(enumerate(species))
    reader = csv.reader(file, lineterminator='\n')

    for *features, label in reader:
        label = species[int(label)]
        row = features + [label]
        result.append(tuple(row))
