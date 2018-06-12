********************
Przydatne Biblioteki
********************

``django-import-export``
========================
* ``INSTALLED_APPS.append('import_export')``


:admin.py:
    .. code-block:: python

        from import_export.admin import ImportExportModelAdmin

        @admin.register(Command)
        class CommandAdmin(ImportExportModelAdmin):
            pass

``django-grappelli``
====================
* ``INSTALLED_APPS.insert(0, 'grappelli')``
