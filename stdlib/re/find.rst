RE Findall, Finditer
====================


Rationale
---------
* ``re.findall()``
* ``re.finditer()``


Example
-------
Usage of ``re.findall()`` and ``re.finditer()``:

.. code-block:: python

    import re


    PATTERN = r'[A-Z]{2,10}-[0-9]{1,6}'
    DATA = 'MYPROJ-1337, MYPROJ-997 removed obsolete comments'

    re.findall(PATTERN, DATA)
    # ['MYPROJ-1337', 'MYPROJ-997']


Use Case
--------
Finding All Adverbs:

.. code-block:: python

    import re


    TEXT = 'He was carefully disguised but captured quickly by police.'
    ADVERBS = r'\w+ly'

    re.findall(ADVERBS, TEXT)
    # ['carefully', 'quickly']


Assignments
-----------
.. literalinclude:: assignments/re_find_a.py
    :caption: :download:`Solution <assignments/re_find_a.py>`
    :end-before: # Solution
