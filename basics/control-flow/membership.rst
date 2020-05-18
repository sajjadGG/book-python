**********
Membership
**********


Str
===
.. code-block:: python
    :caption: Contains

    'x' in 'Python'                 # False
    'P' in 'Python'                 # True
    'p' in 'Python'                 # False

    ('x') in 'Python'               # False
    ('P') in 'Python'               # True
    ('p') in 'Python'               # False

    ('x',) in 'Python'              # TypeError: 'in <string>' requires string as left operand, not tuple
    ('P',) in 'Python'              # TypeError: 'in <string>' requires string as left operand, not tuple
    ('p',) in 'Python'              # TypeError: 'in <string>' requires string as left operand, not tuple

    'Python' in 'Python'            # True
    'Py' in 'Python'                # True

.. code-block:: python
    :caption: Missing

    'P' not in 'Python'             # False
    'p' not in 'Python'             # True
    'py' not in 'Python'            # True
    'Py' not in 'Python'            # False


Tuple
=====
.. code-block:: python
    :caption: Contains

    1 in (1, 2)               # True
    2 in (1, 2)               # True
    3 in (1, 2)               # False

    (1) in (1, 2)             # True
    (2) in (1, 2)             # True
    (3) in (1, 2)             # False

    (1,) in (1, 2)            # False
    (2,) in (1, 2)            # False
    (3,) in (1, 2)            # False

    (1, 2) in (1, 2)          # False
    (3, 4) in (1, 2, (3, 4))  # True

.. code-block:: python
    :caption: Missing

    1 not in (1, 2)           # False
    3 not in (1, 2)           # True

    (2) not in (1, 2)        # False
    (1, 2) not in (1, 2)     # True


List
====
* ``in`` - Contains
* ``not in`` - Missing

.. code-block:: python
    :caption: Contains

    1 in [1, 2]               # True
    2 in [1, 2]               # True
    3 in [1, 2]               # False

    [1] in [1, 2]             # False
    [2] in [1, 2]             # False
    [3] in [1, 2]             # False

    [1,] in [1, 2]            # False
    [2,] in [1, 2]            # False
    [3,] in [1, 2]            # False

    [1, 2] in [1, 2]          # False
    [3, 4] in [1, 2, [3, 4]]  # True

.. code-block:: python
    :caption: Missing

    1 not in [1, 2]           # False
    3 not in [1, 2]           # True

    [2] not in [1, 2]         # True
    [1, 2] not in [1, 2]      # True


Set
===
.. code-block:: python
    :caption: Contains

    1 in {1, 2}               # True
    2 in {1, 2}               # True
    3 in {1, 2}               # False

    {1} in {1, 2}             # False
    {2} in {1, 2}             # False
    {3} in {1, 2}             # False

    {1,} in {1, 2}            # False
    {2,} in {1, 2}            # False
    {3,} in {1, 2}            # False

    {1, 2} in {1, 2}          # False
    {3, 4} in {1,2, {3, 4}}   # True

.. code-block:: python
    :caption: Missing

    1 not in {1, 2}           # False
    3 not in {1, 2}           # True

    {2} not in {1, 2}         # True
    {1, 2} not in {1, 2}      # True
