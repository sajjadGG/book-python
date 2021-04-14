"""
* Assignment: About Environment
* Complexity: easy
* Lines of code: 0 lines
* Time: 3 min

English:
    TODO: English Translation

Polish:
    1. Stwórz plik o nazwie `about_env.py`
    2. Użyj danych z sekcji "Given" (patrz poniżej)
    3. Uruchom plik w swoim IDE (menu `Run -> Run... -> nazwa Twojego skryptu`)
    4. Gdzie Python jest zainstalowany?
    5. Czy korzystasz z "Virtualenv"?
    6. Upewnij się, że w linijce z "Virtualenv" nie masz `None`

Tests:
    >>> assert python_executable
    >>> assert python_version
    >>> assert venv
"""


# Given
import sys
import os


python_executable = sys.executable
python_version = tuple(sys.version_info)
venv = os.getenv("VIRTUAL_ENV")

# Solution
python_executable = sys.executable
python_version = tuple(sys.version_info)
venv = os.getenv("VIRTUAL_ENV")
