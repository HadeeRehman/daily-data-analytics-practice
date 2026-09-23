# Compute custom multi-metric summary table using Pandas named aggregations

import pandas as pd

data = {
    'dept': ['Sales', 'Sales', 'IT', 'IT', 'HR', 'HR', 'Sales', 'IT', 'HR'],
    'salary': [52000, 61000, 75000, 88000, 50000, 53000, 64000, 92000, 48000],
    'bonus': [5000, 7000, 8000, 11000, 4000, 4500, 6500, 12000, 3500],
}

df = pd.DataFrame(data)

# Perform multiple named aggregations per group
dept_summary = df.groupby('dept').agg(
    avg_salary=('salary', 'mean'),
    max_salary=('salary', 'max'),
    total_bonus=('bonus', 'sum'),
    headcount=('salary', 'count')
).reset_index()

print(dept_summary)