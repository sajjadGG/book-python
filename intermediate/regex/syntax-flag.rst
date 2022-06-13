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

The final piece of regex syntax that Python's regular expression engine offers
is a means of setting the flags. Usually the flags are set by passing them as
additional parameters when calling the re.compile() function, but sometimes
it's more convenient to set them as part of the regex itself. The syntax is
simply (?flags) where flags is one or more of the following:

* ``re.ASCII``
* ``re.IGNORECASE``
* ``re.LOCALE``
* ``re.MULTILINE``
* ``re.DOTALL``
* ``re.UNICODE``
* ``re.VERBOSE``
* ``re.DEBUG``

If the flags are set this way, they should be put at the start of the regex;
they match nothing, so their effect on the regex is only to set the flags.
The letters used for the flags are the same as the ones used by Perl's regex
engine, which is why s is used for re.DOTALL and x is used for re.VERBOSE
[#Summerfield2008]_.


ASCII
-----
* Short: ``a``
* Long: ``re.ASCII``

Make ``\w``, ``\W``, ``\b``, ``\B``, ``\d``, ``\D``, ``\s`` and ``\S`` perform ASCII-only matching instead of full Unicode matching

>>> import re
>>>
>>>
>>> TEXT = 'zażółć gęślą jaźń'
>>>
>>> re.findall('\w+', TEXT)
['zażółć', 'gęślą', 'jaźń']
>>>
>>> re.findall('\w+', TEXT, flags=re.ASCII)
['za', 'g', 'l', 'ja']


IGNORECASE
----------
* Short: ``i``
* Long: ``re.IGNORECASE``

Case-insensitive (has Unicode support i.e. Ą and ą)

>>> import re
>>>
>>>
>>> TEXT = 'Mark Watney of Ares 3 landed on Mars on: Nov 7th, 2035 at 1:37 pm'
>>>
>>> re.findall(r'ares', TEXT)
[]
>>>
>>> re.findall(r'ares', TEXT, flags=re.IGNORECASE)
['Ares']


LOCALE
------
* Short: ``L``
* Long: ``re.LOCALE``
* Use of this flag is discouraged as the locale mechanism is very unreliable
* It only works with 8-bit locales

make ``\w``, ``\W``, ``\b``, ``\B`` and case-insensitive matching dependent on the current locale


MULTILINE
----------
* Short: ``m``
* Long: ``re.MULTILINE``

match can start in one line, and end in another: ``^`` - start of line, ``$`` - end of line

>>> import re
>>>
>>>
>>> TEXT = """We choose to go to the moon.
... We choose to go to the moon in this decade and do the other things,
... not because they are easy,
... but because they are hard,
... because that goal will serve to organize and measure the best of our energies and skills,
... because that challenge is one that we are willing to accept,
... one we are unwilling to postpone,
... and one which we intend to win,
... and the others, too."""
>>>
>>>
>>> sentence = '[A-Z][a-z, ]+\.'
>>> re.findall(sentence, TEXT)
['We choose to go to the moon.']
>>>
>>> sentence = '[A-Z][a-z, \n]+\.'
>>> re.findall(sentence, TEXT)
['We choose to go to the moon.', 'We choose to go to the moon in this decade and do the other things,\nnot because they are easy,\nbut because they are hard,\nbecause that goal will serve to organize and measure the best of our energies and skills,\nbecause that challenge is one that we are willing to accept,\none we are unwilling to postpone,\nand one which we intend to win,\nand the others, too.']


DOTALL
------
* Short: ``s``
* Long: ``re.DOTALL``

``.`` matches also newlines (default newlines are not matched by ``.``)

>>> import re
>>>
>>>
>>> TEXT = 'hello\nworld'
>>>
>>> re.findall('.+', TEXT)
['hello', 'world']
>>>
>>> re.findall('.+', TEXT, flags=re.DOTALL)
['hello\nworld']


UNICODE
-------
* Short: ``u``
* Long: ``re.UNICODE``
* On by default

Turns on UNICODE mode

>>> import re
>>>
>>>
>>> TEXT = 'zażółć gęślą jaźń'
>>>
>>> re.findall('\w+', TEXT)
['zażółć', 'gęślą', 'jaźń']
>>>
>>> re.findall('\w+', TEXT, flags=re.UNICODE)
['zażółć', 'gęślą', 'jaźń']


VERBOSE
-------
* Short: ``x``
* Long: ``re.VERBOSE``
* Ignores spaces (except ``\s``) and allows for comments in in ``re.compile()``

>>> x = re.compile(r"\d+\.\d*")

>>> x = re.compile(r"\d(?#integral part)+\.(?#separator)\d*(?#fractional part)")

>>> x = re.compile(r"""\d +  # integral part
...                    \.    # separator
...                    \d *  # fractional part""", re.VERBOSE)


DEBUG
-----
>>> import re
>>>
>>>
>>> re.compile(r'[A-Z][a-z, \n]+\.')
re.compile('[A-Z][a-z, \\n]+\\.')

>>> import re
>>>
>>>
>>> re.compile(r'[A-Z][a-z, \n]+\.', flags=re.DEBUG)
IN
  RANGE (65, 90)
MAX_REPEAT 1 MAXREPEAT
  IN
    RANGE (97, 122)
    LITERAL 44
    LITERAL 32
    LITERAL 10
LITERAL 46
<BLANKLINE>
 0. INFO 8 0b100 3 MAXREPEAT (to 9)
      in
 5.     RANGE 0x41 0x5a ('A'-'Z')
 8.     FAILURE
 9: IN 5 (to 15)
11.   RANGE 0x41 0x5a ('A'-'Z')
14.   FAILURE
15: REPEAT_ONE 16 1 MAXREPEAT (to 32)
19.   IN 11 (to 31)
21.     CHARSET [0x00000400, 0x00001001, 0x00000000, 0x07fffffe, 0x00000000, 0x00000000, 0x00000000, 0x00000000]
30.     FAILURE
31:   SUCCESS
32: LITERAL 0x2e ('.')
34. SUCCESS
re.compile('[A-Z][a-z, \\n]+\\.', re.DEBUG)


References
----------
.. [#Summerfield2008] Summerfield, Mark. Programming in Python 3. Regular Expressions. Chapter: 12. Pages: 445-465. Year: 2008. Retrieved: 2021-04-11. Publisher: Addison-Wesley Professional. ISBN: 978-0-13-712929-4. URL: https://www.informit.com/articles/article.aspx?p=1278986
