Syntax Identifier
=================
* Identifiers specifies what to find
* They are also called Character Classes


SetUp
-----
>>> import re


Numeric
-------
* ``\d`` - digit
* ``\D`` - anything but digit

>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 1:37 pm'

>>> re.findall(r'[0-9]', TEXT)
['3', '7', '2', '0', '3', '5', '1', '3', '7']

>>> re.findall(r'\d', TEXT)
['3', '7', '2', '0', '3', '5', '1', '3', '7']

>>> re.findall(r'\D', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['M', 'a', 'r', 'k', ' ', 'W', 'a', 't', 'n', 'e', 'y', ' ', 'o', 'f',
 ' ', 'A', 'r', 'e', 's', ' ', ' ', 'l', 'a', 'n', 'd', 'e', 'd', ' ',
 'o', 'n', ' ', 'M', 'a', 'r', 's', ' ', 'o', 'n', ':', ' ', 'N', 'o',
 'v', ' ', 't', 'h', ',', ' ', ' ', 'a', 't', ' ', ':', ' ', 'p', 'm']


Whitespaces
-----------
* ``\s`` - whitespace (space, tab, newline, non-breaking space)
* ``\S`` - anything but whitespace
* ``\n`` - newline
* ``\r\n`` - windows newline
* ``\r`` - carriage return
* ``\b`` - backspace
* ``\t`` - tab
* ``\v`` - vertical space
* ``\f`` - form feed

>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 1:37 pm'

>>> re.findall(r'\s', TEXT)
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

>>> re.findall(r'\S', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['M', 'a', 'r', 'k', 'W', 'a', 't', 'n', 'e', 'y', 'o', 'f', 'A', 'r',
 'e', 's', '3', 'l', 'a', 'n', 'd', 'e', 'd', 'o', 'n', 'M', 'a', 'r',
 's', 'o', 'n', ':', 'N', 'o', 'v', '7', 't', 'h', ',', '2', '0', '3',
 '5', 'a', 't', '1', ':', '3', '7', 'p', 'm']

>>> re.findall(r'\n', TEXT)
[]
>>>
>>> re.findall(r'\r\n', TEXT)
[]
>>>
>>> re.findall(r'\r', TEXT)
[]


Anchors
-------
* Matches the empty string, but only at the beginning or end of a word
* ``\b`` - word boundary
* ``\B`` - anything but word boundary

Examples:

    * ``\babc\b`` - performs a "whole words only" search
    * ``\Babc\B`` - pattern is fully surrounded by word characters

>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 1:37 pm'

>>> re.findall(r'[a-z][a-z]', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['ar', 'at', 'ne', 'of', 're', 'la', 'nd', 'ed', 'on', 'ar', 'on', 'ov', 'th', 'at', 'pm']

>>> re.findall(r'\b[a-z][a-z]\b', TEXT)
['of', 'on', 'on', 'at', 'pm']

>>> re.findall('\b[a-z][a-z]\b', TEXT)  # without raw-string
[]


String
------
* ``\w`` - any unicode alphabet character (lower or upper, also with diacritics (i.e. ąćęłńóśżź...), numbers and underscores
* ``\W`` - anything but any unicode alphabet character (i.e. whitespace, dots, comas, dashes)
* lowercase letters including diacritics (i.e. ąćęłńóśżź...) and accents
* uppercase letters including diacritics (i.e. ąćęłńóśżź...) and accents
* digits
* underscores ``_``

Valid characters are the same as allowed in variable/modules names in Python:

>>> imie = 'Mark'
>>> IMIE = 'Mark'
>>> imię = 'Mark'
>>> imię1 = 'Mark'
>>> Imię_1 = 'Mark'

>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 1:37 pm'

>>> re.findall(r'\w', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['M', 'a', 'r', 'k', 'W', 'a', 't', 'n', 'e', 'y', 'o', 'f', 'A', 'r',
 'e', 's', '3', 'l', 'a', 'n', 'd', 'e', 'd', 'o', 'n', 'M', 'a', 'r',
 's', 'o', 'n', 'N', 'o', 'v', '7', 't', 'h', '2', '0', '3', '5', 'a',
 't', '1', '3', '7', 'p', 'm']

>>> re.findall(r'\W', TEXT)
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ':', ' ', ' ', ',', ' ', ' ', ' ', ':', ' ']

Mind, that following code gives similar output to ``\w`` but it is not
completely true. ``\w`` would extract also unicode characters while this
``[a-zA-Z0-9]`` will not.

>>> re.findall(r'[a-zA-Z0-9]', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['M', 'a', 'r', 'k', 'W', 'a', 't', 'n', 'e', 'y', 'o', 'f', 'A', 'r',
 'e', 's', '3', 'l', 'a', 'n', 'd', 'e', 'd', 'o', 'n', 'M', 'a', 'r',
 's', 'o', 'n', 'N', 'o', 'v', '7', 't', 'h', '2', '0', '3', '5', 'a',
 't', '1', '3', '7', 'p', 'm']

Example:

>>> text = 'cześć'
>>>
>>> re.findall(r'[a-z]', text)
['c', 'z', 'e']
>>>
>>> re.findall(r'\w', text)
['c', 'z', 'e', 'ś', 'ć']
>>>
>>> re.findall(r'\w', text, flags=re.ASCII)
['c', 'z', 'e']
>>>
>>> re.findall(r'\w', text, flags=re.UNICODE)
['c', 'z', 'e', 'ś', 'ć']

Flag ``re.UNICODE`` is set by default.


Use Case - 0x01
---------------
* Phone

>>> phone = '+48 123 456 789'
>>> re.findall(r'\d', phone)
['4', '8', '1', '2', '3', '4', '5', '6', '7', '8', '9']

>>> phone = '+48 (12) 345 6789'
>>> re.findall(r'\d', phone)
['4', '8', '1', '2', '3', '4', '5', '6', '7', '8', '9']


Use Case - 0x02
---------------
* Compare Phones

>>> PHONE1 = '+48 123 456 789'
>>> PHONE2 = '+48 (12) 345 6789'
>>>
>>> phone1 = re.findall(r'\d', PHONE1)
>>> phone2 = re.findall(r'\d', PHONE2)
>>>
>>> phone1 == phone2
True


Use Case - 0x03
---------------
* EU VAT Tax ID

>>> number = '777-286-18-23'
>>> re.findall(r'\d', number)
['7', '7', '7', '2', '8', '6', '1', '8', '2', '3']

>>> number = '777-28-61-823'
>>> re.findall(r'\d', number)
['7', '7', '7', '2', '8', '6', '1', '8', '2', '3']

>>> number = '7772861823'
>>> re.findall(r'\d', number)
['7', '7', '7', '2', '8', '6', '1', '8', '2', '3']


Use Case - 0x04
---------------
* Number and Spaces

>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 1:37 pm'

>>> re.findall(r'[0-9]\s', TEXT)
['3 ', '5 ', '7 ']

>>> re.findall(r'\d\s', TEXT)
['3 ', '5 ', '7 ']
