"""
* Assignment: Numpy Trigonometry
* Complexity: easy
* Lines of code: 8 lines
* Time: 13 min

English:
    1. Define function `trigonometry(angle_deg: int|float) -> dict`
    2. Return angle in radians and trigonometric function values (sin, cos, tg, ctg)
    3. Ctg for angle 180 and Tan for 90 degrees has infinite value, return `np.inf`

Polish:
    1. Zdefiniuj funkcję `trigonometry(angle_deg: int|float) -> dict`
    2. Zwróć kąt w radianach oraz wartości funkcji trygonometrycznych (sin, cos, tg, ctg)
    3. Ctg dla angle 180 oraz Tan dla 0 i 90 stopni ma wartość nieskończoną, zwróć `np.inf`

Tests:
    >>> trigonometry(180)  # doctest: +NORMALIZE_WHITESPACE
    {'rad': 3.141592653589793,
     'sin': 1.2246467991473532e-16,
     'cos': -1.0,
     'tan': inf,
     'ctg': -8165619676597685.0}
    >>> trigonometry(90)  # doctest: +NORMALIZE_WHITESPACE
    {'rad': 1.5707963267948966,
     'sin': 1.0,
     'cos': 6.123233995736766e-17,
     'tan': 1.633123935319537e+16, 'ctg': inf}
    >>> trigonometry(0)
    {'rad': 0.0, 'sin': 0.0, 'cos': 1.0, 'tan': 0.0, 'ctg': inf}
    >>> trigonometry(np.pi)  # doctest: +NORMALIZE_WHITESPACE
    {'rad': 0.05483113556160755,
     'sin': 0.05480366514878953,
     'cos': 0.9984971498638638,
     'tan': 0.054886150808003326,
     'ctg': 18.21953234611204}
"""


# Given
import numpy as np


def trigonometry(angle_deg):
    return {
        'rad': ...,
        'sin': ...,
        'cos': ...,
        'tan': ...,
        'ctg': ...,
    }


# Solution
def trigonometry(angle_deg):
    angle_rad = np.deg2rad(angle_deg)
    return {
        'rad': np.deg2rad(angle_deg),
        'sin': np.sin(angle_rad),
        'cos': np.cos(angle_rad),
        'tan': np.tan(angle_rad) if angle_deg != 180 else np.inf,
        'ctg': 1/np.tan(angle_rad) if angle_deg not in (90, 0) else np.inf,
    }
