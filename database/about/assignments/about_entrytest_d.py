"""
* Assignment: About EntryTest Endswith
* Complexity: medium
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Define `result: list[str]`
    2. Iterate over `DATA`
    3. Append to `result` emails with top-level domain in DOMAINS
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: list[str]`
    2. Iterując po `DATA`
    3. Dodaj do `result` emaile z domenami najwyższego rzędu w DOMAINS
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result` instead of Ellipsis `...`'
    >>> assert type(result) is list, \
    'Result must be a list'
    >>> assert len(result) > 0, \
    'Result cannot be empty'
    >>> assert all(type(element) is str for element in result), \
    'All elements in result must be a str'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    ['mlewis@nasa.gov', 'rmartinez@nasa.gov', 'avogel@esa.int',
     'cbeck@nasa.gov', 'bjohanssen@nasa.gov', 'mwatney@nasa.gov']
"""

DATA = {
    'mission': 'Ares 3',
    'launch': '2035-06-29',
    'landing': '2035-11-07',
    'destination': 'Mars',
    'location': 'Acidalia Planitia',
    'crew': [{'name': 'Melissa Lewis', 'email': 'mlewis@nasa.gov'},
             {'name': 'Rick Martinez', 'email': 'rmartinez@nasa.gov'},
             {'name': 'Alex Vogel', 'email': 'avogel@esa.int'},
             {'name': 'Chris Beck', 'email': 'cbeck@nasa.gov'},
             {'name': 'Beth Johanssen', 'email': 'bjohanssen@nasa.gov'},
             {'name': 'Mark Watney', 'email': 'mwatney@nasa.gov'},
             {'name': 'Pan Twardowski', 'email': 'ptwardowski@polsa.gov.pl'},
             {'name': 'Ivan Ivanovich', 'email': 'iivanovich@roscosmos.ru'}]}

DOMAINS = ('.gov', '.int')

# list[str]: emails with top-level domain in DOMAINS
result = ...


# Solution
result = []
for astronaut in DATA['crew']:
    if astronaut['email'].endswith(DOMAINS):
        result.append(astronaut['email'])
