Syntax Recap
============
* Also known as ``Regular Expressions``
* Also known as ``Regular Expr``
* Also known as ``regexp``
* Also known as ``regex``
* Also known as ``re``


SetUp
-----
>>> import re
>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 1:37 pm'


Qualifiers
----------
* Qualifier specifies what to find.
* ``a`` - Exact
* ``a|b`` - Alternative
* ``[abc]`` - Enumeration
* ``[a-z]`` - Range

>>> x = re.findall(r'1', TEXT)
>>> x = re.findall(r'1|3', TEXT)
>>> x = re.findall(r'[12345]', TEXT)
>>> x = re.findall(r'[0-9]', TEXT)
>>> x = re.findall(r'[a-z]', TEXT)
>>> x = re.findall(r'[A-Z]', TEXT)
>>> x = re.findall(r'[a-zA-Z0-9]', TEXT)


Anchors
-------
* ``.`` - any character except a newline (changes meaning with ``re.DOTALL``)
* ``^`` - start of line (changes meaning with ``re.MULTILINE``)
* ``$`` - end of line (changes meaning with ``re.MULTILINE``)
* ``\A`` - start of text (doesn't change meaning with ``re.MULTILINE``)
* ``\Z`` - end of text (doesn't change meaning with ``re.MULTILINE``)

>>> x = re.findall(r'.', TEXT)
>>> x = re.findall(r'^.', TEXT)
>>> x = re.findall(r'.$', TEXT)
>>> x = re.findall(r'\A.', TEXT)
>>> x = re.findall(r'.\Z', TEXT)


Negation
--------
* Negation logically inverts qualifier
* ``[^...]`` - anything but ...

>>> x = re.findall(r'[^0-9]', TEXT)
>>> x = re.findall(r'[^a-zA-Z]', TEXT)


Identifiers
-----------
* Identifiers specifies what to find
* They are also called Character Classes
* ``\d`` - digit
* ``\D`` - anything but digit
* ``\s`` - whitespace (space, tab, newline, non-breaking space)
* ``\S`` - anything but whitespace
* ``\b`` - word boundary - empty string at the beginning or end of a word
* ``\B`` - anything but word boundary, word being a part of other word
* ``\w`` - any unicode alphabet character (lower or upper, also with diacritics (i.e. ąćęłńóśżź...), numbers and underscores
* ``\W`` - anything but any unicode alphabet character (i.e. whitespace, dots, comas, dashes)

Digit:

>>> x = re.findall(r'[0-9]', TEXT)
>>> x = re.findall(r'\d', TEXT)
>>>
>>> x = re.findall(r'[^0-9]', TEXT)
>>> x = re.findall(r'\D', TEXT)

Whitespace:

>>> x = re.findall(r'[ \t\v\f\n\r\n]', TEXT)
>>>
>>> x = re.findall(r'\s', TEXT)
>>> x = re.findall(r'\S', TEXT)

Word boundary:

>>> x = re.findall(r'\b[a-z][a-z]\b', TEXT)
>>> x = re.findall(r'\B[a-z][a-z]\B', TEXT)

Word character (unicode):

>>> x = re.findall(r'\w', TEXT)
>>> x = re.findall(r'\W', TEXT)


Quantifiers
-----------
* Quantifier specifies how many occurrences of preceding qualifier or identifier
* Exact
* Greedy (default)
* Lazy

Exact:

* Exact match
* ``{n}`` - exactly `n` repetitions

>>> x = re.findall('\d{2,4}', TEXT)

Greedy:

* Greedy - Prefer longest matches
* Greedy - Works better with numbers, not that good results for text
* Greedy - Default behavior
* ``{,n}`` - maximum `n` repetitions, prefer longer (greedy)
* ``{n,}`` - minimum `n` repetitions, prefer longer (greedy)
* ``{n,m}`` - minimum `n` repetitions, maximum `m` times, prefer longer (greedy)
* ``*`` - minimum 0 repetitions, no maximum, prefer longer (alias to ``{0,}``) (greedy)
* ``+`` - minimum 1 repetitions, no maximum, prefer longer (alias to ``{1,}``) (greedy)
* ``?`` - minimum 0 repetitions, maximum 1 repetitions, prefer longer  (alias to ``{0,1}``) (greedy)

>>> x = re.findall('\d{2,4}', TEXT)
>>> x = re.findall('\d{2,}', TEXT)
>>> x = re.findall('\d{,4}', TEXT)
>>>
>>> x = re.findall('\d{1,}', TEXT)
>>> x = re.findall('\d+', TEXT)
>>>
>>> x = re.findall('\d{0,}', TEXT)
>>> x = re.findall('\d*', TEXT)
>>>
>>> x = re.findall('\d{0,1}', TEXT)
>>> x = re.findall('\d?', TEXT)

Lazy:

* Lazy - Prefer shortest matches
* Lazy - Works better with text, not that good results for numbers
* ``{,n}?`` - maximum `n` repetitions, prefer shorter
* ``{n,}?`` - minimum `n` repetitions, prefer shorter
* ``{n,m}?`` - minimum `n` repetitions, maximum `m` times, prefer shorter
* ``*?`` - minimum 0 repetitions, no maximum, prefer shorter (alias to ``{0,}?``)
* ``+?`` - minimum 1 repetitions, no maximum, prefer shorter (alias to ``{1,}?``)
* ``??`` - minimum 0 repetitions, maximum 1 repetition, prefer shorter (alias to ``{0,1}?``)

>>> x = re.findall('\d{2,4}?', TEXT)
>>> x = re.findall('\d{2,}?', TEXT)
>>> x = re.findall('\d{,4}?', TEXT)
>>>
>>> x = re.findall('\d{1,}?', TEXT)
>>> x = re.findall('\d+?', TEXT)
>>>
>>> x = re.findall('\d{0,}?', TEXT)
>>> x = re.findall('\d*?', TEXT)
>>>
>>> x = re.findall('\d{0,1}?', TEXT)
>>> x = re.findall('\d??', TEXT)

Greedy vs Lazy:

>>> re.findall('\d+', TEXT)
['3', '7', '2035', '1', '37']
>>>
>>> re.findall('\d+?', TEXT)
['3', '7', '2', '0', '3', '5', '1', '3', '7']

>>> text = 'Litwo ojczyzno moja. Jankiel na weselu.'
>>> zdanie = r'[A-Z].+\.'
>>> re.findall(zdanie, text)
['Litwo ojczyzno moja. Jankiel na weselu.']
>>>
>>> zdanie = r'[A-Z].+?\.'
>>> re.findall(zdanie, text)
['Litwo ojczyzno moja.', 'Jankiel na weselu.']

>>> html = '<p>We choose to go to the Moon</p>'
>>> tag = r'<.+>'
>>> re.findall(tag, html)
['<p>We choose to go to the Moon</p>']
>>>
>>> tag = r'<.+?>'
>>> re.findall(tag, html)
['<p>', '</p>']


Groups
------
* Catch expression results
* Can be named or positional
* Note, that for backreference, must use raw-sting or double backslash
* ``(...)`` - unnamed (positional) group
* ``(?P<mygroup>...)`` - named group with name: `mygroup`
* ``(?:...)`` - non-capturing group
* ``(?#...)`` - comment

TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 1:37 pm'

Positional Groups:

>>> day = r'[0-9]th'
>>> re.findall(day, TEXT)
['7th']
>>>
>>> day = r'([0-9])th'
>>> re.findall(day, TEXT)
['7']
>>>
>>> day = r'[0-9](th)'
>>> re.findall(day, TEXT)
['th']

Named Groups:

>>> year = r'(?P<rok>\d{4})'
>>> month = r'(?P<miesiac>[A-Z][a-z]{2})'
>>> day = r'(?P<dzien>\d{1,2})'
>>>
>>> date = f'{month} {day}th, {year}'
>>>
>>> re.findall(date, TEXT)
[('Nov', '7', '2035')]

Non-capturing Groups:

>>> date = f'{month} {day}(st|nd|rd|th), {year}'
>>> re.findall(date, TEXT)
[('Nov', '7', 'th', '2035')]
>>>
>>> date = f'{month} {day}(?:st|nd|rd|th), {year}'
>>> re.findall(date, TEXT)
[('Nov', '7', '2035')]


Backreference
-------------
* ``\g<number>`` - backreferencing by group number
* ``\g<name>`` - backreferencing by group name
* ``(?P=name)`` - backreferencing by group name
* ``\number`` - backreferencing by group number

>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 1:37 pm'
>>>
>>> year = r'(?P<year>\d{4})'
>>> month = r'(?P<month>\w+)'
>>> day = r'(?P<day>\d{1,2})'
>>>
>>>
>>> re.sub(f'{month} {day}th, {year}', '\g<day> \g<month> \g<year>', TEXT)
'Mark Watney of Ares 3 landed on Mars on: 7 Nov 2035 at 1:37 pm'
>>>
>>> re.sub(date, '\g<2> \g<1> \g<3>', TEXT)
'Mark Watney of Ares 3 landed on Mars on: 7 Nov 2035 at 1:37 pm'

Example:

>>> html = '<p>We choose to go to the <strong>Moon</strong></p>'
>>>
>>>
>>> re.findall(r'<(?P<tagname>[a-z]+)>.*</(?P=tagname)>', html)
['p']
>>>
>>> re.findall(r'<(?P<tagname>[a-z]+)>(.*)</(?P=tagname)>', html)
[('p', 'We choose to go to the <strong>Moon</strong>')]


Flags
-----
* ``re.ASCII``
* ``re.IGNORECASE``
* ``re.LOCALE``
* ``re.MULTILINE``
* ``re.DOTALL``
* ``re.UNICODE``
* ``re.VERBOSE``
* ``re.DEBUG``


Python
------
* ``re.findall()`` - all matches at once
* ``re.finditer()`` - all matches one at a time
* ``re.search()`` - whether text contains (does not search after first match)
* ``re.match()`` - whether text matches pattern (validation, np. email, ssn, tax id, phone)
* ``re.split()`` - splits text by pattern
* ``re.sub()`` - replaces group matches in text (works best with named groups)
* ``re.compile()`` - prepares pattern for further use (match against it)

