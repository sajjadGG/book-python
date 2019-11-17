***************
Object Identity
***************


``id()``
========
.. highlights::
    * ``id()`` will change every time you execute script
    * An integer which is guaranteed to be unique and constant for this object during its lifetime
    * Two objects with non-overlapping lifetimes may have the same id() value.
    * In CPython it's also the memory address of the corresponding C object

``hash()``
==========
.. highlights::
    * Return the hash value of the object (if it has one)
    * ``hash() ->  int``
    * They are used to quickly compare dictionary keys during a dictionary lookup
    * ``set()`` elements has to be hashable
    * ``dict()`` keys has to be hashable
    * User-defined classes have ``__eq__()`` and ``__hash__()`` methods by default
    * All objects compare unequal (except with themselves)
    * ``x.__hash__()`` returns an appropriate value such that ``x == y`` implies both that ``x is y`` and ``hash(x) == hash(y)``

.. code-block:: python
    :caption: ``dict()`` keys has to be hashable

    key = 'my_key'

    my_dict = {
        'a': 'key can be str',
        2: 'key can be int',
        3.3: 'key can be float',
        ('a', 2, 3.3): 'key can be tuple',
        key: 'key can be str',
    }

.. code-block:: python
    :caption: ``set()`` elements has to be hashable

    {1, 1, 2}
    # {1, 2}

    {1, 1.1, 'a'}
    # {1, 1.1, 'a'}

    {'a', (1, 2)}
    # {'a', (1, 2)}

.. code-block:: python
    :caption: ``set()`` elements has to be hashable

    class Astronaut:
        def __init__(self, name):
            self.name = name


    jan = Astronaut('Jan Twardowski')
    data = {jan, jan}
    len(data)
    # 1

    data = {Astronaut('Jan Twardowski'), Astronaut('Jan Twardowski')}
    len(data)
    # 2

.. code-block:: python
    :caption: Generating hash and object comparision

    class Astronaut:
        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name

        def __hash__(self, *args, **kwargs):
            """
            __hash__ should return the same value for objects that are equal.
            It also shouldn't change over the lifetime of the object;
            generally you only implement it for immutable objects.
            """
            return hash(self.first_name) + hash(self.last_name)

        def __eq__(self, other):
            if self.first_name == other.first_name and \
                    self.last_name == other.last_name:
                return True
            else:
                return False

.. code-block:: python
    :caption: Generating hash and object comparision. Since Python 3.7 ``dict`` has fixed order

    class Astronaut:
        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name

        def __hash__(self):
            return hash(self.__dict__)

        def __eq__(self, other):
            if self.__dict__ == other.__dict__:
                return True
            else:
                return False

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
.. warning:: In Python 3.8 the compiler produces a ``SyntaxWarning`` when identity checks (``is`` and ``is not``) are used with certain types of literals (e.g. ``str``, ``int``). These can often work by accident in *CPython*, but are not guaranteed by the language spec. The warning advises users to use equality tests (``==`` and ``!=``) instead.

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
    :caption: Using this code in script.

    a = 'Jan Twardowski'
    b = 'Jan Twardowski'

    print(a)        # Jan Twardowski
    print(b)        # Jan Twardowski

    print(a == b)   # True
    print(a is b)   # True

    print(id(a))    # 4430933296
    print(id(b))    # 4430933296

Using ``is`` in REPL (evaluated line by line)
---------------------------------------------
.. code-block:: python
    :caption: Evaluated in REPL line by line.

    a = 'Jan Twardowski'
    b = 'Jan Twardowski'

    print(a)        # Jan Twardowski
    print(b)        # Jan Twardowski

    print(a == b)   # True
    print(a is b)   # False

    print(id(a))    # 4784790960
    print(id(b))    # 4784791408

Using ``is`` in REPL (evaluated at once)
----------------------------------------
.. code-block:: python
    :caption: Evaluated in REPL at once.

    a = 'Jan Twardowski'
    b = 'Jan Twardowski'

    print(a)        # Jan Twardowski
    print(b)        # Jan Twardowski

    print(a == b)   # True
    print(a is b)   # True

    print(id(a))    # 4784833072
    print(id(b))    # 4784833072
