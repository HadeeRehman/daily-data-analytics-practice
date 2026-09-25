# Calculate department mean and deviation using Pandas transform
import pandas as pd

data = {
    'employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'dept': ['Sales', 'Sales', 'Sales', 'IT', 'IT', 'IT'],
    'salary': [50000, 70000, 80000, 60000, 90000, 100000],
}

df = pd.DataFrame(data)

# Broadcast group-level mean back to original DataFrame shape
df['dept_mean_salary'] = df.groupby('dept')['salary'].transform('mean')

# Calculate deviation from the department average
df['diff_from_dept_mean'] = df['salary'] - df['dept_mean_salary']

print(df)