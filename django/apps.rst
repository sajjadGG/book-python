Apps
====


Reusability
-----------


Location
--------


Create
------
.. code-block:: console

    $ cd addressbook
    $ django-admin startapp myapp

.. code-block:: python

    # settings.py
    INSTALLED_APPS += ['myproject.myapp.apps.ContactConfig']


Structure
---------
.. code-block:: text

    myproject/
        manage.py
        myproject/
            __init__.py
            asgi.py
            settings.py
            urls.py
            wsgi.py
        myapp/
            __init__.py
            admin.py
            migrations/
                __init__.py
                0001_initial.py
            models.py
            static/
                myapp/
                    img/
                        image.png
                    css/
                        style.css
                    js/
                        script.js
            templates/
                myapp/
                    detail.html
                    index.html
                    results.html
            tests.py
            urls.py
            views.py


Configuration
-------------
.. code-block:: python

    from django.apps import AppConfig
    from django.utils.translation import gettext_lazy as _


    class ContactConfig(AppConfig):
        default_auto_field = 'django.db.models.BigAutoField'
        name = 'myapp'
        verbose_name = _('MyApp')
