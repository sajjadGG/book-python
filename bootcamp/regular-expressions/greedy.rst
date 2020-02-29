*****************
Regexp Non-Greedy
*****************


About
=====
* Adding ``?`` after the qualifier makes it non-greedy
* Non-greedy - as few as possible
* Greedy - as many as possible

.. csv-table:: Regular Expression Greedy and Non-Greedy Qualifiers
    :widths: 15, 85
    :header: "Syntax", "Description"

    "``?``", "zero or one (greedy)"
    "``*``", "zero or more (greedy)"
    "``+``", "one or more (greedy)"
    "``??``", "zero or one (non greedy)"
    "``*?``", "zero or more (non greedy)"
    "``+?``", "one or more (non greedy)"


Examples
========
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


Assignments
===========

Moon Speech (non-greedy)
------------------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/greedy_moon_speech.py`
* References: "Moon Speech" by John F. Kennedy at Rice Stadium, Houston, TX on 1962-09-12 :cite:`RegexpKennedy1962`

:English:
    #. Download "Moon Speech" text :download:`data/moon_speech.html`
    #. Save as ``moon_speech.html``
    #. Using ``re.findall()`` and non-greedy qualifier split text by paragraphs
    #. Print paragraph starting with "We choose to go to the moon"

:Polish:
    #. Pobierz tekst przemówienia "Moon Speech" :download:`data/moon_speech.html`
    #. Zapisz jako ``moon_speech.html``
    #. Za pomocą ``re.findall()`` i non-greedy qualifier podziel tekst na paragrafy
    #. Wyświetl paragraf zaczynający się od słów "We choose to go to the moon"
