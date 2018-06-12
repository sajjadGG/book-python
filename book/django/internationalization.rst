*************
i18n and l10n
*************

- transifex-client
- gettext
- makemessages -l en
- compilemessages
- django.utils.timezone
- blocktrans
- trans templatetag
- from django.conf.locale.en import formats as en_formats
- from django.utils.translation import ugettext_lazy as _


.. code-block:: python

    # Internationalization
    # https://docs.djangoproject.com/en/dev/topics/i18n/
    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    en_formats.DATETIME_FORMAT = 'Y-m-d H:i'
    en_formats.DATE_FORMAT = 'Y-m-d'
    en_formats.TIME_FORMAT = 'H:i'


.. code-block:: console

    $ cd botnet/heartbeat
    $ mkdir locale

    $ django-admin makemessages -l en
    processing locale en

    $ django-admin makemessages -l pl
    processing locale pl

    $ django-admin compilemessages
    processing file django.po in /private/tmp/botnet/botnet/heartbeat/locale/en/LC_MESSAGES
    processing file django.po in /private/tmp/botnet/botnet/heartbeat/locale/pl/LC_MESSAGES
