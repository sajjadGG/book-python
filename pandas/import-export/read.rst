***********
Pandas Read
***********


Import data
===========
* File paths works also with URLs
* SQL functions uses SQLAlchemy, which supports many RDBMS

.. code-block:: python

    import pandas as pd


    # Important
    pd.read_csv()
    pd.read_excel()
    pd.read_html()
    pd.read_json()
    pd.read_sql()        # Read SQL query or database table into a DataFrame

    # Others
    pd.read_clipboard()
    pd.read_feather()
    pd.read_fwf()
    pd.read_gbq()
    pd.read_hdf()
    pd.read_msgpack()
    pd.read_parquet()
    pd.read_pickle()
    pd.read_sas()
    pd.read_spss()
    pd.read_sql_query()  # Read SQL query into a DataFrame
    pd.read_sql_table()  # Read SQL database table into a DataFrame
    pd.read_stata()
    pd.read_table()


Examples
========
.. code-block:: python

    import pandas as pd


    DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/iris-clean.csv'
    header = pd.read_csv(DATA, nrows=0).columns

.. code-block:: python

    import pandas as pd


    DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/iris-clean.csv'
    df = pd.read_csv(DATA)

    df.head(3)
    #    sepal_length  sepal_width  petal_length  petal_width     species
    # 0           5.4          3.9           1.3          0.4      setosa
    # 1           5.9          3.0           5.1          1.8   virginica
    # 2           6.0          3.4           4.5          1.6  versicolor

.. code-block:: python

    import pandas as pd


    DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/iris-dirty.csv'
    COLUMNS =  ['sepal_length', 'sepal_width',
                'petal_length', 'petal_width', 'species']

    df = pd.read_csv(DATA)
    df.head(3)
    #      150    4  setosa  versicolor  virginica
    # 0    5.4  3.9     1.3         0.4          0
    # 1    5.9  3.0     5.1         1.8          2
    # 2    6.0  3.4     4.5         1.6          1

    df = pd.read_csv(url, skiprows=1, names=COLUMNS)
    df.head(3)
    #    sepal_length  sepal_width  petal_length  petal_width  species
    # 0           5.4          3.9           1.3          0.4        0
    # 1           5.9          3.0           5.1          1.8        2
    # 2           6.0          3.4           4.5          1.6        1

    df['species'].replace({
        0: 'setosa',
        1: 'versicolor',
        2: 'virginica',
    }, inplace=True)
    #    sepal_length  sepal_width  petal_length  petal_width  species
    # 0           5.4          3.9           1.3          0.4        setosa
    # 1           5.9          3.0           5.1          1.8        virginica
    # 2           6.0          3.4           4.5          1.6        versicolor


Compressed
==========
* If the extension is ``.gz``, ``.bz2``, ``.zip``, and ``.xz``, the corresponding compression method is automatically selected

.. code-block:: python

    df = pd.read_json('sample_file.gz', compression='infer')


Read HTML
=========
.. code-block:: python

    DATA = 'https://python.astrotech.io/numerical-analysis/pandas/df-create.html'

    pd.read_html(DATA)
    # Traceback (most recent call last):
    # urllib.error.HTTPError: HTTP Error 403: Forbidden

.. code-block:: python

    import requests

    DATA = 'https://python.astrotech.io/numerical-analysis/pandas/df-create.html'
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'

    resp = requests.get(DATA, headers={'User-Agent': USER_AGENT})
    dfs = pd.read_html(resp.content)

    dfs[0]
    #      Crew Role        Astronaut
    # 0   Prime  CDR   Neil Armstrong
    # 1   Prime  LMP      Buzz Aldrin
    # 2   Prime  CMP  Michael Collins
    # 3  Backup  CDR     James Lovell
    # 4  Backup  LMP   William Anders
    # 5  Backup  CMP       Fred Haise


StringIO
========
* Converts ``str`` to File-like object

.. code-block:: python

    from io import StringIO


    DATA = """
    "Crew", "Role", "Astronaut"
    "Prime", "CDR", "Neil Armstrong"
    "Prime", "LMP", "Buzz Aldrin"
    "Prime", "CMP", "Michael Collins"
    "Backup", "CDR", "James Lovell"
    "Backup", "LMP", "William Anders"
    "Backup", "CMP", "Fred Haise"
    """

    data = StringIO(DATA)
    df = pd.read_csv(data)

    df
    #      Crew  "Role"         "Astronaut"
    # 0   Prime   "CDR"    "Neil Armstrong"
    # 1   Prime   "LMP"       "Buzz Aldrin"
    # 2   Prime   "CMP"   "Michael Collins"
    # 3  Backup   "CDR"      "James Lovell"
    # 4  Backup   "LMP"    "William Anders"
    # 5  Backup   "CMP"        "Fred Haise"

.. code-block:: python

    from io import StringIO


    DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/astro-order.csv'

    resp = requests.get(DATA)
    data = StringIO(resp.text)
    df = pd.read_csv(data)

    df
    #      Order           Astronaut         Date       Mission
    # 0      1.0        Yuri Gagarin   1961-04-12        Vostok
    # 1      2.0       Gherman Titov   1961-08-06      Vostok 2
    # 2      3.0   Andrian Nikolayev   1962-08-11      Vostok 3
    # 3      4.0      Pavel Popovich   1962-08-12      Vostok 4
    # 4      5.0     Valeri Bykovsky   1963-06-14      Vostok 5
    # ..     ...                 ...          ...           ...
    # 530  531.0      Thomas Pesquet   2016-11-17   Soyuz MS-03
    # 531  532.0        Jack Fischer   2017-04-20   Soyuz MS-04
    # 532  533.0      Mark Vande Hei   2017-09-12   Soyuz MS-06
    # 533  534.0     Norishige Kanai   2017-12-17   Soyuz MS-07
    # 534    NaN        Scott Tingle   2017-12-17   Soyuz MS-07
    # [535 rows x 4 columns]


Read SQL
========
.. code-block:: python

    import sqlite3
    import requests

    DATA = r'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/sqlite3/astro-timeline.sqlite3'
    DATABASE = r'/tmp/astro-timeline.sqlite3'
    SQL = """
        SELECT *
        FROM logs
    """

    with open(DATABASE, mode='wb') as db:
        resp = requests.get(DATA)
        db.write(resp.content)

    with sqlite3.connect(DATABASE) as db:
        astro_timeline = pd.read_sql(SQL, db, parse_dates=['datetime'])

    astro_timeline
    #     id  ...                                            message
    # 0    1  ...                         Terminal countdown started
    # 1    2  ...                          S-IC engine ignition (#5)
    # 2    3  ...          Maximum dynamic pressure (735.17 lb/ft^2)
    # 3    4  ...                                      S-II ignition
    # 4    5  ...                     Launch escape tower jettisoned
    # 5    6  ...                          S-II center engine cutoff
    # 6    7  ...                               Translunar injection
    # 7    8  ...                           CSM docked with LM/S-IVB
    # 8    9  ...                     Lunar orbit insertion ignition
    # 9   10  ...               Lunar orbit circularization ignition
    # 10  11  ...                                    CSM/LM undocked
    # 11  12  ...                 LM powered descent engine ignition
    # 12  13  ...                                      LM 1202 alarm
    # 13  14  ...                                      LM 1201 alarm
    # 14  15  ...                                   LM lunar landing
    # 15  16  ...                           EVA started (hatch open)
    # 16  17  ...                 1st step taken lunar surface (CDR)
    # 17  18  ...  That's one small step for [a] man... one giant...
    # 18  19  ...        Contingency sample collection started (CDR)
    # 19  20  ...                               LMP on lunar surface
    # 20  21  ...                           EVA ended (hatch closed)
    # 21  22  ...                 LM lunar liftoff ignition (LM APS)
    # 22  23  ...                                      CSM/LM docked
    # 23  24  ...                Transearth injection ignition (SPS)
    # 24  25  ...                                   CM/SM separation
    # 25  26  ...                                              Entry
    # 26  27  ...                     Splashdown (went to apex-down)
    # 27  28  ...                                        Crew egress
    # [28 rows x 4 columns]


XML and XSLT
============
.. code-block:: python

    from io import StringIO
    from lxml.etree import XML, XSLT, parse
    import pandas as pd

    DATA = """<?xml version="1.0"?>
    <catalog>
       <book id="bk101">
          <author>Gambardella, Matthew</author>
          <title>XML Developer's Guide</title>
          <genre>Computer</genre>
          <price>44.95</price>
          <publish_date>2000-10-01</publish_date>
          <description>An in-depth look at creating applications
          with XML.</description>
       </book>
       <book id="bk102">
          <author>Ralls, Kim</author>
          <title>Midnight Rain</title>
          <genre>Fantasy</genre>
          <price>5.95</price>
          <publish_date>2000-12-16</publish_date>
          <description>A former architect battles corporate zombies,
          an evil sorceress, and her own childhood to become queen
          of the world.</description>
       </book>
       <book id="bk103">
          <author>Corets, Eva</author>
          <title>Maeve Ascendant</title>
          <genre>Fantasy</genre>
          <price>5.95</price>
          <publish_date>2000-11-17</publish_date>
          <description>After the collapse of a nanotechnology
          society in England, the young survivors lay the
          foundation for a new society.</description>
       </book>
    </catalog>
    """

    TEMPLATE = """
        <html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
            <table>
                <thead>
                    <tr>
                        <th>Id</th>
                        <th>Author</th>
                        <th>Title</th>
                        <th>Genre</th>
                        <th>Price</th>
                        <th>Publish Date</th>
                        <th>Description</th>
                    </tr>
                </thead>
                <tbody>

                    <xsl:for-each select="catalog/book">
                        <tr>
                            <td><xsl:value-of select="@id"/></td>
                            <td><xsl:value-of select="author"/></td>
                            <td><xsl:value-of select="title"/></td>
                            <td><xsl:value-of select="genre"/></td>
                            <td><xsl:value-of select="price"/></td>
                            <td><xsl:value-of select="publish_date"/></td>
                            <td><xsl:value-of select="description"/></td>
                        </tr>
                    </xsl:for-each>

                </tbody>
            </table>
        </html>
    """

    transform = XSLT(XML(TEMPLATE))
    data = parse(StringIO(DATA))
    html = str(transform(data))
    dfs = pd.read_html(html)
    result = dfs[0]

    result
    # [      Id  ...                                        Description
    # 0  bk101  ...  An in-depth look at creating applications  wit...
    # 1  bk102  ...  A former architect battles corporate zombies, ...
    # 2  bk103  ...  After the collapse of a nanotechnology  societ...
    # [3 rows x 7 columns]]

    type(result) is pd.DataFrame
    # True

    len(result) > 0
    # True

    result.columns
    # Index(['Id', 'Author', 'Title', 'Genre', 'Price', 'Publish Date',
    #        'Description'],
    #       dtype='object')

    result['Title']
    # 0    XML Developer's Guide
    # 1            Midnight Rain
    # 2          Maeve Ascendant
    # Name: Title, dtype: object


Assignments
===========

.. literalinclude:: assignments/pandas_read_csv_dates.py
    :caption: :download:`Solution <assignments/pandas_read_csv_dates.py>`
    :end-before: # Solution

.. literalinclude:: assignments/pandas_read_csv_replace.py
    :caption: :download:`Solution <assignments/pandas_read_csv_replace.py>`
    :end-before: # Solution

.. literalinclude:: assignments/pandas_read_json_iris.py
    :caption: :download:`Solution <assignments/pandas_read_json_iris.py>`
    :end-before: # Solution

.. literalinclude:: assignments/pandas_read_json_openapi.py
    :caption: :download:`Solution <assignments/pandas_read_json_openapi.py>`
    :end-before: # Solution

.. literalinclude:: assignments/pandas_read_html.py
    :caption: :download:`Solution <assignments/pandas_read_html.py>`
    :end-before: # Solution

.. literalinclude:: assignments/pandas_read_xslt_plants.py
    :caption: :download:`Solution <assignments/pandas_read_xslt_plants.py>`
    :end-before: # Solution
