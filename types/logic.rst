.. _Logical Types:

*************
Logical Types
*************


``None``
========
* Empty value (null)
* It is not ``False``, ``0`` or ``''`` (empty string)
* With ``if`` statements behaves like ``False``, ``0`` or ``''`` (empty string)
* Used for unknown (unset) values:

    .. code-block:: python

        my_var = None


``bool``
========
* First letter capitalized, other are lower cased
* Defining ``bool``:

    .. code-block:: python

        my_var = True
        my_var = False

        my_var: bool = True
        my_var: bool = False

* ``bool()`` converts argument to ``bool``:

    .. code-block:: python

        var1 = 'José'
        var2 = None

        bool(var1)              # True
        bool(var2)              # False

* Using ``and`` and ``or``:

    .. code-block:: python

        var1 = 'José'
        var2 = None
        var3 = 'Иван'

        var1 or var2            # True
        var1 or var3            # True

        var1 and var2           # False
        var1 and var3           # True


Assignments
===========
