****
XSLT
****

* Using ``lxml`` module

Example 1
---------
.. code-block:: python

    from io import StringIO
    from lxml.etree import XML, XSLT, parse


    TEMPLATE = """
        <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

            <xsl:template match="/">
                <my_tag><xsl:value-of select="/outer/inner/text()" /></my_tag>
            </xsl:template>

        </xsl:stylesheet>
    """

    DATA = """
        <outer>
            <inner>Hello World</inner>
        </outer>
    """

    xslt_root = XML(TEMPLATE)
    transform = XSLT(xslt_root)
    output = transform(parse(StringIO(DATA)))

    print(output)
    # <?xml version="1.0"?>
    # <my_tag>Hello World</my_tag>

Example 2
---------
.. code-block:: python

    from io import StringIO
    from lxml.etree import XML, XSLT, parse


    DATA = """
        <astronauts>
            <astro>
                <firstname>Jan</firstname>
                <lastname>Jan</lastname>
            </astro>
            <astro>
                <firstname>Mark</firstname>
                <lastname>Watney</lastname>
            </astro>
        </astronauts>
    """

    TEMPLATE = """
        <html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
        <body>
            <table>

                <xsl:for-each select="astronauts/astro">
                    <tr>
                        <td><xsl:value-of select="firstname"/></td>
                        <td><xsl:value-of select="lastname"/></td>
                    </tr>
                </xsl:for-each>

            </table>
        </body>
        </html>
    """

    xslt_root = XML(TEMPLATE)
    transform = XSLT(xslt_root)
    output = transform(parse(StringIO(DATA)))

    print(output)
    # <html><body><table>
    # <tr>
    # <td>Jan</td>
    # <td>Jan</td>
    # </tr>
    # <tr>
    # <td>Mark</td>
    # <td>Watney</td>
    # </tr>
    # </table></body></html>

Example 3
---------
.. code-block:: python

    from io import StringIO
    from lxml.etree import XML, XSLT, parse


    DATA = """
        <CATALOG>
            <PLANT>
                <COMMON>Bloodroot</COMMON>
                <BOTANICAL>Sanguinaria canadensis</BOTANICAL>
                <ZONE>4</ZONE>
                <LIGHT>Mostly Shady</LIGHT>
                <PRICE>$2.44</PRICE>
                <AVAILABILITY>031599</AVAILABILITY>
            </PLANT>
            <PLANT>
                <COMMON>Columbine</COMMON>
                <BOTANICAL>Aquilegia canadensis</BOTANICAL>
                <ZONE>3</ZONE>
                <LIGHT>Mostly Shady</LIGHT>
                <PRICE>$9.37</PRICE>
                <AVAILABILITY>030699</AVAILABILITY>
            </PLANT>
        </CATALOG>
    """

    TEMPLATE = """
        <html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

        <style>
            body {font-family: Arial; font-size: 1em; background-color: #EEEEEE}
            div.title {background-color: teal; color: white; padding: 4px}
            div.description {margin-left:20px;margin-bottom:1em;font-size:10pt}
            span {font-weight: bold}
        </style>

        <body>

        <xsl:for-each select="CATALOG/PLANT">

            <div class="title">
                <span><xsl:value-of select="BOTANICAL"/></span>
                <xsl:value-of select="PRICE"/>
            </div>

            <div class="description">
                    <xsl:value-of select="description"/>
                    <span> (<xsl:value-of select="AVAILABILITY"/> will be available)</span>
            </div>

        </xsl:for-each>
        </body>
        </html>
    """

    xslt_root = XML(TEMPLATE)
    transform = XSLT(xslt_root)
    output = transform(parse(StringIO(DATA)))

    print(output)
    # <html>
    # <style>
    #     body {font-family: Arial; font-size: 1em; background-color: #EEEEEE}
    #     div.title {background-color: teal; color: white; padding: 4px}
    #     div.description {margin-left:20px;margin-bottom:1em;font-size:10pt}
    #     span {font-weight: bold}
    # </style>
    # <body>
    # <div class="title">
    # <span>Sanguinaria canadensis</span>$2.44</div>
    # <div class="description"><span> (031599 will be available)</span></div>
    # <div class="title">
    # <span>Aquilegia canadensis</span>$9.37</div>
    # <div class="description"><span> (030699 will be available)</span></div>
    # </body>
    # </html>


Assignments
===========

XSLT Transformation
-------------------
* Complexity level: medium
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/df_import_xml_xslt.py`

:English:
    #. Download :download:`data/xml_plants.xml`
    #. Read data from file
    #. Using XSLT transformation convert it to pandas readable format
    #. Read data to ``pd.DataFrame``
    #. Make sure that columns and indexes are named properly
    #. Calculate average cost of flower

:Polish:
    #. Pobierz dane z pliku :download:`data/xml_plants.xml`
    #. Zaczytaj dane z pliku
    #. Używając transformaty XSLT sprowadź je do formatu zrozumiałego dla Pandas
    #. Wczytaj dane do ``pd.DataFrame``
    #. Upewnij się, że nazwy kolumn i indeks są dobrze ustawione
    #. Wylicz średni koszt kwiatów dla każdej grupy
