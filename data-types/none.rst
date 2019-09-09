.. _Logical Types:

********
``None``
********


Defining ``None``
=================
* First letter capitalized, other are lower cased
* Empty (null) or unknown (unset) value
* It is not ``False`` value
* With ``if`` statements behaves like negative values

.. code-block:: python

    my_var = None


Logic operators
===============
* Do not use ``==`` or ``!=`` to check ``None`` values

.. csv-table:: Logic operators
    :header: "Operand", "Description"
    :widths: 15, 85

    "``x is None``", "``x`` is the same object as ``y``"
    "``x is not None``", "``x`` is not the same object as ``y``"


Assignments
===========

Is ``None`` or ``not``
----------------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/none.py`

:English:
    #. What you need to put in expressions to get the expected outcome?

:Polish:
    #. Co należy podstawić w wyrażeniach aby otrzymać wartość oczekiwaną?

:Input:
    .. code-block:: python

            a = ... is None                                                                       # True
            b = ... is not None                                                                   # False
            c = bool(bool(...) is not bool(...)) == False                                         # True
            d = (bool(bool(...) is not bool(...)) == False and bool(...))                         # False
            e = (bool(bool(...) is not bool(...)) == False and bool(...)) and (... is not None)   # False

:Output:
    .. code-block:: python

            print(a)    # True
            print(b)    # False
            print(c)    # True
            print(d)    # False
            print(e)    # False

:The whys and wherefores:
    * Defining variables
    * Type casting
    * Logic types


.. todo:: Create more assignments
