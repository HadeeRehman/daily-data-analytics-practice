# Filter DataFrame rows matching a list of values using the isin method

import pandas as pd

data = {
    'product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Desk', 'Chair'],
    'category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Furniture', 'Furniture'],
    'price': [1200, 25, 45, 300, 150, 85],
}

df = pd.DataFrame(data)

# Target categories to include
target_categories = ['Electronics', 'Accessories']

# 1. Filter rows matching any value in target_categories
filtered_df = df[df['category'].isin(target_categories)].reset_index(drop=True)

# 2. Invert filter with ~ to exclude those categories
excluded_df = df[~df['category'].isin(target_categories)].reset_index(drop=True)

print("--- Included Categories ---")
print(filtered_df)

print("\n--- Excluded Categories (Furniture only) ---")
print(excluded_df)