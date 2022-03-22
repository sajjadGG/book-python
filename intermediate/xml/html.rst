XML Parsing HTML
================
* Using ``lxml`` module

.. code-block:: html

    <html><body>Iris<br/>Setosa</body></html>

.. code-block:: python

    from lxml.etree import tostring, Element, SubElement


    html = Element("html")
    body = SubElement(html, "body")

    body.text = "Iris"
    tostring(html)
    # b'<html><body>Iris</body></html>'

    br = SubElement(body, "br")
    tostring(html)
    # b'<html><body>Iris<br/></body></html>'

    br.tail = 'Setosa'
    tostring(html)
    # b'<html><body>Iris<br/>Setosa</body></html>'
