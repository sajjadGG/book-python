Regex Group
===========


Rationale
---------
* Catch expression results
* Can be named or positional
* Note, that for backreference, must use raw-sting or double backslash


Syntax
------
* ``()`` - matches whatever regular expression is inside the parentheses, and indicates the start and end of a group
* ``(...)`` - unnamed group
* ``(?P<mygroup>...)`` - define named group `mygroup`
* ``(?:...)`` - non-capturing group
* ``(?#...) - comment


Backreference
-------------
    * ``\g<number>`` - backreferencing by group number
    * ``\g<name>`` - backreferencing by group name
    * ``(?P=name)`` - backreferencing by group name
    * ``\number`` - backreferencing by group number


Examples
--------
* ``(\w+)`` - word character (including unicode chars, numbers an underscores)
* ``\d+(\.\d+)?`` - float with optional decimals
* ``\d+(,\d+)?`` - number with coma (``,``) as  thousands separator
* ``(?P<word>\w+)`` - name group `word` with ``\w+`` with at least one word character (including unicode chars, numbers an underscores)
* ``(?P<tag><.*?>).+(?P=tag)`` - matches text inside of a ``<tag>`` (opening and closing tag is the same)
* ``(.+) \1`` - matches ``the the`` or ``55 55``
* ``(.+) \1`` - not matches ``thethe`` (note the space after the group)


Use Case
--------
>>> import re
>>>
>>>
>>> DATA = 'My name... José Jiménez'
>>> result = re.search(r'(?P<firstname>[A-Z]\w+) (?P<lastname>[A-Z]\w+)', DATA)
>>>
>>> result.groupdict()
{'firstname': 'José', 'lastname': 'Jiménez'}
>>> result.groups()
('José', 'Jiménez')
>>> result[0]
'José Jiménez'
>>> result[1]
'José'
>>> result[2]
'Jiménez'
