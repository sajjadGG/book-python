Pętle
=====


Wybitnie użyteczne pętla ``for``
--------------------------------

.. code-block:: python

    for x in [1, 3, 4, 2]:
        print(f'Value is: {x}')


``while``
---------

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
