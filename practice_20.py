# Categorize salary grades and compute cost per rating using Pandas

import pandas as pd
import io

csv_data = """name,dept,salary,rating,status
Alice,Sales,50000,4.5,active
Bob,IT,70000,3.8,active
Charlie,Sales,55000,4.9,active
Diana,IT,80000,4.2,inactive
Eve,Sales,45000,3.5,active
Frank,IT,90000,4.7,active
Grace,HR,48000,4.1,active
Hank,HR,52000,3.9,inactive
Ivan,Sales,60000,4.6,active
Jane,IT,75000,3.2,active
Karen,HR,51000,4.3,active
Leo,Sales,48000,2.9,active"""

df = pd.read_csv(io.StringIO(csv_data))

df['salary_grade'] = 'Low'  # default
df.loc[df['salary'] >= 50000, 'salary_grade'] = 'Medium'
df.loc[df['salary'] >= 70000, 'salary_grade'] = 'High'

df['salary_per_rating'] = (df['salary'] / df['rating']).round(2)
df = df.drop(columns=['status'])

print(df)