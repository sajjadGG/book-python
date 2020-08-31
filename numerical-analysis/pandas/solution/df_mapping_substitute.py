import pandas as pd

LETTERS_PLEN = {'ą': 'a', 'ć': 'c', 'ę': 'e',
                'ł': 'l', 'ń': 'n', 'ó': 'o',
                'ś': 's', 'ż': 'z', 'ź': 'z'}

LETTERS_PLEN.update({k.upper():v.upper()
                     for k,v in LETTERS_PLEN.items()})


def translate(text):
    return ''.join(LETTERS_PLEN.get(x,x) for x in str(text))


trl = pd.read_excel(io='trl.xlsx', sheet_name='Polish')
trl.columns = trl.loc[0]
trl.drop(0, inplace=True)
trl.set_index('TRL')
trl = trl.applymap(translate)
trl.columns = trl.columns.map(translate)
trl
