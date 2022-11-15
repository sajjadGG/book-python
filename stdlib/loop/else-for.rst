Loop Else For
=============
* ``else`` will execute, if ``break`` was not used to exit the loop


.. code-block:: python

    DATA = """
    127.0.0.1       localhost
    127.0.0.1       astromatt
    10.13.37.1      nasa.gov esa.int
    255.255.255.255 broadcasthost
    ::1             localhost
    """
    DNS = []

    for line in DATA.splitlines():
        if not line:
            continue

        ip, *hostnames = line.split()
        # ip == '10.13.37.1'
        # hostnames == ['nasa.gov', 'esa.int']

        for record in DNS:
            if record['ip'] == ip:
                record['hostnames'].update(hostnames)
                break
        else:
            DNS.append({
                'hostnames': set(hostnames),
                'ip': ip,
            })

    print(DNS)
    # [
    #   {'ip': '127.0.0.1', 'hostnames': {'astromatt', 'localhost'}},
    #   {'ip': '10.13.37.1', 'hostnames': {'esa.int', 'nasa.gov'}},
    #   {'ip': '255.255.255.255', 'hostnames': {'broadcasthost'}},
    #   {'ip': '::1', 'hostnames': {'localhost'}},
    # ]


.. todo:: Assignments
