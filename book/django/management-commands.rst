*******************
Management Commands
*******************

Built-in
========
.. code-block:: text

    [auth]
        changepassword
        createsuperuser

    [contenttypes]
        remove_stale_contenttypes

    [dashboard]
        customdashboard

    [django]
        check
        compilemessages
        createcachetable
        dbshell
        diffsettings
        dumpdata
        flush
        inspectdb
        loaddata
        makemessages
        makemigrations
        migrate
        sendtestemail
        shell
        showmigrations
        sqlflush
        sqlmigrate
        sqlsequencereset
        squashmigrations
        startapp
        startproject
        test
        testserver

    [sessions]
        clearsessions

    [staticfiles]
        collectstatic
        findstatic
        runserver

Writing own management commands
===============================
.. code-block:: text

    app
        management
        __init__.py
            commands
            __init__.py
            my_command.py

.. literalinclude:: src/django-management-commands.py
    :language: python
    :name: listing-django-management-commands
    :caption: Writing own management commands
