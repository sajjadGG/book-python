***************
Regexp Examples
***************


National Identification Numbers (Worldwide)
===========================================
* https://github.com/arthurdejong/python-stdnum/tree/master/stdnum/pl


Finding All Adverbs
===================
.. code-block:: python
    :caption: Finding all Adverbs

    import re


    TEXT = 'He was carefully disguised but captured quickly by police.'
    ADVERBS = r'\w+ly'

    re.findall(ADVERBS, TEXT)
    # ['carefully', 'quickly']


Making a Phonebook
==================
.. code-block:: python
    :caption: Practical example of Regexp usage

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
