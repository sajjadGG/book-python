import pandas as pd

from matplotlib import pyplot as plt


CONFIRMED = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19' \
            '/master/csse_covid_19_data/csse_covid_19_time_series' \
            '/time_series_covid19_confirmed_global.csv'
DEATHS = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master' \
         '/csse_covid_19_data/csse_covid_19_time_series' \
         '/time_series_covid19_deaths_global.csv'
RECOVERED = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19' \
            '/master/csse_covid_19_data/csse_covid_19_time_series' \
            '/time_series_covid19_recovered_global.csv'


confirmed = pd.read_csv(CONFIRMED)
deaths = pd.read_csv(DEATHS)
recovered = pd.read_csv(RECOVERED)


def _get(column_name, df, country=None):
    """
    >>> _get('Confirmed', confirmed, 'Poland').loc['2020-11-11']
    Confirmed    618813
    Name: 2020-11-11 00:00:00, dtype: int64

    >>> _get('Confirmed', confirmed, 'US').loc['2020-11-11']
    Confirmed    10495075
    Name: 2020-11-11 00:00:00, dtype: int64

    >>> _get('Deaths', confirmed, 'Poland').loc['2020-11-11']
    Deaths    618813
    Name: 2020-11-11 00:00:00, dtype: int64
    """
    if country is not None:
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
    Confirmed    10495075
    Deaths         243077
    Recovered     3997175
    Name: 2020-11-11 00:00:00, dtype: int64
    """
    return pd.concat((
            _get('Confirmed', confirmed, country),
            _get('Deaths', deaths, country),
            _get('Recovered', recovered, country),
    ), axis=1)


def trend(df, since='2020-06-01', until='2021'):
    """
    >>> poland = covid19('Poland')
    >>> trend(poland).loc['2020-11-11']
    2.54786618630983
    """
    df = df.loc[since:until]
    return df['Confirmed'] / df['Recovered']


poland = covid19('Poland')
us = covid19('US')
india = covid19('India')
france = covid19('France')
china = covid19('China')
world = covid19()

trend(poland, since='2021-01-01', until='2021').plot()
trend(india, since='2021-01-01', until='2021').plot()
trend(us, since='2021-01-01', until='2021').plot()
trend(china, since='2021-01-01', until='2021').plot()
trend(world, since='2021-01-01', until='2021').plot()


# Numer of new cases in last two weeks
new_cases = poland.last('2W').diff().plot()

# Average number of confirmed cases each month
average_cases = poland.resample('M').sum().plot()

# Select timeframe
since_december = poland.loc['2021-12':, ['Confirmed', 'Deaths']].plot(subplots=True, layout=(1,2))

# Ratio of deaths vs new cases in last two weeks
timeframe = poland.last('2W')
ratio = timeframe['Deaths'] / timeframe['Confirmed']
ratio.plot()

# Percent of deaths vs new cases in last two weeks
timeframe = poland.last('2W')
ratio = timeframe['Deaths'] / timeframe['Confirmed']
percent = ratio * 100
percent.round(decimals=3).plot(
    kind='line',
    title='Percent of deaths vs new cases in last two weeks',
    xlabel='Day',
    ylabel='Percent',
    ylim=(2.1, 2.5),
    figsize=(10,10),
    grid=True)



poland = covid19('Poland')
usa = covid19('US')
france = covid19('France')
china = covid19('China')
world = covid19()

# Zwykły wykres
def plot(df, title):
    plot = df.plot(kind='line', subplots=True, layout=(3,1), title=title)
    plt.show()

plot(poland, 'Poland')
plot(usa, 'USA')


# Bardziej fancy
plot = (
    poland
    .loc['2021-01-01':, ['Confirmed','Deaths']]
    .plot(kind='line',
          subplots=True,
          layout=(3,1),
          sharex=True,
          figsize=(16,10),
          grid=True))
plt.show()

# Ratio
ratio = poland['Deaths'] / poland['Confirmed']
plot = (
    ratio
    .plot(kind='line',
          title='Ratio',
          xlabel='Time',
          ylabel='Percent',
          # yticks=['0%', '1%', '2%', '3%', '4%', '5%'],
          figsize=(10,10),
          color='red'))
plt.show()


# przyrost Confirmed (n do n-1)
poland['Confirmed'].diff().plot(kind='line')

# Resample
poland['Confirmed'].shift(periods=1, freq='D').plot(kind='line')


# Z rozróżnianiem na kwartały (Q)
plot = poland['Confirmed'].resample('Q').plot(kind='line', legend=True)
plot[0].name = '2020-Q1'
plot[1].name = '2020-Q2'
plot[2].name = '2020-Q3'
plot[3].name = '2020-Q4'
plot[4].name = '2021-Q1'
plot[5].name = '2021-Q2'
plot[6].name = '2021-Q3'
plot[7].name = '2021-Q4'
plot[8].name = '2022-Q1'
plt.show()


# Makrotrendy
poland['Confirmed'].diff().rolling(window=14).median().plot()
plt.show()

poland['Confirmed'].diff().rolling(window=14).median().plot()
plt.show()

poland['Confirmed'].diff().resample('W').median().plot()
plt.show()

poland['Confirmed'].diff().resample('M').median().plot()
plt.show()

poland['Confirmed'].diff().resample('Q').median().plot()
plt.show()



# Jak po świętach wzrasta liczba zakażonych COVID-19
import pandas as pd
from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday, EasterMonday, Easter
from pandas.tseries.offsets import Day


class PLHolidayCalendar(AbstractHolidayCalendar):
    """
    Custom Holiday calendar for Poland based on
    https://en.wikipedia.org/wiki/Public_holidays_in_Poland
    """
    rules = [
        Holiday('New Years Day', month=1, day=1),
        Holiday('Epiphany', month=1, day=6),
        Holiday('Easter', month=1, day=1, offset=[Easter()]),
        EasterMonday,
        Holiday('May Day', month=5, day=1),
        Holiday('Constitution Day', month=5, day=3),
        Holiday('Pentecost Sunday', month=1, day=1, offset=[Easter(), Day(49)]),
        Holiday('Corpus Christi', month=1, day=1, offset=[Easter(), Day(60)]),
        Holiday('Assumption of the Blessed Virgin Mary', month=8, day=15),
        Holiday('All Saints Day', month=11, day=1),
        Holiday('Independence Day', month=11, day=11),
        Holiday('Christmas Day', month=12, day=25),
        Holiday('Second Day of Christmastide', month=12, day=26),
    ]


pl_holidays = PLHolidayCalendar().holidays(start='2021-01-01', end='2022-01-29')
for holiday in pl_holidays:
    start = holiday
    end = holiday + pd.Timedelta('10D')
    data = poland.loc[start:end, 'Confirmed'].diff()
    data.plot(kind='line', title=holiday)
    plt.show()
