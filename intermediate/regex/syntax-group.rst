Syntax Group
============


Rationale
---------
* Catch expression results
* Can be named or positional
* Note, that for backreference, must use raw-sting or double backslash

Syntax
------
* ``()`` - matches whatever regular expression is inside the parentheses, and indicates the start and end of a group
* ``(...)`` - unnamed group
* ``(?P<mygroup>...)`` - named group `mygroup`
* ``(?:...)`` - non-capturing group
* ``(?#...)`` - comment


Positional Group
----------------
* ``(...)`` - unnamed (positional) group

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> re.findall(r'\d{2}th', TEXT)
['12th']
>>>
>>> re.findall(r'(\d{2})th', TEXT)
['12']
>>>
>>> re.findall(r'\d{2}(th)', TEXT)
['th']

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> re.findall('\d:\d\d', TEXT)
['6:07']
>>> re.findall('(\d):\d\d', TEXT)
['6']
>>> re.findall('\d:(\d\d)', TEXT)
['07']
>>> re.findall('(\d):(\d\d)', TEXT)
[('6', '07')]

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> re.findall(r'([A-Z][a-z]+\s[A-Z][a-z]+)', TEXT)
['Yuri Gagarin']
>>>
>>> re.findall(r'([A-Z][a-z]+) ([A-Z][a-z]+)', TEXT)
[('Yuri', 'Gagarin')]
>>>
>>> re.findall(r'([A-Z][a-z]+) ([A-Z][a-z]+)', TEXT)[0]
('Yuri', 'Gagarin')

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> firstname = r'([A-Z][a-z]+)'
>>> lastname = r'([A-Z][a-z]+)'
>>>
>>> re.findall(f'{firstname} {lastname}', TEXT)[0]
('Yuri', 'Gagarin')

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> firstname = r'([A-Z][a-z]+)'
>>> lastname = r'([A-Z][a-z]+)'
>>> name = f'{firstname} {lastname}'
>>>
>>> re.findall(name, TEXT)[0]
('Yuri', 'Gagarin')

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> firstname = r'[A-Z][a-z]+'
>>> lastname = r'[A-Z][a-z]+'
>>> name = f'({firstname}) ({lastname})'
>>>
>>> re.findall(name, TEXT)[0]
('Yuri', 'Gagarin')


Named Group
-----------
* ``(?P<mygroup>...)`` - named group `mygroup`


>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> firstname = r'[A-Z][a-z]+'
>>> lastname = r'[A-Z][a-z]+'
>>> name = f'(?P<firstname>{firstname}) (?P<lastname>{lastname})'
>>>
>>> re.findall(name, TEXT)
[('Yuri', 'Gagarin')]
>>>
>>> re.search(name, TEXT)
<re.Match object; span=(0, 12), match='Yuri Gagarin'>
>>>
>>> re.search(name, TEXT).groups()
('Yuri', 'Gagarin')
>>>
>>> re.search(name, TEXT).groupdict()
{'firstname': 'Yuri', 'lastname': 'Gagarin'}

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> re.findall('(?P<hour>\d):(?P<minute>\d\d)', TEXT)
[('6', '07')]
>>>
>>> re.search('(?P<hour>\d):(?P<minute>\d\d)', TEXT).groups()
('6', '07')
>>>
>>> re.search('(?P<hour>\d):(?P<minute>\d\d)', TEXT).group(0)
'6:07'
>>>
>>> re.search('(?P<hour>\d):(?P<minute>\d\d)', TEXT).group(1)
'6'
>>>
>>> re.search('(?P<hour>\d):(?P<minute>\d\d)', TEXT).group(2)
'07'
>>>
>>> re.search('(?P<hour>\d):(?P<minute>\d\d)', TEXT).groupdict()
{'hour': '6', 'minute': '07'}


Non-Capturing Group
-------------------
* ``(?:...)``

>>> import re
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'

>>> re.findall('[A-Z][a-z][a-z] \d{1,2}th, \d{4}', TEXT)
['Apr 12th, 1961']
>>>
>>> re.findall('[A-Z][a-z][a-z] \d{1,2}st|nd|rd|th, \d{4}', TEXT)
['th, 1961']
>>>
>>> re.findall('[A-Z][a-z][a-z] \d{1,2}(st|nd|rd|th), \d{4}', TEXT)
['th']
>>>
>>> re.findall('[A-Z][a-z][a-z] \d{1,2}(?:st|nd|rd|th), \d{4}', TEXT)
['Apr 12th, 1961']
>>>
>>> re.findall('([A-Z][a-z][a-z]) (\d{1,2})(?:st|nd|rd|th), (\d{4})', TEXT)
[('Apr', '12', '1961')]
>>>
>>> re.findall('([A-Z][a-z][a-z]) (\d{1,2})(st|nd|rd|th), (\d{4})', TEXT)
[('Apr', '12', 'th', '1961')]
>>>

>>> import re
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>>
>>> date = r'([A-Z][a-z]{2} \d{2}(?:st|nd|rd|th), \d{4})'
>>> re.findall(date, TEXT)
['Apr 12th, 1961']
>>>

>>> import re
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> year = '\d{4}'
>>> month = '[A-Z][a-z]{2}'
>>> day = '\d{2}'
>>>
>>> re.findall(f'{month} {day}(st|nd|rd|th), {year}', TEXT)
['th']
>>>
>>> re.findall(f'{month} {day}(?:st|nd|rd|th), {year}', TEXT)
['Apr 12th, 1961']


Comment
-------
* ``(?#...)`` - comment

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> re.findall(r'\d{4}(?#year)', TEXT)
['1961']

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> re.findall('\d{1,2}(?#hour):\d{2}(?#minute)', TEXT)
['6:07']

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> hour = '\d{1,2}(?#hour)'
>>> minute = '\d{2}(?#minute)'
>>> time = f'{hour}:{minute}'
>>>
>>> re.findall(time, TEXT)
['6:07']
>>>
>>> time
'\\d{1,2}(?#hour):\\d{2}(?#minute)'

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


>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> re.findall(r'\d{,2}(st|nd|rd|th)?', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
 '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
 'th', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
>>>
>>> re.findall(r'\d{2}(st|nd|rd|th)?', TEXT)
['th', '', '', '']
>>>
>>> re.findall(r'\d{2}(st|nd|rd|th)+?', TEXT)
['th']
>>>
>>> re.findall(r'\d{2}st|nd|rd|th+?', TEXT)
['th']
>>>
>>> re.findall(r'\d{2}(?:st|nd|rd|th)+?', TEXT)
['12th']
>>>
>>> re.findall(r'(\d{2})(st|nd|rd|th)+?', TEXT)
[('12', 'th')]
>>>
>>> re.findall(r'(\d{2})(?:st|nd|rd|th)+?', TEXT)
['12']
>>>
>>> re.findall(r'([A-Z][a-z]{2}) (\d{2})(?:st|nd|rd|th)+?, (\d{4})', TEXT)
[('Apr', '12', '1961')]
>>>
>>> re.findall(r'([A-Z][a-z]{2}) (\d{2})(?:st|nd|rd|th)+?, (\d{4})', TEXT)[0]
('Apr', '12', '1961')
>>>
>>> re.findall(r'([A-Z][a-z]{2} \d{2}(?:st|nd|rd|th)+?, \d{4})', TEXT)
['Apr 12th, 1961']


Use Case - 0x01
---------------
* Dates

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> year = r'(?P<year>\d{4})'
>>> month = r'(?P<month>[A-Z][a-z]{2})'
>>> day = r'(?P<day>\d{2}(?:st|nd|rd|th)+?)'
>>> date = f'{month} {day}, {year}'
>>>
>>> re.search(date, TEXT).groupdict()
{'month': 'Apr', 'day': '12th', 'year': '1961'}


Use Case - 0x02
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


Use Case - 0x03
---------------
>>> import re
>>>
>>>
>>> variable = '(?P<variable>\w+)'
>>> space = '\s?'  # optional space
>>> value = '(?P<value>.+)'
>>> assignment = f'^{variable}{space}={space}{value}$'
>>>
>>> line_of_code = 'myvar = 123'
>>> re.findall(assignment, line_of_code)
[('myvar', '123')]


Use Case - 0x04
---------------
>>> import re
>>>
>>>
>>> variable = '(?P<variable>\w+)'
>>> space = '\s?(?#optional space)'
>>> value = '(?P<value>.+)'
>>> assignment = f'^{variable}{space}={space}{value}$'
>>>
>>> assignment
'^(?P<variable>\\w+)\\s?(?#optional space)=\\s?(?#optional space)(?P<value>.+)$'
