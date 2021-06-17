"""
* Assignment: Loop For Segmentation
* Required: yes
* Complexity: easy
* Lines of code: 10 lines
* Time: 8 min

English:
    1. Count occurrences of each group
    2. Define groups:
        a. `small` - numbers in range [0-3)
        b. `medium` - numbers in range [3-7)
        c. `large` - numbers in range [7-10)
    3. Print `result: dict[str, int]`:
        a. key - group
        b. value - number of occurrences
    4. Run doctests - all must succeed

Polish:
    1. Policz wystąpienia każdej z group
    2. Zdefiniuj grupy
        a. `small` - liczby z przedziału <0-3)
        b. `medium` - liczby z przedziału <3-7)
        c. `large` - liczby z przedziału <7-10)
    3. Wypisz `result: dict[str, int]`:
        a. klucz - grupa
        b. wartość - liczba wystąpień
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result)
    <class 'dict'>

    >>> assert all(type(x) is str for x in result.keys())
    >>> assert all(type(x) is int for x in result.values())

    >>> result
    {'small': 16, 'medium': 19, 'large': 15}
"""

DATA = [1, 4, 6, 7, 4, 4, 4, 5, 1, 7, 0,
        0, 6, 5, 0, 0, 9, 7, 0, 4, 4, 8,
        2, 4, 0, 0, 1, 9, 1, 7, 8, 8, 9,
        1, 3, 5, 6, 8, 2, 8, 1, 3, 9, 5,
        4, 8, 1, 9, 6, 3]

# dict[str,int] number of digit occurrences in segments
result = {
        'small': 0,
        'medium': 0,
        'large': 0}

# Solution
SMALL = {0, 1, 2}
MEDIUM = {3, 4, 5, 6}
LARGE = {7, 8, 9}

for digit in DATA:
    if digit in SMALL:
        result['small'] += 1
    elif digit in MEDIUM:
        result['medium'] += 1
    elif digit in LARGE:
        result['large'] += 1

## Alternative Solution
#
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# for digit in DATA:
#     if 0 <= digit < 3:
#         result['small'] += 1
#     elif 3 <= digit < 7:
#         result['medium'] += 1
#     elif 7 <= digit <= 9:
#         result['large'] += 1
# # 13 µs ± 333 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
#
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# for digit in DATA:
#     if digit < 3:
#         result['small'] += 1
#     elif digit < 7:
#         result['medium'] += 1
#     elif digit <= 9:
#         result['large'] += 1
# # 9.41 µs ± 421 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
#
#
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# for digit in DATA:
#     if digit in [0,1,2]:
#         result['small'] += 1
#     elif digit in [3,4,5,6]:
#         result['medium'] += 1
#     elif digit in [7,8,9]:
#         result['large'] += 1
# # 12.2 µs ± 343 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
#
#
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# for digit in DATA:
#     if digit in (0,1,2):
#         result['small'] += 1
#     elif digit in (3,4,5,6):
#         result['medium'] += 1
#     elif digit in (7,8,9):
#         result['large'] += 1
# # 12.2 µs ± 436 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
#
#
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# for digit in DATA:
#     if digit in {0,1,2}:
#         result['small'] += 1
#     elif digit in {3,4,5,6}:
#         result['medium'] += 1
#     elif digit in {7,8,9}:
#         result['large'] += 1
# # 8.92 µs ± 285 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
#
#
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# for digit in DATA:
#     if digit in range(0,3):
#         result['small'] += 1
#     elif digit in range(3,7):
#         result['medium'] += 1
#     elif digit in range(7,10):
#         result['large'] += 1
# # 38.7 µs ± 798 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
#
#
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# SMALL = range(0,3)
# MEDIUM = range(3,7)
# LARGE = range(7,10)
# for digit in DATA:
#     if digit in SMALL:
#         result['small'] += 1
#     elif digit in MEDIUM:
#         result['medium'] += 1
#     elif digit in LARGE:
#         result['large'] += 1
# # 16.3 µs ± 499 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
#
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# SMALL = [0,1,2]
# MEDIUM = [3,4,5,6]
# LARGE = [7,8,9]
# for digit in DATA:
#     if digit in SMALL:
#         result['small'] += 1
#     elif digit in MEDIUM:
#         result['medium'] += 1
#     elif digit in LARGE:
#         result['large'] += 1
# # 13.1 µs ± 902 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
#
#
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# SMALL = (0,1,2)
# MEDIUM = (3,4,5,6)
# LARGE = (7,8,9)
# for digit in DATA:
#     if digit in SMALL:
#         result['small'] += 1
#     elif digit in MEDIUM:
#         result['medium'] += 1
#     elif digit in LARGE:
#         result['large'] += 1
# # 12.4 µs ± 372 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
#
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# SMALL = {0,1,2}
# MEDIUM = {3,4,5,6}
# LARGE = {7,8,9}
# for digit in DATA:
#     if digit in SMALL:
#         result['small'] += 1
#     elif digit in MEDIUM:
#         result['medium'] += 1
#     elif digit in LARGE:
#         result['large'] += 1
# # 9.52 µs ± 342 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
#
#
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# SMALL = [x for x in range(0,3)]
# MEDIUM = [x for x in range(3,7)]
# LARGE = [x for x in range(7,10)]
# for digit in DATA:
#     if digit in SMALL:
#         result['small'] += 1
#     elif digit in MEDIUM:
#         result['medium'] += 1
#     elif digit in LARGE:
#         result['large'] += 1
# # 15.6 µs ± 2.15 µs per loop (mean ± std. dev. of 10 runs, 10000 loops each)
#
#
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# SMALL = (x for x in range(0,3))
# MEDIUM = (x for x in range(3,7))
# LARGE = (x for x in range(7,10))
# for digit in DATA:
#     if digit in SMALL:
#         result['small'] += 1
#     elif digit in MEDIUM:
#         result['medium'] += 1
#     elif digit in LARGE:
#         result['large'] += 1
# # 10.2 µs ± 392 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
#
#
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# SMALL = {x for x in range(0,3)}
# MEDIUM = {x for x in range(3,7)}
# LARGE = {x for x in range(7,10)}
# for digit in DATA:
#     if digit in SMALL:
#         result['small'] += 1
#     elif digit in MEDIUM:
#         result['medium'] += 1
#     elif digit in LARGE:
#         result['large'] += 1
# # 11.1 µs ± 273 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
#
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# for digit in DATA:
#     if digit in [x for x in range(0,3)]:
#         result['small'] += 1
#     elif digit in [x for x in range(3,7)]:
#         result['medium'] += 1
#     elif digit in [x for x in range(7,10)]:
#         result['large'] += 1
# # 70.2 µs ± 1.71 µs per loop (mean ± std. dev. of 10 runs, 10000 loops each)
#
#
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# for digit in DATA:
#     if digit in (x for x in range(0,3)):
#         result['small'] += 1
#     elif digit in (x for x in range(3,7)):
#         result['medium'] += 1
#     elif digit in (x for x in range(7,10)):
#         result['large'] += 1
# # 93.7 µs ± 1.07 µs per loop (mean ± std. dev. of 10 runs, 10000 loops each)
#
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# for digit in DATA:
#     if digit in {x for x in range(0,3)}:
#         result['small'] += 1
#     elif digit in {x for x in range(3,7)}:
#         result['medium'] += 1
#     elif digit in {x for x in range(7,10)}:
#         result['large'] += 1
# # 74.6 µs ± 6.46 µs per loop (mean ± std. dev. of 10 runs, 10000 loops each)
