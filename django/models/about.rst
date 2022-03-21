Model About
===========


Important
---------
* What are model fields?
* Model field arguments
* Fat model architecture
* Single File vs. Models per file


Attributes
----------
* ``verbose_name``
* ``max_length``
* ``choices``
* ``validators``
* ``help_text``
* ``null``
* ``blank``
* ``default``
* ``db_index``
* ``db_column``
* ``default``
* ``limit_choices_to``
* ``editable``
* ``primary_key``
* ``help_text``
* ``error_message``
* ``unique``


Abstract Models
---------------
.. code-block:: python

    class Meta:
        abstract = True



Database schema migration
-------------------------
Makemigrations:

.. code-block:: console

    $ python manage.py makemigrations
    Migrations for 'contact':
      addressbook/contact/migrations/0001_initial.py
        - Create model Contact


Migrate:

.. code-block:: console

    $ python manage.py migrate
    Operations to perform:
      Apply all migrations: admin, auth, contenttypes, contact, sessions
    Running migrations:
      Applying contact.0001_initial... OK
