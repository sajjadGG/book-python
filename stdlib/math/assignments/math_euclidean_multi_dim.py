"""
* Assignment: Math Euclidean Distance n-dim
* Complexity: easy
* Lines of code: 10 lines
* Time: 5 min

English:
    1. Given are two points `A: Sequence[int]` and `B: Sequence[int]`
    2. Coordinates are in cartesian system
    3. Points `A` and `B` are in `N`-dimensional space
    4. Points `A` and `B` must be in the same space
    5. Calculate distance between points using Euclidean algorithm
    6. Run doctests - all must succeed

Polish:
    1. Dane są dwa punkty `A: Sequence[int]` i `B: Sequence[int]`
    2. Koordynaty są w systemie kartezjańskim
    3. Punkty `A` i `B` są w `N`-wymiarowej przestrzeni
    4. Punkty `A` i `B` muszą być w tej samej przestrzeni
    5. Oblicz odległość między nimi wykorzystując algorytm Euklidesa
    6. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `for n1, n2 in zip(A, B)`

Tests:
    >>> euclidean_distance_n_dimensions((0,0,0), (0,0,0))
    0.0

    >>> euclidean_distance_n_dimensions((0,0,0), (1,1,1))
    1.7320508075688772

    >>> euclidean_distance_n_dimensions((0,1,0,1), (1,1,0,0))
    1.4142135623730951

    >>> euclidean_distance_n_dimensions((0,0,1,0,1), (1,1,0,0,1))
    1.7320508075688772

    >>> euclidean_distance_n_dimensions((0,0,1,0,1), (1,1))
    Traceback (most recent call last):
    ValueError: Points must be in the same dimensions
"""

from math import sqrt


def euclidean_distance_n_dimensions(A, B):
    ...


# Solution
def euclidean_distance_n_dimensions(A, B):
    if len(A) != len(B):
        raise ValueError('Points must be in the same dimensions')

    under_sqrt = 0

    for n1, n2 in zip(A, B):
        under_sqrt += (n2 - n1) ** 2

    # for index, _ in enumerate(A):
    #     n1 = A[index]
    #     n2 = B[index]
    #     under_sqrt += (n2-n1) ** 2

    # for index in range(len(A)):
    #     n1 = A[index]
    #     n2 = B[index]
    #     under_sqrt += (n2-n1) ** 2

    # number_of_dimensions = len(A)
    # for index in range(number_of_dimensions):
    #     n1 = A[index]
    #     n2 = B[index]
    #     under_sqrt += (n2-n1) ** 2

    return sqrt(under_sqrt)
