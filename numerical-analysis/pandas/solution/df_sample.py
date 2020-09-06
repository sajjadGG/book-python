import pandas as pd

FILE = r'../data/astronauts.csv'


df = pd.read_csv(FILE)
df['Order'] = df['Order'].astype(int)
df['Order'].ffill(inplace=True)
df = df.sample(frac=1.0)
df.reset_index(drop=True, inplace=True)
