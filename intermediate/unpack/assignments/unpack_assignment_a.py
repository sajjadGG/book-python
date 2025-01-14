"""
* Assignment: Unpack Assignment List
* Required: yes
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Separate ip address and host name
    2. Run doctests - all must succeed

Polish:
    1. Odseparuj adres ip i nazwę hosta
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert ip is not Ellipsis, \
    'Assign your result to variable `ip`'
    >>> assert host is not Ellipsis, \
    'Assign your result to variable `host`'
    >>> assert type(ip) is str, \
    'Variable `ip` has invalid type, should be str'
    >>> assert type(host) is str, \
    'Variable `hosts` has invalid type, should be str'

    >>> ip
    '10.13.37.1'

    >>> host
    'nasa.gov'
"""

DATA = ['10.13.37.1', 'nasa.gov']

# String with IP address: 10.13.37.1
# type: str
ip = ...

# String with host name: nasa.gov
# type: str
host = ...

# Solution
ip, host = DATA
