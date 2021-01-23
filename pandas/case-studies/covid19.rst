Case Study COVID-19
===================


Rationale
-------------------------------------------------------------------------------
* Data Source: https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series
* https://www.youtube.com/watch?v=54XLXg4fYsc
* https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series
* https://aatishb.com/covidtrends/?location=Poland
* https://aatishb.com/covidtrends/?location=Brazil&location=China&location=India&location=Poland&location=Russia&location=US
* https://youtu.be/xtZYKcOdJp0?t=168

Code
-------------------------------------------------------------------------------
.. code-block:: python

    import pandas as pd
    import numpy as np
    from doctest import testmod

    CONFIRMED = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
    DEATHS = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
    RECOVERED = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'

    confirmed = pd.read_csv(CONFIRMED)
    deaths = pd.read_csv(DEATHS)
    recovered = pd.read_csv(RECOVERED)


    def _get(column_name, df, country):
        """
        >>> _get('Confirmed', confirmed, 'Poland').loc['2020-11-11']
        Confirmed    618813
        Name: 2020-11-11 00:00:00, dtype: int64

        >>> _get('Confirmed', confirmed, 'US').loc['2020-11-11']
        Confirmed    10448056
        Name: 2020-11-11 00:00:00, dtype: int64

        >>> _get('Deaths', confirmed, 'Poland').loc['2020-11-11']
        Deaths    618813
        Name: 2020-11-11 00:00:00, dtype: int64
        """
        if country:
            query = df['Country/Region'] == country
            df = df[query]

        df = df.transpose()[4:].sum(axis='columns').astype(int)
        df = pd.DataFrame(df)
        df.columns = [column_name]
        df.index = pd.to_datetime(df.index)
        return df


    def covid19(country=None):
        """
        >>> covid19('Poland').loc['2020-11-11']
        Confirmed    618813
        Deaths         8805
        Recovered    242875
        Name: 2020-11-11 00:00:00, dtype: int64

        >>> covid19('US').loc['2020-11-11']
        Confirmed    10448056
        Deaths         242171
        Recovered     3997175
        Name: 2020-11-11 00:00:00, dtype: int64
        """
        return pd.concat((
            _get('Confirmed', confirmed, country),
            _get('Deaths', deaths, country),
            _get('Recovered', recovered, country),
        ), axis=1)


    def ratio(df, since='2020-11-01', until='2020-12-14'):
        """
        >>> ratio(poland).loc['2020-11-11']
        2.54786618630983
        """
        df = df.loc[since:until]
        return (df['Confirmed'] / df['Recovered'])


    poland = covid19('Poland')
    us = covid19('US')
    india = covid19('India')
    france = covid19('France')
    china = covid19('China')
    world = covid19()

    ratio(poland, since='2020-06-01', until='2020-12-14').plot()
    ratio(india, since='2020-06-01', until='2020-12-14').plot()
    ratio(us, since='2020-06-01', until='2020-12-14').plot()
    ratio(china, since='2020-11-01', until='2020-12-14').plot()
    ratio(world, since='2020-12-09', until='2020-12-14').plot()
