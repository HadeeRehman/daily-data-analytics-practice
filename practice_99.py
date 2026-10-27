# Discretize continuous values into equal-frequency quantiles using pd.qcut
import pandas as pd

data = {
    'customer_id': [101, 102, 103, 104, 105, 106, 107, 108],
    'annual_spend': [120, 250, 310, 450, 780, 1100, 1500, 2400],
}

df = pd.DataFrame(data)

# 1. Segment spend into 4 equal-frequency quartiles with semantic labels
df['spend_quartile'] = pd.qcut(
    df['annual_spend'],
    q=4,
    labels=['Low', 'Medium-Low', 'Medium-High', 'High'],
)

# 2. Extract numeric quantile rank indices (1 to 4)
df['quartile_rank'] = pd.qcut(df['annual_spend'], q=4, labels=False) + 1

print(df)
print('\n--- Distribution Across Quartiles ---')
print(df['spend_quartile'].value_counts(sort=False))