Model About
===========
* What are model fields?
* Model field arguments
* Fat model architecture
* Single File vs. Models per file


Attributes
----------
* ``blank``
* ``choices``
* ``db_column``
* ``db_index``
* ``default``
* ``editable``
* ``error_message``
* ``help_text``
* ``limit_choices_to``
* ``max_length``
* ``null``
* ``primary_key``
* ``unique``
* ``validators``
* ``verbose_name``


Abstract Models
---------------
.. code-block:: python

    class MyBaseModel(models.Model):
        class Meta:
            abstract = True

.. code-block:: python

    class BaseModel(models.Model):
        uuid = models.UUIDField(verbose_name=_('Unique UUID'), unique=True, null=False, blank=False, default=uuid4, editable=False)
        creation_author = models.ForeignKey(verbose_name=_('Creation Author'), to='auth.User', null=True, blank=True, default=None, on_delete=models.SET_NULL, related_name='creation_author')
        creation_date = models.DateTimeField(verbose_name=_('Creation Date'), auto_now_add=True, editable=False)
        modification_date = models.DateTimeField(verbose_name=_('Modification Date'), auto_now=True)
        modification_author = models.ForeignKey(verbose_name=_('Modification Author'), to='auth.User', null=True, blank=True, default=None, on_delete=models.SET_NULL, related_name='modification_author')
        ip_address = models.GenericIPAddressField(verbose_name=_('IP Address'), null=True, blank=True, default=None, editable=False)

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
