# Aggregate multi-dimensional metrics with marginal totals using pd.pivot_table
import pandas as pd

data = {
    'region': ['North', 'North', 'South', 'South', 'East', 'East', 'West', 'West'],
    'product': ['Laptop', 'Phone', 'Laptop', 'Phone', 'Laptop', 'Phone', 'Laptop', 'Phone'],
    'sales': [12000, 8000, 15000, 7000, 9000, 6000, 11000, 8500],
    'units': [10, 15, 12, 14, 8, 11, 9, 16],
}

df = pd.DataFrame(data)

# Aggregate revenue across region and product with subtotal margins
pivot = pd.pivot_table(
    df,
    values='sales',
    index='region',
    columns='product',
    aggfunc='sum',
    margins=True,
    margins_name='Total'
)

print(pivot)