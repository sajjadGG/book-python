XML Stdlib
==========


Important
---------
``xml`` module from standard library:

.. code-block:: python

    from xml.etree.ElementTree import parse


    FILE = r'_temporary.xml'
    # <execute>
    #     <command timeout="2">/bin/ls -la /etc/</command>
    #     <command>/bin/ls -l /home/ /tmp/</command>
    #     <command timeout="1">/bin/sleep 2</command>
    #     <command timeout="2">/bin/echo 'hello'</command>
    # </execute>

    root = parse(FILE).getroot()

    for command in root.findall('./command'):
        print(command.tag)
        print(command.text)
        print(command.attrib)
        print()

    # command
    # /bin/ls -la /etc/
    # {'timeout': '2'}
    #
    # command
    # /bin/ls -l /home/ /tmp/
    # {}
    #
    # command
    # /bin/sleep 2
    # {'timeout': '1'}
    #
    # command
    # /bin/echo 'hello'
    # {'timeout': '2'}
