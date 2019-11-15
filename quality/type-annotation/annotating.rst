************************
Annotating existing code
************************


``PyAnnotate``
==============
* http://mypy-lang.blogspot.com/2017/11/dropbox-releases-pyannotate-auto.html

.. code-block:: console

    $ pip install pyannotate

    # (the -w flag means “go ahead, update the file”)
    $ pyannotate -w FILE


``monkeytype``
==============
* https://instagram-engineering.com/let-your-code-type-hint-itself-introducing-open-source-monkeytype-a855c7284881

.. code-block:: console

    $ pip install monkeytype
    $ monkeytype run runtests.py
    $ monkeytype stub some.module
    $ monkeytype apply some.module

