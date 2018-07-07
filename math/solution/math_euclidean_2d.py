import math


def euclidean_distance(A, B):
    """
    >>> A = (1, 0)
    >>> B = (0, 1)
    >>> euclidean_distance(A, B)
    1.4142135623730951

    >>> euclidean_distance((0,0), (1,0))
    1.0

    >>> euclidean_distance((0,0), (1,1))
    1.4142135623730951

    >>> euclidean_distance((0,1), (1,1))
    1.0

    >>> euclidean_distance((0,10), (1,1))
    9.055385138137417
    """

    x1 = A[0]
    x2 = B[0]

    y1 = A[1]
    y2 = B[1]

    odleglosc_x = (x2-x1) ** 2
    odleglosc_y = (y2-y1) ** 2

    return math.sqrt(odleglosc_x + odleglosc_y)
