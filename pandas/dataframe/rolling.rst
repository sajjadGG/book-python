DataFrame Rolling
=================


Resample
--------
>>> df.resample()


Rolling
-------
>>> df.rolling()


Shift
-----
>>> df - df.shift(periods=1, freq="D")


Diff
----
>>> df.diff()

>>> df = pd.DataFrame([20,35,70,100])
>>> df.diff()
