*****************
Regexp Substitute
*****************


About
=====
* ``re.sub()``
* Replace matched substring with text


Example
=======
.. code-block:: python
    :caption: Usage of ``re.sub()``

    import re


    PATTERN = r'\s[a-z]{3}\s'
    INPUT = 'Baked Beans And Spam'

    re.sub(PATTERN, ' & ', INPUT, flags=re.IGNORECASE)
    # 'Baked Beans & Spam'

