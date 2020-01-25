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

def translate(text):
    return ''.join(TRANSLATE.get(letter, letter) for letter in str(text))


# Read data
df = pd.read_excel('../numerical-analysis/pandas/data/trl.xlsx', sheet_name=['Polish'])
df = df['Polish']

# Translate strings
df = df.applymap(translate)

# Convert first row to header
df.rename(columns=df.iloc[0], inplace=True)
df.drop(0, inplace=True)

# Convert first column to index
df.set_index('TRL')
