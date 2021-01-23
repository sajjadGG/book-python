Builder
=======


Rationale
---------
* EN: Builder
* PL: Budowniczy
* Type: object


Use Cases
---------
* When language does not have keyword arguments to functions and methods


Problem
-------
* https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html

>>> def read_csv(filepath_or_buffer, sep=', ', delimiter=None, header='infer',
...              names=None, index_col=None, usecols=None, squeeze=False, prefix=None,
...              mangle_dupe_cols=True, dtype=None, engine=None, converters=None,
...              true_values=None, false_values=None, skipinitialspace=False,
...              skiprows=None, nrows=None, na_values=None, keep_default_na=True,
...              na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False,
...              infer_datetime_format=False, keep_date_col=False, date_parser=None,
...              dayfirst=False, iterator=False, chunksize=None, compression='infer',
...              thousands=None, decimal=b'.', lineterminator=None, quotechar='"',
...              quoting=0, escapechar=None, comment=None, encoding=None, dialect=None,
...              tupleize_cols=None, error_bad_lines=True, warn_bad_lines=True,
...              skipfooter=0, doublequote=True, delim_whitespace=False, low_memory=True,
...              memory_map=False, float_precision=None):
...     pass
>>>
>>> data = read_csv('myfile.csv', ', ', None, 'infer', None, None, None, False, None,
...                 True, None, None, None, None, None, False, None, None, None, True,
...                 True, False, True, False, False, False, None, False, False, None,
...                 'infer', None, b'.', None, '"', 0, None, None, None, None, None,
...                 True, True, 0, True, False, True, False, None)


Design
------


Implementation
--------------
.. literalinclude:: ../_src/designpatterns-builder.py
    :language: python


Assignments
-----------
.. todo:: Create assignments
