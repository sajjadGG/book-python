"""
* Assignment: About Environment
* Filename: about_environment.py
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
"""

# Given
import sys
import os


print(f'Python Executable: {sys.executable}')
print(f'Python Version: {sys.version}')
print(f'Virtualenv: {os.getenv("VIRTUAL_ENV")}')

# Solution
