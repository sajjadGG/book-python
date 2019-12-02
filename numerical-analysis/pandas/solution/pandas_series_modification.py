# . Z danych wejściowych stwórz ``pd.Series``
# . Wypełnij puste wartości zerami
# . Usuń wartości na indeksach 2, 4, 6
# . Zresetuj indeks (bez kopii starego)
# . Wypisz serię

import pandas as pd
import numpy as np


values = [1, np.nan, 5, np.nan, 1, 2, 1, np.inf]
s = pd.Series(values)

s.fillna(0, inplace=True)
s.drop(2, inplace=True)
s.drop(4, inplace=True)
s.drop(6, inplace=True)
s.drop_duplicates(inplace=True)

s.reset_index(drop=True)
# 0    1.0
# 1    0.0
# 2    2.0
# 3    inf
# dtype: float64
