Model Introspect
================


Reverse engineering database
----------------------------
* ``python manage.py inspectdb``


Graph Model
-----------
* GraphViz + Dot
* Django Extensions: https://django-extensions.readthedocs.io/en/latest/graph_models.html#example-usage

.. code-block:: console

    $ brew install graphviz
    $ pip install pydotplus
    $ pip install django-extensions

    # Add 'django_extensions' to INSTALLED_APP

    $ python manage.py graph_models -a -g -o all.png
    $ python manage.py graph_models myapp -g -o myapp.png
    $ python manage.py graph_models -a -I Contact,Address -o models.png
    $ python manage.py graph_models -a --arrow-shape normal -o myproject.png

.. figure:: img/uml-django-models-1.png
.. figure:: img/uml-django-models-2.png
.. figure:: img/uml-django-models-3.png
.. figure:: img/uml-django-models-4.png
.. figure:: img/uml-django-models-5.png
.. figure:: img/uml-django-models-6.png
