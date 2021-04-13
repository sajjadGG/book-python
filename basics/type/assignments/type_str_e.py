"""
* Assignment: Type String Clean
* Complexity: easy
* Lines of code: 8 lines
* Time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Expected value is `Jana III Sobieskiego`
    3. Use only `str` methods to clean each variable
    4. Discuss how to create generic solution which fit all cases
    5. Implementation of such generic function will be in `Function Arguments Clean` chapter
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Oczekiwana wartość `Jana III Sobieskiego`
    3. Wykorzystaj tylko metody `str` do oczyszczenia każdej zmiennej
    4. Przeprowadź dyskusję jak zrobić rozwiązanie generyczne pasujące do wszystkich przypadków
    5. Implementacja takiej generycznej funkcji będzie w rozdziale `Function Arguments Clean`
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> import sys
    >>> sys.tracebacklimit = 0

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

# Given
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
