# Extract date parts, filter by month, and calculate date differences using .dt

import pandas as pd
import io

csv_data = """order_id,customer,amount,order_date
1,Alice,500,2024-01-15
2,Bob,300,2024-02-20
3,Alice,700,2024-03-10
4,Charlie,450,2024-01-28
5,Bob,600,2024-03-05
6,Diana,250,2024-02-14
7,Alice,800,2024-04-01
8,Charlie,350,2024-04-15"""

df = pd.read_csv(io.StringIO(csv_data))

df['order_date'] = pd.to_datetime(df['order_date'])
df['month'] = df['order_date'].dt.month   # Think of .dt as a toolbox for dates.like str
df['day_of_week'] = df['order_date'].dt.day_name() 

# df['order_date'] = df['order_date'].dt.month_name() # changes the numbers into actual month with name

# df = df[(df['month'] == 1) | (df['month'] == 2)] 
df = df[df['month'].isin([1, 2])] # shorter verson
highest_order = df['order_date'].max()

# df['days_since_order'] = highest_order - df['order_date'] # this will give difference
df['days_since_order'] = (highest_order - df['order_date']).dt.days # does not give error while adding numbers
df['days_since_order'] + 10

print(highest_order)
print(df)

