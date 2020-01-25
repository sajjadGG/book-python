******************
DataFrame Cleaning
******************


Cleaning User Input
===================
.. highlights::
    * 80% of machine learning and data science is cleaning data

Is This the Same Address?
-------------------------
.. highlights::
    * This is a dump of distinct records of a single address
    * Which one of the below is a true address?

.. code-block:: text

    'ul. Jana III Sobieskiego'
    'ul Jana III Sobieskiego'
    'ul.Jana III Sobieskiego'
    'ulicaJana III Sobieskiego'
    'Ul. Jana III Sobieskiego'
    'UL. Jana III Sobieskiego'
    'ulica Jana III Sobieskiego'
    'Ulica. Jana III Sobieskiego'

    'os. Jana III Sobieskiego'

    'Jana 3 Sobieskiego'
    'Jana 3ego Sobieskiego'
    'Jana III Sobieskiego'
    'Jana Iii Sobieskiego'
    'Jana IIi Sobieskiego'
    'Jana lll Sobieskiego'  # three small letters 'L'

Spelling and Abbreviations
--------------------------
.. code-block:: text

    'ul'
    'ul.'
    'Ul.'
    'UL.'
    'ulica'
    'Ulica'

.. code-block:: text

    'os'
    'os.'
    'Os.'
    'osiedle'

    'oś'
    'oś.'
    'Oś.'
    'ośedle'

.. code-block:: text

    'pl'
    'pl.'
    'Pl.'
    'plac'

.. code-block:: text

    'al'
    'al.'
    'Al.'

    'aleja'
    'aleia'
    'alei'
    'aleii'
    'aleji'

House and Apartment Number
--------------------------
.. code-block:: text

    '1/2'
    '1 / 2'
    '1/ 2'
    '1 /2'
    '3/5/7'

.. code-block:: text

    '1 m. 2'
    '1 m 2'
    '1 apt 2'
    '1 apt. 2'

.. code-block:: text

    '180f/8f'
    '180f/8'
    '180/8f'

.. code-block:: text

    '13d bud. A'

Phone Numbers
-------------
.. code-block:: text

    +48 (12) 355 5678
    +48 123 555 678

.. code-block:: text

    123 555 678

    +48 12 355 5678
    +48 123-555-678
    +48 123 555 6789

    +1 (123) 555-6789
    +1 (123).555.6789

    +1 800-python
    +48123555678

    +48 123 555 678 wew. 1337
    +48 123555678,1
    +48 123555678,1,2,3


Assignments
===========

Translate
---------
* Complexity level: easy
* Lines of code to write: 10-15 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/df_mapping_substitute.py`

:English:
    #. Download :download:`data/astro-dates.csv`
    #. Set header and index to data from file
    #. Convert Polish month names to English
    #. Parse dates to ``datetime`` objects

:Polish:
    #. Pobierz :download:`data/astro-dates.csv`
    #. Ustaw nagłówek i index na dane zaczytane z pliku
    #. Przekonwertuj polskie nazwy miesięcy na angielskie
    #. Sparsuj daty do obiektów ``datetime``

:Hint:
    * ``df['column'].replace(regex=True)``
    * ``df['column'].apply()``
    * ``pd.Timestamp``

Substitute
----------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 30 min
* Filename: :download:`solution/df_mapping_translate.py`

:English:
    #. Download :download:`data/trl.xlsx`
    #. Select ``Polish`` spreadsheet
    #. Set header and index to data from file
    #. Mind the encoding
    #. Substitute Polish Diacritics to English alphabet letters
    #. Compare ``df.replace(regex=True)`` with ``df.applymap()``

:Polish:
    #. Pobierz :download:`data/trl.xlsx`
    #. Wybierz arkusz ``Polish``
    #. Ustaw nagłówek i index na dane zaczytane z pliku
    #. Zwróć uwagę na encoding
    #. Podmień polskie znaki diakrytyczne na litery z alfabetu angielskiego
    #. Porównaj ``df.replace(regex=True)`` z ``df.applymap()``

:Example:
    .. code-block:: text
        :caption: Polish -> English conversion table

        ą: a
        ć: c
        ę: e
        ł: l
        ń: n
        ó: o
        ś: s
        ż: z
        ź: z

:Hint:
        * ``df.set_index()``
        * ``df.applymap()``
        * ``s.map()``

Month number to text
--------------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/df_workflow_month_text.py`

:English:
    #. Download :download:`data/phones.csv`
    #. Add column ``year`` and ``month_name`` by parsing ``month`` column
    #. Month name must be a string month name, not a number (i.e.: 'January', 'May')

:Polish:
    #. Pobierz :download:`data/phones.csv`
    #. Dodaj kolumnę ``year`` i ``month_name`` poprzez sparsowanie kolumny ``month``
    #. Nazwa miesiąca musi być ciągiem znaków, a nie liczbą (i.e. 'January', 'May')

:Example:
    #. if ``month`` column is "2015-01"
    #. ``year``: 2015
    #. ``month_name``: January

:Input:
    .. code-block:: text

        1, January
        2, February
        3, March
        4, April
        5, May
        6, June
        7, July
        8, August
        9, September
        10, October
        11, November
        12, December

:Hint:
    * ``Series.str.split()``
    * ``df[ ['A', 'b'] ]``
