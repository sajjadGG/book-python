"""
* Assignment: Function Definition Print
* Complexity: easy
* Lines of code: 5 lines
* Time: 3 min

English:
    1. Define function `call` without parameters
    2. Function appends `Beetlejuice` to `results`
    3. Call function three times

Polish:
    1. Zdefiniuj funkcję `call` bez parametrów
    2. Funkcja dodaje `Beetlejuice` do `result`
    3. Wywołaj funkcję trzy razy

Tests:
    >>> from inspect import isfunction
    >>> isfunction(call)
    True
    >>> result
    ['Beetlejuice', 'Beetlejuice', 'Beetlejuice']
"""

result = []


# Solution
def call():
    result.append('Beetlejuice')


call()
call()
call()
