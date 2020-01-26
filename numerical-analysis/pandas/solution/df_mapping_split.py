import pandas as pd

MONTH = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}

df = pd.read_csv('../numerical-analysis/pandas/data/phones.csv', index_col=0)

df[ ['year', 'month_name'] ] = df['month'].str.split('-', expand=True)

print(df)

## Alternative Solution
df['year'] = df['month'].str[:4]
df['month_name'] = df['month'].str[-2:]
