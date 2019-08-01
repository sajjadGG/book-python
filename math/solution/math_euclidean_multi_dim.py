import math


def euclidean_distance_n_dimensions(A, B):
    """
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
        ...
    ValueError: Points must be in the same dimensions
    """
    if len(A) != len(B):
        raise ValueError('Points must be in the same dimensions')

    number_of_dimensions = len(A)
    under_root = 0

    # for index, _ in enumerate(A):
    #     n1 = A[index]
    #     n2 = B[index]
    #     under_root += (n2-n1) ** 2

    for index in range(number_of_dimensions):
        n1 = A[index]
        n2 = B[index]
        under_root += (n2-n1) ** 2

    return math.sqrt(under_root)
