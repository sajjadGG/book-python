****************
DataFrame Locate
****************


* ``loc`` zaawansowane opcje wyszukiwania
* ``iloc`` integer locate - tylko po numerkach indeksów

.. warning::
    * ``df.loc`` - start and stop are included!!
    * ``df.iloc`` - behaves like Python slices

.. code-block:: python

    import numpy as np
    import pandas as pd

    np.random.seed(0)


    data =  np.random.randn(6, 4)
    columns = ['Morning', 'Noon', 'Evening', 'Midnight']
    index = pd.date_range('1970-01-01', periods=6)

    df = pd.DataFrame(data, index, columns)
    #               Morning       Noon    Evening   Midnight
    # 1970-01-01   0.486726  -0.291364  -1.105248  -0.333574
    # 1970-01-02   0.301838  -0.603001   0.069894   0.309209
    # 1970-01-03  -0.424429   0.845898  -1.460294   0.109749
    # 1970-01-04   0.909958  -0.986246   0.122176   1.205697
    # 1970-01-05  -0.172540  -0.974159  -0.848519   1.691875
    # 1970-01-06   0.047059   0.359687   0.531386  -0.587663

Single row
----------
* Returns the row as a Series

.. code-block:: python

    df.loc['1970-01-01']
    # Morning    -0.438232
    # Noon        1.493865
    # Evening    -1.113116
    # Midnight   -0.042712
    # Name: 1970-01-01 00:00:00, dtype: float64

Range of rows
-------------
.. code-block:: python

    df.loc['1970-01-02': '1970-01-04']
    #               Morning       Noon    Evening   Midnight
    # 1970-01-02   0.301838  -0.603001   0.069894   0.309209
    # 1970-01-03  -0.424429   0.845898  -1.460294   0.109749
    # 1970-01-04   0.909958  -0.986246   0.122176   1.205697

Range of dates
--------------
.. code-block:: python

    df.loc['1970-01']
    #                 Morning        Noon    Evening   Midnight
    # 1970-01-01     2.269755   -1.454366   0.045759  -0.187184
    # 1970-01-02     1.532779    1.469359   0.154947   0.378163
    # 1970-01-03    -0.887786   -1.980796  -0.347912   0.156349
    # 1970-01-04     1.230291    1.202380  -0.387327  -0.302303
    # 1970-01-05    -1.048553   -1.420018  -1.706270   1.950775
    # 1970-01-06    -0.509652   -0.438074  -1.252795   0.777490

Single row and single column
----------------------------
.. code-block:: python

    df.loc['1970-01-02', 'Morning']
    # -1.7982538699804334

Range of rows and single column
-------------------------------
* Note that both the start and stop of the slice are included

.. code-block:: python

    df.loc['1970-01-02':'1970-01-04', 'Noon']
    # 1970-01-02   -1.440613
    # 1970-01-03    0.301141
    # 1970-01-04   -0.574301
    # Freq: D, Name: Noon, dtype: float64

Range of rows and single column
-------------------------------
.. todo:: naprawić to

.. code-block:: python

    df.loc[['1970-01-02','1970-01-04'], 'Noon']
    # KeyError: "None of [['1970-01-02', '1970-01-04']] are in the [index]"

Single row and selected columns
-------------------------------
.. code-block:: python

    df.loc['1970-01-02', ['Noon', 'Midnight']]
    # Noon       -0.132430
    # Midnight   -0.444758
    # Name: 1970-01-02 00:00:00, dtype: float64

Single row and column range
---------------------------
.. code-block:: python

    df.loc['1970-01-02', 'Noon':'Midnight']
    # Noon       -0.132430
    # Evening    -0.504896
    # Midnight   -0.444758
    # Name: 1970-01-02 00:00:00, dtype: float64

Boolean list with the same length as the row axis
-------------------------------------------------
* Print row for given index is ``True``
* Default to ``False``

.. code-block:: python

    df.loc[[True, False, True]]
    #               Morning      Noon    Evening   Midnight
    # 1970-01-01  -0.438232  1.493865  -1.113116  -0.042712
    # 1970-01-03  -0.802938  0.301141  -0.258279  -1.492688

Conditional that returns a boolean Series
-----------------------------------------
.. code-block:: python

    df.loc[df['Morning'] < 0]
    #               Morning       Noon    Evening   Midnight
    # 1970-01-01  -0.438232   1.493865  -1.113116  -0.042712
    # 1970-01-02  -1.798254  -1.440613  -0.946041  -2.732719
    # 1970-01-03  -0.802938   0.301141  -0.258279  -1.492688

Conditional that returns a boolean Series with column labels specified
----------------------------------------------------------------------
.. code-block:: python

    df.loc[df['Morning'] < 0, 'Evening']
    # 1970-01-01   -1.113116
    # 1970-01-02   -0.946041
    # 1970-01-03   -0.258279
    # Freq: D, Name: Evening, dtype: float64

.. code-block:: python

    df.loc[df['Morning'] < 0, ['Morning', 'Evening']]
    #               Morning    Evening
    # 1970-01-01  -0.438232  -1.113116
    # 1970-01-02  -1.798254  -0.946041
    # 1970-01-03  -0.802938  -0.258279

Filtering with callable
-----------------------
.. code-block:: python

    def morning_below_zero(df):
        return df['Morning'] < 0

    df.loc[morning_below_zero]
    #               Morning       Noon    Evening   Midnight
    # 1970-01-01  -0.438232   1.493865  -1.113116  -0.042712
    # 1970-01-02  -1.798254  -1.440613  -0.946041  -2.732719
    # 1970-01-03  -0.802938   0.301141  -0.258279  -1.492688

.. code-block:: python

    df.loc[lambda df: df['Morning'] < 0]
    #               Morning       Noon    Evening   Midnight
    # 1970-01-01  -0.438232   1.493865  -1.113116  -0.042712
    # 1970-01-02  -1.798254  -1.440613  -0.946041  -2.732719
    # 1970-01-03  -0.802938   0.301141  -0.258279  -1.492688

Set value for all items matching the list of labels
---------------------------------------------------
.. code-block:: python

    df.loc[df['Morning'] < 0, 'Evening'] = 0.0
    #               Morning       Noon    Evening   Midnight
    # 1970-01-01  -0.438232   1.493865   0.000000  -0.042712
    # 1970-01-02  -1.798254  -1.440613   0.000000  -2.732719
    # 1970-01-03  -0.802938   0.301141   0.000000  -1.492688
    # 1970-01-04   0.820863  -0.574301  -0.901532  -0.191122
    # 1970-01-05   1.800466  -0.777165   0.611194   1.345492
    # 1970-01-06   0.141029  -0.134463  -0.046938   0.401554

Set value for an entire row
---------------------------
.. code-block:: python

    df.loc['1970-01-01'] = 0.0
    #               Morning       Noon    Evening   Midnight
    # 1970-01-01   0.000000   0.000000   0.000000   0.000000
    # 1970-01-02   0.391381  -0.034658  -0.026441  -0.528525
    # 1970-01-03   0.292151   1.328559   1.510460   0.973299
    # 1970-01-04   0.985247   1.033980  -0.688412   1.171957
    # 1970-01-05  -0.210144   0.112805  -0.691808   0.339706
    # 1970-01-06   1.259968  -0.283706  -1.333459  -0.962464

Set value for an entire column
------------------------------
.. code-block:: python

    df.loc[:, 'Evening'] = 0.0
    #               Morning       Noon  Evening   Midnight
    # 1970-01-01   0.000000   0.000000      0.0   0.000000
    # 1970-01-02   0.391381  -0.034658      0.0  -0.528525
    # 1970-01-03   0.292151   1.328559      0.0   0.973299
    # 1970-01-04   0.985247   1.033980      0.0   1.171957
    # 1970-01-05  -0.210144   0.112805      0.0   0.339706
    # 1970-01-06   1.259968  -0.283706      0.0  -0.962464

Set value for rows matching callable condition
----------------------------------------------
* Important!

.. code-block:: python

    df.loc[df['Morning'] < 0] = 0.0
    #              Morning       Noon  Evening   Midnight
    # 1970-01-01  0.000000   0.000000      0.0   0.000000
    # 1970-01-02  0.391381  -0.034658      0.0  -0.528525
    # 1970-01-03  0.292151   1.328559      0.0   0.973299
    # 1970-01-04  0.985247   1.033980      0.0   1.171957
    # 1970-01-05  0.000000   0.000000      0.0   0.000000
    # 1970-01-06  1.259968  -0.283706      0.0  -0.962464


Assignments
===========
.. todo:: Create assignments
