# Compute cumulative sum and running percentage using Pandas cumsum
import pandas as pd

data = {
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'sales': [15000, 18000, 12000, 22000, 19000, 25000],
}

df = pd.DataFrame(data)

# 1. Calculate cumulative running total across months
df['running_total'] = df['sales'].cumsum()

# 2. Calculate cumulative percentage contribution to annual sales
total_sales = df['sales'].sum()
df['cum_pct'] = ((df['running_total'] / total_sales) * 100).round(1)

print(df)