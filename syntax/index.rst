.. _Syntax:

******
Syntax
******


Indentation instead of braces
=============================
* Python uses indentation instead of braces
* 4 spaces indentation
* Code indented on the same level belongs to block:

    .. code-block:: python

        if True:
            print('This is true')
        else:
            print('This is false')


End of lines
============
* No ``;`` at the end of lines
* ``\r\n`` and ``\n`` is ok

.. code-block:: python

    print('Hello!\nHow are you?')
    print('Hello!\r\nHow are you?')

Comments
========

Line comments
---------------
* ``# `` - hash and space, then comment
* Indent must be on the same level as block indent

.. code-block:: python

    # Jose Jimenez says hello
    print('My name Jose Jimenez')

Inline comments
---------------
* ``  # `` - some code, two spaces, hash, space, then comment

.. code-block:: python

    print('My name Jose Jimenez')  # Jose Jimenez says hello

Multiline comments
------------------
* Both single and double are good
* Single quotes ``'''``
* Double quotes ``"""``
* Double quotes are more common:

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
* First multiline comment in:

    * File / Module
    * Class
    * Method / Function

* Used for ``help()`` documentation

    .. code-block:: python

        def apollo_dsky(noun, verb):
            """
            This is the Apollo Display Keyboard
            It takes noun and verb
            """
            print(f'Program selected. Noun: {noun}, verb: {verb}')

* Used for ``doctest``

    .. code-block:: python

        def add(a, b):
            """
            Sums two numbers.

            >>> add(1, 2)
            3
            """
            return a + b


Commented out code
------------------
* Never!
* Use Version Control System instead (``git blame``)
* IDE has Local history (modifications) and you can compare file
