import pandas as pd


TRANSLATE = {
    'ą': 'a',
    'ć': 'c',
    'ę': 'e',
    'ł': 'l',
    'ń': 'n',
    'ó': 'o',
    'ś': 's',
    'ż': 'z',
    'ź': 'z',
}

# Read data
df = pd.read_excel('../numerical-analysis/pandas/data/trl.xlsx', sheet_name=['Polish'])
df = df['Polish']

# Translate strings
df = df.applymap(lambda text: ''.join(TRANSLATE.get(letter, letter) for letter in str(text)))

# Convert first row to header, and drop old row
df.columns = df.loc[0]
df.drop(0, inplace=True)

# Convert first column to index
df.set_index('TRL')


## Alternative solution
import pandas as pd

TRANSLATE = {
    'ą': 'a',
    'ć': 'c',
    'ę': 'e',
    'ł': 'l',
    'ń': 'n',
    'ó': 'o',
    'ś': 's',
    'ż': 'z',
    'ź': 'z',
}


def remove_pl_diacritics(text):
    return ''.join(TRANSLATE.get(letter, letter) for letter in str(text))


df = pd.read_excel(
    io='../numerical-analysis/pandas/data/trl.xlsx',
    sheet_name='Polish',
    header=1,
    index_col=0)

df = df.applymap(remove_pl_diacritics)
df.columns = df.columns.map(remove_pl_diacritics)

print(df)
