"""
* Assignment: Loop While Input
* Status: optional
* Complexity: medium
* Lines of code: 14 lines
* Time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Define `grades: list[float]`
    3. Using `input()` ask user about grade, one at a time
    4. User will type only valid `int` or `float`
    5. To iterate use only `while` loop
    6. If grade is in `GRADE_SCALE` - add it to `grades`
    7. If grade is not in `GRADE_SCALE`, skip this iteration
    8. If user pressed Enter key, end inserting data
    9. At the end, define `result: float` with calculated mean of `grades`
    10. Test case when report list is empty
    11. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj `grades: list[float]`
    3. Do iterowania użyj tylko pętli `while`
    4. Używając `input()` poproś użytkownika o ocenę, jedną na raz
    5. Użytkownik poda tylko poprawne `int` lub `float`
    6. Jeżeli ocena jest w `GRADE_SCALE` - dodaj ją do `grades`
    7. Jeżeli oceny nie ma w `GRADE_SCALE`, pomiń tą iterację
    8. Jeżeli użytkownik wcisnął Enter, zakończ wprowadzanie danych
    9. Na zakończenie zdefiniuj `result` z wyliczeniem średniej
       arytmetycznej `grades`
    10. Przetestuj przypadek, gdy dzienniczek jest pusty
    11. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `Stop` or `Ctrl+C` kills infinite loop
    * `mean = sum(...) / len(...)`

Tests:
    >>> from statistics import mean
    >>> import sys
    >>> sys.tracebacklimit = 0

    >>> type(grades)
    <class 'list'>
    >>> type(result)
    <class 'float'>

    >>> assert all(type(x) is float for x in grades)

    >>> mean(grades) == result  # doctest: +SKIP
    True

    >>> result
    3.5
"""

# Simulate user input (for test automation)
from unittest.mock import MagicMock
input = MagicMock(side_effect=['1', '2', '2.5', '3', '3.5', '4', '5', '6', ''])


# Given
GRADE_SCALE = (2.0, 3.0, 3.5, 4.0, 4.5, 5.0)

grades = ...  # list[float]: all user grades
result = ...  # float: arithmetic mean of grades

# Solution
grades = []

while True:
    grade = input('What grade you received?: ')

    if not grade:
        break

    grade = float(grade)

    if grade in GRADE_SCALE:
        grades.append(grade)


if grades:
    result = sum(grades) / len(grades)
