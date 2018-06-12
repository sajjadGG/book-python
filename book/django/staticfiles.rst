***********
Staticfiles
***********


Settings
========
.. code-block:: python

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/dev/howto/static-files/
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, '_static')
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, '_media')

Serving staticfiles
===================
.. code-block:: python

    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
