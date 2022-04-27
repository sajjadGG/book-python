Syntax Extension
================
* In other programming languages
* PCRE - Perl Compatible Regular Expressions

.. figure:: img/regex-xkcd-standards.png

    How Standards Proliferate. XKCD Standards [#xkcd927]_


Named Ranges
------------
* ``[:allnum:]`` - Alphabetic and numeric character ``[a-zA-Z0-9]``
* ``[:alpha:]`` - Alphabetic character ``[a-zA-Z]``
* ``[:alnum:]`` - Alphabetic and numeric character ``[a-zA-Z0-9]``
* ``[:alpha:]`` - Alphabetic character ``[a-zA-Z]``
* ``[:blank:]`` - Space or tab
* ``[:cntrl:]`` - Control character
* ``[:digit:]`` - Digit
* ``[:graph:]`` - Non-blank character (excludes spaces, control characters, and similar)
* ``[:lower:]`` - Lowercase alphabetical character
* ``[:print:]`` - Like [:graph:], but includes the space character
* ``[:punct:]`` - Punctuation character
* ``[:space:]`` - Whitespace character (``[:blank:]``, newline, carriage return, etc.)
* ``[:upper:]`` - Uppercase alphabetical
* ``[:xdigit:]`` - Digit allowed in a hexadecimal number (i.e., 0-9a-fA-F)
* ``[:word:]`` - A character in one of the following Unicode general categories Letter, Mark, Number, Connector_Punctuation
* ``[:ascii:]`` - A character in the ASCII character set

In Python those Named Ranges does not work. String ``[:alpha:]`` will be
interpreted literally as either: ``:`` or ``a`` or ``l`` or ``p`` or ``h``
or ``a``.

>>> import re
>>> TEXT = 'hello world'
>>>
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
>>> TEXT = 'hello world'
>>>
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

>>> HTML = '<span>Hello World</span>'
>>> re.findall('<(?P<tag>.+)>(?:.+)</(?P=tag)>', HTML)
['span']


References
----------
.. [#xkcd927] Munroe, R. How Standards Proliferate. Year: 2022. Retrieved: 2022-04-27. URL: https://xkcd.com/927/
