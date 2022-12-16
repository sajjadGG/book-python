XPATH
=====
* Using ``lxml`` module


Example
-------
.. code-block:: python

    print(html.xpath("string()")) # lxml.etree only!
    # IrisSetosa

    print(html.xpath("//text()")) # lxml.etree only!
    # ['Iris', 'Setosa']


Use Case - 0x01
---------------
>>> class XPath:
...     def __init__(self, current):
...         self.current = current
...
...     def __div__(self, other):
...         return self.current.xpath(other)
>>>
>>>
>>> XPath(root) / 'Header' / 'Depth' / 'Max'  # doctest: +SKIP

