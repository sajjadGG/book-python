import pandas as pd


data =  [x for x in range(0, 20) if x % 2 == 0]

s = pd.Series(data)


s ** 2
s + 5
