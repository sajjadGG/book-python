"""
* Assignment: File Path Exception
* Complexity: easy
* Lines of code: 6 lines
* Time: 3 min

English:
    1. Modify `check` function
    2. If `filename` exists, print 'Ok'
    3. If `filename` does not exist, print 'File not found'
    4. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj funkcję `check`
    2. Jeżeli `filename` istnieje, wypisz 'Ok'
    3. Jeżeli `filename` nie istnieje, wypisz 'File not found'
    4. Uruchom doctesty - wszystkie muszą się powieść

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
