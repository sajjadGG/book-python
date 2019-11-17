.. _Basic Syntax:

*************
Syntax Basics
*************


Indentation instead of braces
=============================
.. highlights::
    * Python uses indentation instead of braces
    * `4 spaces indentation, no tabs <https://youtu.be/SsoOG6ZeyUI>`_
    * Python throws ``IndentationError`` exception on problem
    * Code indented on the same level belongs to block:

.. code-block:: python

    if True:
        print('First line of the true statement')
        print('Second line of the true statement')
        print('Third line of the true statement')
    else:
        print('This is false')


End of lines
============
.. highlights::
    * No semicolon (``;``) at the end of lines
    * ``\r\n`` and ``\n`` are good:

.. code-block:: python

    print('Hello!\nHow are you?')
    print('Hello!\r\nHow are you?')


Comments
========

Line comments
---------------
.. highlights::
    * Indent must be on the same level as block indent
    * Hash (``#``), space and then comment:

.. code-block:: python

    # José Jiménez says hello
    print('My name... José Jiménez')

Inline comments
---------------
.. highlights::
    * Source code, two spaces, hash (``#``), space and then comment:

.. code-block:: python

    print('My name... José Jiménez')  # José Jiménez says hello

Multiline comments
------------------
.. highlights::
    * Triple single quotes ``'''``
    * Triple double quotes ``"""`` (more common)
    * Both ``'''`` and ``"""`` quotes works the same
    * if assigned to variable, it serves as multiline ``str``

.. code-block:: python

    """
    We choose to go to the Moon!
    We choose to go to the Moon in this decade and do the other things,
    not because they are easy, but because they are hard;
    because that goal will serve to organize and measure the best of our energies and skills,
    because that challenge is one that we are willing to accept, one we are unwilling to postpone,
    and one we intend to win, and the others, too.
    """

Docstring
---------
.. highlights::
    * Docstring is a first multiline comment in:

        * File / Module
        * Class
        * Method / Function

    * It is accessible in ``__doc__`` property of an object
    * Used for generating ``help()`` documentation
    * Used for ``doctest``

.. code-block:: python
    :caption: Docstring used for documentation

    def apollo_dsky(noun, verb):
        """
        This is the Apollo Display Keyboard
        It takes noun and verb
        """
        print(f'Program selected. Noun: {noun}, verb: {verb}')

.. code-block:: python
    :caption: Docstring used for doctest

    def add(a, b):
        """
        Sums two numbers.

        >>> add(1, 2)
        3
        >>> add(-1, 1)
        0
        """
        return a + b

Commented out code
------------------
.. highlights::
    * Never!
    * Use Version Control System instead - e.g.: ``git blame``
    * IDE has Local history (modifications) and you can compare file


Variables and constants
=======================
.. highlights::
    * ``NameError`` when using not declared variable
    * ``AttributeError`` when cannot assign to variables
    * Names are case sensitive

.. code-block:: python

    name = 'José Jiménez'
    NAME = 'Иван Иванович'
    Name = 'Jan Twardowski'

Variable declaration
--------------------
.. highlights::
    * Lowercase letters for variable names
    * Underscore ``_`` is used for multi-word names

.. code-block:: python

    name = 'José Jiménez'

.. code-block:: python

    first_name = 'José'
    last_name = 'Jiménez'

Constant declaration
--------------------
.. highlights::
    * Uppercase letters for constants names
    * Underscore ``_`` is used for multi-word names

.. code-block:: python

    PATH = '/etc/passwd'

.. code-block:: python

    FILE_NAME = '/etc/shadow'

Variables vs. constants
-----------------------
.. highlights::
    * Names are case sensitive
    * Python do not distinguish between variables and constants
    * Python allows you to change "constants" but it's a bad practice (good IDE will tell you)

.. code-block:: python

    name = 'José Jiménez'
    NAME = 'Иван Иванович'
    Name = 'Jan Twardowski'

.. code-block:: python

    NAME = 'José Jiménez'
    NAME = 'Иван Иванович'


``print()``
===========
.. highlights::
    * ``print()`` adds ``'\n'`` at the end
    * Prints on the screen
    * Variable substitution
    * Special characters
    * More in :ref:`Print Formatting`

.. code-block:: python

    print('My name... José Jiménez')
    # My name... José Jiménez

.. code-block:: python

    name = 'José Jiménez'


    print('My name... {name}')
    # My name... {name}

    print(f'My name... {name}')
    # My name... José Jiménez

    print(f'My name...\n\t{name}')
    # My name...
    #     José Jiménez


Type Annotations
================
.. epigraph::
    Types are not required, and never will be
    -- Guido van Rossum, Python BDFL

.. highlights::
    * Since Python 3.5
    * ``SyntaxError`` in Python before 3.5
    * Sometimes called "type hints"
    * Good IDE will give you hints
    * Types are used extensively in system libraries
    * More and more books and documentations use types
    * To type check use: ``mypy`` or ``pyre-check`` (more in :ref:`cicd-tools`)

Basic types
-----------
.. code-block:: python

    name: str = 'Jan Twardowski'
    age: int = 30
    is_adult: bool = True

Types do not enforce checking
-----------------------------
.. highlights::
    * This code will run without any problems
    * Although ``mypy`` or ``pyre-check`` will throw error

.. code-block:: python

    name: int = 'Jan Twardowski'
    age: float = 30
    is_adult: int = True

Why?
----
.. highlights::
    * Good IDE will highlight, incorrect types

.. code-block:: python

    def add_numbers(a: int, b: float) -> int:
        return int(a + b)


    add_numbers(1, 2.5)
    add_numbers('a', 'b')       # Good IDE should highlight the problem here

More advanced topics
--------------------
.. note::
    The topic will be continued in chapter: :ref:`Type Annotation`


Assignments
===========

Meet Python
-----------
* Complexity level: easy
* Lines of code to write: 2 lines + 2 lines of comment
* Estimated time of completion: 5 min
* Filename: :download:`solution/syntax_python.py`

#. Create Python script
#. Add interpreter declaration
#. Under interpreter declaration add multiline comment with program description (copy-paste from book)
#. Declare variable ``name`` and set its value to your name
#. Add inline comment to variable declaration with text: "This is my name"
#. Print variable
#. Next line under ``print`` statement add line comment, with expected output
#. Run script

:The whys and wherefores:
    * Tworzenie skryptów Python
    * Deklaracja zmiennych
    * Komentowanie kodu
    * Wyświetlanie wartości zmiennych

:Hint:
    * ``print()``
