# Bin continuous data using pd.cut and pd.qcut
import pandas as pd
import io

csv_data = """name,age,salary,score
Alice,25,35000,82
Bob,42,85000,91
Charlie,31,52000,67
Diana,28,48000,75
Eve,55,92000,88
Frank,38,61000,55
Grace,22,32000,93
Hank,47,78000,71
Ivan,33,58000,84
Jane,29,44000,62"""

df = pd.read_csv(io.StringIO(csv_data))

# pd.cut -> Equal ranges, unequal number of rows.

bins = [0, 50000, 75000, float('inf')]
labels = ['Low', 'Mid', 'High']

df['salary_band'] = pd.cut(df['salary'], bins=bins, labels=labels, right=False)

bins2 = [0, 60, 70, 80, float('inf')]
labels2 = ['F', 'C', 'B', 'A']

df['score_grade'] = pd.cut(df['score'], bins=bins2, labels=labels2, right=False)

df['Quantity'] = pd.qcut(df['salary'], q=4, labels=['Q1','Q2','Q3','Q4']) # pd.qcut() → Unequal ranges, equal number of rows.

print(df)
