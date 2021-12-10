Syntax Negation
===============


Rationale
---------
Negation logically inverts qualifier.


Syntax
------
* ``[^...]`` - anything but ...


Example
-------
* ``[^abc]`` - anything but letter `a` or `b` or `c`

>>> import re
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'


>>> re.findall(r'[0-9]', TEXT)
['1', '2', '1', '9', '6', '1', '6', '0', '7']


>>> re.findall(r'[^0-9]', TEXT)
['Y', 'u', 'r', 'i', ' ', 'G', 'a', 'g', 'a', 'r', 'i', 'n', ' ', 'l', 'a', 'u', 'n', 'c', 'h', 'e', 'd', ' ', 't', 'o', ' ', 's', 'p', 'a', 'c', 'e', ' ', 'o', 'n', ' ', 'A', 'p', 'r', ' ', 't', 'h', ',', ' ', ' ', 'a', 't', ' ', ':', ' ', 'a', 'm', '.']



Compare
-------
>>> import re
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'

>>> re.findall('[A-Z]', TEXT)
['Y', 'G', 'A']

>>> re.findall('^[A-Z]', TEXT)
['Y']

>>> re.findall('[^A-Z]', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['u', 'r', 'i', ' ', 'a', 'g', 'a', 'r', 'i', 'n', ' ', 'l', 'a', 'u',
 'n', 'c', 'h', 'e', 'd', ' ', 't', 'o', ' ', 's', 'p', 'a', 'c', 'e',
 ' ', 'o', 'n', ' ', 'p', 'r', ' ', '1', '2', 't', 'h', ',', ' ', '1',
 '9', '6', '1', ' ', 'a', 't', ' ', '6', ':', '0', '7', ' ', 'a', 'm', '.']

>>> re.findall('^[^A-Z]', TEXT)
[]
