Builder
=======
* EN: Builder
* PL: Budowniczy
* Type: object
* Why: To separate the construction of an object from its representation
* Usecase: Export data to different formats


Pattern
-------
.. figure:: img/designpatterns-builder-pattern.png

.. literalinclude:: src/designpatterns-builder-pattern.md
    :language: md


Problem
-------
* Violates Open/Close Principle
* Tight coupling between Presentation class with formats
* PDF has pages, Movies has frames, this knowledge belongs to somewhere else
* Duplicated code
* Magic number

.. figure:: img/designpatterns-builder-problem.png

.. literalinclude:: src/designpatterns-builder-problem.md
    :language: md

.. literalinclude:: src/designpatterns-builder-problem.py
    :language: python


Solution
--------
* Use the builder pattern to separate the exporting logic from the presentation format
* The same exporting logic belongs to the different formats

.. figure:: img/designpatterns-builder-solution.png

.. literalinclude:: src/designpatterns-builder-solution.md
    :language: md

.. literalinclude:: src/designpatterns-builder-solution.py
    :language: python


Use Case - 0x01
---------------
.. literalinclude:: src/designpatterns-builder-usecase-1.py
    :language: python


Use Case - 0x02
---------------
* When language does not have keyword arguments to functions and methods
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


Assignments
-----------
.. todo:: Assignments
          You’re building a word processor similar to Word. The user can add text or image elements to a document and then export it to a variety of different formats such as HTML, text, and so on.
          Look at the implementation of the Document class in the builder package.
          Note that if the selected format is HTML, all text and image elements are written to an HTML document. If the selected format is text, however, only text elements are written to a text file. You can run the code in the Demo class to see this in action.
          What are the problems with the current design? Refactor this design using the builder pattern.
