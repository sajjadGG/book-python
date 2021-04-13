"""
* Assignment: Type String Normalize
* Complexity: easy
* Lines of code: 4 lines
* Time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Use `str` methods to clean `DATA`
    3. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wykorzystaj metody `str` do oczyszczenia `DATA`
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> import sys
    >>> sys.tracebacklimit = 0

    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> result
    'Jana Twardowskiego III'
"""

# Given
DATA = 'UL. jana \tTWArdoWskIEGO 3'

result = ...  # str: Jana Twardowskiego III

# Solution
result = DATA.replace('UL. ', '').replace('\t', '').title().replace('3', 'III')


# Alternative Solution
result = (DATA
        # Convert to common format
        .upper()
        # Remove unwanted whitespaces
        .replace('\n', '')
        .replace('\t', '')
        .replace('     ', '')
        .replace('    ', '')
        .replace('   ', '')
        .replace('  ', '')
        # Remove unwanted special characters
        .replace('.', '')
        .replace(',', '')
        .replace('-', '')
        .replace('|', '')
        # Remove unwanted text
        .replace('ULICA', '')
        .replace('UL', '')
        .replace('TRZECIEGO', 'III')
        .replace('3', 'III')
        # Formatting
        .title()
        .replace('Iii', 'III')
        .replace('Ii', 'II')
        .strip())
