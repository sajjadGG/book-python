********************
Substitute and Split
********************


``re.sub()``
============
.. code-block:: python
    :caption: Usage of ``re.sub()``

    import re


    PATTERN = r'\s[a-z]{3}\s'
    INPUT = 'Baked Beans And Spam'

    re.sub(PATTERN, ' & ', INPUT, flags=re.IGNORECASE)
    # 'Baked Beans & Spam'


``re.split()``
==============
.. code-block:: python
    :caption: Usage of ``re.split()``

    import re

    PATTERN = r'\s[a-z]{3}\s'
    INPUT = 'Baked Beans And Spam'

    re.split(PATTERN, INPUT, flags=re.IGNORECASE)
    # ['Baked Beans', 'Spam']
