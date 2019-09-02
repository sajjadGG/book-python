****************************
Greedy and non-greedy search
****************************

* greedy qualifiers: ``*``, ``+``, ``?``
* they match as much text as possible
* Adding ``?`` after the qualifier makes it non-greedy

.. code-block:: python
    :caption: Usage of greedy and non-greedy search in ``re.findall()``

    import re

    TEXT = '<strong>Ehlo World</strong>'

    re.findall(r'<.*>', TEXT)         # ['<strong>Ehlo World</strong>']
    re.findall(r'<.*?>', TEXT)        # ['<strong>', '</strong>']

.. code-block:: python
    :caption: Usage of greedy and non-greedy search with groups

    re.findall(r'<(.*)>', TEXT)       # ['strong>Ehlo World</strong']
    re.findall(r'<(.*?)>', TEXT)      # ['strong', '/strong']
    re.findall(r'</?(.*?)>', TEXT)    # ['strong', 'strong']
