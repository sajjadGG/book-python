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
    3. Run doctests - all must succeed

Polish:
    1. Policz wystąpienia każdej z group
    2. Zdefiniuj grupy:
        a. `small` - liczby z przedziału <0-3)
        b. `medium` - liczby z przedziału <3-7)
        c. `large` - liczby z przedziału <7-10)
    3. Uruchom doctesty - wszystkie muszą się powieść

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
result = {'small': 0, 'medium': 0, 'large': 0}

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

# Alternative Solution
#
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# for digit in DATA:
#     if 0 <= digit < 3:
#         result['small'] += 1
#     elif 3 <= digit < 7:
#         result['medium'] += 1
#     elif 7 <= digit < 10:
#         result['large'] += 1
#
#
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# for digit in DATA:
#     if 0 <= digit and digit < 3:
#         result['small'] += 1
#     elif 3 <= digit and digit < 7:
#         result['medium'] += 1
#     elif 7 <= digit and digit < 10:
#         result['large'] += 1
#
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# for digit in DATA:
#     if 0 <= digit < 3:
#         result['small'] += 1
#     elif 3 <= digit < 7:
#         result['medium'] += 1
#     else:
#         result['large'] += 1
#
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# for digit in DATA:
#     if digit < 3:
#         result['small'] += 1
#     elif digit < 7:
#         result['medium'] += 1
#     elif digit < 10:
#         result['large'] += 1
#
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# for digit in DATA:
#     if digit < 3:
#         result['small'] += 1
#     elif digit < 7:
#         result['medium'] += 1
#     else:
#         result['large'] += 1
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
#
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# SMALL = {x for x in (0,1,2)}
# MEDIUM = {x for x in (3,4,5,6)}
# LARGE = {x for x in (7,8,9)}
# for digit in DATA:
#     if digit in SMALL:
#         result['small'] += 1
#     elif digit in MEDIUM:
#         result['medium'] += 1
#     elif digit in LARGE:
#         result['large'] += 1
#
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# SMALL = (x for x in (0,1,2))
# MEDIUM = (x for x in (3,4,5,6))
# LARGE = (x for x in (7,8,9))
# for digit in DATA:
#     if digit in SMALL:
#         result['small'] += 1
#     elif digit in MEDIUM:
#         result['medium'] += 1
#     elif digit in LARGE:
#         result['large'] += 1
#
# %%timeit -r 10 -n 10000
# result = {'small': 0,'medium': 0,'large': 0}
# SMALL = [x for x in (0,1,2)]
# MEDIUM = [x for x in (3,4,5,6)]
# LARGE = [x for x in (7,8,9)]
# for digit in DATA:
#     if digit in SMALL:
#         result['small'] += 1
#     elif digit in MEDIUM:
#         result['medium'] += 1
#     elif digit in LARGE:
#         result['large'] += 1
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
