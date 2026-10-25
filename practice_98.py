# Compute custom group metrics with single-level column headers using Pandas named aggregation
import pandas as pd

data = {
    'store': ['North', 'North', 'North', 'South', 'South', 'West'],
    'category': [
        'Electronics',
        'Furniture',
        'Electronics',
        'Electronics',
        'Furniture',
        'Furniture',
    ],
    'sales': [1200, 850, 2100, 1750, 920, 1100],
    'profit': [300, 120, 550, 410, 180, 250],
}

df = pd.DataFrame(data)

# 1. Apply named aggregation inside groupby to assign clean column names directly
summary = df.groupby('store').agg(
    total_sales=('sales', 'sum'),
    avg_sales=('sales', 'mean'),
    total_profit=('profit', 'sum'),
    order_count=('sales', 'count'),
).reset_index()

# 2. Derive summary metrics on the flattened table
summary['avg_sales'] = summary['avg_sales'].round(2)
summary['profit_margin_pct'] = (
    (summary['total_profit'] / summary['total_sales']) * 100
).round(1)

print(summary)