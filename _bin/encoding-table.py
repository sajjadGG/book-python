from encodings import iso8859_2, cp1250
from unicodedata import name
from pprint import pprint


result = [{
    'dec': i,
    'hex': hex(i),
    'oct': oct(i),
    'utf-8': chr(i),
    'iso-8859-2': iso8859_2.decoding_table[i],
    'cp-1250': cp1250.decoding_table[i],
    'name': name(chr(i), '')
} for i in range(0,255)]

# pprint(result)

import pandas as pd
df = pd.DataFrame(result)

