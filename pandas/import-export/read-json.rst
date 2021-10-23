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
.. literalinclude:: assignments/pandas_readjson_a.py
    :caption: :download:`Solution <assignments/pandas_readjson_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/pandas_readjson_b.py
    :caption: :download:`Solution <assignments/pandas_readjson_b.py>`
    :end-before: # Solution
