******************
Standalone scripts
******************

- lepiej management commands

.. code-block:: python

    import sys
    import os
    import django

    sys.path.append('/path/to/django-project')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apollo.settings')
    django.setup()

    from apollo.models import MyModel