# Create conditional columns using numpy where for vectorized if-else logic
import numpy as np
import pandas as pd

data = {
    'employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'sales': [120, 80, 150, 45, 95],
    'target': [100, 100, 100, 100, 100],
}

df = pd.DataFrame(data)

# 1. Binary condition: status is 'Met' if sales >= target, else 'Missed'
df['status'] = np.where(df['sales'] >= df['target'], 'Met', 'Missed')

# 2. Numeric calculation based on condition: 10% bonus if met, else 0.0
df['bonus'] = np.where(df['status'] == 'Met', df['sales'] * 0.10, 0.0)

print(df)