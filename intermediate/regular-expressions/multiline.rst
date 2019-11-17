**************************
Regexp Multi line searches
**************************

.. code-block:: python
    :caption: Usage of regexp

    import re

    PATTERN = r'[A-Z]{2,10}-[0-9]{1,6}'
    TEXT = """
    MYPROJ-1337 Fixed inspectdb crash;
    MYPROJ-997 Remove commented out code
    """

    re.findall(PATTERN, TEXT)
    # []

    re.findall(PATTERN, TEXT, flags=re.MULTILINE)
    # ['MYPROJ-1337', 'MYPROJ-997']
