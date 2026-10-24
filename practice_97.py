# Reconcile datasets and audit merge integrity using pd.merge with indicator=True
import pandas as pd

# Transactions table (fact dataset)
transactions = pd.DataFrame({
    'txn_id': [101, 102, 103, 104, 105],
    'cust_id': ['C10', 'C20', 'C10', 'C30', 'C99'],
    'amount': [250, 400, 150, 600, 80],
})

# Customer master table (dimension dataset)
customers = pd.DataFrame({
    'cust_id': ['C10', 'C20', 'C30', 'C40'],
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'tier': ['Gold', 'Silver', 'Gold', 'Bronze'],
})

# 1. Outer merge with merge indicator enabled
merged = pd.merge(
    transactions,
    customers,
    on='cust_id',
    how='outer',
    indicator=True,
)

print('--- Merged Table with Alignment Indicator ---')
print(merged)

# 2. Extract orphan transactions (transactions with no customer profile)
orphan_txns = merged[merged['_merge'] == 'left_only'][['txn_id', 'cust_id', 'amount']]
print('\n--- Orphan Transactions (Missing Customer Profile) ---')
print(orphan_txns)

# 3. Extract inactive customers (customers with zero transactions)
inactive_cust = merged[merged['_merge'] == 'right_only'][['cust_id', 'name', 'tier']]
print('\n--- Inactive Customers (No Purchases) ---')
print(inactive_cust)