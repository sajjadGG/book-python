Pętle
=====


Pętla ``for``
-------------

.. code-block:: python

    for x in [1, 3, 4, 2]:
        print(f'Value is: {x}')

.. code-block:: python

    for x in range(0, 30):
        print(f'Value is: {x}')

Pętla ``while``
---------------

.. code-block:: python

    x = 0

    while x <= 10:
        print(f'Value is: {x}')
        x = x + 1

.. code-block:: python

    while True:
        number = input('Type number: ')

        if number:
            break
