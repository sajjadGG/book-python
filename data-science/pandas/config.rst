*************
Configuration
*************

Display Output
==============
* Set options for whole script:

    .. code-block:: python

        pd.set_option('display.height',1000)
        pd.set_option('display.max_rows',500)
        pd.set_option('display.max_columns',500)
        pd.set_option('display.width',1000)

* Unlimited for whole script:

    .. code-block:: python

        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)

* Use config only with context:

    .. code-block:: python

        with pd.option_context('display.max_rows', None, 'display.max_columns', 3):
            print(df)
