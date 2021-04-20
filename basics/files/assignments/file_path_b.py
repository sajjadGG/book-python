"""
* Assignment: File Path Abspath
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Define `path` with converted `filename` to absolute path
    2. To `result` assgin string:
        a. `file` if path is a file
        b. `directory` if path is a directory
        c. `not exist` if path does not exist
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `path` z przekonwertowym `filename` do ścieżki bezwzględnej
    2. Do `result` przypisz ciąg znaków:
        a. `file` jeżeli ścieżka jest plikiem
        b. `directory` jeżeli ścieżka jest katalogiem
        c. `not exist` jeżeli ścieżka nie istnieje
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys
    >>> sys.tracebacklimit = 0

    >>> assert isinstance(result, str), \
    'Result must be a str with: `file`, `directory` or `not exist`'

    >>> assert isinstance(path, Path), \
    'Use Path class from pathlib library to create a filepath'

    >>> current_directory = Path.cwd()
    >>> assert str(current_directory) in str(path), \
    'File Path must be absolute, check if you have current directory in path'

    >>> result
    'not exist'
"""


# Given
from pathlib import Path


filename: str = 'myfile.txt'
path: Path = ...
result: str = ...

# Solution
path = Path(Path.cwd(), filename)

if not path.exists():
    result = 'not exist'

if path.is_dir():
    result = 'directory'

if path.is_file():
    result = 'file'
