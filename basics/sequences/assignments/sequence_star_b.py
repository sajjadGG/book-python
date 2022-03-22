"""
* Assignment: Sequence UnpackStar Split
* Required: yes
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Separate ip address from host names
    2. Use asterisk `*` notation
    3. Run doctests - all must succeed

Polish:
    1. Odseparuj adres ip od nazwy hostów
    2. Skorzystaj z notacji z gwiazdką `*`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `str.split()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert ip is not Ellipsis, \
    'Assign result to variable: `ip`'
    >>> assert hosts is not Ellipsis, \
    'Assign result to variable: `hosts`'

    >>> assert type(ip) is str
    >>> assert type(hosts) is list
    >>> assert all(type(host) is str for host in hosts)
    >>> '' not in hosts
    True

    >>> ip
    '10.13.37.1'

    >>> hosts
    ['nasa.gov', 'esa.int', 'roscosmos.ru']
"""

DATA = '10.13.37.1      nasa.gov esa.int roscosmos.ru'

# ip address: '10.13.37.1'
# type: str
ip = ...

# list of host names: ['nasa.gov', 'esa.int', 'roscosmos.ru']
# type: list[str]
hosts = ...

# Solution
ip, *hosts = DATA.split()
