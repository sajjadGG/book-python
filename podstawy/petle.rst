Pętle
=====


Pętla ``for``
-------------

.. code-block:: python

    for x in [1, 3, 4, 2]:
        print(f'Value is: {x}')


.. code-block:: python

    for x in ['Max', 3, 'Peck', 2.8, [1, 'José', 'Jiménez']]:
        print(f'Value is: {x}')

.. code-block:: python

    for x in range(0, 30):
        print(f'Value is: {x}')

.. code-block:: python

    for x in range(0, 30, 5):
        print(f'Value is: {x}')

.. code-block:: python

    for key, value in [(0, 0), (1, 1), (1, 2)]:
        print(f'{key} -> {value}')

.. code-block:: python

    slownik = {'x': 1, 'y': 2}

    for key in slownik:
        print(slownik.get(key))

    for key, value in slownik.items():
        print(key, value)


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
