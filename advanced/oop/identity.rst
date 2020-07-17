***************
Object Identity
***************


Identity
========
.. highlights::
    * ``id()`` will change every time you execute script
    * An integer which is guaranteed to be unique and constant for this object during its lifetime
    * Two objects with non-overlapping lifetimes may have the same id() value.
    * In CPython it's also the memory address of the corresponding C object

.. code-block:: python
    :caption: Note, that ``id()`` will change every time you execute script

    a = 'str'

    id(a)
    # 4499664048

    hex(id(a))
    # '0x10c336cb0'



.. _String interning:

String interning
================
.. highlights::
    * https://en.wikipedia.org/wiki/String_interning
    * Method of storing only one copy of each distinct string value, which must be immutable
    * many high level languages use it
    * string literals and values are internally kept in a hashed list called 'string intern pool' and those which are identical are rendered as references to the same object
    * possible because ``str`` are immutable
    * implementation dependent
    * Jython, IronPython, PyPy and others may intern more aggressively
    * Calling the ``intern()`` function on strings will "force" a string to have the same object identity as any equivalent and previously interned string

.. code-block:: python
    :caption: CPython 3.7.4

    ('a' * 4096) is ('a' * 4096)
    # True

    ('a' * 4097) is ('a' * 4097)
    # False


``is``
======
.. highlights::
    * ``is`` checks for object identity
    * ``is`` tests for identity, not equality
    * Compares ``id()`` output for both objects
    * CPython: compares the memory address a object resides in
    * Is used for checking if ``None``
    * Testing strings with ``is`` only works when the strings are interned

Test if empty
-------------
.. code-block:: python

    if name is None:
        print('Your name is empty')
    else:
        print(f'Hello {name}')

Test if value is equal
----------------------
.. versionchanged:: Python 3.8
    Compiler produces a ``SyntaxWarning`` when identity checks (``is`` and ``is not``) are used with certain types of literals (e.g. ``str``, ``int``). These can often work by accident in *CPython*, but are not guaranteed by the language spec. The warning advises users to use equality tests (``==`` and ``!=``) instead.

 .. code-block:: python
    :caption: Bad

     if name is 'Mark Watney':
        print('You are Space Pirate!')
     else:
        print('You are just a regular astronaut...')

 .. code-block:: python
    :caption: Good

     if name == 'Mark Watney':
        print('You are Space Pirate!')
     else:
        print('You are just a regular astronaut...')

Using ``is`` in script
----------------------
.. highlights::
    * both objects has the same ``id``.

.. code-block:: python

    a = 'Jan Twardowski'
    b = 'Jan Twardowski'

.. code-block:: python

    print(a)        # Jan Twardowski
    print(b)        # Jan Twardowski

    print(a == b)   # True
    print(a is b)   # True

    print(id(a))    # 4430933296
    print(id(b))    # 4430933296

Using ``is`` in REPL (evaluated line by line)
---------------------------------------------
.. code-block:: python

    a = 'Jan Twardowski'

.. code-block:: python

    b = 'Jan Twardowski'

.. code-block:: python

    print(a)        # Jan Twardowski
    print(b)        # Jan Twardowski

    print(a == b)   # True
    print(a is b)   # False

    print(id(a))    # 4784790960
    print(id(b))    # 4784791408

Using ``is`` in REPL (evaluated at once)
----------------------------------------
.. code-block:: python

    a = 'Jan Twardowski'
    b = 'Jan Twardowski'

.. code-block:: python

    print(a)        # Jan Twardowski
    print(b)        # Jan Twardowski

    print(a == b)   # True
    print(a is b)   # True

    print(id(a))    # 4784833072
    print(id(b))    # 4784833072


Assignments
===========
.. todo:: Create Assignments
