"""
* Assignment: Numpy Round Floor and Ceil
* Filename: numpy_round_ceilfloor.py
* Complexity: medium
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Ceil round `data` values and assign to `ceil`
    3. Floor round `data` values and assign to `floor`
    4. Round `data` values and assign to `round`
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zaokrąglij wartości `data` w górę (ceil) i przypisz do `ceil`
    3. Zaokrąglij wartości `data` w dół (floor) i przypisz do `floor`
    4. Zaokrąglij wartości `data` i przypisz do `round`
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(ceil) is np.ndarray
    True
    >>> type(floor) is np.ndarray
    True
    >>> type(round) is np.ndarray
    True
    >>> ceil
    array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
           1., 1., 1., 1.])

    >>> floor
    array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           0., 0., 0., 0.])

    >>> round
    array([1., 1., 1., 1., 0., 1., 0., 1., 1., 0., 1., 1., 1., 1., 0., 0., 0.,
           1., 1., 1., 1.])
"""


# Given
import numpy as np
np.random.seed(0)


DATA = np.array([0.5488135 , 0.71518937, 0.60276338, 0.54488318, 0.4236548 ,
                 0.64589411, 0.43758721, 0.891773  , 0.96366276, 0.38344152,
                 0.79172504, 0.52889492, 0.56804456, 0.92559664, 0.07103606,
                 0.0871293 , 0.0202184 , 0.83261985, 0.77815675, 0.87001215,
                 0.97861834])


# Solution
ceil = np.ceil(DATA)
floor = np.floor(DATA)
round = np.round(DATA)
