String Methods
==============
* ``str`` is immutable
* ``str`` methods create a new modified ``str``


Strip Whitespace
----------------
* ``str.strip()`` - remove whitespaces from both ends
* ``str.lstrip()`` - remove whitespaces from left side only
* ``str.rstrip()`` - remove whitespaces from right side only

Strip is a very common method, which you should always call upon any text
from user input, that is from ``input()`` function, but also from files,
socket communication and from internet data transfer. You never know, if
the user did not pasted text from other source, which will add whitespace
at the end of at the beginning of a string.

There are three strip methods: left strip, right strip and strip from both
ends. Word whitespace refers to:

    * ``\n`` - newline
    * ``\t`` - tab
    * `` `` - space
    * ``\v`` - vertical space
    * ``\f`` - form-feed

Most common is plain strip, which will remove all whitespace characters from
both sides at the same time:

>>> name = '\tAngus MacGyver    \n'
>>> name.strip()
'Angus MacGyver'

Right strip:

>>> name = '\tAngus MacGyver    \n'
>>> name.rstrip()
'\tAngus MacGyver'

Left strip:

>>> name = '\tAngus MacGyver    \n'
>>> name.lstrip()
'Angus MacGyver    \n'


Change Case
-----------
* ``str.upper()`` - all letters will be uppercase
* ``str.lower()`` - all letters will be lowercase
* ``str.capitalize()`` - will uppercase first letter of text, lowercase others
* ``str.title()`` - will uppercase first letter of each word, lowercase others
* ``str.swapcase()`` - make lowercase letters upper, and uppercase lower

Comparing not normalized strings will yield invalid or at least
unexpected results:

>>> 'MacGyver' == 'Macgyver'
False

Normalize strings before comparing:

>>> 'MacGyver'.upper() == 'Macgyver'.upper()
True

This is necessary to perform further data analysis.

Upper:

>>> name = 'Angus MacGyver III'
>>> name.upper()
'ANGUS MACGYVER III'

Lower:

>>> name = 'Angus MacGyver III'
>>> name.lower()
'angus macgyver iii'

Title:

>>> name = 'Angus MacGyver III'
>>> name.title()
'Angus Macgyver Iii'


Capitalize:

>>> name = 'Angus MacGyver III'
>>> name.capitalize()
'Angus macgyver iii'


Replace
-------
Replace substring:

>>> name = 'Angus MacGyver Iii'
>>> name.replace('Iii', 'III')
'Angus MacGyver III'

Replace is case sensitive:

>>> name = 'Angus MacGyver Iii'
>>> name.replace('iii', 'III')
'Angus MacGyver Iii'


Starts or Ends With
-------------------
* ``str.startswith()`` - return ``True`` if ``str`` starts with the specified prefix, ``False`` otherwise
* ``str.endswith()`` - return ``True`` if ``str`` ends with the specified suffix, ``False`` otherwise
* optional ``start``, test ``str`` beginning at that position
* optional ``end``, stop comparing ``str`` at that position
* prefix/suffix can also be a tuple of strings to try

>>> email = 'mark.watney@nasa.gov'
>>>
>>>
>>> email.startswith('mark.watney')
True
>>>
>>> email.startswith('melissa.lewis')
False

It also works with tuple of strings to try:

>>> email = 'mark.watney@nasa.gov'
>>> vip = ('mark.watney', 'melissa.lewis')
>>>
>>> email.startswith(vip)
True

>>> email = 'mark.watney@nasa.gov'
>>>
>>>
>>> email.endswith('nasa.gov')
True
>>>
>>> email.endswith('esa.int')
False

>>> email = 'mark.watney@nasa.gov'
>>> whitelist = ('nasa.gov', 'esa.int')
>>>
>>> email.endswith(whitelist)
True


Split by Line
-------------
* ``str.splitlines()`` - split by newline character, don't leave empty lines at the end
* ``str.split('\n')`` - will leave empty string if newline is a the end of str

>>> text = 'Hello\nPython\nWorld'
>>>
>>> text.splitlines()
['Hello', 'Python', 'World']

>>> text = """We choose to go to the Moon!
... We choose to go to the Moon in this decade and do the other things,
... not because they are easy, but because they are hard;
... because that goal will serve to organize and measure the best of our
... energies and skills, because that challenge is one that we are willing
... to accept, one we are unwilling to postpone, and one we intend to win,
... and the others, too."""
>>>
>>>
>>> text.splitlines()  # doctest: +NORMALIZE_WHITESPACE
['We choose to go to the Moon!',
 'We choose to go to the Moon in this decade and do the other things,',
 'not because they are easy, but because they are hard;',
 'because that goal will serve to organize and measure the best of our',
 'energies and skills, because that challenge is one that we are willing',
 'to accept, one we are unwilling to postpone, and one we intend to win,',
 'and the others, too.']


Split by Character
------------------
* ``str.split()`` - Split by given character
* No argument - any number of whitespaces

>>> text = '1,2,3,4'
>>> text.split(',')
['1', '2', '3', '4']

>>> setosa = '5.1,3.5,1.4,0.2,setosa'
>>> setosa.split(',')
['5.1', '3.5', '1.4', '0.2', 'setosa']

>>> text = 'We choose to go to the Moon'
>>> text.split(' ')
['We', 'choose', 'to', 'go', 'to', 'the', 'Moon']

>>> text = 'We choose to go to the Moon'
>>> text.split()
['We', 'choose', 'to', 'go', 'to', 'the', 'Moon']

>>> text = '10.13.37.1      nasa.gov esa.int'
>>> text.split(' ')
['10.13.37.1', '', '', '', '', '', 'nasa.gov', 'esa.int']

>>> text = '10.13.37.1      nasa.gov esa.int'
>>> text.split()
['10.13.37.1', 'nasa.gov', 'esa.int']


Join by Character
-----------------
* [#PyDocStrJoin]_
* ``str.join(sep, sequence)`` - concatenate sequence using separator
* Note, this is a method of a ``str``, not ``tuple.join()`` or ``list.join()``

>>> letters = ['a', 'b', 'c']
>>> ''.join(letters)
'abc'

>>> words = ['We', 'choose', 'to', 'go', 'to', 'the', 'Moon']
>>> ' '.join(words)
'We choose to go to the Moon'

>>> setosa = ['5.1', '3.5', '1.4', '0.2', 'setosa']
>>> ','.join(setosa)
'5.1,3.5,1.4,0.2,setosa'

>>> crew = ['First line', 'Second line', 'Third line']
>>> '\n'.join(crew)
'First line\nSecond line\nThird line'


Join Numbers
------------
* ``(str(x) for x in data)`` - using comprehension or generator expression
* ``map(str, data)`` - using map transformation
* Type cast won't work ``str(data)`` - it will stringify whole list

Method ``str.join()`` expects, that all arguments are strings. Therefore it raises
and error if sequence of numbers is passed:

>>> data = [1, 2, 3]
>>> ','.join(data)
Traceback (most recent call last):
TypeError: sequence item 0: expected str instance, int found

In order to avoid errors, you have to manually convert all the values to strings
before passing them to ``str.join()``. In the following example the generator
expression syntax is used. It will apply ``str()`` to all elements in ``data``.
More information in `Generator Expression`:

>>> data = [1, 2, 3]
>>> ','.join(str(x) for x in data)
'1,2,3'

You can also use ``map()`` function. Map will apply ``str()`` to all elements
in ``data``. More information in `Generator Mapping`:

>>> data = [1, 2, 3]
>>> ','.join(map(str,data))
'1,2,3'


Is Whitespace
-------------
* ``str.isspace()`` - Is whitespace (space, tab, newline)
* `` `` - space
* ``\t`` - tab
* ``\n`` - newline

>>> text = ''
>>> text.isspace()
False

>>> text = ' '
>>> text.isspace()
True

>>> text = '\t'
>>> text.isspace()
True

>>> text = '\n'
>>> text.isspace()
True

.. figure:: img/str-methods-iss.jpg

    ISS - International Space Station.
    Credits: NASA/Crew of STS-132 (img: s132e012208).


Is Alphabet Characters
----------------------
* ``text in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'``

>>> text = 'hello'
>>> text.isalpha()
True

>>> text = 'hello1'
>>> text.isalpha()
False


Is Numeric
----------
* ``str.isdecimal()``
* ``str.isdigit()``
* ``str.isnumeric()``
* ``str.isalnum()``
* https://docs.python.org/library/stdtypes.html#str.isdecimal
* https://docs.python.org/library/stdtypes.html#str.isdigit
* https://docs.python.org/library/stdtypes.html#str.isnumeric
* https://docs.python.org/library/stdtypes.html#str.isalnum

>>> '1'.isdecimal()
True
>>>
>>> '+1'.isdecimal()
False
>>>
>>> '-1'.isdecimal()
False
>>>
>>> '1.'.isdecimal()
False
>>>
>>> '1,'.isdecimal()
False
>>>
>>> '1.0'.isdecimal()
False
>>>
>>> '1,0'.isdecimal()
False
>>>
>>> '1_0'.isdecimal()
False
>>>
>>> '10'.isdecimal()
True

>>> '1'.isdigit()
True
>>>
>>> '+1'.isdigit()
False
>>>
>>> '-1'.isdigit()
False
>>>
>>> '1.'.isdigit()
False
>>>
>>> '1,'.isdigit()
False
>>>
>>> '1.0'.isdigit()
False
>>>
>>> '1,0'.isdigit()
False
>>>
>>> '1_0'.isdigit()
False
>>>
>>> '10'.isdigit()
True

>>> '1'.isnumeric()
True
>>>
>>> '+1'.isnumeric()
False
>>>
>>> '-1'.isnumeric()
False
>>>
>>> '1.'.isnumeric()
False
>>>
>>> '1.0'.isnumeric()
False
>>>
>>> '1,0'.isnumeric()
False
>>>
>>> '1_0'.isnumeric()
False
>>>
>>> '10'.isnumeric()
True

>>> '1'.isalnum()
True
>>>
>>> '+1'.isalnum()
False
>>>
>>> '-1'.isalnum()
False
>>>
>>> '1.'.isalnum()
False
>>>
>>> '1,'.isalnum()
False
>>>
>>> '1.0'.isalnum()
False
>>>
>>> '1,0'.isalnum()
False
>>>
>>> '1_0'.isalnum()
False
>>>
>>> '10'.isalnum()
True


Find Sub-String Position
------------------------
* ``str.find()`` - Finds position of a letter in text
* returns -1 if not found

Finds position of a letter in text:

>>> text = 'We choose to go to the Moon'
>>> text.find('M')
23

Will find first occurrence:

>>> text = 'We choose to go to the Moon'
>>> text.find('o')
5

Also works on substrings:

>>> text = 'We choose to go to the Moon'
>>> text.find('Moo')
23

Will yield ``-1`` if substring is not found:

>>> text = 'We choose to go to the Moon'
>>> text.find('x')
-1


Count Occurrences
-----------------
* ``str.count()``
* returns 0 if not found

>>> text = 'Moon'
>>>
>>>
>>> text.count('o')
2
>>>
>>> text.count('Moo')
1
>>>
>>> text.count('x')
0


Remove Prefix or Suffix
-----------------------
* ``str.removeprefix()``
* ``str.removesuffix()``
* Since Python 3.9: :pep:`616` -- String methods to remove prefixes and suffixes

>>> filename = 'myfile.txt'
>>> filename.removeprefix('my')
'file.txt'

>>> filename = 'myfile.txt'
>>> filename.removesuffix('.txt')
'myfile'


Method Chaining
---------------
>>> text = 'Python'
>>>
>>> text = text.upper()
>>> text = text.replace('P', 'C')
>>> text = text.title()
>>>
>>> print(text)
Cython

>>> text = 'Python'
>>>
>>> text = text.upper().replace('P', 'C').title()
>>>
>>> print(text)
Cython

Note, that there cannot be any char, not even space after ``\`` character:

>>> text = 'Python'
>>>
>>> text = text.upper() \
...            .replace('P', 'C') \
...            .title()
>>>
>>> print(text)
Cython

Backslash method is very error-prone, this is the reason why brackets are
recommended:

>>> text = 'Python'
>>>
>>> text = (
...     text
...     .upper()
...     .replace('P', 'C')
...     .title()
... )
>>>
>>> print(text)
Cython

How it works:

    #. ``text -> 'Python'``
    #. ``'Python'.upper() -> 'PYTHON'``
    #. ``'PYTHON'.replace('P', 'C') -> 'CYTHON'``
    #. ``'CYTHON'.title() -> 'Cython'``

>>> text = 'Python'
>>>
>>> text = text.upper().startswith('P').replace('P', 'C')
Traceback (most recent call last):
AttributeError: 'bool' object has no attribute 'replace'


Use Case - 0x01
---------------
>>> DATA = 'ul. pANA tWARdoWSKiego 3'
>>>
>>> result = (
...     DATA
...
...     # Normalize
...     .upper()
...
...     # Remove whitespace control chars
...     .replace('\n', ' ')
...     .replace('\t', ' ')
...     .replace('\v', ' ')
...     .replace('\f', ' ')
...
...     # Remove whitespaces
...     .replace('    ', ' ')
...     .replace('   ', ' ')
...     .replace('  ', ' ')
...
...     # Remove special characters
...     .replace('$', '')
...     .replace('@', '')
...     .replace('#', '')
...     .replace('^', '')
...     .replace('&', '')
...     .replace('.', '')
...     .replace(',', '')
...     .replace('|', '')
...
...     # Remove prefixes
...     .removeprefix('ULICA')
...     .removeprefix('UL')
...     .removeprefix('OSIEDLE')
...     .removeprefix('OS')
...
...     # Substitute
...     .replace('3', 'III')
...     .replace('2', 'II')
...     .replace('1', 'I')
...
...     # Format output
...     .title()
...     .replace('Iii', 'III')
...     .replace('Ii', 'II')
...     .strip()
... )
>>>
>>> print(result)
Pana Twardowskiego III


References
----------
.. [#PyDocStrJoin] van Rossum, G. et al. Why is join() a string method instead of a list or tuple method? Python documentation. Year: 2022. Retrieved: 2022-09-25. URL: https://docs.python.org/3/faq/design.html#why-is-join-a-string-method-instead-of-a-list-or-tuple-method


Assignments
-----------
.. literalinclude:: assignments/type_strmethods_a.py
    :caption: :download:`Solution <assignments/type_strmethods_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_strmethods_b.py
    :caption: :download:`Solution <assignments/type_strmethods_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_strmethods_c.py
    :caption: :download:`Solution <assignments/type_strmethods_c.py>`
    :end-before: # Solution
