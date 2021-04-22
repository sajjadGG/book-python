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
>>>
>>> data = """First line
... Second line
... Third line"""


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

HTML and XML uses double quotes to enclose attribute values, hence it's better
to use single quotes for the string:

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
.. literalinclude:: assignments/type_strdefine_a.py
    :caption: :download:`Solution <assignments/type_strdefine_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_strdefine_b.py
    :caption: :download:`Solution <assignments/type_strdefine_b.py>`
    :end-before: # Solution
