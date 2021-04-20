"""
* Assignment: Loop For Count
* Status: required
* Complexity: easy
* Lines of code: 7 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Count occurrences of each color
    X. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zlicz wystąpienia każdego z kolorów
    3. Porównaj wynik z sekcją "Tests" poniżej
    X. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> type(red)
    <class 'int'>
    >>> type(green)
    <class 'int'>
    >>> type(blue)
    <class 'int'>
    >>> red
    3
    >>> green
    2
    >>> blue
    2
"""

# Given
DATA = ['red', 'green', 'blue', 'red', 'green', 'red', 'blue']

red = ...  # int: number of 'red' elements in DATA
green = ...  # int: number of 'green' elements in DATA
blue = ...  # int: number of 'blue' elements in DATA

# Solution
red = 0
green = 0
blue = 0

for color in DATA:
    if color == 'red':
        red += 1
    elif color == 'green':
        green += 1
    elif color == 'blue':
        blue += 1
