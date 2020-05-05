************************
Regexp Findall, Finditer
************************


About
=====
* ``re.findall()``
* ``re.finditer()``


Examples
========
.. code-block:: python
    :caption: Usage of ``re.findall()`` and ``re.finditer()``

    import re


    PATTERN = r'[A-Z]{2,10}-[0-9]{1,6}'
    DATA = 'MYPROJ-1337, MYPROJ-997 removed obsolete comments'

    re.findall(PATTERN, DATA)
    # ['MYPROJ-1337', 'MYPROJ-997']

.. code-block:: python
    :caption: Finding All Adverbs

    import re


    TEXT = 'He was carefully disguised but captured quickly by police.'
    ADVERBS = r'\w+ly'

    re.findall(ADVERBS, TEXT)
    # ['carefully', 'quickly']


Assignments
===========

Finding Dates
-------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/find_dates.py`
* References: :cite:`RegexpWikipediaApollo11`

:English:
    #. Download :download:`data/apollo11-content.txt` and save as ``regex_dates.txt``
    #. Using regular expressions find dates in US format (example: "April 12, 1961")
    #. Print all dates

:Polish:
    #. Pobierz :download:`data/apollo11-content.txt` i zapisz jako ``regex_dates.txt``
    #. Używając wyrażeń regularnych wyszukaj dat w formacie US (przykład: "April 12, 1961")
    #. Wyświetl wszystkie daty

:Output:
    .. code-block:: python

        print(output)
        # ['October 4, 1957',
        #  'April 12, 1961',
        #  'May 5, 1961',
        #  'May 25, 1961',
        #  'September 12, 1962',
        #  'September 12, 1962']
