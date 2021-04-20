"""
* Assignment: File Write Str
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Write `DATA` to file `FILE`
    3. Check in your operating system if data was written correctly
    4. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zapisz `DATA` do pliku `FILE`
    3. Sprawdź w systemie operacyjnym czy dane zapisały się poprawnie
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * Add newline `\n` at the end of line and file

Tests:
    >>> open(FILE).read()
    'hello world\\n'
    >>> from os import remove
    >>> remove(FILE)
"""


# Given
FILE = r'_temporary.txt'
DATA = 'hello world'


# Solution
with open(FILE, mode='wt') as file:
    file.write(DATA + '\n')
