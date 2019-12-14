************
Regexp Split
************


About
=====
* ``re.split()``
* Split text by pattern


Example
=======
.. code-block:: python
    :caption: Usage of ``re.split()``

    import re

    PATTERN = r'\s[a-z]{3}\s'
    INPUT = 'Baked Beans And Spam'

    re.split(PATTERN, INPUT, flags=re.IGNORECASE)
    # ['Baked Beans', 'Spam']

.. code-block:: python
    :caption: Making a Phonebook

    import re


    TEXT = """Jan Twardowski: 834.345.1254 Polish Space Agency

    Mark Watney: 892.345.3428 Johnson Space Center
    Matt Kowalski: 925.541.7625 Kennedy Space Center


    Melissa Lewis: 548.326.4584 Bajkonur, Kazakhstan"""

    entries = re.split('\n+', TEXT)
    print(entries)
    # [
    #   'Jan Twardowski: 834.345.1254 Polish Space Agency',
    #   'Mark Watney: 892.345.3428 Johnson Space Center',
    #   'Matt Kowalski: 925.541.7625 Kennedy Space Center',
    #   'Melissa Lewis: 548.326.4584 Bajkonur, Kazakhstan'
    # ]

    output = [re.split(':?\s', entry, maxsplit=3) for entry in entries]
    print(output)
    # [
    #   ['Jan', 'Twardowski', '834.345.1254', 'Polish Space Agency'],
    #   ['Mark', 'Watney', '892.345.3428', 'Johnson Space Center'],
    #   ['Matt', 'Kowalski', '925.541.7625', 'Kennedy Space Center'],
    #   ['Melissa', 'Lewis', '548.326.4584', 'Bajkonur, Kazakhstan']
    # ]

Assignments
===========

Moon Speech (split)
-------------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/split_moon_speech.py`
* References: "Moon Speech" by John F. Kennedy at Rice Stadium, Houston, TX on 1962-09-12 :cite:`RegexpKennedy1962`

:English:
    #. Download "Moon Speech" text :download:`data/moon_speech.html`
    #. Save as ``moon_speech.html``
    #. Using ``re.split()`` split text by paragraphs
    #. Print paragraph starting with "We choose to go to the moon"

:Polish:
    #. Pobierz tekst przemówienia "Moon Speech" :download:`data/moon_speech.html`
    #. Zapisz jako ``moon_speech.html``
    #. Za pomocą ``re.split()`` podziel tekst na paragrafy
    #. Wyświetl paragraf zaczynający się od słów "We choose to go to the moon"
