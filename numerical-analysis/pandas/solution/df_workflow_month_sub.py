import pandas as pd


# Read data
df = pd.read_csv('../numerical-analysis/pandas/data/astro-dates.csv')

df['Mission Date'].replace({
    'styczeń': 'January',
    'luty': 'February',
    'marzec': 'March',
    'kwiecień': 'April',
    'maj': 'May',
    'czerwiec': 'June',
    'lipiec': 'July',
    'sierpień': 'August',
    'wrzesień': 'September',
    'październik': 'October',
    'listopad': 'November',
    'grudzień': 'December',
}, regex=True, inplace=True)

df['Mission Date'] = df['Mission Date'].apply(pd.Timestamp)

print(df)



## Alternative solution
import pandas as pd

MONTHS = {
    'styczeń': 'January',
    'luty': 'February',
    'marzec': 'March',
    'kwiecień': 'April',
    'maj': 'May',
    'czerwiec': 'June',
    'lipiec': 'July',
    'sierpień': 'August',
    'wrzesień': 'September',
    'październik': 'October',
    'listopad': 'November',
    'grudzień': 'December',
}

def substitute(text):
    for pl, en in MONTHS.items():
        result = text.replace(pl, en)
        if text != result:
            return result

# Read data
df = pd.read_csv('../numerical-analysis/pandas/data/astro-dates.csv')

df['Mission Date'] = df['Mission Date'].apply(substitute)
df['Mission Date'] = df['Mission Date'].apply(pd.Timestamp)

print(df)
