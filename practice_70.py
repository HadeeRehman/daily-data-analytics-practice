# Filter Pandas DataFrame using multiple boolean conditions with logical AND

import pandas as pd

data = {
    'employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'dept': ['Sales', 'IT', 'IT', 'HR', 'Sales', 'IT'],
    'salary': [62000, 75000, 58000, 49000, 82000, 91000],
    'rating': [4.6, 4.2, 3.9, 4.1, 4.8, 4.7],
}

df = pd.DataFrame(data)

# Filter: Salary >= 60,000 AND rating >= 4.5
high_performers = df[(df['salary'] >= 60000) & (df['rating'] >= 4.5)]

print(high_performers[['employee', 'dept', 'salary', 'rating']])