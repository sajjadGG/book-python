"""
* Assignment: Idioms Range Impl
* Complexity: medium
* Lines of code: 25 lines
* Time: 21 min

English:
    1. Use data from "Given" section (see below)
    2. Define function `myrange` with parameters: `start`, `stop`, `step`
    3. Write own implementation of a built-in `myrange(start, stop, step)` function
    4. How to implement passing only stop argument (`myrange(start=0, stop=???, step=1)`)?
    5. All tests must pass
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj funkcję `myrange` z parametrami: `start`, `stop`, `step`
    3. Zaimplementuj własne rozwiązanie wbudowanej funkcji `myrange(start, stop, step)`
    4. Jak zaimplementować możliwość podawania tylko końca (`myrange(start=0, stop=???, step=1)`)?
    5. Wszystkie testy muszą przejść
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hint:
    * use `*args` and `**kwargs`
    * `if len(args) == ...`

Tests:
    >>> from inspect import isfunction
    >>> assert isfunction(myrange)

    >>> myrange(0, 10, 2)
    [0, 2, 4, 6, 8]

    >>> myrange(0, 5)
    [0, 1, 2, 3, 4]

    >>> myrange(5)
    [0, 1, 2, 3, 4]

    >>> myrange()
    Traceback (most recent call last):
    ValueError: Invalid arguments

    >>> myrange(1,2,3,4)
    Traceback (most recent call last):
    ValueError: Invalid arguments

    >>> myrange(stop=2)
    Traceback (most recent call last):
    TypeError: myrange() takes no keyword arguments

    >>> myrange(start=1, stop=2)
    Traceback (most recent call last):
    TypeError: myrange() takes no keyword arguments

    >>> myrange(start=1, stop=2, step=2)
    Traceback (most recent call last):
    TypeError: myrange() takes no keyword arguments
"""


# Solution
def myrange(*args, **kwargs):
    if kwargs:
        raise TypeError('myrange() takes no keyword arguments')
    if len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
        step = 1
    elif len(args) == 1:
        start = 0
        stop = args[0]
        step = 1
    else:
        raise ValueError('Invalid arguments')

    current = start
    result = []

    while current < stop:
        result.append(current)
        current += step

    return result
