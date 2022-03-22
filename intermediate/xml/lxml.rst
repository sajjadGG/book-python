XML Module lxml
===============
* ``pip install lxml``


Creating elements
-----------------
Creating elements:

.. code-block:: python

    from lxml.etree import tostring, Element


    root = Element("iris")

    print(tostring(root))
    # b'<iris/>'

Adding elements using list interface:

.. code-block:: python

    from lxml.etree import tostring, Element


    root = Element('iris')
    root.append(Element('setosa'))
    root.append(Element('versicolor'))
    root.append(Element('virginica'))

    print(tostring(root))
    # b'<iris><setosa/><versicolor/><virginica/></iris>'

Length of a subtree
-------------------
Length of a subtree:

.. code-block:: python

    from lxml.etree import Element


    root = Element('iris')
    root.append(Element('setosa'))
    root.append(Element('versicolor'))
    root.append(Element('virginica'))

    print(len(root))
    # 3

Selecting subtree
-----------------
Selecting subtree:

.. code-block:: python

    from lxml.etree import Element


    root = Element('iris')
    root.append(Element('setosa'))
    root.append(Element('versicolor'))
    root.append(Element('virginica'))

    selected = root[2]
    print(selected.tag)
    # virginica

Where is selected element:

.. code-block:: python

    from lxml.etree import Element


    root = Element('iris')
    root.append(Element('setosa'))
    root.append(Element('versicolor'))
    root.append(Element('virginica'))

    selected = root[1]
    root.index(selected)
    # 1

    selected = root[2]
    root.index(selected)
    # 2

Element tree as a lists
-----------------------
Elements are lists:

.. code-block:: python

    from lxml.etree import tostring, Element


    root = Element('iris")
    root.append(Element('setosa"))
    root.append(Element('versicolor"))
    root.append(Element('virginica"))

    children = list(root)
    print(children)
    # [
    #     <Element setosa at 0x113cd4048>,
    #     <Element versicolor at 0x113cd4188>,
    #     <Element virginica at 0x113cd41c8>
    # ]

Iterating over elements:

.. code-block:: python

    from lxml.etree import Element


    root = Element("iris")
    root.append(Element("setosa"))
    root.append(Element("versicolor"))
    root.append(Element("virginica"))

    for child in root:
        print(child.tag)

    # setosa
    # versicolor
    # virginica

Slicing elements:

.. code-block:: python

    from lxml.etree import Element


    root = Element("iris")
    root.append(Element("setosa"))
    root.append(Element("versicolor"))
    root.append(Element("virginica"))

    root.insert(0, Element("arctica"))

    start = root[:1]
    end = root[-1:]

    print(start[0].tag)  # arctica
    print(end[0].tag)    # virginica

Elements as a dict
------------------
Create element using ``dict`` interface:

.. code-block:: python

    from lxml.etree import tostring, Element


    tag = Element("iris", kingdom="plantae")

    print(tostring(tag))
    # b'<iris kingdom="plantae"/>'

Get element attributes and values:

.. code-block:: python

    from lxml.etree import tostring, Element


    tag = Element("iris", kingdom="plantae")

    print(tag.get("kingdom"))          # plantae
    print(tag.get("not-existing"))     # None

Set element attributes and values:

.. code-block:: python

    from lxml.etree import tostring, Element


    tag = Element("iris", kingdom="plantae")
    tag.set("kind", "flower")

    print(tag.get("kind"))
    # flower

    print(tostring(tag))
    # b'<iris kingdom="plantae" kind="flower"/>'

Elements carry attributes as a dict:

.. code-block:: python

    from lxml.etree import Element


    tag = Element("iris", kingdom="plantae")
    tag.set("kind", "flower")

    tag.keys()
    # ['kind', 'kingdom']

    tag.values()
    # ['plantae', 'flower']

    tag.items()
    # [('kingdom', 'plantae'), ('kind', 'flower')]

Iterating over element attributes and values:

.. code-block:: python

    from lxml.etree import Element


    tag = Element("iris", kingdom="plantae")
    tag.set("kind", "flower")

    for key, value in tag.items():
        print(f'{key} -> {value}')

    # kingdom -> plantae
    # kind -> flower

Elements carry attributes as a dict:

.. code-block:: python

    from lxml.etree import Element


    tag = Element("iris", kingdom="plantae")
    tag.set("kind", "flower")

    tag.attrib['kingdom']
    # 'plantae'

    tag.attrib['not-existing']
    # Traceback (most recent call last):
    # KeyError: 'not-existing'

    tag.attrib['species'] = 'Setosa'
    tag.attrib.get('species')
    # 'Setosa'

    tag.attrib
    # {'kingdom': 'plantae', 'kind': 'flower'}

    tag.attrib.items()
    # [('kingdom', 'plantae'), ('kind', 'flower'), ('species', 'Setosa')]

Elements contain text
---------------------
.. code-block:: python

    from lxml.etree import tostring, Element

    tag = Element("iris")
    tag.text = "Setosa"

    tag.text
    # 'Setosa'

    tostring(tag)
    # b'<iris>Setosa</iris>'

Tree iteration
--------------
.. code-block:: python

    from lxml.etree import tostring, Element, SubElement

    root = Element("iris")
    SubElement(root, "species").text = "Setosa"
    SubElement(root, "species").text = "Virginica"
    SubElement(root, "flower").text = "Versicolor"

    print(tostring(root, pretty_print=True))
    # b'<iris>
    #       <species>Setosa</species>
    #       <species>Virginica</species>
    #       <flower>Versicolor</flower>
    # </iris>'


    for element in root.iter():
        print(f'{element.tag} -> {element.text}')

    # iris -> None
    # species -> Setosa
    # species -> Virginica
    # flower -> Versicolor


    for element in root.iter("species"):
        print(f'{element.tag} -> {element.text}')

    # species -> Setosa
    # species -> Virginica


    for element in root.iter("species", "flower"):
        print(f'{element.tag} -> {element.text}')

    # species -> Setosa
    # species -> Virginica
    # flower -> Versicolor

Entities
--------
.. code-block:: python

    from lxml.etree import tostring, Element, SubElement, Entity

    root = Element("iris")
    print(tostring(root))
    # b'<iris/>'

    root.append(Entity("#234"))
    print(tostring(root))
    # b'<iris>&#234;</iris>'

Comments
--------
.. code-block:: python

    from lxml.etree import tostring, Element, SubElement, Comment

    root = Element("iris")
    print(tostring(root))
    # b'<iris/>'

    root.append(Comment("Hello World"))
    print(tostring(root))
    # b'<iris><!--Hello World--></iris>'

.. code-block:: python

    from lxml.etree import tostring, Element, SubElement

    root = Element('iris')
    SubElement(root, 'species').text = 'setosa'
    SubElement(root, 'species').text = 'virginica'
    SubElement(root, 'flower').text = 'versicolor'

    print(tostring(root))
    # b'<iris><species>setosa</species><species>virginica</species><flower>versicolor</flower></iris>'

.. code-block:: python

    from lxml.etree import tostring, Element, Entity

    root = Element('iris')
    root.append(Entity('#234'))

    print(tostring(root))
    # b'<iris>&#234;</iris>'

.. code-block:: python

    from lxml.etree import tostring, Element, Comment

    root = Element('iris')
    root.append(Comment('Hello World'))
    print(tostring(root))
    # b'<iris><!--Hello World--></iris>'

.. code-block:: python

    from lxml.etree import tostring, Element, Entity, Comment

    root = Element('iris')
    root.append(Element('species'))
    root.append(Element('species'))
    root.append(Element('flower'))
    root.append(Entity('#234'))
    root.append(Comment('Hello World'))

    print(tostring(root))
    # b'<iris><species/><species/><flower/>&#234;<!--Hello World--></iris>'


    for element in root.iter():
        if isinstance(element.tag, str):
            print(f'Tag: {element.tag} -> {element.text}')
        else:
            print(f'Special: {element} -> {element.text}')

    # Tag: iris -> None
    # Tag: species -> None
    # Tag: species -> None
    # Tag: flower -> None
    # Special: &#234; -> &#234;
    # Special: <!--Hello World--> -> Hello World


    for element in root.iter(tag=Element):
            print(f'{element.tag} -> {element.text}')

    # iris -> None
    # species -> None
    # species -> None
    # flower -> None


    for element in root.iter(tag=Entity):
        print(element.text)

    # &#234;


    for element in root.iter(tag=Comment):
        print(element.text)

    # Hello World

Serialization
-------------
.. code-block:: python

    from lxml.etree import tostring, XML


    root = XML('<root><a><b/></a></root>')

    tostring(root)
    # b'<root><a><b/></a></root>'

    print(tostring(root, xml_declaration=True))
    # b"<?xml version='1.0' encoding='ASCII'?>\n<root><a><b/></a></root>"

    print(tostring(root, encoding='utf-8'))
    # b'<root><a><b/></a></root>'

    print(tostring(root, encoding='iso-8859-2'))
    # b"<?xml version='1.0' encoding='iso-8859-2'?>\n<root><a><b/></a></root>"

    print(tostring(root, pretty_print=True))
    # b'<root>\n  <a>\n    <b/>\n  </a>\n</root>\n'

    print(tostring(root, pretty_print=True).decode())
    # <root>
    #   <a>
    #     <b/>
    #   </a>
    # </root>

.. code-block:: python

    from lxml.etree import tostring, XML

    root = XML('<html><head/><body><p>Hello<br/>World</p></body></html>')

    # default: method = 'xml'
    tostring(root)
    # b'<html><head/><body><p>Hello<br/>World</p></body></html>'

    tostring(root, method='xml')
    # b'<html><head/><body><p>Hello<br/>World</p></body></html>'

    tostring(root, method='html')
    # b'<html><head></head><body><p>Hello<br>World</p></body></html>'

    print(tostring(root, method='html', pretty_print=True))
    # b'<html>\n<head></head>\n<body><p>Hello<br>World</p></body>\n</html>\n'

    print(tostring(root, method='html', pretty_print=True).decode())
    # <html>
    # <head></head>
    # <body><p>Hello<br>World</p></body>
    # </html>

    tostring(root, method='text')
    # b'HelloWorld'
