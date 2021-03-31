"""
* Assignment: Mapping Dict Define
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Create `result: dict` representing input data
    3. Non-functional requirements:
        a. Assignmnet verifies creation of `dict()`
        b. Do not parse `DATA`, simply model `result` based on `DATA`
        c. Do not use `str.split()`, `slice`, `getitem`, `for`, `while` or any other control-flow statement

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz `result: dict` reprezentujący dane wejściowe
    3. Wymagania niefunkcjonalne:
        a. Zadanie sprawdza tworzenie `dict()`
        b. Nie parsuj `DATA`, po prostu zamodeluj `result` bazując na `DATA`
        c. Nie używaj `str.split()`, `slice`, `getitem`, `for`, `while` lub jakiejkolwiek innej instrukcji sterującej

Tests:
    >>> type(result)
    <class 'dict'>
    >>> 'First Name' in result.keys()
    True
    >>> 'Last Name' in result.keys()
    True
    >>> 'Missions' in result.keys()
    True
    >>> result['First Name'] == 'Jan'
    True
    >>> result['Last Name'] == 'Twardowski'
    True
    >>> type(result['Missions']) is list
    True
    >>> 'Apollo' in result['Missions']
    True
    >>> 'Artemis' in result['Missions']
    True
"""


# Given
DATA = """
    First Name: Jan
    Last Name: Twardowski
    Missions: Apollo, Artemis
"""

result = ...  # dict with First Name, Last Name and Missions as keys


# Solution
result = {
    'First Name': 'Jan',
    'Last Name': 'Twardowski',
    'Missions': ['Apollo', 'Artemis'],
}
