Str Methods
===========


Rationale
---------
* ``str`` is immutable
* ``str`` methods create a new modified ``str``

>>> a = 'Python'
>>> a.replace('P', 'C')
'Cython'
>>> print(a)
Python

>>> a = 'Python'
>>> b = a.replace('P', 'C')
>>>
>>> print(a)
Python
>>> print(b)
Cython

>>> a = 'Python'
>>> a = a.replace('P', 'C')
>>>
>>> print(a)
Cython


Strip Whitespace
----------------
>>> name = '\tAngus MacGyver    \n'
>>>
>>> name.strip()
'Angus MacGyver'
>>> name.rstrip()
'\tAngus MacGyver'
>>> name.lstrip()
'Angus MacGyver    \n'


Change Case
-----------
* Unify data format before analysis

>>> name = 'Angus MacGyver III'
>>>
>>> name.upper()
'ANGUS MACGYVER III'
>>> name.lower()
'angus macgyver iii'
>>> name.title()
'Angus Macgyver Iii'
>>> name.capitalize()
'Angus macgyver iii'


Replace
-------
>>> name = 'Angus MacGyver Iii'
>>>
>>> name.replace('Iii', 'III')
'Angus MacGyver III'


Starts With
-----------
>>> email = 'mark.watney@nasa.gov'
>>>
>>> email.startswith('mark.watney')
True
>>> email.startswith('melissa.lewis')
False

>>> email = 'mark.watney@nasa.gov'
>>>
>>> email.startswith(('mark.watney', 'melissa.lewis'))
True

>>> email = 'mark.watney@nasa.gov'
>>> vip = ('mark.watney', 'melissa.lewis')
>>>
>>> email.startswith(vip)
True


Ends With
---------
>>> email = 'mark.watney@nasa.gov'
>>>
>>> email.endswith('nasa.gov')
True
>>> email.endswith('esa.int')
False

>>> email = 'mark.watney@nasa.gov'
>>>
>>> email.endswith(('nasa.gov', 'esa.int'))
True

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

>>> setosa = '5.1,3.5,1.4,0.2,setosa'
>>>
>>> setosa.split(',')
['5.1', '3.5', '1.4', '0.2', 'setosa']

>>> text = 'We choose to go to the Moon'
>>>
>>> text.split(' ')
['We', 'choose', 'to', 'go', 'to', 'the', 'Moon']
>>> text.split()
['We', 'choose', 'to', 'go', 'to', 'the', 'Moon']

>>> text = '10.13.37.1      nasa.gov esa.int roscosmos.ru'
>>>
>>> text.split(' ')
['10.13.37.1', '', '', '', '', '', 'nasa.gov', 'esa.int', 'roscosmos.ru']
>>> text.split()
['10.13.37.1', 'nasa.gov', 'esa.int', 'roscosmos.ru']


Join by Character
-----------------
>>> text = ['We', 'choose', 'to', 'go', 'to', 'the', 'Moon']
>>> ' '.join(text)
'We choose to go to the Moon'

>>> setosa = ['5.1', '3.5', '1.4', '0.2', 'setosa']
>>> ','.join(setosa)
'5.1,3.5,1.4,0.2,setosa'

>>> crew = ['Mark Watney', 'Jan Twardowski', 'Melissa Lewis']
>>>
>>> '\n'.join(crew)
'Mark Watney\nJan Twardowski\nMelissa Lewis'

>>> TEXT = ['We choose to go to the Moon!',
...         'We choose to go to the Moon in this decade and do the other things,',
...         'not because they are easy, but because they are hard;',
...         'because that goal will serve to organize and measure the best of our energies and skills,',
...         'because that challenge is one that we are willing to accept, one we are unwilling to postpone,',
...         'and one we intend to win, and the others, too.']
...
>>> print('\n'.join(TEXT))
We choose to go to the Moon!
We choose to go to the Moon in this decade and do the other things,
not because they are easy, but because they are hard;
because that goal will serve to organize and measure the best of our energies and skills,
because that challenge is one that we are willing to accept, one we are unwilling to postpone,
and one we intend to win, and the others, too.


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
>>> '+1'.isdecimal()
False
>>> '-1'.isdecimal()
False
>>> '1.'.isdecimal()
False
>>> '1,'.isdecimal()
False
>>> '1.0'.isdecimal()
False
>>> '1,0'.isdecimal()
False
>>> '1_0'.isdecimal()
False
>>> '10'.isdecimal()
True

>>> '1'.isdigit()
True
>>> '+1'.isdigit()
False
>>> '-1'.isdigit()
False
>>> '1.'.isdigit()
False
>>> '1,'.isdigit()
False
>>> '1.0'.isdigit()
False
>>> '1,0'.isdigit()
False
>>> '1_0'.isdigit()
False
>>> '10'.isdigit()
True

>>> '1'.isnumeric()
True
>>> '+1'.isnumeric()
False
>>> '-1'.isnumeric()
False
>>> '1.'.isnumeric()
False
>>> '1.0'.isnumeric()
False
>>> '1,0'.isnumeric()
False
>>> '1_0'.isnumeric()
False
>>> '10'.isnumeric()
True

>>> '1'.isalnum()
True
>>> '+1'.isalnum()
False
>>> '-1'.isalnum()
False
>>> '1.'.isalnum()
False
>>> '1,'.isalnum()
False
>>> '1.0'.isalnum()
False
>>> '1,0'.isalnum()
False
>>> '1_0'.isalnum()
False
>>> '10'.isalnum()
True


Find Sub-String Position
------------------------
>>> text = 'We choose to go to the Moon'
>>>
>>> text.find('M')
23
>>> text.find('Moo')
23
>>> text.find('x')
-1


Count Occurrences
-----------------
>>> text = 'Moon'
>>>
>>> text.count('o')
2
>>> text.count('Moo')
1
>>> text.count('x')
0


Remove Prefix or Suffix
-----------------------
Since Python 3.9: :pep:`616` -- String methods to remove prefixes and suffixes

>>> filename = '1969-apollo11.txt'
>>>
>>> filename.removeprefix('1969-')
'apollo11.txt'
>>> filename.removesuffix('.txt')
'1969-apollo11'
>>> filename.removeprefix('1969-').removesuffix('.txt')
'apollo11'


Method Chaining
---------------
>>> a = 'Python'
>>>
>>> a = a.upper()
>>> a = a.replace('P', 'C')
>>> a = a.title()
>>>
>>> print(a)
Cython

>>> a = 'Python'
>>> a = a.upper().replace('P', 'C').title()
>>>
>>> print(a)
Cython

>>> a = 'Python'
>>> a.upper().replace('P', 'C').title()
'Cython'

How it works:

    #. a -> 'Python'
    #. 'Python'.upper() -> 'PYTHON'
    #. 'PYTHON'.replace('P', 'C') -> 'CYTHON'
    #. 'CYTHON'.title() -> 'Cython'

>>> a = 'Python'
>>> a = a.upper().startswith('P').replace('P', 'C')
Traceback (most recent call last):
AttributeError: 'bool' object has no attribute 'replace'

Note, that there cannot be any char, not even space after ``\`` character:

>>> a = 'Python'
>>> a = a.upper() \
...      .replace('P', 'C') \
...      .title()
>>>
>>> print(a)
Cython

>>> a = 'Python'
>>> a = (a.upper()
...       .replace('P', 'C')
...       .title())
>>>
>>> print(a)
Cython


Assignments
-----------
.. literalinclude:: assignments/str_methods_a.py
    :caption: :download:`Solution <assignments/str_methods_a.py>`
    :end-before: # Solution
