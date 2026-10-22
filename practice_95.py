# Aggregate multidimensional data and calculate grand totals using pd.pivot_table
import pandas as pd

data = {
    'region': ['East', 'East', 'West', 'West', 'East', 'West'],
    'rep': ['Alice', 'Bob', 'Charlie', 'David', 'Alice', 'Charlie'],
    'quarter': ['Q1', 'Q1', 'Q1', 'Q1', 'Q2', 'Q2'],
    'sales': [15000, 18000, 22000, 19000, 21000, 24000],
}

df = pd.DataFrame(data)

# Reshape data into a cross-tabulated summary table with row/column totals
pivot = pd.pivot_table(
    df,
    values='sales',
    index='region',
    columns='quarter',
    aggfunc='sum',
    fill_value=0,
    margins=True,
    margins_name='Total',
)

print(pivot)