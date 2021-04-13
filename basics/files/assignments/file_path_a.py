"""
* Assignment: File Path Exception
* Complexity: easy
* Lines of code: 6 lines
* Time: 3 min

English:
    1. Modify `check` function
    3. If `filename` exists, print 'Ok'
    2. If `filename` does not exist, print 'File not found'

Polish:
    1. Zmodyfikuj funkcję `check`
    2. Jeżeli `filename` istnieje, wypisz 'Ok'
    2. Jeżeli `filename` nie istnieje, wypisz 'File not found'

Tests:
    >>> check(__file__)
    Ok
    >>> check('_notexisting.txt')
    File not found
"""

# Given
def check(filename):
    ...


# Solution
def check(filename):
    try:
        open(filename)
    except FileNotFoundError:
        print('File not found')
    else:
        print('Ok')
