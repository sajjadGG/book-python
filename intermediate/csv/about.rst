CSV About
=========
* CSV - Comma/Character Separated Values
* No CSV formal standard, just a good practice
* Flat file (2D) without relations
* Relations has to be flatten (serialization, additional columns, etc...)
* Typically first line (header) represents column names
* Rarely first line can also have a structure (nrows, ncols)
* Internationalization: encoding
* Localization: decimal separator, thousands separator, date format
* Parameters: delimiter, quotechar, quoting, lineterminator, dialect

Example CSV file:

.. code-block:: text

    SepalLength, SepalWidth, PetalLength, PetalWidth, Species
    5.8, 2.7, 5.1, 1.9, virginica
    5.1, 3.5, 1.4, 0.2, setosa
    5.7, 2.8, 4.1, 1.3, versicolor
    7.3, 2.9, 6.3, 1.8, virginica
    5.6, 2.5, 3.9, 1.1, versicolor
    5.4, 3.9, 1.3, 0.4, setosa


Header
------
File without header:

.. code-block:: text

    5.8, 2.7, 5.1, 1.9, virginica
    5.1, 3.5, 1.4, 0.2, setosa
    5.7, 2.8, 4.1, 1.3, versicolor

First line is a header:

.. code-block:: text

    SepalLength, SepalWidth, PetalLength, PetalWidth, Species
    5.8, 2.7, 5.1, 1.9, virginica
    5.1, 3.5, 1.4, 0.2, setosa
    5.7, 2.8, 4.1, 1.3, versicolor

First line is a structure: number of rows (nrows) and columns (ncols):

.. code-block:: text

    3, 5
    5.8, 2.7, 5.1, 1.9, virginica
    5.1, 3.5, 1.4, 0.2, setosa
    5.7, 2.8, 4.1, 1.3, versicolor


Variants
--------
CSV file with numeric values:

.. code-block:: text

    5.8, 2.7, 5.1, 1.9, 2
    5.1, 3.5, 1.4, 0.2, 0
    5.7, 2.8, 4.1, 1.3, 1

.. code-block:: text

    3, 4, setosa, versicolor, virginica
    5.8, 2.7, 5.1, 1.9, 2
    5.1, 3.5, 1.4, 0.2, 0
    5.7, 2.8, 4.1, 1.3, 1

CSV file with text values. First line is a header:

.. code-block:: text

    Firstname, Lastname, Born
    Melissa, Lewis, 1995-07-15
    Rick, Martinez, 1996-01-21
    Alex, Vogel, 1994-11-15
    Chris, Beck, 1999-08-02
    Beth, Johanssen, 2006-05-09
    Mark, Watney, 1994-10-12


Delimiter
---------
``delimiter=','``:

.. code-block:: text

    SepalLength, SepalWidth, PetalLength, PetalWidth, Species
    5.8, 2.7, 5.1, 1.9, virginica
    5.1, 3.5, 1.4, 0.2, setosa
    5.7, 2.8, 4.1, 1.3, versicolor

``delimiter=';'``:

.. code-block:: text

    SepalLength; SepalWidth; PetalLength; PetalWidth; Species
    5.8; 2.7; 5.1; 1.9; virginica
    5.1; 3.5; 1.4; 0.2; setosa
    5.7; 2.8; 4.1; 1.3; versicolor

``delimiter=':'``:

.. code-block:: text

    root:x:0:0:root:/root:/bin/bash
    bin:x:1:1:bin:/bin:/sbin/nologin
    daemon:x:2:2:daemon:/sbin:/sbin/nologin
    adm:x:3:4:adm:/var/adm:/sbin/nologin
    shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
    halt:x:7:0:halt:/sbin:/sbin/halt
    nobody:x:99:99:Nobody:/:/sbin/nologin
    sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
    watney:x:1000:1000:Mark Watney:/home/watney:/bin/bash
    lewis:x:1001:1001:Melissa Lewis:/home/lewis:/bin/bash
    martinez:x:1002:1002:Rick Martinez:/home/martinez:/bin/bash

``delimiter='|'``:

.. code-block:: text

    | Firstname | Lastname | Role      |
    |-----------|----------|-----------|
    | Mark      | Watney   | Botanist  |
    | Melissa   | Lewis    | Commander |
    | Rick      | Martinez | Pilot     |

``delimiter='\t'``:

.. code-block:: text

    SepalLength	SepalWidth	PetalLength	PetalWidth	Species
    5.8	2.7	5.1	1.9	virginica
    5.1	3.5	1.4	0.2	setosa
    5.7	2.8	4.1	1.3	versicolor


Quotechar
---------
* ``"`` - quote char (best)
* ``'`` - apostrophe

``quotechar='"'``:

.. code-block:: text

    "SepalLength", "SepalWidth", "PetalLength", "PetalWidth", "Species"
    "5.8", "2.7", "5.1", "1.9", "virginica"
    "5.1", "3.5", "1.4", "0.2", "setosa"
    "5.7", "2.8", "4.1", "1.3", "versicolor"

``quotechar="'"``:

.. code-block:: text

    'SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species'
    '5.8', '2.7', '5.1', '1.9', 'virginica'
    '5.1', '3.5', '1.4', '0.2', 'setosa'
    '5.7', '2.8', '4.1', '1.3', 'versicolor'

``quotechar='|'``:

.. code-block:: text

    |SepalLength|, |SepalWidth|, |PetalLength|, |PetalWidth|, |Species|
    |5.8|, |2.7|, |5.1|, |1.9|, |virginica|
    |5.1|, |3.5|, |1.4|, |0.2|, |setosa|
    |5.7|, |2.8|, |4.1|, |1.3|, |versicolor|

``quotechar='/'``:

.. code-block:: text

    /SepalLength/, /SepalWidth/, /PetalLength/, /PetalWidth/, /Species/
    /5.8/, /2.7/, /5.1/, /1.9/, /virginica/
    /5.1/, /3.5/, /1.4/, /0.2/, /setosa/
    /5.7/, /2.8/, /4.1/, /1.3/, /versicolor/


Quoting
-------
* ``csv.QUOTE_ALL`` (safest)
* ``csv.QUOTE_MINIMAL``
* ``csv.QUOTE_NONE``
* ``csv.QUOTE_NONNUMERIC``

``quoting=csv.QUOTE_ALL``:

.. code-block:: text

    "SepalLength", "SepalWidth", "PetalLength", "PetalWidth", "Species"
    "5.8", "2.7", "5.1", "1.9", "virginica"
    "5.1", "3.5", "1.4", "0.2", "setosa"
    "5.7", "2.8", "4.1", "1.3", "versicolor"

``quoting=csv.QUOTE_MINIMAL``:

.. code-block:: text

    SepalLength, SepalWidth, PetalLength, PetalWidth, Species
    5.8, 2.7, 5.1, 1.9, virginica
    5.1, 3.5, 1.4, 0.2, setosa
    5.7, 2.8, 4.1, 1.3, versicolor

``quoting=csv.QUOTE_NONE``:

.. code-block:: text

    SepalLength, SepalWidth, PetalLength, PetalWidth, Species
    5.8, 2.7, 5.1, 1.9, virginica
    5.1, 3.5, 1.4, 0.2, setosa
    5.7, 2.8, 4.1, 1.3, versicolor

``quoting=csv.QUOTE_NONNUMERIC``:

.. code-block:: text

    "SepalLength", "SepalWidth", "PetalLength", "PetalWidth", "Species"
    5.8, 2.7, 5.1, 1.9, "virginica"
    5.1, 3.5, 1.4, 0.2, "setosa"
    5.7, 2.8, 4.1, 1.3, "versicolor"


Lineterminator
--------------
* ``\r\n`` - New line on Windows
* ``\n`` - New line on ``*nix``
* ``*nix`` operating systems: Linux, macOS, BSD and other POSIX compliant OSes (excluding Windows)


Decimal Separator
-----------------
* ``0.1`` - Decimal point
* ``0,1`` - Decimal comma

.. figure:: img/l10n-decimal-separator.png

.. code-block:: text

    SepalLength, SepalWidth, PetalLength, PetalWidth, Species
    5.8; 2.7; 5.1; 1.9; virginica
    5.1; 3.5; 1.4; 0.2; setosa
    5.7; 2.8; 4.1; 1.3; versicolor

.. code-block:: text

    SepalLength, SepalWidth, PetalLength, PetalWidth, Species
    5,8; 2,7; 5,1; 1,9; virginica
    5,1; 3,5; 1,4; 0,2; setosa
    5,7; 2,8; 4,1; 1,3; versicolor


Thousands Separator
-------------------
* ``1000000`` - None
* ``1'000'000`` - Apostrophe
* ``1 000 000`` - Space, the internationally recommended thousands separator
* ``1.000.000`` - Period, used in many non-English speaking countries
* ``1,000,000`` - Comma, used in most English-speaking countries


Date and Time
-------------
>>> date = '1961-04-12'
>>> date = '12.4.1961'
>>> date = '12.04.1961'
>>> date = '12-04-1961'
>>> date = '12/04/1961'
>>> date = '4/12/61'
>>> date = '4.12.1961'
>>> date = 'Apr 12, 1961'
>>> date = 'Apr 12th, 1961'

>>> time = '12:00:00'
>>> time = '12:00'
>>> time = '12:00 pm'

>>> duration = '04:30:00'
>>> duration = '4h 30m'
>>> duration = '4 hours 30 minutes'


Encoding
--------
* ``utf-8`` - international standard (should be always used!)
* ``iso-8859-1`` - ISO standard for Western Europe and USA
* ``iso-8859-2`` - ISO standard for Central Europe (including Poland)
* ``cp1250`` or ``windows-1250`` - Central European encoding on Windows
* ``cp1251`` or ``windows-1251`` - Eastern European encoding on Windows
* ``cp1252`` or ``windows-1252`` - Western European encoding on Windows
* ``ASCII`` - ASCII characters only

.. code-block:: python

    with open(FILE, encoding='utf-8') as file:
        ...


Dialects
--------
.. code-block:: python

    import csv

    csv.list_dialects()
    # ['excel', 'excel-tab', 'unix']

* Microsoft Excel 2016-2020:

    * ``quoting=csv.QUOTE_MINIMAL``
    * ``quotechar='"'``
    * ``delimiter=','`` or ``delimiter=';'`` depending on Windows locale decimal separator
    * ``lineterminator='\r\n'``
    * ``encoding='...'`` - depends on Windows locale typically ``windows-*``

* Microsoft Excel macOS:

    * ``quoting=csv.QUOTE_MINIMAL``
    * ``quotechar='"'``
    * ``delimiter=','``
    * ``lineterminator='\r\n'``
    * ``encoding='utf-8'``

* Microsoft export options:

.. figure:: img/csv-standard-dialects.png

.. code-block:: console

    $ file utf8.csv
    utf8.csv: CSV text

    $ cat utf8.csv
    Firstname,Lastname,Age,Comment
    Mark,Watney,21,zażółć gęślą jaźń
    Melissa,Lewis,21.5,"Some, comment"
    ,,"21,5",Some; Comment

.. code-block:: console

    $ file standard.csv
    standard.csv: CSV text

    $ cat standard.csv
    Firstname,Lastname,Age,Comment
    Mark,Watney,21,za_?__ g__l_ ja__
    Melissa,Lewis,21.5,"Some, comment"
    ,,"21,5",Some; Comment

.. code-block:: console

    $ file dos.csv
    dos.csv: CSV text

    $ cat dos.csv
    Firstname,Lastname,Age,Comment
    Mark,Watney,21,za_?__ g__l_ ja__
    Melissa,Lewis,21.5,"Some, comment"
    ,,"21,5",Some; Comment

.. code-block:: console

    $ file macintosh.csv
    macintosh.csv: Non-ISO extended-ASCII text, with CR line terminators

    $ cat macintosh.csv
    ,,"21,5",Some; Comment


Good Practices
--------------
Always specify:

    * ``delimiter=','`` to  ``csv.DictReader()`` object
    * ``quotechar='"'`` to ``csv.DictReader()`` object
    * ``quoting=csv.QUOTE_ALL`` to ``csv.DictReader()`` object
    * ``lineterminator='\n'`` to ``csv.DictReader()`` object
    * ``encoding='utf-8'`` to ``open()`` function (especially when working with Microsoft Excel)


Assignments
-----------
.. literalinclude:: assignments/csv_format_a.py
    :caption: :download:`Solution <assignments/csv_format_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/csv_format_b.py
    :caption: :download:`Solution <assignments/csv_format_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/csv_format_c.py
    :caption: :download:`Solution <assignments/csv_format_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/csv_format_d.py
    :caption: :download:`Solution <assignments/csv_format_d.py>`
    :end-before: # Solution

.. literalinclude:: assignments/csv_format_e.py
    :caption: :download:`Solution <assignments/csv_format_e.py>`
    :end-before: # Solution

.. literalinclude:: assignments/csv_format_f.py
    :caption: :download:`Solution <assignments/csv_format_f.py>`
    :end-before: # Solution

.. literalinclude:: assignments/csv_format_g.py
    :caption: :download:`Solution <assignments/csv_format_g.py>`
    :end-before: # Solution

.. literalinclude:: assignments/csv_format_h.py
    :caption: :download:`Solution <assignments/csv_format_h.py>`
    :end-before: # Solution

.. literalinclude:: assignments/csv_format_i.py
    :caption: :download:`Solution <assignments/csv_format_i.py>`
    :end-before: # Solution

.. literalinclude:: assignments/csv_format_j.py
    :caption: :download:`Solution <assignments/csv_format_j.py>`
    :end-before: # Solution

.. literalinclude:: assignments/csv_format_k.py
    :caption: :download:`Solution <assignments/csv_format_k.py>`
    :end-before: # Solution

.. literalinclude:: assignments/csv_format_l.py
    :caption: :download:`Solution <assignments/csv_format_l.py>`
    :end-before: # Solution
