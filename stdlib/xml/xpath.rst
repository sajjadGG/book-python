XPATH
=====

Rationale
---------
* Using ``lxml`` module

.. code-block:: python

    print(html.xpath("string()")) # lxml.etree only!
    # IrisSetosa

    print(html.xpath("//text()")) # lxml.etree only!
    # ['Iris', 'Setosa']
