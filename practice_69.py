# Filter Pandas Series values using boolean condition indexing

import pandas as pd

data = [100, 101, 102, 204, 205]

series = pd.Series(data, index=['a','b','c','d','e'])


print(series[series >= 200])