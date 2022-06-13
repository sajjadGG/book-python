RE Group
========
* Match particular parts of a string
* Possible to name matches


Syntax
------
Define:

    * ``(...)`` - Positional group
    * ``(?P<name>...)`` - Named group
    * ``(?:...)`` - Non-matching group
    * ``(?#...)`` - Comment

Backreference:

    * ``(?P=name)``- Backreferencing by group name
    * ``\number`` - Backreferencing by group number

Example:

    * ``(?P<tag><.*?>)text(?P=tag)``
    * ``(?P<tag><.*?>)text\1``
    * ``(.+) \1`` matches ``the the`` or ``55 55``
    * ``(.+) \1`` not matches ``thethe`` (note the space after the group)


Positional Groups
-----------------
>>> import re
>>>
>>>
>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 1:37 pm'
>>>
>>> pattern = r'(\w+) (\w+)'
>>> result = re.match(pattern, TEXT)
>>>
>>> result
<re.Match object; span=(0, 11), match='Mark Watney'>
>>>
>>> result.group()
'Mark Watney'
>>>
>>> result.group(1)
'Mark'
>>>
>>> result.group(2)
'Watney'
>>>
>>> result.groups()
('Mark', 'Watney')


Named Groups
------------
* Usage of group in ``re.match()``

>>> import re
>>>
>>>
>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 1:37 pm'
>>>
>>> pattern = r'(?P<firstname>\w+) (?P<lastname>\w+)'
>>> result = re.match(pattern, TEXT)
>>>
>>> result.group('firstname')
'Mark'
>>>
>>> result.group('lastname')
'Watney'
>>>
>>> result.group(1)
'Mark'
>>>
>>> result.group(2)
'Watney'
>>>
>>> result.groups()
('Mark', 'Watney')
>>>
>>> result.groupdict()
{'firstname': 'Mark', 'lastname': 'Watney'}


Use Case - 0x01
---------------
>>> import re
>>>
>>>
>>> line = 'value=123'
>>>
>>> re.findall(r'(\w+)\s?=\s?(\d+)', line)
[('value', '123')]

>>> import re
>>>
>>>
>>> line = 'value = 123'
>>>
>>> re.findall(r'(\w+)\s?=\s?(\d+)', line)
[('value', '123')]
