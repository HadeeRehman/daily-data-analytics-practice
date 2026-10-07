# Rank and sort numerical values using Pandas rank and sort_values
import pandas as pd

data = {
    'student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'score': [85, 92, 78, 92, 88],
}

df = pd.DataFrame(data)

# 1. Assign competition ranks (highest score gets rank 1)
df['rank'] = df['score'].rank(ascending=False, method='min').astype(int)

# 2. Sort DataFrame by rank
df_sorted = df.sort_values(by=['rank', 'student']).reset_index(drop=True)

print(df_sorted)