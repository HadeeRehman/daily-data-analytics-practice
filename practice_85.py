# Assign multi-tier categories based on conditions using np.select
import numpy as np
import pandas as pd

data = {
    'customer': ['Liam', 'Noah', 'Emma', 'Olivia', 'Ava'],
    'total_spend': [1200, 450, 80, 2500, 300],
}

df = pd.DataFrame(data)

# 1. Define ordered conditions from highest to lowest threshold
conditions = [
    df['total_spend'] >= 1000,
    df['total_spend'] >= 500,
    df['total_spend'] >= 100,
]

# 2. Define corresponding values for each condition
choices = ['Platinum', 'Gold', 'Silver']

# 3. Apply multi-case logic with a fallback default
df['tier'] = np.select(conditions, choices, default='Bronze')

print(df)