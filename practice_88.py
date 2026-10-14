# Filter text columns using regex pattern matching with Pandas str.contains
import pandas as pd

data = {
    'product_id': ['SKU-101', 'SKU-202', 'ACC-303', 'SKU-404', 'ACC-505'],
    'description': [
        'Wireless Bluetooth Mouse',
        'Mechanical USB Keyboard',
        'USB-C Charging Cable',
        'Bluetooth Over-Ear Headphones',
        'Ergonomic Mouse Pad',
    ],
    'price': [29.99, 89.99, 14.99, 119.99, 19.99],
}

df = pd.DataFrame(data)

# 1. Filter rows containing 'Bluetooth' (case-insensitive)
bluetooth_items = df[
    df['description'].str.contains('bluetooth', case=False, na=False)
].reset_index(drop=True)

# 2. Filter using regex alternation pattern ('Mouse' OR 'Keyboard')
input_devices = df[
    df['description'].str.contains('Mouse|Keyboard', na=False)
].reset_index(drop=True)

print("--- Bluetooth Items ---")
print(bluetooth_items[['product_id', 'description', 'price']])

print("\n--- Mouse or Keyboard Items ---")
print(input_devices[['product_id', 'description', 'price']])