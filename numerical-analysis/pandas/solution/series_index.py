import numpy as np
import pandas as pd
np.random.seed(0)

data = np.random.randn(100)
index = pd.date_range('1970-01-01', freq='D', periods=data.size)

s = pd.Series(data, index)

s['2000-01-05']
# 1.8675579901499675

s['2000-02-29']
# -0.3627411659871381

s[0]
# 1.764052345967664

s[-1]
# 0.40198936344470165

s.median()
# 0.09409611943799814

s[int(s.size/2)]
# -0.8954665611936756
