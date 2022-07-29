

Syntax About
============
* Also known as ``Regular Expressions``
* Also known as ``Regular Expr``
* Also known as ``regexp``
* Also known as ``regex``
* Also known as ``re``
* https://www.youtube.com/watch?v=BmF-gEYXWVM&list=PLv4THqSPE6meFeo_jNLgUVKkP40UstIQv&index=3


Syntax
------
* Identifiers - what to find (single character)
* Qualifiers - range to find (range)
* Negation
* Quantifiers - how many occurrences of preceding qualifier or identifier
* Groups
* Look Ahead and Look Behind
* Flags
* Extensions
* ``[]`` - Qualifier
* ``{}`` - Quantifier
* ``()`` - Groups


Escape characters
-----------------
* Escape characters
* ``\n`` - newline
* ``\r\n`` - newline (on Windows)
* ``\t`` - tab
* ``\r`` - carriage return
* ``\b`` - backspace
* ``\v`` - vertical space
* ``\f`` - form feed
* ``\x`` - hexadecimal
* ``\o`` - octal
* ``\u`` - Unicode entity 16-bit
* ``\U`` - Unicode entity 32-bit
* ``\\`` - backslash
* ``\'`` - apostrophe
* ``\"`` - double quote


Raw Strings
-----------
* Recap information about raw strings ``r'...'``


>>> filepath = '/home/mwatney/myfile.txt'
>>>
>>> filepath = '/Users/mwatney/myfile.txt'
>>>
>>> filepath = 'C:\Users\mwatney\myfile.txt'
  Input In [221]
    filepath = 'C:\Users\mwatney\myfile.txt'
                                            ^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

>>>
>>> print('\n')


>>> print('\m')
\m


>>> print('\U')
  Input In [224]
    print('\U')
              ^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 0-1: truncated \UXXXXXXXX escape

>>>
>>> print('\U0001F610')
😐
>>> import string
>>> string.hexdigits
'0123456789abcdefABCDEF'
>>>
>>> filepath = 'C:\\Users\\mwatney\\myfile.txt'
>>> print(filepath)
C:\Users\mwatney\myfile.txt
>>>
>>>
>>> filepath = 'C:/Users/mwatney/myfile.txt'
>>> print(filepath)
C:/Users/mwatney/myfile.txt
>>>
>>>
>>> filepath = r'C:\Users\mwatney\myfile.txt'
>>> print(filepath)
C:\Users\mwatney\myfile.txt



ASCII vs Unicode
----------------
* ``re.UNICODE``
* ``re.ASCII``
* ASCII for letters in latin alphabet
* UNICODE includes diacritics and accent characters (ąśćłóźć, etc.)


Digit, Hexadecimal, Octal
-------------------------


Punctuation
-----------


Visualization
-------------
* https://regexper.com/
* https://regex101.com/


Further Reading
---------------
* https://www.youtube.com/watch?v=BmF-gEYXWVM&list=PLv4THqSPE6meFeo_jNLgUVKkP40UstIQv&index=3
* Kinsley, Harrison "Sentdex". Python 3 Programming Tutorial - Regular Expressions / Regex with re. Year: 2014. Retrieved: 2021-04-11. URL: https://www.youtube.com/watch?v=sZyAn2TW7GY
* https://www.rexegg.com/regex-trick-conditional-replacement.html
* https://www.rexegg.com/regex-lookarounds.html
* https://www.rexegg.com/regex-anchors.html#z


Syntax Qualifier
================
* Qualifier specifies what to find.
* ``a`` - Exact
* ``a|b`` - Alternative
* ``[abc]`` - Enumeration
* ``[a-z]`` - Range


Exact
-----
* ``a`` - Exact


Exact Alternate
---------------
* ``a|b`` - letter `a` or `b` (also works with expressions)


Enumeration
-----------
* ``[abc]`` - letter `a` or `b` or `c`


Range
-----
* ``[a-z]`` - any lowercase ASCII letter from `a` to `z`
* ``[A-Z]`` - any uppercase ASCII letter from `A` to `Z`
* ``[0-9]`` - any digit from `0` to `9`
* ``[a-zA-Z]`` - any ASCII letter from: `a` to `z` or from `A` to `Z`
* ``[A-z]`` - any ASCII letter from: `a` to `z` or from `A` to `Z`
* ``[a-zA-Z0-9]`` - any ASCII letter from `a` to `z` or from `A` to `Z` or digit from `0` to `9`


Joining
-------
* ``[abc]|[123]`` - Enumeration alternative - letter `a`, `b` or `c` or digit `1`, `2` `3`
* ``[a-z]|[0-9]`` - Range alternative - any lowercase ASCII letter from `a` to `z` or digit from `0` to `9`


>>> phone1 = '+48 123 456 789'
>>> phone2 = '+48 (12) 345-6789'
>>>
>>> phone1 == phone2
False
>>>
>>> re.findall('[0-9]', phone1) == re.findall('[0-9]', phone2)
True
>>>
>>> re.findall('[0-9]', phone1)
['4', '8', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>>
>>> re.findall('[0-9]', phone2)
['4', '8', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>>

>>> #TODO
>>> # +48 -> 0048
>>> # +1  -> 0001
>>> # +348 -> 0348


Syntax Anchor
=============
* ``.`` - any character except a newline (changes meaning with ``re.DOTALL``)
* ``^`` - start of line (changes meaning with ``re.MULTILINE``)
* ``$`` - end of line (changes meaning with ``re.MULTILINE``)
* ``\A`` - start of text (doesn't change meaning with ``re.MULTILINE``)
* ``\Z`` - end of text (doesn't change meaning with ``re.MULTILINE``)


Any Character
-------------
* ``.`` - any character except a newline (changes meaning with ``re.DOTALL``)


Start of Line
-------------
* ``^`` - start of a line
* Changes meaning with ``re.MULTILINE``


End of Line
-----------
* ``$`` - end of line
* Changes meaning with ``re.MULTILINE``


Start of String
---------------
* ``\A`` - start of a text
* Doesn't change meaning with ``re.MULTILINE``


End of String
-------------
* ``\Z`` - end of a text
* Doesn't change meaning with ``re.MULTILINE``


Syntax Negation
===============
* Negation logically inverts qualifier


Syntax
------
* ``[^...]`` - anything but ...


Compare
-------




Syntax Identifier
=================
* Identifiers specifies what to find
* They are also called Character Classes


Numeric
-------
* ``\d`` - digit to samo co ``[0-9]``
* ``\D`` - anything but digit, to samo co ``[^0-9]``

>>> phone1 = '+48 123 456 789'
>>> phone2 = '+48 (12) 345-6789'

>>> re.findall('\d', phone1)
['4', '8', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> re.findall('\d', phone2)
['4', '8', '1', '2', '3', '4', '5', '6', '7', '8', '9']

>>> re.sub('\D', '', phone1)
'48123456789'
>>> re.sub('\D', '', phone2)
'48123456789'

>>> re.sub('\D', '', phone1).zfill(13)  #TODO
'0048123456789'


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

>>> phone1 = '+48 123 456 789'
>>> phone2 = '+48 (12) 345-6789'
>>>
>>>
>>> re.findall('\S', phone1)
['+', '4', '8', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>>
>>> re.findall('\S', phone2)
['+', '4', '8', '(', '1', '2', ')', '3', '4', '5', '-', '6', '7', '8', '9']
>>>
>>> re.sub('\s', '', phone1)
'+48123456789'
>>>
>>> re.sub('\s', '', phone2)
'+48(12)345-6789'


Anchors
-------
* Matches the empty string, but only at the beginning or end of a word
* ``\b`` - word boundary
* ``\B`` - anything but word boundary

>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 1:37 pm'
>>>
>>>
>>> re.findall('th', TEXT)
['th']
>>>
>>> re.findall('on', TEXT)
['on', 'on']
>>>
>>> re.findall('at', TEXT)
['at', 'at']
>>>
>>> re.findall(' at ', TEXT)
[' at ']
>>>
>>>
>>>
>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at: 1:37 pm'
>>>
>>> re.findall(' at ', TEXT)
[]
>>> re.findall('[^a-z]at[^a-z]', TEXT)
[' at:']
>>>
>>> re.findall('\bat\b', TEXT)
[]
>>> re.findall(r'\bat\b', TEXT)
['at']
>>>
>>> print('hello\b\b\bworld')
heworld


String
------
* ``\w`` - any unicode alphabet character (lower or upper, also with diacritics (i.e. ąćęłńóśżź...), numbers and underscores
* ``\W`` - anything but any unicode alphabet character (i.e. whitespace, dots, comas, dashes)
* lowercase letters including diacritics (i.e. ąćęłńóśżź...) and accents
* uppercase letters including diacritics (i.e. ąćęłńóśżź...) and accents
* digits
* underscores ``_``

$ cat /tmp/myfile.py
imie = 'Mark'
nazwisko='Watney'
WIEK = 10
IMIĘ = 'Marek'
Imię_1 = 'Marek'
print(imie)
print(nazwisko)


>>> with open('/tmp/myfile.py', mode='r') as file:
...     code = file.read()
...     zmienne = re.findall('^(\w+)\s?=', code, flags=re.MULTILINE)
...     funkcje = re.findall('^(\w+)\(', code, flags=re.MULTILINE)
...
>>>
>>>
>>> zmienne
['imie', 'nazwisko', 'WIEK', 'IMIĘ', 'Imię_1']
>>>
>>> funkcje
['print', 'print']



$ cat /tmp/myfile.py
imie = 'Mark'; agencja='NASA'
nazwisko='Watney'
WIEK = 10
IMIĘ = 'Marek'
Imię_1 = 'Marek'
print(imie)
print(nazwisko)

>>> re.split('\n|;', code)
["imie = 'Mark'",
 " agencja='NASA'",
 "nazwisko='Watney'",
 'WIEK = 10',
 "IMIĘ = 'Marek'",
 "Imię_1 = 'Marek'",
 'print(imie)',
 'print(nazwisko)',
 '']
>>> [x.strip() for x in re.split('\n|;', code)]
["imie = 'Mark'",
 "agencja='NASA'",
 "nazwisko='Watney'",
 'WIEK = 10',
 "IMIĘ = 'Marek'",
 "Imię_1 = 'Marek'",
 'print(imie)',
 'print(nazwisko)',
 '']

>>> print('w plikach znak \\n znaczy koniec linii')
w plikach znak \n znaczy koniec linii

>>> print('w plikach znak \n znaczy koniec linii')
w plikach znak
 znaczy koniec linii

>>> print(r'w plikach znak \n znaczy koniec linii')
w plikach znak \n znaczy koniec linii


Recap
-----
Qualifiers - a a|b [abc] [a-z] --> [a-zA-Z0-9]
Anchor - . ^ $ \A \Z
Negation - [^] --> [^a] -> [^0-9] -> [^a-zA-Z0-9]
Identifier - \d \D \s \S \w \W \b \B


Syntax Quantifier
=================
* Quantifier specifies how many occurrences of preceding qualifier or identifier
* Exact
* Greedy
* Lazy


Exact
-----
* Exact match
* ``{n}`` - exactly `n` repetitions, prefer longer


Greedy
------
* Prefer longest matches
* Works better with numbers
* Not that good results for text
* Default behavior
* ``{,n}`` - maximum `n` repetitions, prefer longer
* ``{n,}`` - minimum `n` repetitions, prefer longer
* ``{n,m}`` - minimum `n` repetitions, maximum `m` times, prefer longer
* ``*`` - minimum 0 repetitions, no maximum, prefer longer (alias to ``{0,}``)
* ``+`` - minimum 1 repetitions, no maximum, prefer longer (alias to ``{1,}``)
* ``?`` - minimum 0 repetitions, maximum 1 repetitions, prefer longer  (alias to ``{0,1}``)


Lazy
----
* Prefer shortest matches
* Works better with text
* Not that good results for numbers
* Non-greedy
* ``{,n}?`` - maximum `n` repetitions, prefer shorter
* ``{n,}?`` - minimum `n` repetitions, prefer shorter
* ``{n,m}?`` - minimum `n` repetitions, maximum `m` times, prefer shorter
* ``*?`` - minimum 0 repetitions, no maximum, prefer shorter (alias to ``{0,}?``)
* ``+?`` - minimum 1 repetitions, no maximum, prefer shorter (alias to ``{1,}?``)
* ``??`` - minimum 0 repetitions, maximum 1 repetition, prefer shorter (alias to ``{0,1}?``)


Greedy vs. Lazy
---------------


Special
-------


Syntax Group
============
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


Named Group
-----------
* ``(?P<mygroup>...)`` - named group `mygroup`



>>> def add(a,b):
...     return a + b
...
>>>
>>> add.__code__.co_varnames
('a', 'b')
>>>
>>>
>>>
>>> CODE = """
...
... def fun(param, param2):
...     pass
...
... """
>>>
>>>
>>> re.findall('^def \w+\(\w+, \w+):', CODE, flags=re.MULTILINE)
error: unbalanced parenthesis

>>> re.findall('^def \w+\(\w+, \w+\):', CODE, flags=re.MULTILINE)
['def fun(param, param2):']
>>>
>>>
>>>
>>> re.findall('^def \w+\((\w+), (\w+)\):', CODE, flags=re.MULTILINE)
[('param', 'param2')]
>>>
>>>
>>> re.findall('^def (\w+)\((\w+), (\w+)\):', CODE, flags=re.MULTILINE)
[('fun', 'param', 'param2')]
>>>
>>>
>>> re.search('^def (\w+)\((\w+), (\w+)\):', CODE, flags=re.MULTILINE).group()
'def fun(param, param2):'
>>> re.search('^def (\w+)\((\w+), (\w+)\):', CODE, flags=re.MULTILINE).groups()
('fun', 'param', 'param2')
>>> re.search('^def (?P<name>\w+)\((?P<arg1>\w+), (?P<arg2>\w+)\):', CODE, flags=re.MULTILINE).groups()
('fun', 'param', 'param2')
>>> re.search('^def (?P<name>\w+)\((?P<arg1>\w+), (?P<arg2>\w+)\):', CODE, flags=re.MULTILINE).groupdict()
{'name': 'fun', 'arg1': 'param', 'arg2': 'param2'}




Non-Capturing Group
-------------------
* ``(?:...)``


Comment
-------
* ``(?#...)`` - comment


Backreference
-------------
* ``\g<number>`` - backreferencing by group number
* ``\g<name>`` - backreferencing by group name
* ``(?P=name)`` - backreferencing by group name
* ``\number`` - backreferencing by group number


Syntax Flag
===========
* ``re.ASCII``
* ``re.IGNORECASE``
* ``re.LOCALE``
* ``re.MULTILINE``
* ``re.DOTALL``
* ``re.UNICODE``
* ``re.VERBOSE``
* ``re.DEBUG``


ASCII
-----
* Short: ``a``
* Long: ``re.ASCII``


IGNORECASE
----------
* Short: ``i``
* Long: ``re.IGNORECASE``


LOCALE
------
* Short: ``L``
* Long: ``re.LOCALE``
* Use of this flag is discouraged as the locale mechanism is very unreliable
* It only works with 8-bit locales


MULTILINE
----------
* Short: ``m``
* Long: ``re.MULTILINE``


DOTALL
------
* Short: ``s``
* Long: ``re.DOTALL``


UNICODE
-------
* Short: ``u``
* Long: ``re.UNICODE``
* On by default


VERBOSE
-------
* Short: ``x``
* Long: ``re.VERBOSE``
* Ignores spaces (except ``\s``) and allows for comments in in ``re.compile()``


DEBUG
-----


Syntax Look Ahead/Behind
========================


Syntax
------
* ``(?=)`` - Lookahead
* ``(?<=)`` - Lookbehind
* ``(?!foo)`` - Negative Lookahead
* ``(?<!foo)`` - Negative Lookbehind
* ``\K`` - Stop Look Behind


Syntax Extension
================
* In other programming languages
* PCRE - Perl Compatible Regular Expressions


Future
------
* Since Python 3.11
* Atomic grouping ``((?>...))`` and possessive quantifiers (``*+``, ``++``, ``?+``, ``{m,n}+``) are now supported in regular expressions.
* https://www.regular-expressions.info/atomic.html
* https://github.com/python/cpython/issues/34627


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


Range
-----
* ``[a-Z]`` == ``[a-zA-Z]``
* ``[a-9]`` == ``[a-zA-Z0-9]``
* Works in other languages, but not in Python


Group Backreference
-------------------
* ``$1`` == ``\1``


Syntax Use Cases
================


National Identification Numbers
-------------------------------
* Worldwide
* https://github.com/arthurdejong/python-stdnum/tree/master/stdnum/pl


Dates
-----


Email
-----
* [#rfc3696]_


URL
---


Parsing URLs
------------
* Source [#W3CParsingURLs]_


RE Match
========
* ``re.match()``
* Checks exact match
* Checking if user input is correct (email, url, NIP, VAT ID, PESEL)


Good Practices
--------------
* Doctests


Doctests
--------


RE Search
=========
* ``re.search()``
* Searches if pattern contains a string


RE Findall, Finditer
====================
* ``re.findall()``
* ``re.finditer()``


RE Compare
==========
* ``re.match()``
* ``re.search()``
* ``re.findall()``


RE Compile
==========
* ``re.compile()``
* Used when pattern is reused (especially in the loop)


Syntax
------


No Compile
----------


Compile
-------


RE Group
========
* Match particular parts of a string
* Possible to name matches


Syntax
------


Positional Groups
-----------------


Named Groups
------------
* Usage of group in ``re.match()``


RE Multiline
============
* ``re.MULTILINE`` - Flag turns on Multiline search
* ``^`` - Matches the start of the string, and immediately after each newline
* ``$`` - Matches the end of the string or just before the newline at the end of the string also matches before a newline


RE Substitute
=============
* ``re.sub()``
* Replace matched substring with text


RE Split
========
* ``re.split()``
* Split text by pattern


RE Lazy
=======
* Adding ``?`` after the qualifier makes it non-greedy
* Greedy - as many as possible
* Lazy - as few as possible:
* ``?`` - zero or one (greedy)
* ``*`` - zero or more (greedy)
* ``+`` - one or more (greedy)
* ``??`` - zero or one (lazy)
* ``*?`` - zero or more (lazy)
* ``+?`` - one or more (lazy)


RE Type Annotation
==================
* ``typing.Pattern``
* ``typing.Match``
