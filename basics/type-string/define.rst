Str Define
==========


Definition
----------
* ``str`` is a sequence

Empty string:

>>> data = ''
>>> data = str()

Define string:

>>> data = 'Mark Watney'
>>> data = str('Mark Watney')

Multiline string:

>>> data =  'First line\nSecond line\nThird line'

>>> data = """First line
... Second line
... Third line"""

>>> data = """We choose to go to the Moon!
... We choose to go to the Moon in this decade and do the other things,
... not because they are easy, but because they are hard;
... because that goal will serve to organize and measure the best of our
... energies and skills, because that challenge is one that we are willing
... to accept, one we are unwilling to postpone, and one we intend to win,
... and the others, too."""


Quotes or Apostrophe
--------------------
* ``"`` and ``'`` works the same
* Choose one and keep consistency in code
* Python console prefers single quote (``'``) character
* It matters for ``doctest``, which compares two outputs character by character
* :pep:`257` -- Docstring Conventions: For multiline ``str`` always use three
  double quote (``"""``) characters

Python console prefers single quote (``'``):

>>> data = 'My name is José Jiménez'
>>> data
'My name is José Jiménez'

Python console prefers single quote (``'``):

>>> data = "My name is José Jiménez"
>>> data
'My name is José Jiménez'

It's better to use double quotes, when text has apostrophes.
This is the behavior of Python console:

>>> data = 'My name\'s José Jiménez'
>>> data
"My name's José Jiménez"

HTML and XML uses double quotes to enclose attribute values, hence it's
better to use single quotes for the string:

>>> data = '<a href="http://python.astrotech.io">Python and Machine Learning</a>'
>>> data
'<a href="http://python.astrotech.io">Python and Machine Learning</a>'

:pep:`257` -- Docstring Conventions: For multiline ``str`` always use three
double quote (``"""``) characters

>>> data = """My name's \"José Jiménez\""""
>>> data = '''My name\'s "José Jiménez"'''


Type Casting
------------
Builtin function  ``str()`` converts argument to ``str``

>>> str('Moon')
'Moon'
>>> str(1969)
'1969'
>>> str(1.337)
'1.337'

Builtin function ``print()`` before printing on the screen
runs ``str()`` on its arguments:

>>> print(1969)
1969


Assignments
-----------
.. literalinclude:: assignments/str_define_a.py
    :caption: :download:`Solution <assignments/str_define_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/str_define_b.py
    :caption: :download:`Solution <assignments/str_define_b.py>`
    :end-before: # Solution
