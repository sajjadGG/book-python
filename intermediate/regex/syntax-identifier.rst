Syntax Identifier
=================


Rationale
---------
Identifiers specifies what to find.
They are also called Character Classes.


Numeric
-------
* ``\d`` - digit
* ``\D`` - anything but digit

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> re.findall('[0-9]', TEXT)
['1', '2', '1', '9', '6', '1', '6', '0', '7']
>>>
>>> re.findall('\d', TEXT)
['1', '2', '1', '9', '6', '1', '6', '0', '7']
>>>
>>> re.findall('\D', TEXT)
['Y', 'u', 'r', 'i', ' ', 'G', 'a', 'g', 'a', 'r', 'i', 'n', ' ', 'l', 'a', 'u', 'n', 'c', 'h', 'e', 'd', ' ', 't', 'o', ' ', 's', 'p', 'a', 'c', 'e', ' ', 'o', 'n', ' ', 'A', 'p', 'r', ' ', 't', 'h', ',', ' ', ' ', 'a', 't', ' ', ':', ' ', 'a', 'm', '.']


String
------
* ``\w`` - any unicode alphabet character (lower or upper, also with diacritics (i.e. ąćęłńóśżź...), numbers and underscores
* ``\W`` - anything but any unicode alphabet character (i.e. whitespace, dots, comas, dashes)

Valid characters are the same as allowed in variable/modules names in Python:

>>> imie = 'Mark'
>>> IMIE = 'Mark'
>>> imię = 'Mark'
>>> imię1 = 'Mark'
>>> Imię_1 = 'Mark'

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> re.findall('\w', TEXT)
['Y', 'u', 'r', 'i', 'G', 'a', 'g', 'a', 'r', 'i', 'n', 'l', 'a', 'u', 'n', 'c', 'h', 'e', 'd', 't', 'o', 's', 'p', 'a', 'c', 'e', 'o', 'n', 'A', 'p', 'r', '1', '2', 't', 'h', '1', '9', '6', '1', 'a', 't', '6', '0', '7', 'a', 'm']
>>>
>>> re.findall('\W', TEXT)
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ',', ' ', ' ', ' ', ':', ' ', '.']


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

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> re.findall('\s', TEXT)
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
>>>
>>> re.findall('\S', TEXT)
['Y', 'u', 'r', 'i', 'G', 'a', 'g', 'a', 'r', 'i', 'n', 'l', 'a', 'u', 'n', 'c', 'h', 'e', 'd', 't', 'o', 's', 'p', 'a', 'c', 'e', 'o', 'n', 'A', 'p', 'r', '1', '2', 't', 'h', ',', '1', '9', '6', '1', 'a', 't', '6', ':', '0', '7', 'a', 'm', '.']

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> re.findall('\n', TEXT)
[]
>>>
>>> re.findall('\r\n', TEXT)
[]
>>>
>>> re.findall('\r', TEXT)
[]


Anchors
-------
* ``\b`` - word boundary
* ``\B`` - anything but word boundary

Examples:

    * ``\babc\b`` - performs a "whole words only" search
    * ``\Babc\B`` - pattern is fully surrounded by word characters

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> re.findall('[a-z][a-z]', TEXT)
['ur', 'ag', 'ar', 'in', 'la', 'un', 'ch', 'ed', 'to', 'sp', 'ac', 'on', 'pr', 'th', 'at', 'am']
>>>
>>> re.findall(r'\b[a-z][a-z]', TEXT)
['la', 'to', 'sp', 'on', 'at', 'am']
>>>
>>> re.findall(r'\b[a-z][a-z]\b', TEXT)
['to', 'on', 'at', 'am']
>>>
>>> re.findall('\b[a-z][a-z]\b', TEXT)  # without raw-string
[]


Use Case - 0x01
---------------
* Phone

>>> import re
>>>
>>>
>>> phone = '+48 123 456 789'
>>> re.findall('\d', phone)
['4', '8', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>>
>>> phone = '+48 (12) 345 6789'
>>> re.findall('\d', phone)
['4', '8', '1', '2', '3', '4', '5', '6', '7', '8', '9']


Use Case - 0x02
---------------
* Compare Phones

>>> import re
>>>
>>>
>>> PHONE1 = '+48 123 456 789'
>>> PHONE2 = '+48 (12) 345 6789'
>>>
>>> phone1 = re.findall('\d', PHONE1)
>>> phone2 = re.findall('\d', PHONE2)
>>>
>>> phone1 == phone2
True


Use Case - 0x03
---------------
* EU VAT Tax ID

>>> import re
>>>
>>>
>>> number = '777-286-18-23'
>>> re.findall('\d', number)
['7', '7', '7', '2', '8', '6', '1', '8', '2', '3']
>>>
>>> number = '777-28-61-823'
>>> re.findall('\d', number)
['7', '7', '7', '2', '8', '6', '1', '8', '2', '3']
>>>
>>> number = '7772861823'
>>> re.findall('\d', number)
['7', '7', '7', '2', '8', '6', '1', '8', '2', '3']


Use Case - 0x04
---------------
* Number and Spaces

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> re.findall('[0-9]\s', TEXT)
['1 ', '7 ']
>>>
>>> re.findall('\d\s', TEXT)
['1 ', '7 ']
