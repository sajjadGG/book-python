********************
Groups and Variables
********************


RegEx parameters (variables)
============================
.. code-block:: python
    :caption: Usage of group in ``re.match()``

    import re

    PATTERN = r'(?P<first_name>\w+) (?P<last_name>\w+)'
    TEXT = 'Jan Twardowski'

    matches = re.match(PATTERN, TEXT)

    matches.group('first_name')     # 'Jan'
    matches.group('last_name')      # 'Twardowski'
    matches.group(1)                # 'Jan'
    matches.group(2)                # 'Twardowski'
    matches.groups()                # ('Jan', 'Twardowski')
    matches.groupdict()             # {'first_name': 'Jan', 'last_name': 'Twardowski'}
