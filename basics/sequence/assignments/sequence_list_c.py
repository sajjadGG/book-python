"""
* Assignment: Sequence List Modify
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Insert at the begin of `a` last element popped from `b`
    3. Append to the `b` last element popped from `a`
    4. For getting elements use `list.pop()`
    5. From list `c` using `del` delete last element
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Na początek `a` wstaw ostatni element wyciągnięty z `b`
    3. Na koniec `b` wstaw ostatni element wyciągnięty z `a`
    4. Do wyciągnięcia używaj `list.pop()`
    5. Z listy `c` za pomocą `del` usuń ostatni element
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> import sys
    >>> sys.tracebacklimit = 0

    >>> assert a is not Ellipsis, 'Assignment solution must be in `a` instead of ... (Ellipsis)'
    >>> assert b is not Ellipsis, 'Assignment solution must be in `b` instead of ... (Ellipsis)'
    >>> assert c is not Ellipsis, 'Assignment solution must be in `c` instead of ... (Ellipsis)'
    >>> assert type(a) is list, 'Variable `a` has invalid type, should be list'
    >>> assert type(b) is list, 'Variable `b` has invalid type, should be list'
    >>> assert type(c) is list, 'Variable `c` has invalid type, should be list'

    >>> a
    ['versicolor', 4.7, 3.2, 1.3, 0.2]
    >>> b
    [7.0, 3.2, 4.7, 1.4, 'setosa']
    >>> c
    [7.6, 3.0, 6.6, 2.1]
"""

# Given
a = [4.7, 3.2, 1.3, 0.2, 'setosa']
b = [7.0, 3.2, 4.7, 1.4, 'versicolor']
c = [7.6, 3.0, 6.6, 2.1, 'virginica']

# insert at the begin of `a` last element popped from `b`
# append to the `b` last element popped from `a`
# for getting elements use `list.pop()`
# from list `c` using `del` delete last element

# Solution
a.insert(0, b.pop())
b.append(a.pop())
del c[4]
