Pandas Set Option
=================


Rationale
---------


SetUp
-----
>>> import pandas as pd
>>> df = pd.DataFrame()


Display Output
--------------
Limited:

>>> pd.set_option('display.max_rows', 50)
>>> pd.set_option('display.max_columns', 20)
>>> pd.set_option('display.width', 1000)

Unlimited:

>>> pd.set_option('display.max_rows', None)
>>> pd.set_option('display.max_columns', None)
>>> pd.set_option('display.width', None)


Using in context
----------------
>>> with pd.option_context('display.max_rows', 100):
...     print(df)
Empty DataFrame
Columns: []
Index: []

>>> with pd.option_context('display.max_rows', 50, 'display.max_columns', 10):
...     print(df)
Empty DataFrame
Columns: []
Index: []


Assignments
-----------
.. todo:: Create assignments
