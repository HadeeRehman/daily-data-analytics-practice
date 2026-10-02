# Clean string whitespace and remove duplicate records using str methods and drop_duplicates

import pandas as pd

data = {
    'employee': [' Alice ', 'Bob', 'charlie', 'Alice', 'BOB ', 'David'],
    'email': [
        'alice@co.com',
        'bob@co.com',
        'charlie@co.com',
        'alice@co.com',
        'bob@co.com',
        'david@co.com',
    ],
    'dept': ['Sales', 'IT', 'hr', 'Sales', 'IT', 'Marketing'],
    'salary': [55000, 72000, 50000, 55000, 72000, 64000],
}

df = pd.DataFrame(data)

print('--- Raw Data ---')
print(df)

# Standardize string formatting across text columns
df['employee'] = df['employee'].str.strip().str.title()
df['email'] = df['email'].str.strip().str.lower()
df['dept'] = df['dept'].str.strip().str.upper()

# Identify duplicated records based on unique key
print('\n--- Duplicate Flag on Email ---')
print(df.duplicated(subset=['email'], keep='first'))

# Drop duplicate rows, keeping the first occurrence
df_cleaned = df.drop_duplicates(subset=['email'], keep='first').reset_index(
    drop=True
)

print('\n--- Deduplicated and Cleaned DataFrame ---')
print(df_cleaned)