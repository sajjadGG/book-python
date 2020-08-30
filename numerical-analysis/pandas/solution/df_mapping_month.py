import pandas as pd

DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/pandas/data/phones.csv'
MONTHS_EN = ['January', 'February', 'March', 'April',
             'May', 'June', 'July', 'August', 'September',
             'October', 'November', 'December']

MONTHS = dict(enumerate(MONTHS_EN, start=1))

# Read data
df = pd.read_csv(DATA)

# Split data into two columns
df[['year', 'month_name']] = df['month'].str.split('-', expand=True)

# Replace month names
df['month_name'].replace({
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December',
}, inplace=True)

# Print result
print(df)


## Alternative Solution
import pandas as pd

df = pd.read_csv(DATA)

df['year'] = df['month'].str[:4]
df['month_name'] = df['month'].str[-2:]
df['month_name'].replace({
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December',
}, inplace=True)

print(df)
