"""
* Assignment: Type String Clean
* Required: yes
* Complexity: easy
* Lines of code: 8 lines
* Time: 13 min

English:
    1. Expected value is `Jana III Sobieskiego`
    2. Use only `str` methods to clean each variable
    3. Discuss how to create generic solution which fit all cases
    4. Implementation of such generic function will be in `Function Arguments Clean` chapter
    5. Run doctests - all must succeed

Polish:
    1. Oczekiwana wartość `Jana III Sobieskiego`
    2. Wykorzystaj tylko metody `str` do oczyszczenia każdej zmiennej
    3. Przeprowadź dyskusję jak zrobić rozwiązanie generyczne pasujące do wszystkich przypadków
    4. Implementacja takiej generycznej funkcji będzie w rozdziale `Function Arguments Clean`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert example is not Ellipsis, 'Assignment solution must be in `example` instead of ... (Ellipsis)'
    >>> assert a is not Ellipsis, 'Assignment solution must be in `a` instead of ... (Ellipsis)'
    >>> assert b is not Ellipsis, 'Assignment solution must be in `b` instead of ... (Ellipsis)'
    >>> assert c is not Ellipsis, 'Assignment solution must be in `c` instead of ... (Ellipsis)'
    >>> assert d is not Ellipsis, 'Assignment solution must be in `d` instead of ... (Ellipsis)'
    >>> assert e is not Ellipsis, 'Assignment solution must be in `e` instead of ... (Ellipsis)'
    >>> assert f is not Ellipsis, 'Assignment solution must be in `f` instead of ... (Ellipsis)'
    >>> assert g is not Ellipsis, 'Assignment solution must be in `g` instead of ... (Ellipsis)'
    >>> assert h is not Ellipsis, 'Assignment solution must be in `h` instead of ... (Ellipsis)'
    >>> assert i is not Ellipsis, 'Assignment solution must be in `i` instead of ... (Ellipsis)'
    >>> assert type(example) is str, 'Variable `example` has invalid type, should be str'
    >>> assert type(a) is str, 'Variable `a` has invalid type, should be str'
    >>> assert type(b) is str, 'Variable `b` has invalid type, should be str'
    >>> assert type(c) is str, 'Variable `c` has invalid type, should be str'
    >>> assert type(d) is str, 'Variable `d` has invalid type, should be str'
    >>> assert type(e) is str, 'Variable `e` has invalid type, should be str'
    >>> assert type(f) is str, 'Variable `f` has invalid type, should be str'
    >>> assert type(g) is str, 'Variable `g` has invalid type, should be str'
    >>> assert type(h) is str, 'Variable `h` has invalid type, should be str'
    >>> assert type(i) is str, 'Variable `i` has invalid type, should be str'

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

example = 'UL. jana \tTWArdoWskIEGO 3'
a = 'ul Jana III SobIESkiego'
b = '\tul. Jana trzeciego Sobieskiego'
c = 'ulicaJana III Sobieskiego'
d = 'UL. JANA 3 \nSOBIESKIEGO'
e = 'UL. jana III SOBiesKIEGO'
f = 'ULICA JANA III SOBIESKIEGO  '
g = 'ULICA. JANA III SOBIeskieGO'
h = ' Jana 3 Sobieskiego  '
i = 'Jana III\tSobieskiego '

example = example.upper().replace('UL. ', '').replace('\t', '').strip().title().replace('3', 'III')
a = a  # str: Jana III Sobieskiego
b = b  # str: Jana III Sobieskiego
c = c  # str: Jana III Sobieskiego
d = d  # str: Jana III Sobieskiego
e = e  # str: Jana III Sobieskiego
f = f  # str: Jana III Sobieskiego
g = g  # str: Jana III Sobieskiego
h = h  # str: Jana III Sobieskiego
i = i  # str: Jana III Sobieskiego

# Solution
a = a.upper().replace('UL', '').strip().title().replace('Iii', 'III')
b = b.upper().replace('UL.', '').strip().title().replace('Trzeciego', 'III')
c = c.upper().replace('ULICA', '').strip().title().replace('Iii', 'III')
d = d.upper().replace('UL.', '').strip().title().replace('3', 'III').replace('\n', '')
e = e.upper().replace('UL.', '').strip().title().replace('Iii', 'III')
f = f.upper().replace('ULICA', '').strip().title().replace('Iii', 'III')
g = g.upper().replace('ULICA.', '').strip().title().replace('Iii', 'III')
h = h.upper().replace('3', 'III').strip().title().replace('Iii', 'III')
i = i.upper().replace('\t', ' ').strip().title().replace('Iii', 'III')
