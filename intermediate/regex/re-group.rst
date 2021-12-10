RE Group
========


Rationale
---------
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
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> pattern = r'(\w+) (\w+)'
>>> result = re.match(pattern, TEXT)
>>>
>>> result
<re.Match object; span=(0, 12), match='Yuri Gagarin'>
>>>
>>> result.group()
'Yuri Gagarin'
>>>
>>> result.group(1)
'Yuri'
>>>
>>> result.group(2)
'Gagarin'
>>>
>>> result.groups()
('Yuri', 'Gagarin')


Named Groups
------------
* Usage of group in ``re.match()``

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> pattern = r'(?P<firstname>\w+) (?P<lastname>\w+)'
>>> result = re.match(pattern, TEXT)
>>>
>>> result.group('firstname')
'Yuri'
>>>
>>> result.group('lastname')
'Gagarin'
>>>
>>> result.group(1)
'Yuri'
>>>
>>> result.group(2)
'Gagarin'
>>>
>>> result.groups()
('Yuri', 'Gagarin')
>>>
>>> result.groupdict()
{'firstname': 'Yuri', 'lastname': 'Gagarin'}


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
