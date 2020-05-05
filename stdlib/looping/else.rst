.. _Loop Else:

*************
Loop ``else``
*************


``while``
=========
.. highlights::
    * ``else`` will execute, if ``break`` was not used to exit the loop

.. code-block:: python

    abort = False
    countdown = 10


    while countdown >= 0:
        if abort:
            break

        print(f'Launch in T-{countdown}')
        countdown -= 1

    else:
        print('Countdown went smooth and there was no abort at this time')
        print('Lift off! We have lift-off!')


``for``
=======
.. highlights::
    * ``else`` will execute, if ``break`` was not used to exit the loop

.. code-block:: python

    DATA = """
    127.0.0.1       localhost
    127.0.0.1       astromatt
    10.13.37.1      nasa.gov esa.int roscosmos.ru
    255.255.255.255 broadcasthost
    ::1             localhost
    """
    DNS = []

    for line in DATA.splitlines():
        if not line:
            continue

        ip, *hostnames = line.split()
        # ip == '10.13.37.1'
        # hostnames == ['nasa.gov', 'esa.int', 'roscosmos.ru']

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
    #   {'ip': '10.13.37.1', 'hostnames': {'roscosmos.ru', 'esa.int', 'nasa.gov'}},
    #   {'ip': '255.255.255.255', 'hostnames': {'broadcasthost'}},
    #   {'ip': '::1', 'hostnames': {'localhost'}},
    # ]


Assignments
===========
.. todo:: Create assignments
