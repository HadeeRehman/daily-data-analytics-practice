# Parse date strings and extract calendar features using pd.to_datetime and dt accessor
import pandas as pd

# 1. Force Pandas to display all columns on a single line without '...' or line-wrapping
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

data = {
    'order_id': [1001, 1002, 1003, 1004, 1005],
    'customer': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'order_date': [
        '2023-01-15',
        '2023-02-20',
        '2023-03-05',
        '2023-04-12',
        '2023-05-30',
    ],
    'delivery_date': [
        '2023-01-20',
        '2023-02-28',
        '2023-03-12',
        '2023-04-15',
        '2023-06-08',
    ],
    'amount': [250, 410, 180, 520, 310],
}

df = pd.DataFrame(data)

# 2. Convert to datetime with consistent ISO formatting (YYYY-MM-DD)
df['order_date'] = pd.to_datetime(df['order_date'], format='%Y-%m-%d')
df['delivery_date'] = pd.to_datetime(df['delivery_date'], format='%Y-%m-%d')

# 3. Extract calendar attributes
df['order_month'] = df['order_date'].dt.month_name()
df['order_weekday'] = df['order_date'].dt.day_name()
df['delivery_days'] = (df['delivery_date'] - df['order_date']).dt.days

# 4. Print clean subset
output = df[['order_id', 'order_date', 'order_month', 'order_weekday', 'delivery_days']]
print(output)