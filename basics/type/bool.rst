*************
Type ``bool``
*************


Type Definition
===============
.. highlights::
    * ``True`` - Positive value
    * ``False`` - Negative value
    * First letter capitalized, other are lower cased

.. code-block:: python
    :caption: ``bool`` Type Definition

    my_var = True               # True
    my_var = False              # False


Type Casting
============
.. code-block:: python
    :caption: ``bool()`` converts argument to ``bool``

    bool(1)                     # True
    bool(1.0)                   # True
    bool('Jan Twardowski')      # True

.. code-block:: python
    :caption: Negative values

    bool(bool())                # False
    bool(False)                 # False
    bool(None)                  # False
    bool(int())                 # False
    bool(0)                     # False
    bool(float())               # False
    bool(0.0)                   # False
    bool(complex())             # False
    bool(0+0j)                  # False
    bool(0.0+0.0j)              # False
    bool(str())                 # False
    bool('')                    # False
    bool(tuple())               # False
    bool(())                    # False
    bool(list())                # False
    bool([])                    # False
    bool(dict())                # False
    bool({})                    # False
    bool(set())                 # False


Boolean Algebra
===============

Conjunction
-----------
.. code-block:: python

    True and True               # True
    True and False              # False
    False and True              # False
    False and False             # False

.. code-block:: python

    1 and 1                     # True
    1 and 0                     # False
    0 and 1                     # False
    0 and 0                     # False

.. code-block:: python

    'Jan' and 'Jan'             # True
    'Jan' and ''                # False
    '' and 'Jan'                # False
    '' and ''                   # False

.. code-block:: python

    'Jan' and 1                 # True
    'Jan' and 0                 # False
    0.0 and 'Jan'               # False
    1 and False                 # False

Disjunction
-----------
.. code-block:: python

    True or True                # True
    True or False               # True
    False or True               # True
    False or False              # False

.. code-block:: python

    1 or 1                      # True
    1 or 0                      # True
    0 or 1                      # True
    0 or 0                      # False

.. code-block:: python

    'José' or 'Иван'            # True
    'José' or ''                # True
    '' or 'José'                # True
    '' or ''                    # False

.. code-block:: python

    1 or 'Иван'                 # True
    True or ''                  # True
    0 or True                   # True
    0.0 or False                # False

Complex Statements
------------------
.. code-block:: python

    True and True or False      # True
    True and False or False     # False
    False and False or True     # True


Assignments
===========

To ``bool`` or not to ``bool``
------------------------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/type_bool_simple.py`

:English:
    #. Which variables are ``True``?
    #. Which variables are ``False``?

:Polish:
    #. Które zmienne są ``True``?
    #. Które zmienne są ``False``?

:Input:
    .. code-block:: python

        a = bool(False)
        b = bool(True)

        c = bool('a')
        d = bool('.')
        e = bool('0')
        f = bool('0.0')
        g = bool('')
        h = bool(' ')

        i = bool(0)
        j = bool(0.0)
        k = bool(-0)
        l = bool(-0.0)

        m = bool(int('0'))
        n = bool(float('-0'))

        o = bool(-0.0+0.0j)
        p = bool('-0.0+0.0j')

:The whys and wherefores:
    * Defining variables
    * Type casting
    * Logic types

``True`` of ``False``
---------------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/type_bool_true_or_false.py`

:English:
    #. What you need to put in expressions to get the expected outcome?
    #. Insert only ``True`` or ``False``

:Polish:
    #. Co należy podstawić w wyrażeniach aby otrzymać wartość oczekiwaną?
    #. Wstawiaj tylko ``True`` lub ``False``

:Input:
    .. code-block:: python

        a = bool(...) == True                   # True
        b = bool(...) == False                  # True
        c = ... == True                         # True
        d = ... != False                        # True
        e = ... or ...                          # True
        f = ... and ...                         # False
        g = bool(bool(...) == False) or False   # True
        h = bool(...) is not bool(...)          # False

:Output:
    .. code-block:: python

        print(bool(a))                          # True
        print(bool(b))                          # True
        print(bool(c))                          # True
        print(bool(d))                          # True
        print(bool(e))                          # True
        print(bool(f))                          # False
        print(bool(g))                          # True
        print(bool(h))                          # False

:The whys and wherefores:
    * Defining variables
    * Type casting
    * Logic types
