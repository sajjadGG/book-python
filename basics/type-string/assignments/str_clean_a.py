"""
* Assignment: Str Clean Strings
* Required: yes
* Complexity: easy
* Lines of code: 8 lines
* Time: 13 min

English:
    1. Expected value is `Jana III Sobieskiego`
    2. Use only `str` methods to clean each variable
    3. Discuss how to create generic solution which fit all cases
    4. Implementation of such generic function will be in
       `Function Arguments Clean` chapter
    5. Run doctests - all must succeed

Polish:
    1. Oczekiwana wartość `Jana III Sobieskiego`
    2. Wykorzystaj tylko metody `str` do oczyszczenia każdej zmiennej
    3. Przeprowadź dyskusję jak zrobić rozwiązanie generyczne pasujące
       do wszystkich przypadków
    4. Implementacja takiej generycznej funkcji będzie w rozdziale
       `Function Arguments Clean`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert example is not Ellipsis, \
    'Assign result to variable: `example`'
    >>> assert a is not Ellipsis, \
    'Assign result to variable: `a`'
    >>> assert b is not Ellipsis, \
    'Assign result to variable: `b`'
    >>> assert c is not Ellipsis, \
    'Assign result to variable: `c`'
    >>> assert d is not Ellipsis, \
    'Assign result to variable: `d`'
    >>> assert e is not Ellipsis, \
    'Assign result to variable: `e`'
    >>> assert f is not Ellipsis, \
    'Assign result to variable: `f`'
    >>> assert g is not Ellipsis, \
    'Assign result to variable: `g`'
    >>> assert h is not Ellipsis, \
    'Assign result to variable: `h`'
    >>> assert i is not Ellipsis, \
    'Assign result to variable: `i`'
    >>> assert type(example) is str, \
    'Variable `example` has invalid type, should be str'
    >>> assert type(a) is str, \
    'Variable `a` has invalid type, should be str'
    >>> assert type(b) is str, \
    'Variable `b` has invalid type, should be str'
    >>> assert type(c) is str, \
    'Variable `c` has invalid type, should be str'
    >>> assert type(d) is str, \
    'Variable `d` has invalid type, should be str'
    >>> assert type(e) is str, \
    'Variable `e` has invalid type, should be str'
    >>> assert type(f) is str, \
    'Variable `f` has invalid type, should be str'
    >>> assert type(g) is str, \
    'Variable `g` has invalid type, should be str'
    >>> assert type(h) is str, \
    'Variable `h` has invalid type, should be str'
    >>> assert type(i) is str, \
    'Variable `i` has invalid type, should be str'

    >>> example
    'Jana Twardowskiego III'
    >>> a
    'Jana III Sobieskiego'
    >>> b
    'Jana III Sobieskiego'
    >>> c
    'Jana III Sobieskiego'
    >>> d
    'Jana III Sobieskiego'
    >>> e
    'Jana III Sobieskiego'
    >>> f
    'Jana III Sobieskiego'
    >>> g
    'Jana III Sobieskiego'
    >>> h
    'Jana III Sobieskiego'
    >>> i
    'Jana III Sobieskiego'
"""

EXAMPLE = 'UL. jana \tTWArdoWskIEGO 3'
A = 'ul Jana III SobIESkiego'
B = '\tul. Jana trzeciego Sobieskiego'
C = 'ulicaJana III Sobieskiego'
D = 'JANA 3 \nSOBIESKIEGO'
E = 'UL. jana III SOBiesKIEGO'
F = 'ULICA JANA III SOBIESKIEGO  '
G = 'ULICA. JANA III SOBIeskieGO'
H = ' Jana 3 Sobieskiego  '
I = 'Jana III\tSobieskiego '

example = EXAMPLE.upper().replace('UL. ', '').replace('\t', '') \
    .strip().title().replace('3', 'III')

# str: Jana III Sobieskiego
a = ...

# str: Jana III Sobieskiego
b = ...

# str: Jana III Sobieskiego
c = ...

# str: Jana III Sobieskiego
d = ...

# str: Jana III Sobieskiego
e = ...

# str: Jana III Sobieskiego
f = ...

# str: Jana III Sobieskiego
g = ...

# str: Jana III Sobieskiego
h = ...

# str: Jana III Sobieskiego
i = ...

# Solution
a = A.upper().replace('UL', '').strip().title().replace('Iii', 'III')
b = B.upper().replace('UL.', '').strip().title().replace('Trzeciego', 'III')
c = C.upper().replace('ULICA', '').strip().title().replace('Iii', 'III')
d = D.upper().replace('\n', '').strip().title().replace('3', 'III')
e = E.upper().replace('UL.', '').strip().title().replace('Iii', 'III')
f = F.upper().replace('ULICA', '').strip().title().replace('Iii', 'III')
g = G.upper().replace('ULICA.', '').strip().title().replace('Iii', 'III')
h = H.upper().replace('3', 'III').strip().title().replace('Iii', 'III')
i = I.upper().replace('\t', ' ').strip().title().replace('Iii', 'III')
