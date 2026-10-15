# Extract structured substrings into separate columns using regex capture groups with str.extract
import pandas as pd

data = {
    'order_id': ['TXN-101-US', 'TXN-204-CA', 'TXN-305-UK', 'TXN-408-US'],
    'product_info': [
        'Laptop (ID: 5542)',
        'Mouse (ID: 1102)',
        'Monitor (ID: 8821)',
        'Keyboard (ID: 3349)',
    ],
}

df = pd.DataFrame(data)

# 1. Extract numeric transaction number and country code
df[['txn_num', 'country']] = df['order_id'].str.extract(r'TXN-(\d+)-([A-Z]{2})')

# 2. Extract product title and internal ID
df[['product', 'internal_id']] = df['product_info'].str.extract(
    r'([A-Za-z]+)\s+\(ID:\s*(\d+)\)'
)

print(df[['order_id', 'txn_num', 'country', 'product', 'internal_id']])