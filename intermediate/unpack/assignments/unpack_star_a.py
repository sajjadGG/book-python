"""
* Assignment: Unpack Star List
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Separate ip address and host names
    2. Use asterisk `*` notation
    3. Run doctests - all must succeed

Polish:
    1. Odseparuj adres ip i nazw hostów
    2. Skorzystaj z notacji z gwiazdką `*`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert ip is not Ellipsis, \
    'Assign result to variable: `ip`'
    >>> assert hosts is not Ellipsis, \
    'Assign result to variable: `hosts`'
    >>> assert type(ip) is str, \
    'Variable `ip` has invalid type, should be str'
    >>> assert type(hosts) is list, \
    'Variable `hosts` has invalid type, should be list'
    >>> assert all(type(x) is str for x in hosts), \
    'All rows in `hosts` should be str'
    >>> assert '' not in hosts, \
    'Do not pass any arguments to str.split() method'

    >>> ip
    '10.13.37.1'

    >>> hosts
    ['nasa.gov', 'esa.int', 'roscosmos.ru']
"""

DATA = ['10.13.37.1', 'nasa.gov', 'esa.int', 'roscosmos.ru']

# str: IP address
ip = ...

# list[str]: list of hostnames
hosts = ...

# Solution
ip, *hosts = DATA
