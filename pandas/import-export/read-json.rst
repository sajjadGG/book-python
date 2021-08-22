Pandas Read JSON
================


Rationale
---------
* File paths works also with URLs


Compressed
----------
* If the extension is ``.gz``, ``.bz2``, ``.zip``, and ``.xz``, the corresponding compression method is automatically selected

.. code-block:: python

    df = pd.read_json('sample_file.gz', compression='infer')


Assignments
-----------
.. literalinclude:: assignments/pandas_read_json_iris.py
    :caption: :download:`Solution <assignments/pandas_read_json_iris.py>`
    :end-before: # Solution

.. literalinclude:: assignments/pandas_read_json_openapi.py
    :caption: :download:`Solution <assignments/pandas_read_json_openapi.py>`
    :end-before: # Solution
