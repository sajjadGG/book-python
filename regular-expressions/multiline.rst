*******************
Multi line searches
*******************

.. code-block:: python
    :caption: Usage of regexp

    import re

    PATTERN = r'[A-Z]{2,10}-[0-9]{1,6}'
    TEXT = """
    #27533 Fixed inspectdb crash;
    #31337 Remove commented out code
    """

    re.findall(PATTERN, TEXT)
    # []

    re.findall(PATTERN, TEXT, flags=re.MULTILINE)
    # ['#27533', '#31337']
