import pandas as pd


# Read data
df = pd.read_csv('../numerical-analysis/pandas/data/phones.csv')

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

df = pd.read_csv('../numerical-analysis/pandas/data/phones.csv')

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
