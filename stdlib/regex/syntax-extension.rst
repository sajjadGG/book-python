Syntax Extension
================


Rationale
---------
* In other programming languages
* PCRE - Perl Compatible Regular Expressions


Named Ranges
------------
* ``[:allnum:]`` == ``[a-zA-Z0-9]``
* ``[:alpha:]`` == ``[a-zA-Z]``
* Python will treat this literally as either: ``:`` or ``a`` or ``l``
  or ``p`` or ``h`` or ``a``.

>>> import re
>>>
>>>
>>> TEXT = 'hello world'
>>>
>>> re.findall('[:allnum:]', TEXT)
['l', 'l', 'l']
>>>
>>> re.findall('[:alpha:]', TEXT)
['h', 'l', 'l', 'l']


Range
-----
* ``[a-Z]`` == ``[a-zA-Z]``
* ``[a-9]`` == ``[a-zA-Z0-9]``
* Works in other languages, but not in Python

>>> import re
>>>
>>>
>>> TEXT = 'hello world'
>>>
>>> re.findall('[a-Z]', TEXT)
Traceback (most recent call last):
re.error: bad character range a-Z at position 1
>>>
>>> re.findall('[a-9]', TEXT)
Traceback (most recent call last):
re.error: bad character range a-9 at position 1


Group Backreference
-------------------
* ``$1`` == ``\1``
