**********
Membership
**********


Contains
========
* ``in`` - Contains

.. code-block:: python
    :caption: ``str``

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
    :caption: ``list``

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
    :caption: ``tuple``

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
    :caption: ``set``

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


Missing
=======
* ``not in`` - Missing

.. code-block:: python
    :caption: ``str``

    'P' not in 'Python'             # False
    'p' not in 'Python'             # True
    'py' not in 'Python'            # True
    'Py' not in 'Python'            # False

.. code-block:: python
    :caption: ``list``

    1 not in [1, 2]           # False
    3 not in [1, 2]           # True

    [2] not in [1, 2]         # True
    [1, 2] not in [1, 2]      # True

.. code-block:: python
    :caption: ``tuple``

    1 not in (1, 2)           # False
    3 not in (1, 2)           # True

    (2) not in (1, 2)        # False
    (1, 2) not in (1, 2)     # True

.. code-block:: python
    :caption: ``set``

    1 not in {1, 2}           # False
    3 not in {1, 2}           # True

    {2} not in {1, 2}         # True
    {1, 2} not in {1, 2}      # True
