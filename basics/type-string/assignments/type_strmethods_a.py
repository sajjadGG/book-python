"""
* Assignment: Type String Normalize
* Required: yes
* Complexity: easy
* Lines of code: 4 lines
* Time: 8 min

English:
    1. Use `str` methods to clean `DATA`
    2. Run doctests - all must succeed

Polish:
    1. Wykorzystaj metody `str` do oczyszczenia `DATA`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, 'Assignment solution must be in `result` instead of ... (Ellipsis)'
    >>> assert type(result) is str, 'Variable `result` has invalid type, should be str'

    >>> result
    'Jana Twardowskiego III'
"""

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
