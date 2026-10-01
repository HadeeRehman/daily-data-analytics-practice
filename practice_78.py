# Detect, inspect, and impute missing values using isna, fillna, and dropna
import numpy as np
import pandas as pd

# DataFrame with intentional missing values (NaN)
data = {
    'employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'dept': ['Sales', 'IT', 'IT', None, 'Sales', 'HR'],
    'salary': [52000, 75000, np.nan, 48000, 82000, np.nan],
    'rating': [4.6, np.nan, 3.9, 4.1, 4.8, 3.5],
}

df = pd.DataFrame(data)

print('--- Initial DataFrame with Missing Values ---')
print(df)

print('\n--- Missing Value Count per Column ---')
print(df.isna().sum())

# Impute missing salaries with the column median
median_salary = df['salary'].median()
df['salary'] = df['salary'].fillna(median_salary)

# Impute missing departments with a constant string placeholder
df['dept'] = df['dept'].fillna('Unknown')

# Drop rows where critical ratings are missing
df_clean = df.dropna(subset=['rating'])

print('\n--- Cleaned and Imputed DataFrame ---')
print(df_clean)