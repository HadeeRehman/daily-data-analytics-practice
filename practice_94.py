# Broadcast group aggregates to individual rows using groupby and transform
import pandas as pd

data = {
    'department': [
        'Sales',
        'Sales',
        'Sales',
        'Engineering',
        'Engineering',
        'Engineering',
    ],
    'employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'salary': [60000, 75000, 65000, 90000, 110000, 95000],
}

df = pd.DataFrame(data)

# 1. Calculate department average salary broadcasted back to original rows
df['dept_avg_salary'] = (
    df.groupby('department')['salary'].transform('mean').round(2)
)

# 2. Calculate variance against department benchmark
df['diff_from_avg'] = (df['salary'] - df['dept_avg_salary']).round(2)

# 3. Calculate percentage contribution to department payroll
df['dept_total'] = df.groupby('department')['salary'].transform('sum')
df['pct_of_dept_total'] = ((df['salary'] / df['dept_total']) * 100).round(1)

print(
    df[
        [
            'department',
            'employee',
            'salary',
            'dept_avg_salary',
            'diff_from_avg',
            'pct_of_dept_total',
        ]
    ]
)