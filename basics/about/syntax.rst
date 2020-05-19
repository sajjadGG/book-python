.. _Basic Syntax:

*************
Python Syntax
*************


Variables
=========
.. highlights::
    * Names are case sensitive
    * Lowercase letters for variable names
    * Underscore ``_`` is used for multi-word names
    * ``NameError`` when using not declared variable
    * ``AttributeError`` when cannot assign to variables

.. code-block:: python
    :caption: Variable declaration

    name = 'Mark Watney'

    first_name = 'Mark'
    last_name = 'Watney'

    firstname = 'Mark'
    lastname = 'Watney'

.. code-block:: python
    :caption: Variables vs. constants - Names are case sensitive

    name = 'Mark Watney'
    Name = 'Jan Twardowski'


Constants
=========
.. highlights::
    * Names are case sensitive
    * Underscore ``_`` is used for multi-word names
    * Uppercase letters for "constant" names
    * Python do not distinguish between variables and constants
    * Python allows you to change "constants" but it's a bad practice (good IDE will tell you)

.. code-block:: python
    :caption: "Constant" declaration

    FILE = '/etc/passwd'
    FILE_NAME = '/etc/shadow'
    FILENAME = '/etc/group'

.. code-block:: python
    :caption: Python allows you to change "constants" but it's a bad practice (good IDE will tell you)

    NAME = 'Mark Watney'
    NAME = 'Jan Twardowski'

.. code-block:: python
    :caption: Variables vs. constants - Names are case sensitive

    name = 'Mark Watney'
    NAME = 'Jan Twardowski'
    Name = 'José Jiménez'


Printing Values
===============
.. highlights::
    * Prints on the screen
    * f-string formatting for variable substitution
    * More in :ref:`Stdlib Builtin Printing`

.. code-block:: python

    print('My name... José Jiménez')
    # My name... José Jiménez

.. code-block:: python

    name = 'José Jiménez'


    print('My name... {name}')
    # My name... {name}

    print(f'My name... {name}')
    # My name... José Jiménez


End of Lines
============
.. highlights::
    * No semicolon (``;``) at the end of lines
    * ``\r\n`` and ``\n`` works
    * :pep:`8`: Use ``\n``

.. doctest::

    >>> print('Hello!\nHow are you?')
    Hello!
    How are you?


Comments
========
.. highlights::
    * :pep:`8` for line comments: Hash (``#``), space and then comment
    * :pep:`8` for inline comments: code, two spaces, hash (``#``), space and then comment
    * Commented out code:

        * Never!
        * Use Version Control System instead - e.g.: ``git blame``
        * IDE has Local history (modifications) and you can compare file

.. code-block:: python
    :caption: Line comments

    # Mark thinks he is...
    print('Mark Watney: Space Pirate')

.. code-block:: python
    :caption: Inline comments

    print('Mark Watney: Space Pirate')  # This is who Mark Watney is


Indentation
===========
.. highlights::
    * Python uses indentation instead of braces
    * Code indented on the same level belongs to block
    * :pep:`8`: 4 spaces indentation, `no tabs <https://youtu.be/SsoOG6ZeyUI>`_
    * Python throws ``IndentationError`` exception on problem

.. code-block:: python

    if True:
        print('True statement, first line')
        print('True statement, second line')
    else:
        print('Else statement, first line')
        print('Else statement, second line')

.. code-block:: python

    if True:
        print('Outer block, true statement, first line')
        print('Outer block, true statement, second line')

        if True:
            print('Inner block, true statement, first line')
            print('Inner block, true statement, second line')
        else:
            print('Inner block, else statement, fist line')
            print('Inner block, else statement, second line')

    else:
        print('Outer block, else statement, first line')
        print('Outer block, else statement, second line')


Assignments
===========

Pyton Syntax
------------
* Complexity level: easy
* Lines of code to write: 2 lines + 2 lines of comment
* Estimated time of completion: 5 min
* Solution: :download:`solution/about_syntax.py`

:English:
    #. Create Python script
    #. At at top, add a multiline comment with program description (todo from this assignments)
    #. Declare variable ``name`` and set its value to your name
    #. Add inline comment to variable declaration with text: "This is my name"
    #. Print "Hello World NAME", where NAME is your name (variable ``name``)

:Polish:
    #. Stwórz skrypt Python
    #. Na górze pliku dodaj wieloliniowy komentarz z opisem programu (punkty do wykonania z tego zadania)
    #. Zadeklaruj zmienną ``name`` i ustaw jej wartość na Twoje imię
    #. Dodaj komentarz "inline" do zmiennej o treści: "This is my name"
    #. Wypisz "Hello World NAME", gdzie NAME to Twoje imię (zmienna ``name``)

:The whys and wherefores:
    * Tworzenie skryptów Python
    * Deklaracja zmiennych
    * Komentowanie kodu
    * Wyświetlanie wartości zmiennych

:Hint:
    * ``print()``
