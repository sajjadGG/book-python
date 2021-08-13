Syntax Qualifier
================


Rationale
---------
Qualifier specifies range to find.


Exact Matches
-------------
>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> re.findall('Gagarin', TEXT)
['Gagarin']
>>>
>>> re.findall('Yuri Gagarin', TEXT)
['Yuri Gagarin']


Enumerations
------------
* ``[abc]`` - letter `a` or `b` or `c`

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> re.findall('[0123]', TEXT)
['1', '2', '1', '1', '0']
>>>
>>> re.findall('[abc]', TEXT)
['a', 'a', 'a', 'c', 'a', 'c', 'a', 'a']


Range
-----
* ``[a-z]`` - any lowercase ASCII letter from `a` to `z`
* ``[A-Z]`` - any uppercase ASCII letter from `A` to `Z`
* ``[0-9]`` - any digit from `0` to `9`
* ``[a-zA-Z]`` - any ASCII letter from: `a` to `z` or from `A` to `Z`
* ``[a-zA-Z0-9]`` - any ASCII letter from `a` to `z` or from `A` to `Z` or digit from `0` to `9`

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>>
>>> re.findall('[0-9]', TEXT)
['1', '2', '1', '9', '6', '1', '6', '0', '7']
>>>
>>> re.findall('[3-7]', TEXT)
['6', '6', '7']
>>>
>>> re.findall('[A-Z]', TEXT)
['Y', 'G', 'A']
>>>
>>> re.findall('[a-z]', TEXT)
['u', 'r', 'i', 'a', 'g', 'a', 'r', 'i', 'n', 'l', 'a', 'u', 'n', 'c', 'h', 'e', 'd', 't', 'o', 's', 'p', 'a', 'c', 'e', 'o', 'n', 'p', 'r', 't', 'h', 'a', 't', 'a', 'm']
>>>
>>> re.findall('[C-Y]', TEXT)
['Y', 'G']
>>>
>>> re.findall('[a-Z]', TEXT)
Traceback (most recent call last):
re.error: bad character range a-Z at position 1

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> re.findall('[A-Z][a-z][a-z] [0-9][0-9][a-z][a-z]', TEXT)
['Apr 12th']


Alternative
-----------
* ``a|b`` - letter `a` or `b` (also works with expressions)
* ``[a-z]|[0-9]`` - any lowercase ASCII letter from `a` to `z` or digit from `0` to `9`

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> re.findall('G|A', TEXT)
['G', 'A']
>>>
>>> re.findall('G|Z', TEXT)
['G']
>>> re.findall('A|c|6', TEXT)
['c', 'c', 'A', '6', '6']

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> re.findall('1|2|3', TEXT)
['1', '2', '1', '1']
>>>
>>> re.findall('[123]', TEXT)
['1', '2', '1', '1']

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> re.findall('[A-Z]|[0-9]', TEXT)
['Y', 'G', 'A', '1', '2', '1', '9', '6', '1', '6', '0', '7']
>>>
>>> re.findall('[A-Z0-9]', TEXT)
['Y', 'G', 'A', '1', '2', '1', '9', '6', '1', '6', '0', '7']


Anchors
-------
* ``.`` - any character except a newline (changes meaning with ``re.DOTALL``)
* ``^`` - start of a string (changes meaning with ``re.MULTILINE``)
* ``$`` - end of a string (changes meaning with ``re.MULTILINE``)
* ``\A`` - start of a string (doesn't change meaning with ``re.MULTILINE``)
* ``\Z`` - end of a string (doesn't change meaning with ``re.MULTILINE``)
* ``\G`` - beginning of string or end of previous match

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> re.findall('[0-9][0-9]', TEXT)
['12', '19', '61', '07']
>>>
>>> re.findall(' ... ', TEXT)
[' Apr ']
>>>
>>> re.findall(' .... ', TEXT)
[' 1961 ', ' 6:07 ']
>>>
>>> re.findall('....', TEXT)
['Yuri', ' Gag', 'arin', ' lau', 'nche', 'd to', ' spa', 'ce o', 'n Ap', 'r 12', 'th, ', '1961', ' at ', '6:07', ' am.']

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> re.findall('[A-Z]', TEXT)
['Y', 'G', 'A']
>>>
>>> re.findall('^[A-Z]', TEXT)
['Y']

>>> import re
>>>
>>>
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'
>>>
>>> re.findall('[A-Z][a-z][a-z] [0-9][0-9][a-z][a-z]', TEXT)
['Apr 12th']
>>>
>>> re.findall('[A-Z][a-z][a-z] [0-9][0-9]..', TEXT)
['Apr 12th']


Examples
--------
* ``[d-m]`` - any lowercase letter from `d`  to `m`
* ``[3-7]`` - any digit from `3` to `7`
* ``[d-mK-P3-8]`` - any lowercase letter from `d` to `m` or uppercase letter from `K` to `P` or digit from `3` to `8`
* ``[xz2]`` - `x` or `z` or `2`
* ``x|z|2`` - `x` or `z` or `2`
* ``d|x`` - `d` or `x`
* ``[d-k]|[ABC]|[3-8]`` - any lowercase letter from `d` to `k` or uppercase `A`,`B` or `C` or digit from `3` to `8`
* ``[A-Z][a-z]`` - any capital letter from `A` to `Z` immediately followed by lowercase letter from `a` to `z`
* ``abc.e`` - text `abc` then any character followed by letter `e`
