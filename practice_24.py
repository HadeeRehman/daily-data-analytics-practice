# Group delivered orders by customer to calculate total spent and order count
import pandas as pd
df = pd.read_csv('new.csv')

df['total'] = df['price'] * df['qty']
df = df[df['status'] == 'delivered']
df = df.groupby('customer').agg(
    total_spent=('total', 'sum'),
    count_order=('order_id', 'count')
)
df = df.sort_values('total_spent', ascending=False)
print(df)