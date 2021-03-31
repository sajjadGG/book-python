"""
* Assignment: File Path Exception
* Complexity: easy
* Lines of code: 6 lines
* Time: 3 min

English:
    1. Using `input()` ask user for a file path
    3. Handle exception for not existing file
    4. Handle exception for not having sufficient permissions

Polish:
    1. Używając `input()` zapytaj użytkownika o ścieżkę do pliku
    3. Obsłuż wyjątek dla nieistniejącego pliku
    4. Obsłuż wyjątek dla braku wystarczających uprawnień

Tests:
    TODO: Doctests
    TODO: Input Stub
"""

# Stub
def input(__prompt):
    """Stub user input, for testing purpose only"""
    return '_temporary.txt'


# Given
filename = input('Type filename: ')


# Solution
try:
    file = open(filename)
except FileNotFoundError:
    print('Sorry, file not found')
except PermissionError:
    print('Sorry, not permitted')
