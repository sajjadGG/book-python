Syntax Assignment
=================


Rationale
---------
* Identifier is a formal name for variable
* Variables can change it's value during the program
* In Python there are no constants
* ``NameError`` when using not declared variable
* ``AttributeError`` when cannot assign to variables


Variables
---------
Identifiers are case sensitive. Use lowercase letters for variable names:

>>> name = 'Mark Watney'

By convention you should use use Latin characters and English names
(Non-ASCII characters in an identifier):

>>> name = 'Mark'
>>> imię = 'Mark'

Underscore ``_`` is used for multi-word names

>>> first_name = 'Mark'
>>> last_name = 'Watney'

You can also join words.

>>> firstname = 'Mark'
>>> lastname = 'Watney'

Although it works for two words, it could be hard to read for three or more:

You should always use lowercase letters:

>>> name = 'Mark Watney'
>>> Name = 'Mark Watney'

Capital letters by convention has different meaning. The code will run without
errors or warnings, but you can mislead others. Remember code is read by 80%
of a time, and written in 20%.

Not ok by convention :

>>> firstName = 'Mark'  # Camel Case - not used in Python
>>> Firstname = 'Mark'  # Pascal Case - reserved for class names
>>> FirstName = 'Mark'  # Pascal Case - reserved for class names

Camel Case convention is not used in Python. It is common in other programming
language such as C / C++ / C# / Java / JavaScript.

You can put numbers in variables:

>>> name1 = 'Mark'
>>> name2 = 'Mark'

BUt the number cannot be the first character (otherwise will produce
``SyntaxError``):

>>> 1name = 'Mark'  # doctest: +SKIP


Constants
---------
Identifiers (variable/constant names) are case sensitive.
Uppercase letters are used for constants (by convention):

>>> FILE = '/etc/passwd'
>>> FILENAME = '/etc/group'

Underscore ``_`` is used for multi-word names:

>>> FILE_NAME = '/etc/shadow'

Python do not distinguish between variables and constants.
Python allows you to change "constants" but it's a bad practice (good IDE will
tell you):

>>> NAME = 'Mark Watney'
>>> NAME = 'Melissa Lewis'


Variables vs. Constants
-----------------------
* Variables vs. constants - Names are case sensitive

>>> name = 'Mark Watney'  # variable
>>> NAME = 'Mark Watney'  # constant
>>> Name = 'Mark Watney'  # class

Definition of second, minute or hour does not change based on location
or country (those values should be constants).

Definition of workday, workweek and workmonth differs based on location
- each country can have different work times (those values should be
variables).

>>> SECOND = 1
>>> MINUTE = 60 * SECOND
>>> HOUR = 60 * MINUTE

>>> workday = 8 * HOUR
>>> workweek = 40 * HOUR

For physical units it is ok to use proper cased names. It is better to be
compliant with well known standard, than to enforce something which will
mislead everyone.

>>> Pa = 1
>>> hPa = 100 * Pa
>>> kPa = 1000 * Pa
>>> MPa = 1000000 * Pa

The code above is far more readable, than the following snippet:

>>> PA = 1
>>> HPA = 100 * PA
>>> KPA = 1000 * PA
>>> MPA = 1000000 * PA

Note, that the only change was in variable names. As you can see, this could
have a huge impact on describing the intent of what you want to achieve with
the code.


Assignments
-----------
.. literalinclude:: assignments/syntax_assignment_a.py
    :caption: :download:`assignments/syntax_assignment_a.py`
    :end-before: # Solution

.. literalinclude:: assignments/syntax_assignment_b.py
    :caption: :download:`assignments/syntax_assignment_b.py`
    :end-before: # Solution

.. literalinclude:: assignments/syntax_assignment_c.py
    :caption: :download:`assignments/syntax_assignment_c.py`
    :end-before: # Solution

.. literalinclude:: assignments/syntax_assignment_d.py
    :caption: :download:`assignments/syntax_assignment_d.py`
    :end-before: # Solution

.. literalinclude:: assignments/syntax_assignment_e.py
    :caption: :download:`assignments/syntax_assignment_e.py`
    :end-before: # Solution
