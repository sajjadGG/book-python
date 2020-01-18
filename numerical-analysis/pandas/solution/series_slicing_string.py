from statistics import median_low
import numpy as np
import pandas as pd
np.random.seed(0)


ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'

data = np.random.randint(10, 100, size=26)
alphabet = list(ascii_lowercase)
letter_position = median_low(alphabet)
position = alphabet.index(letter_position)

s = pd.Series(data, alphabet)
output = s[position-3:position+4].sum()

print(output)
