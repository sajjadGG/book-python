Syntax Qualifier
================


Important
---------
* Qualifier specifies what to find.
* ``a`` - Exact
* ``a|b`` - Alternative
* ``[abc]`` - Enumeration
* ``[a-z]`` - Range


Exact
-----
>>> import re
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'

Regular expressions allows to find exact matches:

>>> re.findall('a', TEXT)
['a', 'a', 'a', 'a', 'a', 'a']

Note, that regular expressions are case sensitive (unless ``re.IGNORECASE``
flag is present. More information in `Syntax Flags`):

>>> re.findall('A', TEXT)
['A']

Note, that regular expressions are used to search in text, therefore in case
of searching for a number it will return a strings with numbers in it:

>>> re.findall('1', TEXT)
['1', '1', '1']

Python ``re.findall()`` function will return empty list if none match was
found:

>>> re.findall('x', TEXT)
[]


Exact Alternate
---------------
* ``a|b`` - letter `a` or `b` (also works with expressions)

>>> import re
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'

Alternative allows to search for two or more possible matches:

>>> re.findall('a|b', TEXT)
['a', 'a', 'a', 'a', 'a', 'a']

It can find more than two matches:

>>> re.findall('a|b|c', TEXT)
['a', 'a', 'a', 'c', 'a', 'c', 'a', 'a']
>>>
>>> re.findall('1|2|3', TEXT)
['1', '2', '1', '1']

It will work for both numbers, characters or any other object:

>>> re.findall('a|b|c|1|2|3', TEXT)
['a', 'a', 'a', 'c', 'a', 'c', '1', '2', '1', '1', 'a', 'a']

Examples:

>>> re.findall('a|e', TEXT)
['a', 'a', 'a', 'e', 'a', 'e', 'a', 'a']
>>>
>>> re.findall('a|e|i|o|u|y', TEXT)
['u', 'i', 'a', 'a', 'i', 'a', 'u', 'e', 'o', 'a', 'e', 'o', 'a', 'a']


Enumeration
-----------
* ``[abc]`` - letter `a` or `b` or `c`

>>> import re
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'

Enumerations provide compact and more readable syntax for longer alternatives:

>>> re.findall('[abc]', TEXT)
['a', 'a', 'a', 'c', 'a', 'c', 'a', 'a']
>>>
>>> re.findall('[123]', TEXT)
['1', '2', '1', '1']

It will work for both numbers, characters or any other object:

>>> re.findall('[abc123]', TEXT)
['a', 'a', 'a', 'c', 'a', 'c', '1', '2', '1', '1', 'a', 'a']

Examples:

>>> re.findall('[a-z]', TEXT)  # letters from a to z
['u', 'r', 'i', 'a', 'g', 'a', 'r', 'i', 'n', 'l', 'a', 'u', 'n', 'c', 'h', 'e', 'd', 't', 'o', 's', 'p', 'a', 'c', 'e', 'o', 'n', 'p', 'r', 't', 'h', 'a', 't', 'a', 'm']
>>>
>>> re.findall('[az-]', TEXT)  # letters a, z or -
['a', 'a', 'a', 'a', 'a', 'a']

>>> re.findall('[A-z]', TEXT)
['Y', 'u', 'r', 'i', 'G', 'a', 'g', 'a', 'r', 'i', 'n', 'l', 'a', 'u', 'n', 'c', 'h', 'e', 'd', 't', 'o', 's', 'p', 'a', 'c', 'e', 'o', 'n', 'A', 'p', 'r', 't', 'h', 'a', 't', 'a', 'm']
>>>
>>> re.findall('[a-Z]', TEXT)
Traceback (most recent call last):
re.error: bad character range a-Z at position 1
>>>
>>> re.findall('[z-a]', TEXT)
Traceback (most recent call last):
re.error: bad character range z-a at position 1

Use Cases:

>>> re.findall('[aeiouy]', TEXT)
['u', 'i', 'a', 'a', 'i', 'a', 'u', 'e', 'o', 'a', 'e', 'o', 'a', 'a']
>>>
>>> re.findall('a|e|i|o|u|y', TEXT)
['u', 'i', 'a', 'a', 'i', 'a', 'u', 'e', 'o', 'a', 'e', 'o', 'a', 'a']


Enumeration Alternate
---------------------
>>> import re
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'

Alternative enumerations syntax is as follows:

>>> re.findall('[abc]|[123]', TEXT)
['a', 'a', 'a', 'c', 'a', 'c', '1', '2', '1', '1', 'a', 'a']

The effect is identical to:

>>> re.findall('[abc123]', TEXT)
['a', 'a', 'a', 'c', 'a', 'c', '1', '2', '1', '1', 'a', 'a']


Range
-----
* ``[a-z]`` - any lowercase ASCII letter from `a` to `z`
* ``[A-Z]`` - any uppercase ASCII letter from `A` to `Z`
* ``[0-9]`` - any digit from `0` to `9`
* ``[a-zA-Z]`` - any ASCII letter from: `a` to `z` or from `A` to `Z`
* ``[a-zA-Z0-9]`` - any ASCII letter from `a` to `z` or from `A` to `Z` or digit from `0` to `9`

>>> import re
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'

Ranges provide even more readable and convenient way os specifying particular
characters to match. It is very useful to define ranges of numbers or letters
this way:

>>> re.findall('[a-z]', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['u', 'r', 'i', 'a', 'g', 'a', 'r', 'i', 'n', 'l', 'a', 'u', 'n', 'c', 'h',
 'e', 'd', 't', 'o', 's', 'p', 'a', 'c', 'e', 'o', 'n', 'p', 'r', 't', 'h',
 'a', 't', 'a', 'm']
>>>
>>> re.findall('[A-Z]', TEXT)
['Y', 'G', 'A']
>>>
>>> re.findall('[0-9]', TEXT)
['1', '2', '1', '9', '6', '1', '6', '0', '7']

Note, that regular expressions are case sensitive (unless ``re.IGNORECASE``
flag is present. More information in `Syntax Flags`). You can also join ranges
to create even broader matches:

>>> re.findall('[a-zA-Z]', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['Y', 'u', 'r', 'i', 'G', 'a', 'g', 'a', 'r', 'i', 'n', 'l', 'a', 'u', 'n',
 'c', 'h', 'e', 'd', 't', 'o', 's', 'p', 'a', 'c', 'e', 'o', 'n', 'A', 'p',
 'r', 't', 'h', 'a', 't', 'a', 'm']
>>>
>>> re.findall('[a-zA-Z0-9]', TEXT)  # doctest: +NORMALIZE_WHITESPACE
['Y', 'u', 'r', 'i', 'G', 'a', 'g', 'a', 'r', 'i', 'n', 'l', 'a', 'u', 'n',
 'c', 'h', 'e', 'd', 't', 'o', 's', 'p', 'a', 'c', 'e', 'o', 'n', 'A', 'p',
 'r', '1', '2', 't', 'h', '1', '9', '6', '1', 'a', 't', '6', '0', '7', 'a',
 'm']

Ranges are ordered in ASCII table order (more information in `Locale
Encoding`). Because uppercase letters are before lowercase letters (has
lower indexes), you can define range from ``Z-a``, but the opposite is not
true:

>>> re.findall('[Z-a]', TEXT)
['a', 'a', 'a', 'a', 'a', 'a']

>>> re.findall('[a-Z]', TEXT)
Traceback (most recent call last):
re.error: bad character range a-Z at position 1

The last example can work in some other languages due to the different
implementation of the algorithm or PCRE standard. More information in `Syntax
Extensions`.

Mind that ranges not necessarily need to be from a-z. It could be any
alphabetic or numeric range:

>>> re.findall('[3-7]', TEXT)
['6', '6', '7']
>>>
>>> re.findall('[C-Y]', TEXT)
['Y', 'G']
>>>
>>> re.findall('[3-7C-Y]', TEXT)
['Y', 'G', '6', '6', '7']


Range Alternate
---------------
* ``[a-z]|[0-9]`` - any lowercase ASCII letter from `a` to `z` or digit from `0` to `9`

>>> import re
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'

You can define alternative ranges to find:

>>> re.findall('[A-Z]|[0-9]', TEXT)
['Y', 'G', 'A', '1', '2', '1', '9', '6', '1', '6', '0', '7']

The effect is identical to:

>>> re.findall('[A-Z0-9]', TEXT)
['Y', 'G', 'A', '1', '2', '1', '9', '6', '1', '6', '0', '7']


Examples
--------
* ``[d-m]`` - any lowercase letter from `d`  to `m`
* ``[3-7]`` - any digit from `3` to `7`
* ``[xz2]`` - `x` or `z` or `2`
* ``[d-mK-P3-8]`` - any lowercase letter from `d` to `m` or uppercase letter from `K` to `P` or digit from `3` to `8`
* ``x|z|2`` - `x` or `z` or `2`
* ``d|x`` - `d` or `x`
* ``[d-k]|[ABC]|[3-8]`` - any lowercase letter from `d` to `k` or uppercase `A`,`B` or `C` or digit from `3` to `8`


Use Case - 0x01
---------------
>>> import re
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'

>>> re.findall('st|nd|rd|th', TEXT)
['th']

>>> re.findall('[st|nd|rd|th]', TEXT)
['r', 'r', 'n', 'n', 'h', 'd', 't', 's', 'n', 'r', 't', 'h', 't']

>>> re.findall('[stndrdth]', TEXT)
['r', 'r', 'n', 'n', 'h', 'd', 't', 's', 'n', 'r', 't', 'h', 't']
