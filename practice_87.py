# Calculate previous period lag values and differences using Pandas shift
import pandas as pd

data = {
    'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'sales': [200, 250, 220, 310, 290],
}

df = pd.DataFrame(data)

# 1. Shift sales column by 1 period to get the previous day's sales
df['prev_day_sales'] = df['sales'].shift(1)

# 2. Calculate day-over-day absolute difference
df['sales_diff'] = df['sales'] - df['prev_day_sales']

print(df)