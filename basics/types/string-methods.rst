String Methods
==============


Important
---------
* ``str`` is immutable
* ``str`` methods create a new modified ``str``


Strip Whitespace
----------------
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


Starts With
-----------
``.startswith()`` method answers the question if string "starts with" other
substring.

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


Ends With
---------
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

>>> text = '10.13.37.1      nasa.gov esa.int roscosmos.ru'
>>> text.split(' ')
['10.13.37.1', '', '', '', '', '', 'nasa.gov', 'esa.int', 'roscosmos.ru']

>>> text = '10.13.37.1      nasa.gov esa.int roscosmos.ru'
>>> text.split()
['10.13.37.1', 'nasa.gov', 'esa.int', 'roscosmos.ru']


Join by Character
-----------------
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
>>> text = 'hello'
>>> text.isalpha()
True

>>> text = 'hello1'
>>> text.isalpha()
False


Is Numeric
----------
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
Since Python 3.9: :pep:`616` -- String methods to remove prefixes and suffixes

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
