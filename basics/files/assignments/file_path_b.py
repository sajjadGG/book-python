"""
* Assignment: File Path Abspath
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Define `path` with converted `filename` to absolute path
    2. Print if path exists and leads to file or directory
    3. Compare result with "Tests" section (see below)

Polish:
    1. Zdefiniuj `path` z przekonwertowym `filename` do ścieżki bezwzględnej
    2. Wypisz czy ścieżka istnieje i czy prowadzi do pliku czy katalogu
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    TODO: Input Stub
    >>> isinstance(result, Path)
    True
    >>> current_directory = Path.cwd()
    >>> str(current_directory) in str(result)
    True
"""


# Given
from pathlib import Path


filename = 'myfile.txt'
path = ...
result = ...

# Solution
file = Path(Path.cwd(), filename)

if not file.exists():
    result = 'not exist'

if file.is_dir():
    result = 'directory'

if file.is_file():
    result = 'file'
