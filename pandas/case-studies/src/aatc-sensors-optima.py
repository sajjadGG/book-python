import pandas as pd
from matplotlib import pyplot as plt


DATA = 'https://python.astrotech.io/_static/sensors-optima.xlsx'
LUX = 1

df = pd.read_excel(
    io=DATA,
    sheet_name='Luminance',
    header=1,
    parse_dates=['datetime', 'date', 'time'],
    index_col='datetime')

df['time'] = df['time'].dt.time

# Zobaczmy jak wyglądają dane
df.info(memory_usage='deep')

# Statystyki opisowe
df['value'].describe()

# Zobaczmy jak dane się rozkładają
df['value'].plot(kind='density')
plt.show()

# Jakie wartości padają w naszych danych
df['value'].hist(bins=3)
plt.show()

df['value'].hist(bins=10)
plt.show()

df.loc['2019-09-24', 'value'].hist(bins=10)
plt.show()

# próg szumu (poniżej to szum, powyżej sygnał)
THRESHOLD = 20*LUX

noise = df['value'] <= THRESHOLD
activity = ~noise
df['active'] = activity
df['active'].replace({
    True: 1,
    False: 0,
}, inplace=True)

# np.sign()
# - jeżeli jest mniejsza niż 0, to daje -1
# - jeżeli wartość jest 0 to daje 0
# - jeżeli wartość jest większa niż 0 to daje 1

ROOM = df['location'] == 'Kitchen Lab Table'


active = (
    df[ROOM]
    .loc['2019-09-24', 'active']
    .loc[:, ]
    .resample('H')
    .median()
    .interpolate()
    .map(np.sign)
)


plot = (active
     .plot(color='red', figsize=(10,10), yticks=[0,1])
     .set_yticklabels(['seep', 'awake'])
)

plt.show()

# THRESHOLD = 20*LUX
# data = pd.cut(
#     x=df['value'],
#     bins=[0, THRESHOLD, np.inf],
#     labels=['active', 'sleep'])
