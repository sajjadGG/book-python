****
TODO
****

Book TODO
=========
- Machine Learning rewrite
- Newsletter, once a month, what changed in the book


Pandas
======
* pd.explode()
* series.map()
* series.apply(lambda)
* df[column].drop(axis=1) - drop column
* series.groupby()
* series.plot(kind)
* series.describe() - inaczej się zachowuje dla indeksów numerycznych a inaczej dla timeseries; describe ignores NaN values
* series.describe(percentiles)
* series.ffil(), bfill() Interpolate values
* grouping by multiple series
* series.isnull()
* series.isnull().any()
* series.dropna()
* series.groupby([]) and Series.unstack()
* new_series = series / series
* series.describe()
* czym jest axis=0 (wiersze) vs axis=1 (columns)
* pd.to_datetime()
* df.index = pd.to_datetime(df['timestamp'])
* ax = df.plot()
* ax.axhline(df['temperature'].median(), color='r', linestyle=“-“)
* df.index.viewDf.groupby(df.index.date).count()
* df.groupby(df.index.week).count()
* series.isin()
* df[(df.index.hour > 12) & (df.index.hour <= 12)][„temperature”].plot()
* data report by day "D" or "5T" - 5 minute intervals;
* df.resample("D").max().head()dr[„temperature”].resample(“D”).agg([“min”, “max”]).plot()

Python PEP
==========
* type_check decorator, sprawdzający ``function.__annotations__``
* dict(keys=[...], values=[...])
* time().now()
* from pprint import pprint, print(pretty=True) (albo podawanie formattera)
* JSON datetime encoder, decoder to isoformat (UTC)
* from datetime import parse(str, format)
* from datetime import format(str, format)
* Simple interface for HTTP requests (similar to requests)
* CTypes argtypes, restype from TypeAnnotation
* Context manager ``with logging.DEBUG:``
