"""
* Assignment: Math Random Sample
* Complexity: easy
* Lines of code: 1 lines
* Time: 5 min

English:
    1. Print 6 random integers without repetition in range from 1 to 49
    2. Run doctests - all must succeed

Polish:
    1. Wyświetl 6 losowych i nie powtarzających się liczb całkowitych z
       zakresu od 1 do 49.
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> sorted(result)
    [3, 17, 25, 27, 33, 49]
"""

from random import sample, seed
seed(0)


# Solution
result = sample(range(1, 49), 6)


# Alternative solution
from random import randint, seed
seed(0)

MAX_VALUE = 49
MIN_VALUE = 1
REPETITIONS = 6

result = set()

while len(result) < REPETITIONS:
    number = randint(MIN_VALUE, MAX_VALUE)
    result.add(number)
