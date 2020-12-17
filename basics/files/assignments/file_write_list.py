"""
* Assignment: File Write List
* Filename: file_write_list.py
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Write `DATA` to file `FILE`
    3. Check in your operating system if data was written correctly
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zapisz `DATA` do pliku `FILE`
    3. Sprawdź w systemie operacyjnym czy dane zapisały się poprawnie
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * `','.join(...)`
    * Add newline `\n` at the end of line and file

Tests:
    >>> open(FILE).read()
    'hello\\nworld\\n'
    >>> from os import remove
    >>> remove(FILE)
"""


# Given
FILE = r'_temporary.txt'
DATA = ['hello', 'world']


# Solution
data = '\n'.join(DATA) + '\n'

with open(FILE, mode='wt') as file:
    file.write(data)
