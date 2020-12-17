"""
* Assignment: Function Arguments Sequence
* Filename: function_args_sequence.py
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Define function which takes sequence of integers as an argument
    2. Sum only even numbers
    3. Print returned value

Polish:
    1. Zdefiniuj funkcję biorącą sekwencję liczb całkowitych jako argument
    2. Zsumuj tylko parzyste liczby
    3. Wypisz zwróconą wartość

Tests:
    >>> from inspect import isfunction
    >>> isfunction(total)
    True
    >>> total([1,2,3,4])
    6
    >>> total([2,-1,0,2])
    4
    >>> total(range(0,101))
    2550
"""


# Solution
def total(sequence):
    return sum(x for x in sequence if x % 2 == 0)
