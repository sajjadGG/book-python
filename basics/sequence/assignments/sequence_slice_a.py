"""
* Assignment: Sequence Slice Text
* Required: yes
* Complexity: easy
* Lines of code: 8 lines
* Time: 8 min

English:
    1. Remove title and military rank in each variable
    2. Remove also whitespaces at the beginning and end of a text
    3. Use only `slice` to clean text
    4. Run doctests - all must succeed

Polish:
    1. Usuń tytuł naukowy i stopień wojskowy z każdej zmiennej
    2. Usuń również białe znaki na początku i końcu tekstu
    3. Użyj tylko `slice` do oczyszczenia tekstu
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert a is not Ellipsis, 'Assignment solution must be in `a` instead of ... (Ellipsis)'
    >>> assert b is not Ellipsis, 'Assignment solution must be in `b` instead of ... (Ellipsis)'
    >>> assert c is not Ellipsis, 'Assignment solution must be in `c` instead of ... (Ellipsis)'
    >>> assert d is not Ellipsis, 'Assignment solution must be in `d` instead of ... (Ellipsis)'
    >>> assert e is not Ellipsis, 'Assignment solution must be in `e` instead of ... (Ellipsis)'
    >>> assert f is not Ellipsis, 'Assignment solution must be in `f` instead of ... (Ellipsis)'
    >>> assert g is not Ellipsis, 'Assignment solution must be in `g` instead of ... (Ellipsis)'
    >>> assert type(a) is str, 'Variable `a` has invalid type, should be str'
    >>> assert type(b) is str, 'Variable `b` has invalid type, should be str'
    >>> assert type(c) is str, 'Variable `c` has invalid type, should be str'
    >>> assert type(d) is str, 'Variable `d` has invalid type, should be str'
    >>> assert type(e) is str, 'Variable `e` has invalid type, should be str'
    >>> assert type(f) is str, 'Variable `f` has invalid type, should be str'
    >>> assert type(g) is str, 'Variable `g` has invalid type, should be str'

    >>> example
    'Mark Watney'
    >>> a
    'Jan Twardowski'
    >>> b
    'Jan Twardowski'
    >>> c
    'Mark Watney'
    >>> d
    'Melissa Lewis'
    >>> e
    'Ryan Stone'
    >>> f
    'Ryan Stone'
    >>> g
    'Jan Twardowski'
"""

example = 'lt. Mark Watney, PhD'
a = 'dr hab. inż. Jan Twardowski, prof. AATC'
b = 'gen. pil. Jan Twardowski'
c = 'Mark Watney, PhD'
d = 'lt. col. ret. Melissa Lewis'
e = 'dr n. med. Ryan Stone'
f = 'Ryan Stone, MD-PhD'
g = 'lt. col. Jan Twardowski\t'

example: str = example[4:-5]
a  # str: Jan Twardowski
b  # str: Jan Twardowski
c  # str: Mark Watney
d  # str: Melissa Lewis
e  # str: Ryan Stone
f  # str: Ryan Stone
g  # str: Jan Twardowski

# Solution
a = a[13:-12]
b = b[10:]
c = c[:-5]
d = d[14:]
e = e[11:]
f = f[:-8]
g = g[9:-1]
