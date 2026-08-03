# Unpivot sales data from wide to long format using melt()

import pandas as pd

# Wide format
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'Jan': [5000, 3000, 4500],
    'Feb': [6000, 3500, 5500],
    'Mar': [7000, 4000, 6000]
})

df = df.melt(id_vars=['name'], var_name='month', value_name='sales') # Long format

df = df.sort_values(['name', 'month'])

print(df)