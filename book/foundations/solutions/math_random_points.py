import random
from matplotlib import pyplot as plt


def random_point(center, std=0.2):
    if not isinstance(std, (tuple, list)):
        std = (std, std)

    x = random.gauss(center[0], std[0])
    y = random.gauss(center[1], std[1])

    return x, y


def distance(A, B):
    """
    Wylicz odległość między punktami A i B.

    Argumenty:
        A: punkt w przestrzeni wielowymiarowej zdefiniowany następująco:
            [x, y, z, ...]
        B: punkt w przestrzeni wielowymiarowej zdefiniowany następująco:
            [x, y, z, ...]

    Zwraca:
        Odległość euklidesową między punktami A i B.

    >>> distance((0,0), (1,0))
    1.0

    >>> distance((0,0), (1,1))
    1.4142135623730951
    """
    suma = 0
    for a, b in zip(A, B):
        suma += (b - a) ** 2

    return suma ** 0.5


def plot_list_of_points(list_of_points, color='black'):
    """
    Wyrysowuje listę punktów na aktualnie aktywnym wykresie.

    Argumenty:
        list_of_points: lista punktów, zgodnie z konwencją:
            [[x1, y1], [x2, y2], [x3, y3], ...]
        color: kolor jakim mają być punkty narysowane. Domyślnie czarny.
    """
    plt.plot([p[0] for p in list_of_points],
             [p[1] for p in list_of_points],
             'o',
             color=color,
             alpha=0.3)
