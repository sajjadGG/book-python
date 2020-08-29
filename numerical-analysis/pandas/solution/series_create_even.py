import pandas as pd
import numpy as np
np.random.seed(0)


df = np.random.randint(0, 9, size=100)
df = df[df % 2 == 0]

s = pd.Series(df[:10])
# 0    8
# 1    2
# 2    0
# 3    8
# 4    0
# 5    0
# 6    8
# 7    8
# 8    2
# 9    6
# dtype: int64
