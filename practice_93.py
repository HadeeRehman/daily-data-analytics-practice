# Convert dirty numeric strings and handle unparseable values using pd.to_numeric with errors='coerce'
import pandas as pd

data = {
    'product': ['Router', 'Modem', 'Switch', 'Cable', 'Access Point'],
    'inventory_count': ['45', 'missing', '12', 'N/A', '0'],
    'unit_cost': ['120.50', '85.00', 'invalid', '15.75', '210.00'],
}

df = pd.DataFrame(data)

# 1. Coerce unparseable strings into NaN
df['inventory_count'] = pd.to_numeric(df['inventory_count'], errors='coerce')
df['unit_cost'] = pd.to_numeric(df['unit_cost'], errors='coerce')

# 2. Impute nulls and cast inventory counts to integer
df['inventory_count'] = df['inventory_count'].fillna(0).astype(int)
df['unit_cost'] = df['unit_cost'].fillna(df['unit_cost'].median())

# 3. Calculate total inventory valuation
df['total_value'] = (df['inventory_count'] * df['unit_cost']).round(2)

print(df)