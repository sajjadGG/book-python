Syntax Anchor
=============
* ``.`` - any character except a newline (changes meaning with ``re.DOTALL``)
* ``^`` - start of line (changes meaning with ``re.MULTILINE``)
* ``$`` - end of line (changes meaning with ``re.MULTILINE``)
* ``\A`` - start of text (doesn't change meaning with ``re.MULTILINE``)
* ``\Z`` - end of text (doesn't change meaning with ``re.MULTILINE``)


Any Character
-------------
* ``.`` - any character except a newline (changes meaning with ``re.DOTALL``)

>>> import re
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'

Search for letters ``Ap`` followed by any character:

>>> re.findall('Ap.', TEXT)
['Apr']

Search for uppercase letter followed by any two characters:

>>> re.findall('[A-Z]..', TEXT)
['Yur', 'Gag', 'Apr']

Example:

>>> re.findall('[0-9][0-9]..', TEXT)
['12th', '1961', '07 a']
>>>
>>> re.findall('[A-Z].. [0-9][0-9]..', TEXT)
['Apr 12th']


Start of Line
-------------
* ``^`` - start of a line
* Changes meaning with ``re.MULTILINE``

>>> import re
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'

Search for a capital letter in text at the start of a line:

>>> re.findall('^[A-Z]', TEXT)
['Y']

Search for a capital letter anywhere in text:

>>> re.findall('[A-Z]', TEXT)
['Y', 'G', 'A']


End of Line
-----------
* ``$`` - end of line
* Changes meaning with ``re.MULTILINE``

>>> import re
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'

Give me last three characters in a text:

>>> re.findall('...$', TEXT)
['am.']


Start of String
---------------
* ``\A`` - start of a text
* Doesn't change meaning with ``re.MULTILINE``

>>> import re
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'

Search for a capital letter in text at the start of a line:

>>> re.findall('\A[A-Z]', TEXT)
['Y']

Note, that the output is identical to Start of a Line ``^``. It will differ
when ``re.MULTILINE`` flag is present.

>>> re.findall('^[A-Z]', TEXT)
['Y']


End of String
-------------
* ``\Z`` - end of a text
* Doesn't change meaning with ``re.MULTILINE``

>>> import re
>>> TEXT = 'Yuri Gagarin launched to space on Apr 12th, 1961 at 6:07 am.'

Give me last three characters in a text:

>>> re.findall('...\Z', TEXT)
['am.']

Note, that the output is identical to Start of a Line ``^``. It will differ
when ``re.MULTILINE`` flag is present.

>>> re.findall('...$', TEXT)
['am.']


Use Case - 0x01
---------------
* ``abc.e`` - text `abc` then any character followed by letter `e`
