Database Update
===============


SQL Syntax
----------
.. code-block:: sql

    UPDATE astronauts SET
        agency = 'NASA'
    WHERE lastname = 'Watney';

.. code-block:: sql

    UPDATE astronauts SET
        firstname = 'Mark',
        lastname = 'Watney',
        agency = 'NASA'
    WHERE id = 1

.. code-block:: sql

    UPDATE astronauts SET
        mission = 'Ares 3',
    WHERE lastname IN ('Watney', 'Lewis', 'Martinez');
