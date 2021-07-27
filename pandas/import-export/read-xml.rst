Pandas Read XML
===============


Rationale
---------
* File paths works also with URLs
* `io.StringIO` Converts ``str`` to File-like object


XML and XSLT
------------
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
-----------
.. literalinclude:: assignments/pandas_read_xslt_plants.py
    :caption: :download:`Solution <assignments/pandas_read_xslt_plants.py>`
    :end-before: # Solution
