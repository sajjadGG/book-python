Models
======


Model Fields
------------
* What are model fields?


Text fields
-----------
* ``CharField``
* ``TextField``
* ``SlugField``
* ``URLField``
* ``EmailField``


Numeric fields
--------------
* ``IntegerField``
* ``FloatField``
* ``DecimalField``
* ``PositiveIntegerField``
* ``PositiveSmallIntegerField``
* ``PositiveBigIntegerField``
* ``SmallIntegerField``
* ``BigIntegerField``
* float vs decimal


Logic
-----
* ``BooleanField``


Date and Time
-------------
* ``DateField``
* ``DateTimeField``
* ``DurationField``
* ``TimeField``


Storage
-------
* ``BinaryField``
* ``ImageField``
* ``FileField``
* ``FilePathField``


Special
-------
* ``CommaSeparatedIntegerField``
* ``JSONField``
* ``IPAddressField``
* ``GenericIPAddressField``


Auto
----
* ``AutoField``
* ``BigAutoField``
* ``SmallAutoField``


Relations
---------
* ``ForeignKeyField``
* ``OneToOneField``
* ``ManyToManyField``


Model field arguments
---------------------

All
---
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


Relations
---------
* ``to`` (ForeignKey, ManyToManyField)
* ``related_name`` (ForeignKey, ManyToManyField)
* ``on_delete`` (ForeignKey, ManyToManyField)


Date and Time
-------------
* ``auto_add`` (DateField, DateTimeField)
* ``auto_add_now`` (DateField, DateTimeField)


Numeric
-------
* ``decimal_places`` (DecimalField)
* ``max_digits`` (DecimalField)


Abstract Models
---------------
.. code-block:: python

    class Meta:
        abstract = True

Architecture
------------
* Fat model architecture


Single File vs. Models per file
-------------------------------


Reverse engineering database
----------------------------
* ``python manage.py inspectdb``


Graph Model
-----------
* https://django-extensions.readthedocs.io/en/latest/graph_models.html#example-usage

.. code-block:: console

    $ brew install graphviz
    $ pip install pydotplus
    $ python manage.py graph_models -a -g -o all.png
    $ python manage.py graph_models myapp -g -o myapp.png
    $ python manage.py graph_models -a -I Contact,Address -o models.png
    $ python manage.py graph_models -a --arrow-shape normal -o myproject.png


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


Example Model
-------------
.. literalinclude:: src/django-models-example.py
    :language: python
    :caption: Example Model


Assignments
-----------
.. literalinclude:: assignments/django_addressbook.py
    :caption: :download:`Solution <assignments/django_addressbook.py>`
    :end-before: # Solution

